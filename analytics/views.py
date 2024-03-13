# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


from account.permissions import HasPermission
from analytics.models import FIR
from datetime import datetime, timedelta
from analytics.pagination import StandardResultsSetPagination

from analytics.serializer import FIRSerializer

class FIRList(APIView):
    permission_classes=[HasPermission]
    def get(self, request):
        paginator = StandardResultsSetPagination()
        db = FIR.objects.all()
        page = paginator.paginate_queryset(db, request)
        if page is not None:
            serializer = FIRSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = FIRSerializer(db, many=True)
        return Response(
            FIRSerializer(db, many=True).data
        )
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
        
        
        #  Last Month Count
        
        last_month = datetime.now() - timedelta(days=30)
        current_year= datetime.now().year
        last_month_count = db.filter(registered_on__gte=last_month,year=current_year).count()

        #  Last 7 days Count

        last_week = datetime.now() - timedelta(days=7)
        current_year= datetime.now().year
        last_7_days_count = db.filter(registered_on__gte=last_week,year=current_year).count()
        
        # Last Year
        last_year = datetime.now().year
        last_year_count = db.filter(year=last_year).count()



        # Crime Rates per district

        unique_district = list(set(db.values_list("district", flat=True)))
        crime_rates = []

        for dis in unique_district:
            crime_rates.append({
                "district": dis,
                "total": db.filter(district=dis).count()
            })

        return Response(
            {
                "fir":{
                    "total":db.count(),
                    "last_7_days":last_7_days_count,
                    "last_month":last_month_count,
                    "last_year":last_year_count
                },
                "trends":{
                    "fir":{
                        "yearly_trends":yearly_trends,
                        "crime_rates_district":crime_rates
                    }
                }
                
            }
        )