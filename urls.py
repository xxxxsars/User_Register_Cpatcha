from django.conf.urls import include,url
from .views import register,login,logout,send_mail_test

urlpatterns = [
 url(r'^register/', register,name='register'),
 url(r'^login/',login,name="login"),
 url('^logout/',logout,name='logout'),
 url(r"^mail/",send_mail_test),
]

