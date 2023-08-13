from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from users.models import User


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields ='__all__'


class UserCreateForm(UserBaseForm):
    password2= forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(label ='이메일')
    phone= forms.CharField(label='전화번호')
    address = forms.CharField(label='주소')
    class Meta(UserBaseForm.Meta):
        fields= ['username','email','phone','password', 'address']


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'phone','address','password1', 'password2']