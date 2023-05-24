import core.views
from . import views
from django.urls import path

import activity.views



#Views
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard-page'),
    path('dashboard/lectures' , views.dashboard_lectures , name="lectures"),
    path('dashboard/lecture/<slug:slug>' , views.dashboard_lesson , name="lesson-page"),

    path('dashboard/chapters' , views.dashboard_chapters , name="chapters"),
    path('dashboard/chapters/<slug:slug>' , views.dashboard_chapter_details , name="chapter-details"),


    path('groups/invite' , views.invite_group , name="invite-group"),

    path('wallet/recharge', views.charge_wallet_code, name='wallet-recharge-code'),
    path('wallet/requests', views.wallet_requests, name='wallet-requests'),

    path('wallet/code-charge/request', views.code_charge, name='code-recharge'),

    path('purchase-error', views.money_error, name='money-error'),

    path('wallet/statement', core.views.account_activity, name='account-activity'),
    path('wallet/payments', core.views.account_payment, name='account-payment'),
    path('student/results', core.views.account_results, name='student-results'),
]



