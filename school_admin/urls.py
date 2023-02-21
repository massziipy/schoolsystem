from django.urls import path
from . import views

app_name = 'school_admin'

urlpatterns = [
path('admin_home',views.admin_home_page,name='admn'),
path('add_staff',views.add_staff_page,name='ad_staf'),
path('add_class',views.add_class_page,name='ad_cls'),
path('view_staff',views.view_staff_page,name='view_staf'),
path('view_student',views.view_student_page,name='view_student'),
path('assign_salary',views.salary_page,name='salary'),
path('add_division',views.adddvision,name='adddiv'),
path('addsubject',views.addsubjdect,name='addsub'),
path('addfees',views.addfees,name='addfees'),
]
