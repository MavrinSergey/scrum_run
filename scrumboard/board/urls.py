from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

from . import views
from .views import RegistrationViewSet, TaskViewSet

"""создаем объект router на основе класса SimpleRouter"""
router = routers.SimpleRouter()
"""регистрируем в нем класс ViewSet"""
router.register(r'task', TaskViewSet)  # сдесь генерируется весь набор маршрутов


"""маршрутизатор получает запрос и предает его тому представлению которое связано с этим запросом"""
urlpatterns = [
    path('', views.index, name='index'),

    path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/task/

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # запрос access и refresh токенов
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # для получения нового access с помощью refresh
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/user/', RegistrationViewSet.as_view(), name='registration'),

]
