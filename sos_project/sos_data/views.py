from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from .serializers import (
    PersonalInfoSerializer,
    InsurerInfoSerializer,
    PolicyholderInfoSerializer,
    InsuranceInfoSerializer,
    PlanInfoSerializer,
    InsuredInfoSerializer)
from .adapters import HekmatInsuranceAdapter, DefaultInsuranceAdapter


class InsuranceDataView(APIView):

    def post(self, request):
        try:

            insurance_provider = request.data.get("insurer_info", {}).get("name")

            if insurance_provider == "Hekmat":
                adapter = HekmatInsuranceAdapter()
            else:
                adapter = DefaultInsuranceAdapter()

            # Personal Information
            personal_info_data = adapter.adapt_personal_info(request.data.get("personal_info", {}))
            personal_info_serializer = PersonalInfoSerializer(data=personal_info_data)
            personal_info_serializer.is_valid(raise_exception=True)
            personal_info = personal_info_serializer.save()

            # Insurer Information
            insurer_info_data = adapter.adapt_insurer_info(request.data.get("insurer_info", {}))
            insurer_info_serializer = InsurerInfoSerializer(data=insurer_info_data)
            insurer_info_serializer.is_valid(raise_exception=True)
            insurer_info = insurer_info_serializer.save()

            # Policyholder Information
            policyholder_info_data = adapter.adapt_policyholder_info(request.data.get("policyholder_info", {}))
            policyholder_info_serializer = PolicyholderInfoSerializer(data=policyholder_info_data)
            policyholder_info_serializer.is_valid(raise_exception=True)
            policyholder_info = policyholder_info_serializer.save()

            # Insurance Information
            insurance_info_data = adapter.adapt_insurance_info(request.data.get("insurance_info", {}))
            insurance_info_serializer = InsuranceInfoSerializer(data=insurance_info_data)
            insurance_info_serializer.is_valid(raise_exception=True)
            insurance_info = insurance_info_serializer.save()

            # Plan Information
            plan_info_data = adapter.adapt_plan_info(request.data.get("plan_info", {}))
            plan_info_serializer = PlanInfoSerializer(data=plan_info_data)
            plan_info_serializer.is_valid(raise_exception=True)
            plan_info = plan_info_serializer.save()

            # Insured Information
            insured_info_data = adapter.adapt_insured_info(request.data.get("insured_info", {}))
            insured_info_data['personal_info'] = personal_info.id
            insured_info_data['policyholder_info'] = policyholder_info.id
            insured_info_data['insurance_info'] = insurance_info.id
            insured_info_data['plan_info'] = plan_info.id

            insured_info_serializer = InsuredInfoSerializer(data=insured_info_data)
            insured_info_serializer.is_valid(raise_exception=True)
            insured_info = insured_info_serializer.save()

            return Response({"message": "Data saved successfully"}, status=status.HTTP_201_CREATED)

        except serializers.ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"errors": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
