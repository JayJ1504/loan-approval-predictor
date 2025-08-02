import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os

# Load the trained model
model_path = r"C:\Users\jayja\Desktop\Projects\ML-Projects\loan-approval-predictor\model\loan_approval_model.pkl"
model = joblib.load(model_path)

st.set_page_config(page_title="Loan Approval Predictor", layout="centered")

st.title("🏦 Loan Approval Predictor")
st.markdown("Predict whether a loan will be **approved or rejected** based on applicant information.")

# Collect user inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_term = st.selectbox("Loan Amount Term", [12, 36, 60, 84, 120, 180, 240, 300, 360, 480])
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Encode input like the model expects
def encode_input():
    gender_val = 1 if gender == "Male" else 0
    married_val = 1 if married == "Yes" else 0
    dependents_val = 3 if dependents == "3+" else int(dependents)
    education_val = 0 if education == "Graduate" else 1
    self_employed_val = 1 if self_employed == "Yes" else 0
    property_val = {"Urban": 2, "Semiurban": 1, "Rural": 0}[property_area]

    feature_names = [
        'Gender', 'Married', 'Dependents', 'Education',
        'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome',
        'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area'
    ]

    values = [[
        gender_val, married_val, dependents_val, education_val,
        self_employed_val, applicant_income, coapplicant_income,
        loan_amount, loan_term, credit_history, property_val
    ]]

    return pd.DataFrame(values, columns=feature_names)

# Predict
# Make prediction with probability
input_data = encode_input()
proba = model.predict_proba(input_data)[0][1]  # Probability of loan approval

if proba > 0.6:
    st.success(f"✅ Loan Approved — Confidence: {proba:.2f}")
else:
    st.error(f"❌ Loan Rejected — Confidence: {proba:.2f}")

