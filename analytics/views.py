# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from account.permissions import HasPermission

class Dashboard(APIView):
    permission_classes=[HasPermission]
    def get(self, request):
        return Response(
            {
                "FIR":{
                    "total":100,
                    "last_7_days":20,
                    "last_month":80
                },
                
            }
        )