from rest_framework import routers
from .api import DanceViewSet

router = routers.DefaultRouter()
router.register('api/dances', DanceViewSet, 'dances')

urlpatterns = router.urls