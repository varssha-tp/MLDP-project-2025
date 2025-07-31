import streamlit as st
import numpy as np
import joblib
from streamlit_lottie import st_lottie 
import json 

def show_assessment_page():
    # Load model
    model = joblib.load("model/model.pkl")
    scaler = joblib.load('model/scaler.pkl')
    
    # Header with back button
    col1, col2, col3 = st.columns([1, 6, 1])
    
    with col1:
        if st.button("← Back to Home", key="back_home"):
            st.session_state.page = 'home'
            st.rerun()
    
    with col2:
        st.title("Heart Disease Risk Assessment")
    
    st.markdown("""
    <div style='background-color: rgba(42, 157, 143, 0.15); border-left: 5px solid #2a9d8f; padding: 15px; margin-bottom: 25px; border-radius: 5px;'>
    <p style='margin: 0; color: #ffffff;'>Please fill out the form below to assess your heart disease risk.</p>
    </div>
    """, unsafe_allow_html=True)

    # Styling for assessment page
    st.markdown("""
    <style>
    h1 {
    color: white;
    text-align: center;
    margin-bottom: 30px;
    margin-top: -30px;
                
}
            
    h2 {
        color: white;
    }
    h3 {
        color: white;
        font-size: 30px;
        margin-bottom: 10px;
    }
    p{
        font-size: 23px;
    }
                
    [data-testid="stHorizontalBlock"] {
        gap: 15px; 
    }
                
    .stButton>button {
        background-color: #f44336;
        color: white;
        border: 2px solid #f44336;
        border-radius: 5px;
        font-size: 18px;
        font-weight: bold;
        padding: 8px 16px;
    }
    
    .stButton>button:hover {
        background-color: #d32f2f;
        border-color: #d32f2f;
        color: white;
    }

                
    [data-testid="stSelectbox"] label p {
        font-size: 23px;
        font-weight: 500;
    }

    [data-testid="stSelectbox"] {
        max-width: 650px; 
        margin-bottom: 25px; 
    }
                
[data-testid="stSelectbox"] > div > div {
    height: 68px;
    min-height: 68px;
}

.st-ed {
    font-size: 20px;
    padding: 15px 5px;
    line-height: 1.2;
    display: flex;
    align-items: center;
}

[data-testid="stSelectbox"] input {
    height: 68px;
    font-size: 18px;
    padding: 10px 15px;
    line-height: 1.2;
}

    .stSlider {
        max-width: 600px;
    }
    [data-testid="stNumberInput"] label p {
        font-size: 23px;
        font-weight: 500;
    }
    [data-testid="stNumberInputContainer"] {
        max-width: 650px;
        height: 68px; 
        margin-bottom: 25px;
        
    }
    [data-testid="stNumberInputField"] {
        font-size: 20px;
        height: 68px;
        width: 250px;
        padding: 20px 15px;
        border-radius: 8px;
    }
    [data-testid="stSlider"] label p {
        font-size: 23px;
        font-weight: 500;
    }
    [data-testid="stSliderThumbValue"] {
        font-size: 20px;
        top: -35px;  
    }
    [data-baseweb="slider"] > div:first-child {
        margin-top: 30px;
        padding-top: 20px;
    }

    [data-testid="stSliderTickBar"] {
        font-size: 20px;
    }
                
    [data-testid="stSlider"] {
        margin-bottom: 20px;
        max-width: 600px;
    }
                
    .health-factors-header {
        display: flex;
        align-items: flex-start; 
        gap: 8px;
    }
    .info-icon-container {
        display: inline-block;
        margin-top: 0px; 
        margin-left: 1530px; 
        position: relative;
        cursor: pointer;
        font-size: 20px; 
    }
    .tooltip-table {
        display: none;
        position: absolute;
        z-index: 100;
        background-color: #000;
        color: #fff;
        padding: 12px;
        width: 750px;
        top: 0;
        left: -770px; /* Show to the left of the icon */
        border-radius: 8px;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
    }
    .info-icon-container:hover .tooltip-table {
        display: block;
    }
    .tooltip-table table {
        width: 100%;
        border-collapse: collapse;
        color: white;
    }
    .tooltip-table th, .tooltip-table td {
        border: 1px solid #444;
        padding: 6px;
        text-align: center;
    }
    .tooltip-table th {
        background-color: #222;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize form counter for resetting
    if 'form_counter' not in st.session_state:
        st.session_state.form_counter = 0

    with st.form(f"prediction_form_{st.session_state.form_counter}"):
        # Section 1: Basic Information
        st.subheader("🔴 Basic Information")
        age = st.number_input("Age", min_value=1, max_value=120, placeholder="Please enter age")
        gender = st.selectbox("Gender", ["Female", "Male"])
        smoking = st.selectbox("Do you smoke?", ["No", "Yes"])
        family_hd = st.selectbox("Family history of heart disease?", ["Yes", "No"])

        st.markdown("---")
        
        # Section 2: Health Factors
        st.markdown("""
        <div class="health-factors-header">
        <h3>🔴 Health Factors</h3>
        <div class="info-icon-container">ℹ️
            <div class="tooltip-table">
                <table>
                    <tr>
                        <th>Factor</th>
                        <th>Low</th>
                        <th>Normal</th>
                        <th>High</th>
                    </tr>
                    <tr><td>Blood Pressure</td><td>&lt; 90/60</td><td>90–120 / 60–80</td><td>&gt; 140/90</td></tr>
                    <tr><td>Cholesterol</td><td>-</td><td>&lt; 200 mg/dL</td><td>&gt;= 240 mg/dL</td></tr>
                    <tr><td>BMI</td><td>&lt; 18.5</td><td>18.5 – 24.9</td><td>&gt;= 30</td></tr>
                    <tr><td>Sleep Hours</td><td>&lt; 6 hrs</td><td>7 – 9 hrs</td><td>&gt; 10 hrs</td></tr>
                    <tr><td>Triglyceride</td><td>-</td><td>&lt; 150 mg/dL</td><td>&gt;= 200 mg/dL</td></tr>
                    <tr><td>Fasting Blood Sugar</td><td>&lt; 70</td><td>70 – 99 mg/dL</td><td>&gt;= 126 mg/dL</td></tr>
                    <tr><td>CRP</td><td>-</td><td>&lt; 1 mg/L</td><td>&gt; 3 mg/L</td></tr>
                    <tr><td>Homocysteine</td><td>&lt; 5</td><td>5 – 15 µmol/L</td><td>&gt; 15 µmol/L</td></tr>
                </table>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
        bp = st.number_input("Blood Pressure", min_value=0, placeholder="Please enter BP")
        chol = st.number_input("Cholesterol Level", min_value=0, placeholder="Please enter cholesterol level")
        bmi = st.number_input("BMI", min_value=0.0, placeholder="Please enter BMI")
        sleep_hours = st.number_input("Sleep Hours", min_value=0.0, placeholder="Please enter sleep hours")
        triglyceride = st.number_input("Triglyceride Level", min_value=0, placeholder="Please enter level")
        fbs = st.number_input("Fasting Blood Sugar", min_value=0, placeholder="Please enter sugar level")
        crp = st.number_input("CRP Level (C-reactive protein)", min_value=0.0, placeholder="Please enter CRP level")
        homo = st.number_input("Homocysteine Level", min_value=0.0, placeholder="Please enter value")
        diabetes = st.selectbox("Do you have diabetes?", ["Yes", "No"])
        high_bp = st.selectbox("Do you have high blood pressure?", ["No", "Yes"])
        low_hdl = st.selectbox("Do you have low HDL cholesterol?", ["Yes", "No"])
        high_ldl = st.selectbox("Do you have high LDL cholesterol?", ["No", "Yes"])

        st.markdown("---")
        
        # Section 3: Lifestyle Factors
        st.subheader("🔴 Lifestyle Factors")
        exercise_encoded = st.slider("Exercise Habits", 0, 2, 1, help="0 = Never, 1 = Sometimes, 2 = Often")
        stress_encoded = st.slider("Stress Level", 0, 2, 1, help="0 = None, 1 = Mild, 2 = High")
        sugar_encoded = st.slider("Sugar Intake", 0, 2, 1, help="0 = Low, 1 = Moderate, 2 = High")
        alcohol_encoded = st.slider("Alcohol Intake", 0, 2, 1, help="0 = Never, 1 = Sometimes, 2 = Frequent")

        st.markdown("---")

        # Center the Predict button
        col1, col2, col3 = st.columns([4, 1, 4])
        with col2:
            submitted = st.form_submit_button("Predict")

    # Prediction Logic
    if submitted:
        gender_female = 1 if gender == "Female" else 0
        gender_male = 1 if gender == "Male" else 0
        smoking_no = 1 if smoking == "No" else 0
        smoking_yes = 1 if smoking == "Yes" else 0
        family_hd_yes = 1 if family_hd == "Yes" else 0
        family_hd_no = 1 if family_hd == "No" else 0
        diabetes_yes = 1 if diabetes == "Yes" else 0
        diabetes_no = 1 if diabetes == "No" else 0
        high_bp_no = 1 if high_bp == "No" else 0
        high_bp_yes = 1 if high_bp == "Yes" else 0
        low_hdl_yes = 1 if low_hdl == "Yes" else 0
        low_hdl_no = 1 if low_hdl == "No" else 0
        high_ldl_no = 1 if high_ldl == "No" else 0
        high_ldl_yes = 1 if high_ldl == "Yes" else 0

        input_data = np.array([[age, bp, chol, bmi, sleep_hours, triglyceride, fbs, crp, homo,
                                gender_female, gender_male,
                                smoking_no, smoking_yes,
                                family_hd_no, family_hd_yes,
                                diabetes_no, diabetes_yes,
                                high_bp_no, high_bp_yes,
                                low_hdl_no, low_hdl_yes,
                                high_ldl_no, high_ldl_yes,
                                exercise_encoded, stress_encoded, sugar_encoded, alcohol_encoded]])
        
        input_data_scaled = scaler.transform(input_data)
        prediction = model.predict(input_data_scaled)[0]
        probabilities = model.predict_proba(input_data_scaled)[0]

        st.markdown("---")
        st.subheader("Your Result:")
        with st.container():
            if prediction == 1:
                st.markdown(f"""
                <div style="padding: 1rem; border-left: 6px solid #e63946; background-color: rgba(230, 57, 70, 0.1); border-radius: 6px;">
                    <h4 style="color: #b00020;">⚠️ Risk Detected</h4>
                    <p>You may be at risk of <strong>Heart Disease</strong>.</p>
                    <p><strong>Probability:</strong> {probabilities[1]:.2%}</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                <div style="padding: 1rem; background-color: rgba(255, 193, 7, 0.1); border-radius: 6px; margin-top: 20px;">
                    <h4 style="color: #f57c00;">📋 Recommendations:</h4>
                    <p>• Consult with a healthcare professional immediately</p>
                    <p>• Consider lifestyle modifications (diet, exercise, stress management)</p>
                    <p>• Schedule regular health checkups</p>
                    <p>• Monitor your risk factors closely</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="padding: 1rem; border-left: 6px solid #2a9d8f; background-color: rgba(42, 157, 143, 0.1); border-radius: 6px;">
                    <h4 style="color: #00695c;">✅ No Significant Risk Detected</h4>
                    <p>Your heart health looks good based on the input.</p>
                    <p><strong>Probability:</strong> {probabilities[0]:.2%}</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                <div style="padding: 1rem; background-color: rgba(76, 175, 80, 0.1); border-radius: 6px; margin-top: 20px;">
                    <h4 style="color: #388e3c;">💡 Keep Up the Good Work:</h4>
                    <p>• Maintain your healthy lifestyle choices</p>
                    <p>• Continue regular exercise and balanced diet</p>
                    <p>• Schedule routine health checkups</p>
                    <p>• Stay informed about heart health</p>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("© 2025 HeartAware. Built for education and awareness.")