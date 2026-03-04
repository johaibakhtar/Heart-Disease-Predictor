import streamlit as st
import numpy as np
import pandas as pd
import pickle

# -------- Load Model --------
model = pickle.load(open("heart_modell.pkl","rb"))
scaler = pickle.load(open("scalerr.pkl","rb"))
features = pickle.load(open("featuress.pkl","rb"))

st.set_page_config(page_title="Heart Health Predictor", page_icon="❤️", layout="wide")

# -------- Custom CSS --------
st.markdown("""
<style>
.big-title{
font-size:40px;
font-weight:700;
color:#ff4b4b;
}

.card{
padding:25px;
border-radius:18px;
background: linear-gradient(135deg,#667eea,#764ba2);
color:white;
font-size:18px;
box-shadow:0px 10px 25px rgba(0,0,0,0.25);
}

.result-high{
color:#ff4b4b;
font-size:30px;
font-weight:bold;
}

.result-low{
color:#00a86b;
font-size:30px;
font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# -------- Title --------
st.markdown('<p class="big-title">❤️ Heart Disease Risk Predictor</p>', unsafe_allow_html=True)
st.write("Enter simple health information to estimate heart disease risk.")

st.divider()

# -------- Sidebar Inputs --------
st.sidebar.header("🧑 Patient Information")

age = st.sidebar.slider("Age",20,100,40)

bp = st.sidebar.slider("Blood Pressure",80,200,120)

chol = st.sidebar.slider("Cholesterol Level",100,600,200)

sugar = st.sidebar.selectbox("High Blood Sugar?",["No","Yes"])

maxhr = st.sidebar.slider("Maximum Heart Rate",60,220,150)

oldpeak = st.sidebar.slider("ST Depression Level",0.0,6.0,1.0)

sex = st.sidebar.selectbox("Gender",["Male","Female"])

chest = st.sidebar.selectbox("Chest Pain Type",
["No Pain","Mild Pain","Moderate Pain","Severe Pain"])

ecg = st.sidebar.selectbox("ECG Result",
["Normal","Abnormal","Severely Abnormal"])

angina = st.sidebar.selectbox("Exercise Chest Pain",["No","Yes"])

slope = st.sidebar.selectbox("Heart Stress Test Result",
["Normal","Flat","Upward"])

predict = st.sidebar.button("Predict Risk")

# -------- Layout --------
col1,col2,col3 = st.columns(3)

with col1:

    st.markdown("### 🧾 Patient Summary")

    st.markdown(f"""
    <div class="card">
    Age: <b>{age}</b><br><br>
    Blood Pressure: <b>{bp}</b><br><br>
    Cholesterol: <b>{chol}</b><br><br>
    Max Heart Rate: <b>{maxhr}</b><br><br>
    ST Depression: <b>{oldpeak}</b>
    </div>
    """, unsafe_allow_html=True)

# -------- Prediction --------
if predict:

    input_data = pd.DataFrame(np.zeros((1,len(features))), columns=features)

    input_data["Age"] = age
    input_data["RestingBP"] = bp
    input_data["Cholesterol"] = chol
    input_data["FastingBS"] = 1 if sugar=="Yes" else 0
    input_data["MaxHR"] = maxhr
    input_data["Oldpeak"] = oldpeak

    if sex=="Male":
        input_data["Sex_M"]=1

    if chest=="Mild Pain":
        input_data["ChestPainType_ATA"]=1
    elif chest=="Moderate Pain":
        input_data["ChestPainType_NAP"]=1
    elif chest=="Severe Pain":
        input_data["ChestPainType_TA"]=1

    if ecg=="Normal":
        input_data["RestingECG_Normal"]=1
    elif ecg=="Abnormal":
        input_data["RestingECG_ST"]=1

    if angina=="Yes":
        input_data["ExerciseAngina_Y"]=1

    if slope=="Flat":
        input_data["ST_Slope_Flat"]=1
    elif slope=="Upward":
        input_data["ST_Slope_Up"]=1

    # scale numeric columns
    numeric_cols=['Age','RestingBP','Cholesterol','MaxHR','Oldpeak']
    input_data[numeric_cols]=scaler.transform(input_data[numeric_cols])

    prediction=model.predict(input_data)
    probability=model.predict_proba(input_data)[0][1]

    with col2:

        st.markdown("### 📊 Risk Level")

        st.progress(float(probability))

        st.metric("Heart Disease Risk",f"{probability*100:.1f}%")

    with col3:

        st.markdown("### 🧠 Prediction")

        if prediction[0]==1:

            st.markdown('<p class="result-high">⚠️ High Risk</p>', unsafe_allow_html=True)
            st.error("Consult a doctor for proper diagnosis.")

        else:

            st.markdown('<p class="result-low">✅ Low Risk</p>', unsafe_allow_html=True)
            st.success("No strong signs of heart disease detected.")

st.divider()

st.markdown("### 🤖 Model Performance")

m1,m2,m3=st.columns(3)

m1.metric("Accuracy","86%")
m2.metric("ROC AUC","0.93")
m3.metric("Cross Validation","0.84")

st.caption("⚠️ Educational tool — not a medical diagnosis.")