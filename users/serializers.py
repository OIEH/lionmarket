from rest_framework import serializers
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter, DefaultAccountAdapter
from django.core.exceptions import ValidationError as DjangoValidationError



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username', 'email', 'password', 'phone', 'address']
    def get_cleaned_data(self):
        return{
            'username':self.validated_data.get('username',''),
            'password':self.validated_data.get('password',''),
            'email':self.validated_data.get('email',''),
            'phone':self.validated_data.get('phone',''),
            'address':self.validated_data.get('address',''),
        }
    def save(self,request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user,self, commit=False)
        if 'password' in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data['password'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
                )
            user.save()
            return user
   
        