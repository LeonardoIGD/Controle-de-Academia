from django.urls import path, include
from rest_framework import routers

from users.api.viewsets import InstructorProfileViewSet, StudentProfileViewSet

router = routers.DefaultRouter()
router.register(r'instructor', InstructorProfileViewSet, basename='instructor-api')
router.register(r'student', StudentProfileViewSet, basename='student-api')

urlpatterns = [
    path('', include(router.urls)),
]
