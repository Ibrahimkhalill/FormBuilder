from django.urls import path
from .import views

urlpatterns = [
    path('register/',views.Signup,name="signup"),
    path('',views.Login,name="login"),
    path('home/',views.home,name="home"),

]
