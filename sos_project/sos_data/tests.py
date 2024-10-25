from django.test import TestCase
from rest_framework.test import APIClient
from sos_data.models import (
    PersonalInfo, InsurerInfo, PolicyholderInfo, InsuranceInfo, PlanInfo, InsuredInfo
)

from sos_data.adapters import HekmatInsuranceAdapter


class ModelsTestCase(TestCase):

    def setUp(self):
        # Set up initial test data
        self.personal_info = PersonalInfo.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            mobile="1234567890",
            national_id="1234567890",
            birth_date="1990-01-01",
            father_name="Robert",
            issuance_place="Tehran"
        )

        self.insurer_info = InsurerInfo.objects.create(
            name="Hekmat Insurance",
            unique_id="HEK-001"
        )

    def test_personal_info_creation(self):
        self.assertEqual(self.personal_info.first_name, "John")
        self.assertEqual(self.personal_info.last_name, "Doe")
        self.assertTrue(isinstance(self.personal_info, PersonalInfo))

    def test_insurer_info_creation(self):
        self.assertEqual(self.insurer_info.name, "Hekmat Insurance")
        self.assertEqual(self.insurer_info.unique_id, "HEK-001")
        self.assertTrue(isinstance(self.insurer_info, InsurerInfo))
class HekmatInsuranceAdapterTestCase(TestCase):

    def setUp(self):
        self.adapter = HekmatInsuranceAdapter()
        self.raw_data = {
            "personal_info": {
                "f_name": "John",
                "l_name": "Doe",
                "email": "john.doe@example.com",
                "mobile": "1234567890",
                "national_id": "1234567890",
                "birth_date": "1990-01-01",
                "father_name": "Robert",
                "issuance_place": "Tehran"
            }
        }

    def test_adapt_personal_info(self):
        adapted_data = self.adapter.adapt_personal_info(self.raw_data["personal_info"])
        expected_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "mobile": "1234567890",
            "national_id": "1234567890",
            "birth_date": "1990-01-01",
            "father_name": "Robert",
            "issuance_place": "Tehran"
        }
        self.assertEqual(adapted_data, expected_data)


class InsuranceDataViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.insurance_data = {
            "personal_info": {
                "f_name": "John",
                "l_name": "Doe",
                "email": "john.doe@example.com",
                "mobile": "1234567890",
                "national_id": "1234567890",
                "birth_date": "1990-01-01",
                "father_name": "Robert",
                "issuance_place": "Tehran"
            },
            "insurer_info": {
                "name": "Hekmat",
                "unique_id": "HEK-001"
            },
            "policyholder_info": {
                "name": "John Doe",
                "unique_id": "JD-123"
            },
            "insurance_info": {
                "start_date": "2024-01-01",
                "end_date": "2025-01-01",
                "policy_number": "POL-001",
                "approval_date": "2024-01-05"
            },
            "plan_info": {
                "name": "Basic Plan",
                "policy_number": "POL-001",
                "unique_id": "PLAN-001"
            },
            "insured_info": {
                "unique_id": "INS-001"
            }
        }

    def test_create_insurance_data(self):
        response = self.client.post('/api/insurance-data/', self.insurance_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['message'], "Data saved successfully")

    def test_invalid_insurance_data(self):
        # Missing required fields
        invalid_data = {
            "personal_info": {
                "f_name": "John",
                "email": "invalid-email"  # Missing fields
            }
        }
        response = self.client.post('/api/insurance-data/', invalid_data, format='json')
        self.assertEqual(response.status_code, 500)
        self.assertIn('errors', response.data)
