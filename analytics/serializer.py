from rest_framework.serializers import ModelSerializer

from analytics.models import FIR

class FIRSerializer(ModelSerializer):
    class Meta:
        model = FIR
        fields = "__all__"