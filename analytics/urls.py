from django.urls import path
from .views import Dashboard,FIRList

urlpatterns = [
    path("",Dashboard.as_view()),
    path("test/",FIRList.as_view())

    
]
