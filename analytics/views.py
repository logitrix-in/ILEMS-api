# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from ILEMSapi.db import DB


from account.permissions import HasPermission
from analytics.models import FIR
from datetime import datetime, timedelta
from analytics.pagination import StandardResultsSetPagination

from analytics.serializer import FIRSerializer
from django.core.cache import cache

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
        db = DB['analytics_fir']
            
        

        # Yearly Trends

        available_years = db.distinct("year")  # Get unique years
        yearly_trends = []

        for year in available_years:
            yearly_trends.append({
                "year": year,
                "total": db.count_documents({"year": year})
            })

        # Last Month Count

        last_month = datetime.now() - timedelta(days=30)
        current_year = datetime.now().year
        last_month_count = db.count_documents({
            "registered_on": {"$gte": last_month},
            "year": current_year
        })

        # Last 7 Days Count

        last_week = datetime.now() - timedelta(days=7)
        last_7_days_count = db.count_documents({
            "registered_on": {"$gte": last_week},
            "year": current_year
        })

        # Last Year

        last_year = datetime.now().year - 1
        last_year_count = db.count_documents({"year": last_year})

        # Crime Rates per District

        unique_districts = db.distinct("district")
        crime_rates = []

        for district in unique_districts:
            crime_rates.append({
                "district": district,
                "total": db.count_documents({"district": district})
            })
        #  Crime rates per district last month
        
        crime_rates_last_month = []
        for district in unique_districts:
            crime_rates_last_month.append({
                "district": district,
                "total": db.count_documents({"district": district, "registered_on": {"$gte": last_month}})
            })
        max_total_dict = max(crime_rates_last_month, key=lambda x: x["total"])
        
        age_distribution_of_victims_and_accused = []
        for i in range(0, 50, 10):
            age_distribution_of_victims_and_accused.append({
                "age": f"{i}-{i+9}",
                "victims": db.count_documents({"victim_age": {"$gte": i, "$lt": i+10}}),
                "accused": db.count_documents({"accused_age": {"$gte": i, "$lt": i+10}})
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
                        "crime_rates_district":crime_rates,
                        
                    }
                },
                "hotspot":max_total_dict,
                "age_distribution_of_victims_and_accused":age_distribution_of_victims_and_accused
                
            }
        )