from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework . response import Response
from .models import Users,Members
from . serializer import UserSerializer,MemberSerializers
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])

def index(request) : 
    det=Users.objects.all()
    serl=UserSerializer(det,many=True)
    return Response(serl.data)
    return JsonResponse(serl.data,safe=False)

@api_view(['POST'])
def adduser(request):
    serl=UserSerializer(data=request.data)
    if serl.is_valid(): 
        serl.save()
        return JsonResponse({'message':'data inserted succesfully'})
    else:
        print('form not valid')

@api_view(['PUT'])
def updateuser(request,uid):
    usr=Users.objects.get(id=uid) 
    serl=UserSerializer(usr,data=request.data)  
    print(serl)
    if serl.is_valid():
        serl.save()     
        return JsonResponse({'message':'updated succesffully'})
    else:
        print('form not valid')

@api_view(['DELETE'])
def deleteuser(request,uid):
    usr=Users.objects.get(id=uid)
    serl=UserSerializer(usr)
    serl.delete(usr)
    print('ser',serl)

          


def reg(request):
    if request.method=='POST':
        uname=request.POST['name']
        umail=request.POST['email']
        mob=request.POST['phone']

        New=Users.objects.create(
            name=uname,email=umail,mobile=mob
        )
    return render(request,'apis/user.html')    


class MembersView(APIView):
  permission_classes=(IsAuthenticated, )

  def post(self,request,*args,**kwargs):
      serl=MemberSerializers(data=request.data)
      if serl.is_valid():
          serl.save()
          return Response('data saved')
      else:
          return Response(serl.errors)
      
  def get(self,request,*args,**kwargs):
      user=Members.objects.all()
      serl=MemberSerializers(user,many=True)
      return Response(serl.data)

      
          
      
