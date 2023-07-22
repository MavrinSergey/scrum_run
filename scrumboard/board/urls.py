from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from .views import RegistrationViewSet, TaskAPIList, TaskAPIUpdate, TaskAPIDestroy, ProjectViewSet, CompanyViewSet, \
    StatusUserProjectsViewSet, ProjectParticipantsViewSet

# router = routers.SimpleRouter()
# router.register(r'project', ProjectViewSet)
# router.register(r'company', CompanyViewSet)
# router.register(r'statususer', StatusUserProjectsViewSet)
# router.register(r'projectparticipants', ProjectParticipantsViewSet)


urlpatterns = [

    path('api/v1/task/', TaskAPIList.as_view()),
    path('api/v1/task/<int:pk>/', TaskAPIUpdate.as_view()),
    path('api/v1/taskdelete/<int:pk>/', TaskAPIDestroy.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/user', RegistrationViewSet.as_view({'get': 'list'})),
    # path('api/v1/', include(router.urls)),
    path('api/v1/project/', ProjectViewSet.as_view({'get': 'list'})),
    path('api/v1/company/', CompanyViewSet.as_view({'get': 'list'})),
    path('api/v1/statususer/', StatusUserProjectsViewSet.as_view({'get': 'list'})),
    path('api/v1/projectparticipants/', ProjectParticipantsViewSet.as_view({'get': 'list'}))
    # path('api/v1/projectlist/', ProjectViewSet.as_view({'get': 'list'})),
    # path('api/v1/projectdetail/<int:pk>/', ProjectViewSet.as_view({'put': 'update'})),
    # path('api/v1/board-auth/', include('rest_framework.urls')),
]
