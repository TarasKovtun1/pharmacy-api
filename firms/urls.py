from django.urls import path
from .views import FirmListView

urlpatterns = [
    path('firms/', FirmListView.as_view(), name='firm-list'),
]