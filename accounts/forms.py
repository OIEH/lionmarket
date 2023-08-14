from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django.http import JsonResponse


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields ='__all__'


class UserCreateForm(forms.ModelForm):
    password1= forms.CharField(label= 'Password', widget=forms.PasswordInput)
    password2= forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields= ('username', 'email', 'phone', 'address')
    
    def clean_password2(self):
        password1= self.cleaned_data.get('password1')
        password2= self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            return JsonResponse({'message': '비밀번호_확인_오류'}, status=400)
        return password2
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'phone','address','password1', 'password2']