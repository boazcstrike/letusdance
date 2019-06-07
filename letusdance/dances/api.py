from dances.models import Dance
from rest_framework import viewsets, permissions
from .serializers import DanceSerializer

# Dance Viewset
class DanceViewSet(viewsets.ModelViewSet):
    queryset = Dance.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DanceSerializer