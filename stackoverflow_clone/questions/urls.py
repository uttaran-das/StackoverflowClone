from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('ask/', views.ask_question, name='ask_question'),
    path('answer/<int:question_id>/', views.answer_question, name='answer_question'),
    path('register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]