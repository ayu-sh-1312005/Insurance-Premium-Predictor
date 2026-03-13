import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Insurance Premium Predictor", layout="wide")

st.title("🏥 Annual Health Insurance Premium Predictor")
st.write("Fill the details below")

# ----- Layout -----
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", 18, 100)

    gender = st.selectbox(
        "Gender",
        ['Male', 'Female']
    )

    region = st.selectbox(
        "Region",
        ['Northeast', 'Northwest', 'Southeast', 'Southwest']
    )

    marital_status = st.selectbox(
        "Marital Status",
        ['Unmarried', 'Married']
    )

with col2:
    bmi_category = st.selectbox(
        "BMI Category",
        ['Overweight', 'Underweight', 'Normal', 'Obesity']
    )

    smoking_status = st.selectbox(
        "Smoking Status",
        ['Regular', 'No Smoking', 'Occasional']
    )

    employment_status = st.selectbox(
        "Employment Status",
        ['Self-Employed', 'Freelancer', 'Salaried']
    )

    medical_history = st.selectbox(
        "Medical History",
        ['High blood pressure', 'No Disease',
         'Diabetes & High blood pressure',
         'Diabetes & Heart disease',
         'Diabetes',
         'Diabetes & Thyroid',
         'Heart disease',
         'Thyroid',
         'High blood pressure & Heart disease']
    )

with col3:
    income_lakhs = st.number_input("Income (Lakhs)", min_value=0.0)

    number_of_dependants = st.number_input(
        "Number of Dependants", min_value=0, step=1
    )
    genetical_risk = st.number_input("Genetical Risk", min_value=0)

    insurance_plan = st.selectbox(
        "Insurance Plan",
        ['Gold','Silver','Bronze']
    )

st.markdown("---")

# ----- Submit -----
if st.button("Predict", use_container_width=True):

    input_dict = {
        "age": age,
        "gender": gender,
        "region": region,
        "marital_status": marital_status,
        "bmi_category": bmi_category,
        "smoking_status": smoking_status,
        "employment_status": employment_status,
        "medical_history": medical_history,
        "income_lakhs": income_lakhs,
        "number_of_dependants": number_of_dependants,
        "insurance_plan": insurance_plan,
        "genetical_risk": genetical_risk,
    }
    predict(input_dict)

    prediction = predict(input_dict)
    st.success(f"Predicted Premium: ₹{prediction:,.2f}")
    st.success("Submitted Data")
    #st.write(input_dict)