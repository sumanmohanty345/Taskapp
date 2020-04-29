from rest_framework import serializers
from django.contrib.auth.models import User
from testApp.models import TaskModel
from django.contrib.auth import authenticate
class UserRegisterserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
    def Check_password(self, data):
        password=data.get("password","")
        if len(password) >= 8:
            return data
        else:
            raise serializers.ValidationError("Password Length must be more than 8")

class UserLoginSerializer(serializers.Serializer):
    email=serializers.CharField()
    password=serializers.CharField()
    def validate(self, data):
        email=data.get("email","")
        password=data.get("password","")
        if email and password :
            user=User.objects.get(email=email, password=password)
            print(user)
            if user:
                data['user'] =user
            else:
                raise serializers.ValidationError("Uneable to login With Credential")
        else:
            raise serializers.ValidationError("Must provide email and password both")
        return data
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskModel
        fields="__all__"
    def validate(self, data):
        list_status=['TODO','WIP','DONE']
        status=data.get("status")
        if status in list_status:
            return data
        else:
            raise serializers.ValidationError("Invalid status")

