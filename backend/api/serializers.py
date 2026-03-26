from rest_framework import serializers
from .models import RepairRequest

class RepairRequestSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(
        format="%d %b %Y, %I:%M %p", read_only=True
    )
    class Meta:
        model  = RepairRequest
        fields = '__all__'
        read_only_fields = ['id', 'timestamp', 'status']