from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreateForm, SignUpForm
from django.contrib.auth import login,logout
from users.models import User
from django.contrib import messages

def check_view(request):
    return render(request, 'accounts/check.html')

def signup_view(request):
    #get 요청시 html응답
    if request.method == 'GET':
        form = SignUpForm
        context ={'form':form}
        return render(request, 'accounts/signup.html',context)
    else:
        #post 요청시 데이터 확인 후 회원 생성
        form = SignUpForm(request.POST)
        if User.objects.filter(username= request.POST['username']).exists():
            messages.add_message(request, messages.INFO, "아이디 중복")

        if form.is_valid():
            #회원가입 처리
            instance = form.save()
            return redirect('accounts:login')# 미완성 부분 index를 나중에 추가해야함.
        else:
            #리다이렉트
            return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    #get, post 분리
    if request.method == 'GET':
        #로그인 html응답
        return render(request, 'accounts/login.html', {'form':AuthenticationForm()})
    else:
        #데이터 유효성 검사
        form= AuthenticationForm(request, request.POST)

        if form.is_valid():
            #비즈니스 로직 처리- 로그인 처리
            login(request, form.user_cache)
            #응답
            return redirect('accounts:check')#index 추가 필요
        else:
            #비즈니스 로직 처리 - 로그인 실패
            #응답
            
            return render(request, 'accounts/login.html', {'form': form})
    
def logout_view(request):
    #데이터 유효성 검사
    if request.user.is_authenticated:
        logout(request)
        #비즈니스 로직 처리 - 로그아웃
        #응답
        return redirect('accounts:check')
        
        
    