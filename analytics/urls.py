from django.urls import path
from .views import (
    Dashboard,
    FIRList,
    Incidents,
    Resolved,
    CrimeGroupCountAPIView,
    ComplaintModeAPIView,
    FIRProcessingAPIView,
    VictimAccusedAPI,
)

urlpatterns = [
    path("", Dashboard.as_view()),
    path("test/", FIRList.as_view()),
    path("incidents/", Incidents.as_view()),
    path("resolved-unresolved/", Resolved.as_view()),
    path("month-wise/", CrimeGroupCountAPIView.as_view()),
    path("complaint-mode/", ComplaintModeAPIView.as_view()),
    path("fir-processing/", FIRProcessingAPIView.as_view()),
    path("victim-accused/", VictimAccusedAPI.as_view()),
]
