from dataclasses import fields
from .models import Users,Members
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        # fields = ('name','email')
        fields = '__all__'

    def delete(self, instance):
            instance.delete()

class MemberSerializers(serializers.ModelSerializer):
     class Meta:
          model= Members
          fields=('name','password')        


        