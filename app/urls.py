from django.urls import path,include
from . import views
urlpatterns = [
    path("" , views.HomePage,name="home"),
    path("signup/" , views.SignupPage,name="Signup"),
    path("register/" , views.RegisterUser,name='register'),
    path("otppage/" , views.OtpPage,name='otppage'),
    path("otp/" , views.OtpVerify , name = 'otp'),
    



]