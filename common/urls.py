from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
  path('home',views.home_page,name='hom'),
  path('about',views.about_page,name='abt'),
  path('contact',views.contact_page,name='cntct'),
  path('admission',views.admission_page,name='admsn'),
  path('registration',views.registration_form,name='rgstr'),
  path('login/<str:user>',views.login_page,name='login'),
  path('signup',views.signup_page,name='sign'),
  path('usertype',views.usertype,name='usertype'),
  path('logout/<str:user>',views.logout,name='logout')

]