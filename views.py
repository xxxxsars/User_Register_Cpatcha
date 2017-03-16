from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm,LoginForm

#將url定義的name轉回網址
from django.core.urlresolvers import reverse


from django.core.mail import send_mail


def register(request):
    # 檢查用戶有否發出POST請求
    if request.method == "POST":

        # 從表單裡取得request裡的Post參數
        f = RegisterForm(request.POST)

        # 若表單的所有欄位皆填寫正確，取得裡面的資料
        if f.is_valid():
            # username = request.POST.get('username', '')
            # password = request.POST.get('password', '')
            # email = request.POST.get('email', '')

            username = request.POST['username']
            password = request.POST["password"]
            email = request.POST['email']

            # # 若帳號重覆，送出錯誤訊息並返回註冊頁面
            # if User.objects.filter(username=username).count():
            #     messages.error(request, '帳號已重複，請填寫一個新的帳號名稱。')
            #     return HttpResponseRedirect('/user/register')
            #
            # #否則，利用從表單取得的資料建立新帳號，並前往登入後的頁面
            # else:
            user = User.objects.create_user(username, email, password)
            user.save()
            account = auth.authenticate(username=username, password=password)
            auth.login(request, account)
            susessful  ="註冊成功！3秒後跳回登入頁面"
            return render(request, 'register.html',locals())



     #若用戶並沒有發出POST請求，傳送之前建立的RegisterForm至註冊頁面
    else:
        f= RegisterForm()
        if request.user.is_authenticated():
            username = request.user.username
    return render(request,'register.html',locals())

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))


    elif request.method == "POST":

        # 從表單裡取得request裡的Post參數
        f = LoginForm(request.POST)

        # 若表單的所有欄位皆填寫正確，取得裡面的資料
        if f.is_valid():
            #
            username = request.POST['username']
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                 return render(request,'login.html',locals())

    else:
        f = LoginForm()
    return render(request,'login.html',locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))


def send_mail_test(request):
    email = '49990107@stust.edu.tw'
    user = User.objects.create_user(username='test13456', email=email)
    # user.is_confirmed  # False
    # send_mail(email, 'Use %s to confirm your email' % user.confirmation_key)
    # User gets email, passes the confirmation_key back to your server

    # user.confirm_email(user.confirmation_key)
    return HttpResponse ("GO")  # True