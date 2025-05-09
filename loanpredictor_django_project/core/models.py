from django.db import models
from django.contrib.auth.models import User

class PredictionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Gender = models.CharField(max_length=10)
    Married = models.CharField(max_length=10)
    Dependents = models.CharField(max_length=5)
    Education = models.CharField(max_length=20)
    Self_Employed = models.CharField(max_length=10)
    LoanAmount = models.FloatField()
    Loan_Amount_Term = models.FloatField()
    Credit_History = models.FloatField()
    Property_Area = models.CharField(max_length=20)
    TotalIncome = models.FloatField()
    Prediction = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
