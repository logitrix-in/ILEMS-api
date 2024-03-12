# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from account.permissions import HasPermission

class Dashboard(APIView):
    permission_classes=[HasPermission]
    def get(self, request):
        return Response(
            {

            }
        )