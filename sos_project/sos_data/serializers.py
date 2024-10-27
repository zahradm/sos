from rest_framework import serializers
from .models import PersonalInfo, InsurerInfo, PolicyholderInfo, InsuranceInfo, PlanInfo, InsuredInfo
from django.core.validators import RegexValidator, EmailValidator
from datetime import datetime

class PersonalInfoSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()])
    mobile = serializers.CharField(
        validators=[RegexValidator(regex=r'^\d{11}$', message="Mobile number must be exactly 11 digits.")])
    national_id = serializers.CharField(
        validators=[RegexValidator(regex=r'^\d{10}$', message="National ID must be exactly 10 digits.")])

    class Meta:
        model = PersonalInfo
        fields = '__all__'

class InsurerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurerInfo
        fields = '__all__'

    def validate(self, data):
        # Validate that start date is before end date
        if data.get('start_date') and data.get('end_date'):
            if data['start_date'] >= data['end_date']:
                raise serializers.ValidationError("Start date must be before end date.")
        return data

class PolicyholderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyholderInfo
        fields = '__all__'

class InsuranceInfoSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    class Meta:
        model = InsuranceInfo
        fields = '__all__'

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("Insurance start date must be before end date.")
        return data

class PlanInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanInfo
        fields = '__all__'

class InsuredInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuredInfo
        fields = '__all__'
