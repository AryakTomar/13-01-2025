# from django.urls import path, include
# from . import views
# from .views import CustomerAPI
# #from myproject.customer import views
# from rest_framework.routers import DefaultRouter
# from .views import CustomerAPI
# from .views import UserAPI, LoginAPI, ForgotPasswordAPI
# from .views import TelegramWebhook
# from .views import SendOTPTelegramAPI, VerifyTelegramOTP

# urlpatterns = [
#     path('',CustomerAPI.as_view(),name='root'),
#     path('customer/',views.CustomerAPI.as_view(),name='api'),
#     path('<int:id>/',CustomerAPI.as_view(),name='details'),
#     path('login/', LoginAPI.as_view()),
#     path('forgotpassword/', ForgotPasswordAPI.as_view()),
#     path('telegram-webhook/', TelegramWebhook.as_view()),
#     path('send-otp-telegram/', SendOTPTelegramAPI.as_view()),
#     path('verify-telegram-otp/', VerifyTelegramOTP.as_view()),
# ]

# ---------------------------------------------------

from django.urls import path
from . import views
from .views import CustomerAPI, LoginAPI, ForgotPasswordAPI
from .views import TelegramWebhook
from .views import SendOTPTelegramAPI, VerifyTelegramOTP

urlpatterns = [
    path('',CustomerAPI.as_view(), name = 'root'),
    path('user/',views.CustomerAPI.as_view(), name = 'customer_api'),
    path('<int:id>/',CustomerAPI.as_view(), name = 'detail'),
    path('login/', LoginAPI.as_view()),
    path('forgotpassword/', ForgotPasswordAPI.as_view()),
    path('telegram-webhook/', TelegramWebhook.as_view()),
    path('send-otp-telegram/', SendOTPTelegramAPI.as_view()),
    path('verify-telegram-otp/', VerifyTelegramOTP.as_view()),
]
