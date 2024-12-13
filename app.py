import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests

# Set page configuration
st.set_page_config(
    page_title="Health Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to load Lottie animations
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animations
lottie_main = load_lottie("https://lottie.host/7da1cac5-120f-4e4e-8efa-4e641018cfd2/eiJQdParg2.json")
lottie_diabetes = load_lottie("https://lottie.host/4f05d7c4-062f-4b98-a0c7-5d07f3c0725b/jbBdt2hGhr.json")
lottie_heart = load_lottie("https://lottie.host/3eaf5568-d60d-4edb-a6f1-9e8eaef998b2/XAz4MjRguq.json")
lottie_parkinsons = load_lottie("https://lottie.host/d29b3289-7242-4e28-a30b-080a1f56e63c/boTrgVh3Ra.json")

# Load models
diabetes_model = pickle.load(open(r"C:\Users\HP\VS Code Projects\Multiple Disease Prediction System\diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"C:\Users\HP\VS Code Projects\Multiple Disease Prediction System\heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\HP\VS Code Projects\Multiple Disease Prediction System\parkinsons_model.sav", 'rb'))

# Sidebar for navigation
with st.sidebar:
    st_lottie(lottie_main, height=200, key="main_lottie")
    selected = option_menu(
        "Health Assistant",
        ["Diabetes Prediction 🩸", "Heart Disease Prediction ❤️", "Parkinson's Prediction 🧠"],
        menu_icon="hospital-fill",
        icons=["activity", "heart", "person"],
        default_index=0,
    )

# Main Title and Header
st.markdown(
    """
    <style>
        .header {
            text-align: center;
            font-size: 2.5rem;
            color: #4CAF50;
        }
        .footer {
            text-align: center;
            color: #6c757d;
            font-size: 0.9rem;
            margin-top: 50px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<h1 class="header">Health Assistant - Disease Prediction</h1>', unsafe_allow_html=True)

# Helper function to display success/failure messages with dynamic colors
def show_prediction(result, positive_msg, negative_msg):
    if result == 1:
        st.success(positive_msg)
    else:
        st.info(negative_msg)

# Diabetes Prediction
if selected == "Diabetes Prediction 🩸":
    st.title("Diabetes Prediction using Machine Learning")
    if lottie_diabetes:
        st_lottie(lottie_diabetes, height=300, key="diabetes")

    col1, col2, col3 = st.columns(3)
    with col1: Pregnancies = st.text_input('Number of Pregnancies')
    with col2: Glucose = st.text_input('Glucose Level')
    with col3: BloodPressure = st.text_input('Blood Pressure value')
    with col1: SkinThickness = st.text_input('Skin Thickness value')
    with col2: Insulin = st.text_input('Insulin Level')
    with col3: BMI = st.text_input('BMI value')
    with col1: DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2: Age = st.text_input('Age of the Person')

    if st.button('Predict Diabetes'):
        user_input = [float(x) for x in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        result = diabetes_model.predict([user_input])
        show_prediction(result[0], "The person is diabetic", "The person is not diabetic")

# Heart Disease Prediction
elif selected == "Heart Disease Prediction ❤️":
    st.title("Heart Disease Prediction using Machine Learning")
    if lottie_heart:
        st_lottie(lottie_heart, height=300, key="heart")

    # Inputs
    col1, col2, col3 = st.columns(3)
    with col1: age = st.text_input('Age')
    with col2: sex = st.text_input('Sex')
    with col3: cp = st.text_input('Chest Pain Type')
    with col1: trestbps = st.text_input('Resting Blood Pressure')
    with col2: chol = st.text_input('Serum Cholesterol (mg/dl)')
    with col3: fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1: restecg = st.text_input('Resting Electrocardiographic Results')
    with col2: thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3: exang = st.text_input('Exercise-Induced Angina')
    with col1: oldpeak = st.text_input('ST Depression by Exercise')
    with col2: slope = st.text_input('Slope of Peak Exercise ST')
    with col3: ca = st.text_input('Major Vessels Colored by Flouroscopy')
    with col1: thal = st.text_input('Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)')

    if st.button('Predict Heart Disease'):
        user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        result = heart_disease_model.predict([user_input])
        show_prediction(result[0], "The person has heart disease", "The person does not have heart disease")

# Parkinson's Prediction
elif selected == "Parkinson's Prediction 🧠":
    st.title("Parkinson's Disease Prediction using Machine Learning")
    if lottie_parkinsons:
        st_lottie(lottie_parkinsons, height=300, key="parkinsons")

    # Inputs
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: fo = st.text_input('MDVP:Fo(Hz)')
    with col2: fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3: flo = st.text_input('MDVP:Flo(Hz)')
    with col4: Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5: Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    # (Add more fields similarly)

    if st.button("Predict Parkinson's Disease"):
        user_input = [float(x) for x in [fo, fhi, flo, Jitter_percent, Jitter_Abs]]  # Add all inputs
        result = parkinsons_model.predict([user_input])
        show_prediction(result[0], "The person has Parkinson's disease", "The person does not have Parkinson's disease")

# Footer
st.markdown('<div class="footer">Built with ❤️ using Streamlit</div>', unsafe_allow_html=True)
