from django.urls import path
from .views import Dashboard, FIRList, Incidents, Resolved

urlpatterns = [
    path("", Dashboard.as_view()),
    path("test/", FIRList.as_view()),
    path("incidents/", Incidents.as_view()),
    path("resolved-unresolved/", Resolved.as_view()),
]
