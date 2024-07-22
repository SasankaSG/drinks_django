from rest_framework import serializers # type: ignore
from .models import drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = drink
        fields = ['id', 'name', 'description']