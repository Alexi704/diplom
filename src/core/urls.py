from django.urls import path

from core.views import LoginView, ProfileView, SignupView, UpdatePasswordView

urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),    # создание пользователя
    path('login', LoginView.as_view(), name='login'),   # вход пользователя
    path('profile', ProfileView.as_view(), name='profile'),  # изменение данных пользователя
    path('update_password', UpdatePasswordView.as_view(), name='update-password'),  # изменение пароля пользователя
]
