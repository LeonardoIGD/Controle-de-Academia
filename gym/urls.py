from django.urls import path, include
from rest_framework import routers

from gym.api.viewsets import EnrollmentViewSet, PlanViewSet

router = routers.DefaultRouter()
router.register(r'enrollement', EnrollmentViewSet, basename='enrollement-api')
router.register(r'plan', PlanViewSet, basename='plan-api')

urlpatterns = [
    path('', include(router.urls)),
]
