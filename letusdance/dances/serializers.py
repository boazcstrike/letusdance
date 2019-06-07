from rest_framework import serializers
from dances.models import Dance

# Dance serializer
class DanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dance
        fields = '__all__'