# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class Dashboard(APIView):
    def get(self, request):
        return Response(
            {"message": "Welcome to the dashboard"}
        )