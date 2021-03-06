from django.urls import path
from . import views


urlpatterns =[

     path('',views.Index,name="index_page"),
     path('signup/',views.Signup,name="register_user"),
     path('verify_phone/<code>/<phone>',views.verify_ph,name='verify_phone'),
     path('send/<phone>',views.Send,name="send_otp"),
     path('images/<username>',views.CameraLand,name="camera_landing"),
     path('get/images/front/<username>',views.CameraFront,name="camera_record"),
     path('get/images/sideways/<username>',views.CameraSide,name="camera_sideways"),
     path('login',views.Login,name='login'),
     path('dashboard/<code>/<user>',views.Dashboard,name="dashboard"),
     path('logout/<user>',views.Logout,name='logout_user'),
     path('reminders/<user>',views.RemindUser,name='remind_user'),
     path('show/reminders/<user>',views.ShowReminders,name='show_remiders'),
     path('payment_dashboard',views.PayDashboard,name="payment_dashboard"),
     path('payment_page/usercase',views.Pay,name="payment_page"),
     path('final/payment/<user>',views.Proceed,name="proceed_pay"),
     path('payment_verify/<code>/<username>',views.PaymentVerify,name="payment_verify"),
     path('payment_details/<code>/<username>',views.PaymentDetails,name="payment_details"),
     path('payment/success',views.PaymentSuccess,name="success"),
     path('assosiate/with/<username>',views.AddEUser,name="assosiate_user"),


]
