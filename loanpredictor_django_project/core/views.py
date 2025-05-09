from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PredictionLog
from .forms import PredictionForm

import pandas as pd
import joblib
import os

# Load model once
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'loan_approval_pipeline.pkl')
dataset_path = os.path.join(BASE_DIR, 'loan_sanction_train.csv')
model = joblib.load(model_path)
data = pd.read_csv(dataset_path)


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('predict')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('predict')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            df = pd.DataFrame([data])

            try:
                prediction_raw = model.predict(df)[0]
            except Exception as e:
                return render(request, 'predict.html', {
                    'form': form,
                    'error': f"Prediction failed: {e}"
                })

            # Map binary to label
            prediction_label = 'Approved' if prediction_raw == 1 else 'Rejected'

            # Friendly message
            if prediction_label == 'Approved':
                prediction_msg = "✅ Congratulations! Your loan is likely to be approved."
            else:
                prediction_msg = "❌ Unfortunately, your loan is unlikely to be approved."

            # Save prediction to DB
            PredictionLog.objects.create(
                user=request.user,
                Gender=data['Gender'],
                Married=data['Married'],
                Dependents=data['Dependents'],
                Education=data['Education'],
                Self_Employed=data['Self_Employed'],
                LoanAmount=data['LoanAmount'],
                Loan_Amount_Term=data['Loan_Amount_Term'],
                Credit_History=data['Credit_History'],
                Property_Area=data['Property_Area'],
                TotalIncome=data['TotalIncome'],
                Prediction=prediction_label
            )

            return render(request, 'predict.html', {
                'form': form,
                'prediction': prediction_msg
            })
    else:
        form = PredictionForm()

    return render(request, 'predict.html', {'form': form})


@login_required
def dashboard(request):
    records = PredictionLog.objects.all().order_by('-created_at')[:10]
    total = PredictionLog.objects.count()
    approved = PredictionLog.objects.filter(Prediction='Approved').count()
    rejected = PredictionLog.objects.filter(Prediction='Rejected').count()
    user_count = User.objects.count()

    return render(request, 'dashboard.html', {
        'records': records,
        'total': total,
        'approved': approved,
        'rejected': rejected,
        'user_count': user_count,
    })
