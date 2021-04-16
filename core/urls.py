from django.urls import path
from django.contrib.auth import views as auth_views
from .views import IndexView#LoginView SignupView, LogoutView
from .import  views
from allauth import account
from allauth import socialaccount



urlpatterns=[
    path('', IndexView.as_view(), name='index'),
    path('register/', views.register, name='register'),
    path('teacher_register/', views.teacher_register.as_view(), name='teacher_register'),
    path('student_register/', views.student_register.as_view(), name='student_register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #path('', SignupView.as_view(), name='signup'),
   #path('', LogoutView.as_view(), name='logout'),
]

