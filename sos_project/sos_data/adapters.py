class HekmatInsuranceAdapter:

    def adapt_personal_info(self, data):
        return {
            "first_name": data.get("f_name"),
            "last_name": data.get("l_name"),
            "email": data.get("email"),
            "mobile": data.get("mobile"),
            "national_id": data.get("national_id"),
            "birth_date": data.get("birth_date"),
            "father_name": data.get("father_name"),
            "issuance_place": data.get("issuance_place")
        }

    def adapt_insurer_info(self, data):
        return {
            "name": data.get("name"),
            "unique_id": data.get("unique_id")
        }

    def adapt_policyholder_info(self, data):
        return {
            "name": data.get("name"),
            "unique_id": data.get("unique_id")
        }

    def adapt_insurance_info(self, data):
        return {
            "start_date": data.get("start_date"),
            "end_date": data.get("end_date"),
            "policy_number": data.get("policy_number"),
            "approval_date": data.get("approval_date")
        }

    def adapt_plan_info(self, data):
        return {
            "name": data.get("name"),
            "policy_number": data.get("policy_number"),
            "unique_id": data.get("unique_id")
        }

    def adapt_insured_info(self, data):
        return {
            "unique_id": data.get("unique_id")
        }
