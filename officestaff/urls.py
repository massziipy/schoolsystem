from django.urls import path
from . import views

app_name = 'office_staff'

urlpatterns = [
    path('staffhome',views.staffhome,name='staffhome'),
     path('enquiries',views.enquiries,name='enquiries')

]
