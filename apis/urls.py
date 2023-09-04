from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token    

app_name = 'apis'

urlpatterns = [
     path('index',views.index,name='index'),
     path('reg',views.reg,name='reg'),
     path('add',views.adduser,name='add'),
     path('update/<int:uid>',views.updateuser,name='update'),
     path('delete/<int:uid>',views.deleteuser,name='delete'),
     path('postclass',views.MembersView.as_view(),name='post'),
     path('obtain',obtain_auth_token,name='obtain')


]
