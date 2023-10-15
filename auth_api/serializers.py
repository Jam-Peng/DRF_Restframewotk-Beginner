from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"  序列化全部屬性
        fields = ['id', 'username', 'email', 'password']

    def save(self, **kwargs):
        new_user = User.objects.create_user(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            password = self.validated_data['password'],
        )
        new_user.save()
        
        # 建立 token給新的用戶
        new_token = Token.objects.create(user=new_user)
    
