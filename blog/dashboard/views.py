from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from core.models import Notification , Activity , Reply , Comment, Code , RechargeRequest, Profile, Post, LikePost, FollowersCount , Subject , GetPremium , News , Instructor , BuyLesson
from core.models import Notification , Assignment , AssignmentSubmit , Question , Part , AssignmentOpen , Chapter , ChapterLecture , BuyChapter , Group , GroupMember , GroupLecture
from itertools import chain
import random


# necessary imports
import secrets
import string

from django.shortcuts import get_object_or_404

# Create your views here.






@login_required(login_url='register')
def dashboard(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    user_following_list = []
    feed = []
    user_following = FollowersCount.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))




    all_profiles = Profile.objects.all()

    questions = Comment.objects.filter(commented_to=request.user.username)

    active_codes = Code.objects.filter(active=True , teacher=request.user.username).values().order_by('-created_at')
    inactive_codes = Code.objects.filter(active=False , teacher=request.user.username).values().order_by('-created_at')


    teacher_posts = Post.objects.filter(user=request.user.username).order_by('created_at')



    return render(request, 'dashboard/dashboard.html', {'user_profile': user_profile, 'posts':teacher_posts ,'profiles' :all_profiles , 'questions':questions  , 'notifications' : notifications_count , 'active_codes' :active_codes , 'inactive_codes' : inactive_codes})


@login_required(login_url='register')
def dashboard_lectures(request ):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    teacher_posts = Post.objects.filter(user=request.user.username).order_by('created_at')

    return render(request, 'dashboard/lectures.html', {'user_profile': user_profile, 'posts':teacher_posts , 'notifications' : notifications_count })

@login_required(login_url='register')
def dashboard_lesson(request , slug):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''




    post = get_object_or_404(Post ,slug=slug )

    parts = Part.objects.filter(lecture_id=post.id)
    videos_count = Part.objects.filter(lecture_id=post.id , type='video').count()
    links_count = Part.objects.filter(lecture_id=post.id , type='link').count()

    students = BuyLesson.objects.filter(post_id=slug)

    if Assignment.objects.filter(post_id=post.id , assignment_type='homework').first():
        related_homework_assignmnet = Assignment.objects.get(post_id=post.id , assignment_type='homework')
    else:
        related_homework_assignmnet = ''
    
    if Assignment.objects.filter(post_id=post.id , assignment_type='test').first():
        related_test_assignmnet = Assignment.objects.get(post_id=post.id , assignment_type='test')
    else:
        related_test_assignmnet = ''


    if LikePost.objects.filter(username=request.user.username, post_id=post.id).first():
        like_filter = 'yes'
    else:
        like_filter = 'no'
    
    return render(request, 'dashboard/lesson.html', {'post' : post , 'parts':parts, 'videos_count' : videos_count, 'links_count' : links_count ,'students':students , 'user_profile': user_profile, 'notifications' : notifications_count , 'test_assignment' : related_test_assignmnet , 'homework_assignment' : related_homework_assignmnet , 'like' : like_filter})





@login_required(login_url='register')
def dashboard_chapters(request ):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''



    chapters = Chapter.objects.filter(user=request.user.username).order_by('created_at')
    lectures = Post.objects.filter(user=request.user.username).order_by('created_at')



    return render(request, 'dashboard/chapters.html', {'user_profile': user_profile, 'chapters':chapters , 'posts':lectures })



@login_required(login_url='register')
def dashboard_chapter_details(request , slug):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''



    chapter_id = slug
    chapter = Chapter.objects.get(id=chapter_id)

    all_lectures = Post.objects.filter(user=request.user.username).order_by('created_at')

    chapter_lectures = ChapterLecture.objects.filter(chapter_id=chapter_id).order_by('-created_at')

    students = BuyChapter.objects.filter(chapter_id=slug)



    return render(request, 'dashboard/chapter.html', {'user_profile': user_profile, 'chapter':chapter ,  'posts':all_lectures , 'lectures':chapter_lectures , 'students':students , 'notifications':notifications_count})



