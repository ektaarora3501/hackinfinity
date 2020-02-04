from django.urls import path
from . import views


urlpatterns =[

     path('',views.Index,name="index_page"),
     path('signup/',views.Signup,name="register_user"),
     path('verify_phone/<code>/<phone>',views.verify_ph,name='verify_phone'),
     path('send/<phone>',views.Send,name="send_otp"),
     path('front/images/<username>',views.CameraLand,name="camera_landing"),
     path('get/images/<username>',views.CameraRecord,name="camera_record"),
     path('login',views.Login,name='login'),
     path('dashboard/<code>/<user>',views.Dashboard,name="dashboard"),
     path('logout/<user>',views.Logout,name='logout_user'),


]
