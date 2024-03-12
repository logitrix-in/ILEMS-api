# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from account.permissions import HasPermission
from analytics.models import FIR

class Dashboard(APIView):
    permission_classes=[HasPermission]
    def get(self, request):
        db = FIR.objects.all()

        # Yearly Trends

        available_year = list(set(db.values_list("year", flat=True)))
        yearly_trends = []

        for year in available_year:
            yearly_trends.append({
                "year": year,
                "total": db.filter(year=year).count()
            })
        

        return Response(
            {
                "FIR":{
                    "total":db.count(),
                    "last_7_days":20,
                    "last_month":80
                },
                "trends":{
                    "fir":{
                        "yearly_trends":yearly_trends
                    }
                }
                
            }
        )