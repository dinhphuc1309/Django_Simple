from rest_framework import routers

from profiles.viewsets import ProfileViewSet

router = routers.DefaultRouter()
router.register('profiles',ProfileViewSet)