from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InsuredPersonViewSet,
    InsuranceProviderViewSet,
    PolicyHolderViewSet,
    InsurancePolicyViewSet,
    InsurancePlanViewSet
)

router = DefaultRouter()
router.register(r'insured-persons', InsuredPersonViewSet)
router.register(r'insurance-providers', InsuranceProviderViewSet)
router.register(r'policy-holders', PolicyHolderViewSet)
router.register(r'insurance-policies', InsurancePolicyViewSet)
router.register(r'insurance-plans', InsurancePlanViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
