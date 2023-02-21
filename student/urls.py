from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
path('student_home',views.student_home_page,name='std_hom'),
path('pay_fees',views.pay_fee_page,name='pay_fee'),
path('view_report_card/<int:eid>',views.view_report_card_page,name='view_report_card'),
path('selectexam',views.selectexam,name='selectexam'),
path('changestatus/<int:feeid>',views.changefeesstatus,name='changefees')

]

