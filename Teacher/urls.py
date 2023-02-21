from django.urls import path
from . import views

app_name = 'Teacher'

urlpatterns = [
    
path('teacher_home',views.teacher_home_page,name='tchr'),
path('add_student',views.add_student_page,name='ad_stdnt'),
path('view_student',views.view_student_page,name='view_student'),
path('add_mark',views.add_mark_page,name='ad_mark'),
path('create_progress_card',views.progress_card,name='pr_report'),
path('assignmarks/<int:clsid>',views.assignmarks,name='assignmarks'),


]