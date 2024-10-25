from django.contrib import admin
from django.urls import path
from sos_data.views import InsuranceDataView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/insurance-data/', InsuranceDataView.as_view(), name='insurance-data'),
]
