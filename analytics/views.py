# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from ILEMSapi.db import DB
from django.db.models import Count


from account.permissions import HasPermission
from analytics.models import FIR
from datetime import datetime, timedelta
from analytics.pagination import StandardResultsSetPagination

from analytics.serializer import FIRSerializer
from django.core.cache import cache


class FIRList(APIView):
    permission_classes = [HasPermission]

    def get(self, request):
        paginator = StandardResultsSetPagination()
        db = FIR.objects.all()
        page = paginator.paginate_queryset(db, request)
        if page is not None:
            serializer = FIRSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = FIRSerializer(db, many=True)
        return Response(FIRSerializer(db, many=True).data)


class Dashboard(APIView):
    permission_classes = [HasPermission]

    def get(self, request):
        db = DB["analytics_fir"]

        # Yearly Trends

        available_years = db.distinct("year")  # Get unique years
        yearly_trends = []

        for year in available_years:
            yearly_trends.append(
                {"year": year, "total": db.count_documents({"year": year})}
            )

        # Last Month Count

        last_month = datetime.now() - timedelta(days=30)
        current_year = datetime.now().year
        last_month_count = db.count_documents(
            {"registered_on": {"$gte": last_month}, "year": current_year}
        )

        # Last 7 Days Count

        last_week = datetime.now() - timedelta(days=7)
        last_7_days_count = db.count_documents(
            {"registered_on": {"$gte": last_week}, "year": current_year}
        )

        # Last Year

        last_year = datetime.now().year - 1
        last_year_count = db.count_documents({"year": last_year})

        # Crime Rates per District

        unique_districts = db.distinct("district")
        crime_rates = []

        for district in unique_districts:
            crime_rates.append(
                {
                    "district": district,
                    "total": db.count_documents({"district": district}),
                }
            )
        #  Crime rates per district last month

        crime_rates_last_month = []
        for district in unique_districts:
            crime_rates_last_month.append(
                {
                    "district": district,
                    "total": db.count_documents(
                        {"district": district, "registered_on": {"$gte": last_month}}
                    ),
                }
            )
        max_total_dict = max(crime_rates_last_month, key=lambda x: x["total"])

        age_distribution_of_victims_and_accused = []
        for i in range(0, 50, 10):
            age_distribution_of_victims_and_accused.append(
                {
                    "age": f"{i}-{i+9}",
                    "victims": db.count_documents(
                        {"victim_age": {"$gte": i, "$lt": i + 10}}
                    ),
                    "accused": db.count_documents(
                        {"accused_age": {"$gte": i, "$lt": i + 10}}
                    ),
                }
            )

        district_firs_count = []
        district_name = db.distinct("district")

        for distr in district_name:
            district_firs_count.append(
                {"district": distr, "total": db.count_documents({"district": distr})}
            )

        fir_type_count = []
        fir_types = db.distinct("fir_type")

        for firs in fir_types:
            fir_type_count.append(
                {"fir_type": firs, "total": db.count_documents({"fir_type": firs})}
            )

        return Response(
            {
                "fir": {
                    "total": db.count(),
                    "last_7_days": last_7_days_count,
                    "last_month": last_month_count,
                    "last_year": last_year_count,
                },
                "trends": {
                    "fir": {
                        "yearly_trends": yearly_trends,
                        "crime_rates_district": crime_rates,
                    }
                },
                "hotspot": max_total_dict,
                "age_distribution_of_victims_and_accused": age_distribution_of_victims_and_accused,
                "district_wise_count": district_firs_count,
                "crime_type_analysis": fir_type_count,
                # static data
                "fir_processing_analysis": {
                    "ongoing": 752,
                    "completed": db.count() - 752,
                },
                "Demographic Analysis": {
                    "Men": 45124,
                    "Women": 44156,
                    "Children": 42144,
                },
                "IO Performance": "Good",
                "victim_accused_counts": {
                    "victim": 1520,
                    "accused": 1210,
                },
                "arrest_conviction_rates": {
                    "arrested": 1010,
                    "convicted": 1000,
                },
                "complaint_mode_analysis": {
                    "online": 1240,
                    "offline": 2450,
                },
                "place_of_offence_analysis": max_total_dict,
                "act_section_analysis": {
                    "440A": 10,
                    "255B": 153,
                    "156C": 124,
                },
                "victim_counts_by_age_group": {
                    "under_18": 1245,
                    "above_18": 1456,
                    "above_60": 123,
                },
                "temporal_analysis": {
                    "Monday": 50,
                    "Tuesday": 15,
                    "Wednesday": 60,
                    "Thursday": 25,
                    "Friday": 60,
                    "Saturday": 100,
                    "Sunday": 90,
                },
            }
        )


class Incidents(APIView):
    def get(self, request):
        db = DB["analytics_fir"]
        fir_stages = db.distinct("crime_head_name")

        fir_type_count = []

        for firs in fir_stages:
            fir_type_count.append(
                {
                    "incident_type": firs,
                    "total": db.count_documents({"crime_head_name": firs}),
                }
            )

        return Response(
            {
                "incidents": fir_type_count,
            }
        )


class Resolved(APIView):
    def get(self, request):
        db = DB["analytics_fir"]
        fir_stages = db.distinct("fir_stage")
        resolved_stages = [
            "Abated",
            "BoundOver",
            "Compounded",
            "Convicted",
            "Dis/Acq",
            "False Case",
            "Other Disposal",
            "Pending Trial",
        ]
        resolved_count = 0
        total_count = 0
        for firs in fir_stages:
            curr_count = db.count_documents({"fir_stage": firs})
            total_count = total_count + curr_count
            if firs in resolved_stages:
                resolved_count = resolved_count + curr_count

        return Response(
            {
                "resolved": resolved_count,
                "unresolved": total_count - resolved_count,
            }
        )


class CrimeGroupCountAPIView(APIView):
    def get(self, request):
        # Filter data for the year 2023
        db = DB["analytics_fir"]
        response = {}
        for i in range(1, 13):
            data = db.find({"year": 2023, "month": i}, {"_id": False})
            response[i] = {}
            for j in data:
                response[i][j["crime_group_name"]] = (
                    response[i][j["crime_group_name"]] + 1
                    if j["crime_group_name"] in response[i]
                    else 1
                )

        return Response({"data": response})
