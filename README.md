
# 🏦 Loan Approval Predictor (Django App)
# PADIOS, OLIVE FAITH A. BSCS-2C

This Django web application predicts whether a loan application is likely to be **approved** or **rejected**, using a trained machine learning model.

## 🚀 Features

- 🔐 User authentication (Register/Login/Logout)
- 📊 Loan prediction form for logged-in users
- 📈 Dashboard with recent predictions and stats
- 📁 Model integrated with Django using `joblib`
- 🎨 Styled UI using custom CSS (no Bootstrap)

## 🧠 Machine Learning

- Trained on loan approval dataset
- Uses preprocessing, scaling, feature engineering
- Final model is an ensemble of classifiers
- Stored as `loan_approval_pipeline.pkl`

## 📂 Folder Structure

```
loanpredictor_django_project/
├── loanpredictor/         # Main Django app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   │   └── *.html
│   └── static/
│       └── css/
│           └── style.css
├── loan_approval_pipeline.pkl  # Trained ML model
├── loan_sanction_train.csv     # Original dataset
├── manage.py
└── requirements.txt
```

## 🛠 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/loanpredictor_django_project.git
   cd loanpredictor_django_project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # or env\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```


5. **Run the server**
   ```bash
   python manage.py runserver
   ```

6. **Visit in browser**
   ```
   http://127.0.0.1:8000/
   ```

## 🔒 Auth System
Sample account
username: testing
pass: testing12345

- Only logged-in users can access the **Predict** and **Dashboard** pages
- Register and Login through the navigation bar

