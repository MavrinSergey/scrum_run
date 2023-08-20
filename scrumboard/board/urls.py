from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

from .views import RegistrationViewSet, TaskAPIList, TaskAPIUpdate, TaskAPIDestroy


urlpatterns = [
    # path('', index),
    path('api/v1/task/', TaskAPIList.as_view()),
    path('api/v1/task/<int:pk>/', TaskAPIUpdate.as_view()),
    path('api/v1/taskdelete/<int:pk>/', TaskAPIDestroy.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/user/', RegistrationViewSet.as_view(), name='registration'),

]
