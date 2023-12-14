from rest_framework import routers

from myapp.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
