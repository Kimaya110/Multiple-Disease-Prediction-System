import streamlit as st
from streamlit_lottie import st_lottie
import requests
import numpy as np

# Function to fetch Lottie animation URLs
def load_lottieurl(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Load Lottie animations
home_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_u4yrau.json")
prediction_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_tutvdkg0.json")
contact_animation = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_jcikwtux.json")

# Title and Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Prediction", "Contact Us"])

# Home Page
if page == "Home":
    st.title("Welcome to the Disease Prediction App")
    st_lottie(home_animation, height=300, key="home")
    st.write("""
        This application helps predict the likelihood of the following diseases:
        - **Diabetes**
        - **Heart Disease**
        - **Parkinson's Disease**
        
        Leveraging machine learning models, we aim to provide insights based on the data you provide.
    """)
    

# Prediction Page
elif page == "Prediction":
    st.title("Disease Prediction")
    st_lottie(prediction_animation, height=300, key="prediction")

    # Select Disease
    disease = st.selectbox("Select the disease you want to predict", ["Diabetes", "Heart Disease", "Parkinson's Disease"])
    
    # Form for user inputs
    st.subheader(f"Provide details for {disease} prediction")
    if disease == "Diabetes":
        pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
        glucose = st.number_input("Glucose Level", min_value=0)
        blood_pressure = st.number_input("Blood Pressure", min_value=0)
        skin_thickness = st.number_input("Skin Thickness", min_value=0)
        insulin = st.number_input("Insulin Level", min_value=0)
        bmi = st.number_input("BMI", min_value=0.0)
        diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0)
        age = st.number_input("Age", min_value=0)
        
        # Prediction logic
        if st.button("Predict"):
            # Example logic for prediction
            prediction = np.random.choice([0, 1], p=[0.7, 0.3])  # Replace with actual model
            result = "Positive" if prediction == 1 else "Negative"
            st.success(f"Diabetes Prediction: {result}")
    
    elif disease == "Heart Disease":
        age = st.number_input("Age", min_value=0)
        sex = st.selectbox("Sex", ["Male", "Female"])
        chest_pain = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
        resting_bp = st.number_input("Resting Blood Pressure", min_value=0)
        cholesterol = st.number_input("Cholesterol Level", min_value=0)
        fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
        rest_ecg = st.selectbox("Resting ECG Results", [0, 1, 2])
        max_hr = st.number_input("Max Heart Rate Achieved", min_value=0)
        exercise_angina = st.selectbox("Exercise-Induced Angina", ["Yes", "No"])
        
        # Prediction logic
        if st.button("Predict"):
            # Example logic for prediction
            prediction = np.random.choice([0, 1], p=[0.6, 0.4])  # Replace with actual model
            result = "Positive" if prediction == 1 else "Negative"
            st.success(f"Heart Disease Prediction: {result}")
    
    elif disease == "Parkinson's Disease":
        mdvp_fo = st.number_input("MDVP:Fo (Hz)", min_value=0.0)
        mdvp_fhi = st.number_input("MDVP:Fhi (Hz)", min_value=0.0)
        mdvp_flo = st.number_input("MDVP:Flo (Hz)", min_value=0.0)
        jitter_percent = st.number_input("Jitter (%)", min_value=0.0)
        jitter_abs = st.number_input("Jitter (Abs)", min_value=0.0)
        shimmer = st.number_input("Shimmer", min_value=0.0)
        shimmer_db = st.number_input("Shimmer (dB)", min_value=0.0)
        hnr = st.number_input("HNR", min_value=0.0)
        
        # Prediction logic
        if st.button("Predict"):
            # Example logic for prediction
            prediction = np.random.choice([0, 1], p=[0.8, 0.2])  # Replace with actual model
            result = "Positive" if prediction == 1 else "Negative"
            st.success(f"Parkinson's Disease Prediction: {result}")

# Contact Us Page
elif page == "Contact Us":
    st.title("Contact Us")
    st_lottie(contact_animation, height=300, key="contact")
    st.write("For inquiries or feedback, reach out to us:")
    st.write("""
        - **Email**: support@healthapp.com
        - **Phone**: +91-12345-67890
        - **Address**: Pune, Maharashtra, India
    """)
    
