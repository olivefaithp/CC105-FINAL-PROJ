# core/forms.py
from django import forms

class PredictionForm(forms.Form):
    Gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    Married = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    Dependents = forms.ChoiceField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3+', '3+')])
    Education = forms.ChoiceField(choices=[('Graduate', 'Graduate'), ('Not Graduate', 'Not Graduate')])
    Self_Employed = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    LoanAmount = forms.FloatField()
    Loan_Amount_Term = forms.FloatField()
    Credit_History = forms.FloatField()
    Property_Area = forms.ChoiceField(choices=[('Urban', 'Urban'), ('Rural', 'Rural'), ('Semiurban', 'Semiurban')])
    TotalIncome = forms.FloatField()
