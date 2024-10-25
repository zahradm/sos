from rest_framework import serializers
from .models import PersonalInfo, InsurerInfo, PolicyholderInfo, InsuranceInfo, PlanInfo, InsuredInfo

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'

class InsurerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurerInfo
        fields = '__all__'

class PolicyholderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyholderInfo
        fields = '__all__'

class InsuranceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceInfo
        fields = '__all__'

class PlanInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanInfo
        fields = '__all__'

class InsuredInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuredInfo
        fields = '__all__'
