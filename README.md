1.Initial setting on terminal  

```
$git clone git@github.com:xxxxsars/User_Register_Cpatcha.git
$pip install  requirements.txt
```

2.Create your project and using managy.py to initial database
```
$startproject "your projectname"
$makemigration
```

3.Copy user_information dictionary in your project

4.In setting.py INATALL_APP append "user_information" and "captcha" like this
```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_infomation',
    'captcha',
)
```
5.On your urls.py  on urlpatterns list append your index page and named "index"
```python
from django.conf.urls import include

 urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/',here),
    url("^user/",include("user_infomation.urls")),
    url('^$',here,name='index'),
]
```

6.On your project creat views.py

```python
def here(request):
    return  HttpResponse("HI welcome ")
```

7.Run server and connect 127.0.0.1:8000/user/register will show like this

![](https://raw.githubusercontent.com/xxxxsars/User_Register_Cpatcha/master/git_img/register.png)
