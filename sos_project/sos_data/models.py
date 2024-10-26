from django.db import models

class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ و ساعت ثبت
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ و ساعت تغییر

    class Meta:
        abstract = True

class PersonalInfo(TimestampMixin):
    first_name = models.CharField(max_length=100)  # نام
    last_name = models.CharField(max_length=100)  # نام خانوادگی
    email = models.EmailField(unique=True)  # ایمیل
    mobile = models.CharField(max_length=15, unique=True)  # شماره موبایل
    national_id = models.CharField(max_length=10, unique=True)  # کد ملی
    birth_date = models.DateField()  # تاریخ تولد
    father_name = models.CharField(max_length=100, blank=True)  # نام پدر
    issuance_place = models.CharField(max_length=100, blank=True)  # محل صدور

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class InsurerInfo(TimestampMixin):
    name = models.CharField(max_length=100)  # نام بیمه‌گر
    unique_id = models.CharField(max_length=50, unique=True)  # شناسه یکتای بیمه‌گر

    def __str__(self):
        return self.name

class PolicyholderInfo(TimestampMixin):
    name = models.CharField(max_length=100)  # نام بیمه‌گذار
    unique_id = models.CharField(max_length=50, unique=True)  # شناسه یکتای بیمه‌گذار

    def __str__(self):
        return self.name

class InsuranceInfo(TimestampMixin):
    start_date = models.DateField()  # تاریخ شروع بیمه‌نامه
    end_date = models.DateField()  # تاریخ پایان بیمه‌نامه
    policy_number = models.CharField(max_length=50, unique=True)  # شناسه یکتای بیمه‌نامه
    approval_date = models.DateField(null=True, blank=True)  # تاریخ تایید

    def __str__(self):
        return self.policy_number

class PlanInfo(TimestampMixin):
    policy_number = models.CharField(max_length=50)  # شماره بیمه نامه
    name = models.CharField(max_length=100)  # نام طرح
    unique_id = models.CharField(max_length=50, unique=True)  # شناسه یکتای طرح

    def __str__(self):
        return self.name

class InsuredInfo(TimestampMixin):
    unique_id = models.CharField(max_length=50, unique=True)  # شناسه یکتای بیمه‌شده
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)  # اطلاعات شخصی
    policyholder_info = models.ForeignKey(PolicyholderInfo, on_delete=models.CASCADE)  # بیمه‌گذار
    insurance_info = models.ForeignKey(InsuranceInfo, on_delete=models.CASCADE)  # بیمه‌نامه
    plan_info = models.ForeignKey(PlanInfo, on_delete=models.CASCADE)  # طرح

    def __str__(self):
        return self.unique_id