@login_required(login_url='register')
def create_chapter(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if request.method == 'POST':
        title = request.POST.get('title')


        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        alphabet = letters + digits
        pwd_length = 10
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))


        new_chapter = Chapter.objects.create(title=title , user=request.user.username , code=pwd)
        new_chapter.save()


        redirction_link = str(new_chapter.id)
        return redirect('/dashboard/chapters/' + redirction_link)

@login_required(login_url='register')
def delete_chapter(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if request.method == 'POST':
        chapter_id = request.POST.get('chapter-id')

        chapter = Chapter.objects.get(id=chapter_id).delete()
        return redirect('/dashboard/chapters')
    



@login_required(login_url='register')
def chapter_settings(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if request.method == 'POST':
        type = request.POST.get('type')
        chapter_id = request.POST.get('chapter-id')

        chapter = Chapter.objects.get(id=chapter_id)

        if type == 'add-lecture':
            lecture_id = request.POST.get('lecture-id')

            lecture = Post.objects.get(id=lecture_id)

            if ChapterLecture.objects.filter(lecture_id=lecture_id , chapter_id=chapter.id).first():
                redirction_link = str(chapter_id)
                return redirect('/dashboard/chapters/' + redirction_link)
            else:
                new_chapter_lecture = ChapterLecture.objects.create(lecture_id=lecture_id , chapter_id=chapter.id , image=lecture.image , title=lecture.title , teacher_name=lecture.teacher_name , teacher_img=lecture.teacher_img)
                new_chapter_lecture.save()

                chapter_parts = ChapterLecture.objects.filter(chapter_id=chapter.id)
                chapter_buys = BuyChapter.objects.filter(chapter_id=chapter.id)

                for x in chapter_buys:
                    if BuyLesson.objects.filter(username=x.username , post_id=lecture_id ).first():
                        redirction_link = str(chapter_id)
                        return redirect('/dashboard/chapters/' + redirction_link)
                    else:
                        new_lecture_purchase = BuyLesson.objects.create(username=x.username , post_id=lecture_id , name=x.name , image=x.image , method='chapter')
                        new_lecture_purchase.save()


            




        if type == 'settings':
            price = request.POST.get('price')
            description = request.POST.get('description')
            title = request.POST.get('title')
            year = request.POST.get('year')

            chapter.price = price
            chapter.caption = description
            chapter.title = title
            chapter.year = year
            if len(request.FILES) != 0:
                thumbnail = request.FILES['image']
                chapter.image = thumbnail

            chapter.save()

        if type == 'remove-lecture':
            lecture_id = request.POST.get('lecture-id')
            remove_lecture = ChapterLecture.objects.get(lecture_id=lecture_id , chapter_id=chapter.id).delete()



        redirction_link = str(chapter_id)
        return redirect('/dashboard/chapters/' + redirction_link)


@login_required(login_url='register')
def group_settings(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if request.method == 'POST':
        type = request.POST.get('type')


        teacher_name = user_profile.name
        teacher_img = user_profile.image

        if type == 'create':
            title = request.POST.get('title')
            year = request.POST.get('year')

            letters = string.ascii_letters
            digits = string.digits
            special_chars = string.punctuation
            alphabet = letters + digits
            pwd_length = 5
            pwd = ''
            for i in range(pwd_length):
                pwd += ''.join(secrets.choice(alphabet))

            new_group = Group.objects.create(user=request.user.username , title=title , code=pwd , year=year)
            new_group.save()

            new_group.link = new_group.id
            new_group.save()

            redirction_link = new_group.id
            return redirect('/groups/' + str(redirction_link))
        
        if type == 'delete':
            group_id = request.POST.get('group-id')

            group = Group.objects.get(id=group_id)
            group.delete()
            return redirect('/groups')
        
        if type == 'settings':
            group_id = request.POST.get('group-id')
            title = request.POST.get('title')
            year = request.POST.get('year')

            group = Group.objects.get(id=group_id)

            group.title = title
            group.year = year

            if len(request.FILES) != 0:
                thumbnail = request.FILES['image']
                group.image = thumbnail
            
            group.save()

            edit_member_view = GroupMember.objects.filter(group_id=group_id)

            for x in edit_member_view:
                x.group_title = title
                x.group_image = group.image
                x.save()
                

            redirction_link = group.id
            return redirect('/groups/' + str(redirction_link))
        
        if type == 'add-lecture':
            group_id = request.POST.get('group-id')
            group = Group.objects.get(id=group_id)

            lecture_id = request.POST.get('lecture-id')
            lecture = Post.objects.get(id=lecture_id)

            if GroupLecture.objects.filter(group_id=group_id , lecture_id=lecture_id).first():
                redirction_link = group.id
                return redirect('/groups/' + str(redirction_link))
            else:

                add_lecture = GroupLecture.objects.create(group_id=group.id , lecture_id=lecture_id , image=lecture.image , title=lecture.title , teacher_img=lecture.teacher_img , teacher_name=lecture.teacher_name)
                add_lecture.save()

                group.no_of_lectures = group.no_of_lectures + 1
                group.save()

                if GroupMember.objects.filter(group_id=group_id).first():
                    group_members = GroupMember.objects.filter(group_id=group.id)
                    for x in group_members:
                        if BuyLesson.objects.filter(username=x.member , post_id=lecture.id).first():
                            nothing = 'Do Nothing'
                        else:
                            purchase_lesson = BuyLesson.objects.create(username=x.member , post_id=lecture.id , name=x.name , image=x.image , method='group')
                            purchase_lesson.save()
                else:
                    do_nothing = 'Do Nothing'

                redirction_link = group.id
                return redirect('/groups/' + str(redirction_link))
        
        if type == 'remove-lecture':
            group_id = request.POST.get('group-id')
            group = Group.objects.get(id=group_id)

            lecture_id = request.POST.get('lecture-id')
            lecture = Post.objects.get(id=lecture_id)

            remove_lecture = GroupLecture.objects.get(group_id=group_id , lecture_id=lecture_id)
            remove_lecture.delete()

            group.no_of_lectures = group.no_of_lectures - 1
            group.save()

            redirction_link = group.id
            return redirect('/groups/' + str(redirction_link))
        
        if type == 'add-member':
            group_id = request.POST.get('group-id')
            group = Group.objects.get(id=group_id)
            group_lectures = GroupLecture.objects.filter(group_id=group.id)

            member = request.POST.get('member')
            member_object = User.objects.get(username=member)
            member_profile = Profile.objects.get(user=member_object)

            if GroupMember.objects.filter(member=member , group_id=group_id).first():
                redirction_link = group.id
                return redirect('/groups/' + str(redirction_link))
            else:
                new_member = GroupMember.objects.create(member=member , group_id=group_id , group_title=group.title , name=member_profile.name , image=member_profile.image , group_image=group.image)
                new_member.save()
                group.no_of_students = group.no_of_students + 1
                group.save()

                for x in group_lectures:
                    if BuyLesson.objects.filter(username=member , post_id=x.lecture_id).first():
                        nothing = 'Do Nothing'
                    else:
                        purchase_lesson = BuyLesson.objects.create(username=member , post_id=x.lecture_id , name=member_profile.name , image=member_profile.image , method='group')
                        purchase_lesson.save()


                redirction_link = group.id
                return redirect('/groups/' + str(redirction_link))
        
        if type == 'remove-member':
            group_id = request.POST.get('group-id')
            group = Group.objects.get(id=group_id)

            member = request.POST.get('member')

            if GroupMember.objects.filter(member=member , group_id=group_id).first():
                remove_member = GroupMember.objects.get(member=member , group_id=group_id)
                remove_member.delete()
                group.no_of_students = group.no_of_students - 1
                group.save()
                redirction_link = group.id
                return redirect('/groups/' + str(redirction_link))
            
            else:
                redirction_link = group.id
                return redirect('/groups/' + str(redirction_link))


        

        if type == 'join-group':
            code = request.POST.get('code')

            member = request.POST.get('member')
            member_object = User.objects.get(username=member)
            member_profile = Profile.objects.get(user=member_object)

            if Group.objects.filter(code=code).first():
                group = Group.objects.get(code=code)

                if GroupMember.objects.filter(member=member , group_id=group.id).first():
                    redirction_link = group.id
                    return redirect('/groups/' + str(redirction_link))
                else:
                    join_group = GroupMember.objects.create(member=member , group_id=group.id , group_title=group.title , name=member_profile.name , image=member_profile.image , group_image=group.image)
                    join_group.save()
                    group.no_of_students = group.no_of_students + 1
                    group.save()

                    if GroupLecture.objects.filter(group_id=group.id).first():
                        group_lectures = GroupLecture.objects.filter(group_id=group.id)
                        for x in group_lectures:
                            if BuyLesson.objects.filter(username=member , post_id=x.lecture_id).first():
                                nothing = 'Do Nothing'
                            else:
                                purchase_lesson = BuyLesson.objects.create(username=member , post_id=x.lecture_id ,name=member_profile.name , image=member_profile.image , method='group')
                                purchase_lesson.save()

                    redirction_link = group.id
                    return redirect('/groups/' + str(redirction_link))
            
            else:

                messages.info(request, 'كود المجموعة الذي ادخلته غير صحيح للاسف')
                return redirect('/groups')

    else:
        return redirect('/groups')




@login_required(login_url='register')
def invite_group(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    group_id = request.GET.get('group_link')
    check = request.GET.get('check')


    if user_profile.instructor == False:
        if Group.objects.filter(link=group_id).first():
            group = Group.objects.get(link=group_id)


            if check == 'view':
                if GroupMember.objects.filter(member=request.user.username , group_id=group_id).first():
                    valid_text = 'alr'
                    return render(request, 'groups/invite.html', {'group' : group , 'text':valid_text,  'user_profile': user_profile,   'notifications' : notifications_count})
                else:
                    valid_text = 'not'
                    return render(request, 'groups/invite.html', {'group' : group , 'text':valid_text,  'user_profile': user_profile,   'notifications' : notifications_count})
                
            else:
                if GroupMember.objects.filter(member=request.user.username , group_id=group_id).first():
                    valid_text = 'alr'
                    redirction_link = str(group_id)
                    return redirect('/groups/' + redirction_link)
                else:
                    join_group = GroupMember.objects.create(member=request.user.username , group_id=group.id , group_title=group.title , name=user_profile.name , image=user_profile.image , group_image=group.image)
                    join_group.save()
                    group.no_of_students = group.no_of_students + 1
                    group.save()

                    if GroupLecture.objects.filter(group_id=group.id).first():
                        group_lectures =GroupLecture.objects.filter(group_id=group.id)
                        for x in group_lectures:
                            if BuyLesson.objects.filter(username=request.user , post_id=x.lecture_id).first():
                                nothing = 'Do Nothing'
                            else:
                                purchase_lesson = BuyLesson.objects.create(username=request.user , post_id=x.lecture_id , name=user_profile.name , image=user_profile.image , method='group')
                                purchase_lesson.save()


                    valid_text = 'not'
                    redirction_link = str(group_id)
                    return redirect('/groups/' + redirction_link)

    



        else:
            messages.info(request, 'رابط الدعوة الى المجموعة غير صالح')
            return redirect('/groups')
    else:
        redirction_link = str(group_id)
        return redirect('/groups/' + str(redirction_link))






@login_required(login_url='register')
def create_lecture(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if request.method == 'POST':
        title = request.POST.get('title')
        type = request.POST.get('type')


        teacher_name = user_profile.name
        teacher_img = user_profile.image
        subject = user_profile.subject


        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        alphabet = letters + digits
        pwd_length = 10
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        

        new_lecture = Post.objects.create(title=title , user=request.user.username , teacher_name=teacher_name , teacher_img=teacher_img , subject=subject , code=pwd , type=type)


        redirction_link = str(new_lecture.id)
        return redirect('/dashboard/lecture/' + redirction_link)




@login_required(login_url='register')
def add_part(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if request.method == 'POST':
        type = request.POST.get('type')
        lecture_id = request.POST.get('lecture-id')

        if type == 'video':
            title = request.POST.get('title')
            place = request.POST.get('place')

            if len(request.FILES) != 0:
                video = request.FILES['video']

                new_part = Part.objects.create(lecture_id=lecture_id , teacher=request.user.username , type='video' , place=place , title=title , video=video)
                new_part.save()

        if type == 'link':
            link = request.POST.get('link')
            title = request.POST.get('title')
            place = request.POST.get('place')

            new_part = Part.objects.create(lecture_id=lecture_id , teacher=request.user.username , type='link' , place=place , link=link , title=title)

        if type == 'settings':
            price = request.POST.get('price')
            description = request.POST.get('description')
            year = request.POST.get('year')

            lecture = Post.objects.get(id=lecture_id)


            lecture.price = price
            
            lecture.caption = description
            lecture.year = year

            if len(request.FILES) != 0:
                thumbnail = request.FILES['image']
                lecture.image = thumbnail
            
            lecture.save()

            related_group_lectures = GroupLecture.objects.filter(lecture_id=lecture.id)
            related_chapter_lectures = ChapterLecture.objects.filter(lecture_id=lecture.id)

            for x in related_chapter_lectures:
                x.image = lecture.image
                x.save()

            for x in related_group_lectures:
                x.image = lecture.image
                x.save()

        if type == 'assignment':
            name = request.POST.get('title')
            type = request.POST.get('assignment-type')
            lecture_id = request.POST['lecture']


        
            

            new_assignment= Assignment.objects.create(username=request.user.username , assignment_name=name , assignment_type=type , post_id=lecture_id)
            new_assignment.save()
            new_part = Part.objects.create(lecture_id=lecture_id , teacher=request.user.username , type='assignment' , link=new_assignment.assignment_id , title=name , assignment_id=new_assignment.assignment_id).save()

            redirection_link = str(new_assignment.assignment_id)
            return redirect('/dashboard/assignment/' + redirection_link)






         
        redirction_link = str(lecture_id)
        return redirect('/dashboard/lecture/' + redirction_link)


    return render(request, 'dashboard/assignment-upload.html')


@login_required(login_url='register')
def delete_part(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    if request.method == 'POST':
        lecture_id = request.POST.get('lecture-id')
        part_id = request.POST.get('part-id')
        part_type = request.POST.get('part-type')
        assignment_id = request.POST.get('assignment_id')

        if user_profile.instructor == True:

            if part_type == 'assignment':
                delete_part = Part.objects.get(part_id=part_id)
                delete_part.delete()
                delete_assignment = Assignment.objects.get(assignment_id=assignment_id)
                delete_assignment.delete()

            else:

                delete_part = Part.objects.get(part_id=part_id)
                delete_part.delete()



        redirction_link = str(lecture_id)
        return redirect('/dashboard/lecture/' + redirction_link)


    return render(request, 'dashboard/assignment-upload.html')



@login_required(login_url='register')
def delete_lesson(request):
    if request.method == 'POST':
        post_id = request.POST['post-id']


        delete_post = Post.objects.get(id=post_id)
        delete_post.delete()
        return redirect('/dashboard#videos')

    else:
        return redirect('/dashboard#videos')
    
@login_required(login_url='register')
def delete_code(request):
    if request.method == 'POST':
        code_id = request.POST['code']


        delete_code = Code.objects.get(code_id=code_id)
        delete_code.delete()
        return redirect('/dashboard#codes')

    else:
        return redirect('/dashboard#codes')

@login_required(login_url='register')
def delete_assignment(request):
    if request.method == 'POST':
        lecture_id = request.POST['lecture-id']
        assignment_id = request.POST['assignment-id']


        delete_assignment = Assignment.objects.get(assignment_id=assignment_id)
        delete_assignment.delete()

        related_parts = Part.objects.filter(assignment_id=assignment_id).all()
        for x in related_parts:
            x.delete()



        return redirect('/dashboard/lecture/' + lecture_id)

    else:
        return redirect('/dashboard/lecture/' + lecture_id)

@login_required(login_url='register')
def dashboard_delete_assignment(request):
    if request.method == 'POST':

        assignment_id = request.POST['assignment-id']


        delete_assignment = Assignment.objects.get(assignment_id=assignment_id)
        delete_assignment.delete()

        related_parts = Part.objects.filter(assignment_id=assignment_id).all()
        for x in related_parts:
            x.delete()

        return redirect('/dashboard/assignments')

    else:
        return redirect('/dashboard/assignments')






@login_required(login_url='register')
def dashboard_profiles(request):
    if request.method == 'POST':
        student = request.POST['student']
        money = request.POST['money']

        new_wallet = int(money)

        studentt = Profile.objects.get(id_user=student)
        studentt.money = new_wallet
        studentt.save()
        return redirect('/dashboard#students')

    else:
        return redirect('/dashboard#students')
    



@login_required(login_url='register')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        if len(request.FILES) != 0:
            clip = request.FILES['clip']

        new_post = Post.objects.create(user=user, image=image, caption=caption , video=clip)
        new_post.save()

        return redirect('/dashboard#upload-video')
    else:
        return redirect('/dashboard#upload-video')


@login_required(login_url='register')
def wallet_recharge(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''



    all_requests = RechargeRequest.objects.all()
    user_requests = all_requests.filter(username=request.user.username).values()




    if request.method == 'POST':
        usernames = request.user
        amounts = request.POST.get('amount')
        sender_numbers = request.POST.get('sender')
        wallet_numbers = request.POST.get('wallet')
        data = RechargeRequest(username=usernames , amount=amounts ,  sender_number=sender_numbers , wallet_number=wallet_numbers)
        data.save()
        return redirect('/wallet/requests')



    return render(request, 'money/wallet-recharge.html' , {'user_profile': user_profile , 'requests' : user_requests  , 'notifications' : notifications_count})



@login_required(login_url='register')
def wallet_requests(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    all_requests = RechargeRequest.objects.all()
    user_requests = all_requests.filter(username=request.user.username).values()

    return render(request, 'money/wallet-requests.html' , {'user_profile': user_profile , 'requests':user_requests  , 'notifications' : notifications_count})


@login_required(login_url='register')
def money_error(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''


    return render(request, 'money/money-error.html' , {'user_profile': user_profile  , 'notifications' : notifications_count})



@login_required(login_url='register')
def charge_wallet_code(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''

    return render(request, 'money/code-charge.html', {'user_profile': user_profile  , 'notifications' : notifications_count})



@login_required(login_url='register')
def code_charge(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''




    return render(request, 'money/code-charge-request.html', {'user_profile': user_profile, 'notifications' : notifications_count})


@login_required(login_url='register')
def code_charge_function(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''


    if request.method == 'POST':
        code = request.POST['code']

        if Code.objects.filter(code_id=code).first():
            valid_code = Code.objects.get(code_id=code)
            valid_code_money = valid_code.money
            user_profile.money = user_profile.money + valid_code_money



            user_profile.save()
            user_object.save()
            text = 'yes'
            new_activity = Activity.objects.create(username=request.user.username , activity_type='charge' ,purchase_type='code' , wallet=user_profile.money , money=valid_code_money)
            new_notification = Notification.objects.create(username=request.user.username , activity_type='charge' ,purchase_type='code' , wallet=user_profile.money , money=valid_code_money)
            new_notification.save()
            valid_code.active = False
            valid_code.student = request.user.username
            valid_code.save()

            messages.info(request, 'تم شحن مبلغ ' + str(valid_code.money) + ' جنية في محفظنك بنجاح')
            return redirect('/wallet/recharge')

        else:
            messages.info(request, 'الكود الذي ادخلته غير صالح او مستخدم من قبل')
            return redirect('/wallet/recharge')



@login_required(login_url='register')
def lesson_code_charge(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''



    if request.method == 'POST':
        code = request.POST['code']
        post_id = request.POST['post-id']
        post_price = request.POST['price']
        post = Post.objects.get(id=post_id)

        if Code.objects.filter(code_id=code).first():
            valid_code = Code.objects.get(code_id=code)
            valid_code_money = valid_code.money
            user_profile.money = user_profile.money + valid_code_money



            user_profile.save()
            user_object.save()
            new_activity = Activity.objects.create(username=request.user.username , activity_type='charge' ,purchase_type='code' , wallet=user_profile.money , money=valid_code_money)
            new_notification = Notification.objects.create(username=request.user.username , activity_type='charge' ,purchase_type='code' , wallet=user_profile.money , money=valid_code_money)
            valid_code.active = False
            valid_code.student = request.user.username
            valid_code.save()

            lesson_price = post_price
            
            if user_profile.money < post.price:
                messages.info(request, 'للاسف ليس لديك رصيد كافي في المحفظة لشراء هذة المحاضرة')
                return redirect('/lessons/'+post_id)
            else:
                new_buy = BuyLesson.objects.create(post_id=post_id, username=request.user.username , name=user_profile.name , image=user_profile.image , method='code')
                new_buy.save()
                lesson_price = post.price
                user_profile.money = user_profile.money-lesson_price
                user_profile.no_of_buys = user_profile.no_of_buys+1

                post.no_of_buys = post.no_of_buys+1
                post.save()
                user_profile.save()
                new_activity = Activity.objects.create(username=request.user.username , activity_type='purchase' ,purchase_type='code' , wallet=user_profile.money , lesson_name=post.title , money=lesson_price)
                new_notification = Notification.objects.create(username=request.user.username , activity_type='withdraw' ,purchase_type='code' , wallet=user_profile.money , lesson_name=post.title , money=lesson_price)
                new_notification = Notification.objects.create(username=request.user.username , activity_type='purchase' ,purchase_type='code' , wallet=user_profile.money , lesson_name=post.title , money=lesson_price)

                messages.info(request, ' تم شراء المحاضرة بنجاح ')
                return redirect('/lessons/progress/'+post_id)
        else:
            if post.code == code:

                new_buy = BuyLesson.objects.create(post_id=post_id, username=request.user.username , name=user_profile.name , image=user_profile.image , method='lecture_code')
                new_buy.save()

                user_profile.no_of_buys = user_profile.no_of_buys+1

                post.no_of_buys = post.no_of_buys+1
                post.save()
                user_profile.save()
                new_activity = Activity.objects.create(username=request.user.username , activity_type='purchase' ,purchase_type='code' , wallet=user_profile.money , lesson_name=post.title , money='0')
            
                new_notification = Notification.objects.create(username=request.user.username , activity_type='purchase' ,purchase_type='code' , wallet=user_profile.money , lesson_name=post.title , money='0')

                messages.info(request, ' تم شراء المحاضرة بنجاح ')
                return redirect('/lessons/progress/'+post_id)

            else:
                messages.info(request, 'الكود الذي ادخلته غير صالح او مستخدم من قبل')
                return redirect('/lessons/'+post_id)
            
    else:
        return redirect('/lessons')
    




@login_required(login_url='register')
def chapter_code_charge(request):
    if User.objects.filter(username=request.user.username).first():
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        notifications_count = Notification.objects.filter(username=request.user.username).count()
    else:
        user_profile = ''
        notifications_count = ''



    if request.method == 'POST':
        code = request.POST['code']
        chapter_id = request.POST['chapter-id']
        chapter = Chapter.objects.get(id=chapter_id)
        chapter_price = chapter.price

        if Code.objects.filter(code_id=code).first():
            valid_code = Code.objects.get(code_id=code)
            valid_code_money = valid_code.money
            user_profile.money = user_profile.money + valid_code_money

            user_profile.save()
            user_object.save()

            new_activity = Activity.objects.create(username=request.user.username , activity_type='charge' ,purchase_type='code' , wallet=user_profile.money , money=valid_code_money)
            new_notification = Notification.objects.create(username=request.user.username , activity_type='charge' ,purchase_type='code' , wallet=user_profile.money , money=valid_code_money)
            valid_code.active = False
            valid_code.student = request.user.username
            valid_code.save()

            lesson_price = chapter_price
            
            if user_profile.money < chapter_price:
                messages.info(request, 'للاسف ليس لديك رصيد كافي في المحفظة لشراء هذا الفصل')
                return redirect('/chapters/'+ chapter_id)
            else:
                new_buy = BuyChapter.objects.create(chapter_id=chapter_id, username=request.user.username , name=user_profile.name , image=user_profile.image , method='code')
                new_buy.save()

                chapter_lectures = ChapterLecture.objects.filter(chapter_id=chapter.id)
                for x in chapter_lectures:
                    if BuyLesson.objects.filter(post_id=x.lecture_id , username=request.user.username).first():
                        nothing = 'do nothing'
                    else:
                        purchase_lectures = BuyLesson.objects.create(post_id=x.lecture_id , username=request.user.username , name=user_profile.name , image=user_profile.image , method='chapter')
                        purchase_lectures.save()


                chapter_price = chapter.price
                user_profile.money = user_profile.money-chapter_price
                user_profile.no_of_buys = user_profile.no_of_buys+1

                chapter.no_of_buys = chapter.no_of_buys+1
                chapter.save()
            
                user_profile.save()
                new_activity = Activity.objects.create(username=request.user.username , activity_type='purchase' ,purchase_type='code' , wallet=user_profile.money , lesson_name=chapter.title , money=chapter_price)
                new_notification = Notification.objects.create(username=request.user.username , activity_type='withdraw' ,purchase_type='code' , wallet=user_profile.money , lesson_name=chapter.title , money=chapter_price)
                new_notification = Notification.objects.create(username=request.user.username , activity_type='purchase' ,purchase_type='code' , wallet=user_profile.money , lesson_name=chapter.title , money=chapter_price)

                messages.info(request, ' تم شراء المحاضرة بنجاح ')
                return redirect('/chapters/progress/'+chapter_id)
        else:
            if chapter.code == code:

                new_buy = BuyChapter.objects.create(chapter_id=chapter_id, username=request.user.username , name=user_profile.name , image=user_profile.image , method='chapter_code')
                new_buy.save()

                chapter_lectures = ChapterLecture.objects.filter(chapter_id=chapter.id)
                for x in chapter_lectures:
                    if BuyLesson.objects.filter(post_id=x.lecture_id , username=request.user.username).first():
                        nothing = 'do nothing'
                    else:
                        purchase_lectures = BuyLesson.objects.create(post_id=x.lecture_id , username=request.user.username , name=user_profile.name , image=user_profile.image , method='chapter')
                        purchase_lectures.save()

                user_profile.no_of_buys = user_profile.no_of_buys+1

                chapter.no_of_buys = chapter.no_of_buys+1
                chapter.save()
                user_profile.save()
                new_activity = Activity.objects.create(username=request.user.username , activity_type='purchase' ,purchase_type='code' , wallet=user_profile.money , lesson_name=chapter.title , money='0')
            
                new_notification = Notification.objects.create(username=request.user.username , activity_type='purchase' ,purchase_type='code' , wallet=user_profile.money , lesson_name=chapter.title , money='0')

                messages.info(request, ' تم شراء الفصل بنجاح ')
                return redirect('/chapters/progress/'+chapter_id)

            else:
                messages.info(request, 'الكود الذي ادخلته غير صالح او مستخدم من قبل')
                return redirect('/chapters/'+chapter_id)
            
    else:
        return redirect('/lessons')