import streamlit as st
import json 
from streamlit_lottie import st_lottie 

st.set_page_config(page_title="Heart Aware", layout="wide", page_icon="🫀")

if 'page' not in st.session_state:
    st.session_state.page = 'home'

def show_home_page():
    with open("Heart.json", "r") as f:
        heart_animation = json.load(f)

    col1, col2 = st.columns([0.1, 1])  

    with col1:
        st_lottie(heart_animation, height=100, width=100, key="heart") 

    with col2:
        st.title("Heart Disease Awareness & Prediction")

    # Red box for the description
    st.markdown("""
    <div style='background-color: rgba(244, 67, 54, 0.15); border-left: 5px solid #f44336; padding: 15px; margin-bottom: 25px; border-radius: 5px;'>
    <p style='margin: 0; color: #ffffff;'>Heart disease is the <strong>#1 cause of death worldwide</strong>. Early detection and healthy lifestyle choices can make a difference. Learn about the risks and assess your own with our prediction tool below.</p>
    </div>
    """, unsafe_allow_html=True)

    # Styling
    st.markdown("""
    <style>
    h1 {
        color: white;
        display: flex;
        align-items: center; 
        margin-top: 0; 
        margin-bottom: 0;
        margin-left:-60px;
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
                
    [data-testid="stTab"] > div[data-testid="stMarkdownContainer"] p {
        font-size: 20px; 
        font-weight: 600; 
        margin-right: 15px;  
        padding: 10px 20px
    }
                
    [data-baseweb="tab-panel"] p,
    [data-baseweb="tab-panel"] li {
        font-size: 23px;
    }
    
    .stButton {
    display: flex;
    justify-content: center;
    }

    [data-testid="stBaseButton-secondary"] {
        background-color: #f44336;
        width: 450px;
        color: white;
        border: 2px solid #f44336;
        border-radius: 5px;
        font-size: 18px;
        font-weight: bold;
        padding: 8px 16px;
        display: block;
        box-shadow: 0 4px 12px rgba(244, 67, 54, 0.3), 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
}

    [data-testid="stBaseButton-secondary"]:hover {
        background-color: #d32f2f;
        border-color: #d32f2f;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    # Heart Disease Information Tabs
    tabs = st.tabs(["What is Heart Disease?", "Symptoms", "Risk Factors", "Prevention Tips"])
    with tabs[0]:
        st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)
        st.image("images/diagram.png", width=500)
        st.markdown("""
        Heart disease refers to conditions that involve narrowed or blocked blood vessels, which can lead to a heart attack, chest pain or stroke. Common types include coronary artery disease, heart rhythm problems, and heart defects.

        Several health factors can increase the risk of developing heart disease:
        <ul>
          <li>
            <strong>Cholesterol (HDL & LDL):</strong>
            <ul>
              <li><strong>LDL (bad cholesterol):</strong> Can build up in the walls of your arteries, making them narrow and hard. This blocks blood flow to the heart.</li>
              <li><strong>HDL (good cholesterol):</strong> Helps remove LDL from your blood. Low HDL levels mean less protection for your heart.</li>
            </ul>
          </li>
          <li>
            <strong>Triglyceride Level:</strong>
            High triglycerides (a type of fat in your blood) can also lead to plaque buildup in the arteries. This increases the chance of heart disease, especially when combined with high LDL or low HDL.
          </li>
          <li>
            <strong>Fasting Blood Sugar:</strong>
            High blood sugar, often seen in diabetes, can damage blood vessels and the nerves that control the heart. Over time, this raises the risk of heart disease.
          </li>
          <li>
            <strong>CRP Level (C-Reactive Protein):</strong>
            CRP shows inflammation in your body. When CRP is high, it may mean your blood vessels are inflamed, which can speed up the process of artery blockage.
          </li>
          <li>
            <strong>Homocysteine Level:</strong>
            High homocysteine levels can damage the lining of the arteries and increase the risk of blood clots. This raises the chance of a heart attack or stroke.
          </li>
          <li>
            <strong>Blood Pressure:</strong>
            High blood pressure (also called hypertension) forces your heart to work harder to pump blood. Over time, it damages the arteries and increases the risk of heart disease, heart attack, or stroke.
          </li>
        </ul>
        """, unsafe_allow_html=True)
    with tabs[1]:
        st.write("""
        Common symptoms include:
        - Chest pain or discomfort
        - Shortness of breath
        - Fatigue
        - Irregular heartbeat
        """)
    with tabs[2]:
        st.write("""
        Risk factors include:
        - High blood pressure and cholesterol
        - Smoking
        - Diabetes
        - Obesity
        - Lack of physical activity
        - Family history
        """)
    with tabs[3]:
        st.write("""
        To reduce your risk:
        - Eat a heart-healthy diet
        - Exercise regularly
        - Avoid smoking
        - Manage stress
        - Get regular checkups
        """)

    st.markdown("---")
    
    # Get Started Button
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("Click to access our risk assessment tool", 
                    help="Check Your Heart Health"):
            st.session_state.page = 'assessment'
            st.rerun()

    st.markdown("---")
    st.markdown("© 2025 HeartAware. Built for education and awareness.")

# Navigation 
if st.session_state.page == 'home':
    show_home_page()
elif st.session_state.page == 'assessment':
    import assessment_page
    assessment_page.show_assessment_page()