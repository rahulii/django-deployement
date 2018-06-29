from django.conf.urls import url
from userapp import views

app_name='userapp'

urlpatterns=[
url('register/',views.register,name='register'),
url('user_login/',views.user_login,name='user_login'),
#url('',views.index,name='index')
]
