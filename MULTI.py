import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import sklearn

# loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Diabetes & Heart Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           icons=['activity','heart','person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        SkinThickness = st.text_input('Skin Thickness value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Glucose = st.text_input('Glucose Level')
        Insulin = st.text_input('Insulin Level')
        BMI = st.text_input('BMI value')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # page title
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        restecg = st.text_input('Resting Electrocardiographic results')
        oldpeak = st.text_input('ST depression induced by exercise')
        ca = st.text_input('Major vessels colored by flourosopy')
    with col2:
        sex = st.text_input('Sex')
        chol = st.text_input('Serum Cholestoral in mg/dl')
        thalach = st.text_input('Maximum Heart Rate achieved')
        slope = st.text_input('Slope of the peak exercise ST segment')
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    with col3:
        cp = st.text_input('Chest Pain types')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        exang = st.text_input('Exercise Induced Angina')

    # code for Prediction
    heart_diagnosis = ''
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
    st.success(heart_diagnosis)
