from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
  path('home',views.home_page,name='hom'),
  path('about',views.about_page,name='abt'),
  path('contact',views.contact_page,name='cntct'),
  path('admission',views.admission_page,name='admsn'),
  path('registration',views.registration_form,name='rgstr'),
  path('login',views.login_page,name='lgn'),
  path('signup',views.signup_page,name='sign'),

]