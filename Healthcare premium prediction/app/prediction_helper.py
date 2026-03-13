import pandas as pd
from joblib import load
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ARTIFACT_PATH = os.path.join(BASE_DIR, "artifacts")

model_young = load(os.path.join(ARTIFACT_PATH, "model_young.joblib"))
model_rest = load(os.path.join(ARTIFACT_PATH, "model_rest.joblib"))

scaler_young = load(os.path.join(ARTIFACT_PATH, "scaler_young.joblib"))
scaler_rest = load(os.path.join(ARTIFACT_PATH, "scaler_rest.joblib"))

risk_score = {
    'diabetes': 6,
    'heart disease': 8,
    'high blood pressure': 6,
    'thyroid': 5,
    'no disease': 0,
    'none': 0
}
def calculate_normalized_score(medical_history):

    if pd.isna(medical_history):
        return 0

    diseases = medical_history.lower().split(" & ")

    total_score = sum(risk_score.get(d.strip(), 0) for d in diseases)
    max_score=14
    min_score=0
    normalized_score=(total_score-min_score)/(max_score-min_score)
    return normalized_score

def preprocess_input(input_dict):
    expected_columns=['age', 'number_of_dependants', 'income_level', 'income_lakhs',
       'insurance_plan', 'genetical_risk', 'normalized_score', 'gender_Male',
       'region_Northwest', 'region_Southeast', 'region_Southwest',
       'marital_status_Unmarried', 'bmi_category_Obesity',
       'bmi_category_Overweight', 'bmi_category_Underweight',
       'smoking_status_Occasional', 'smoking_status_Regular',
       'employment_status_Salaried', 'employment_status_Self-Employed']


    df=pd.DataFrame(0, columns=expected_columns,index=[0])

    # genetical score
    df['genetical_risk'] = input_dict['genetical_risk']

    # medical history
    medical_history=input_dict['medical_history']
    df['normalized_score']=calculate_normalized_score(medical_history)

    # age
    df['age']=input_dict['age']

    # bmi
    bmi=input_dict['bmi_category']
    df['bmi_category_Obesity']=0
    df['bmi_category_Underweight']=0
    df['bmi_category_Overweight']=0
    if bmi=='Obesity':
        df['bmi_category_Obesity']=1
    elif bmi=='Underweight':
        df['bmi_category_Underweight']=1
    elif bmi=='Overweight':
        df['bmi_category_Overweight']=1

    # employment status
    employment_status=input_dict['employment_status']
    df['employment_status_Self-Employed']=0
    df['employment_status_Salaried']=0
    if employment_status=='Salaried':
        df['employment_status_Salaried']=1
    elif employment_status=='Self-Employed':
        df['employment_status_Self-Employed']=1

    # region
    region=input_dict['region']
    df['region_Northwest']=0
    df['region_Southeast']=0
    df['region_Southwest']=0
    if region=='Northwest':
        df['region_Northwest']=1
    elif region=='Southeast':
        df['region_Southeast']=1
    elif region=='Southwest':
        df['region_Southwest']=1

    # smoking status
    smoking_status=input_dict['smoking_status']
    df['smoking_status_Occasional']=0
    df['smoking_status_Regular']=0
    if smoking_status=='Occasional':
        df['smoking_status_Occasional']=1
    elif smoking_status=='Regular':
        df['smoking_status_Regular']=1

    # insurance plan
    insurance_plan=input_dict['insurance_plan']
    if insurance_plan=='Gold':
        df['insurance_plan']=3
    elif insurance_plan=='Silver':
        df['insurance_plan']=2
    elif insurance_plan=='Bronze':
        df['insurance_plan']=1

    # marital status
    marital_status=input_dict['marital_status']
    if marital_status=='Unmarried':
        df['marital_status_Unmarried']=0
    elif marital_status=='Married':
        df['marital_status_Unmarried']=1

    # no of dependants
    number_of_dependants=input_dict['number_of_dependants']
    df['number_of_dependants']=number_of_dependants

    # gender
    gender=input_dict['gender']
    if gender=='Male':
        df['gender_Male']=1
    else:
        df['gender_Male']=0

    # income
    income_lakhs=input_dict['income_lakhs']
    df['income_lakhs']=income_lakhs

    # income level
    if income_lakhs<=10:
        df['income_level']=1
    elif income_lakhs<=25:
        df['income_level']=2
    elif income_lakhs<=40:
        df['income_level']=3
    else:
        df['income_level']=4

    return df
def predict(input_dict):

    input_df = preprocess_input(input_dict)

    if input_dict['age'] <= 25:
        scaler_dict = load(os.path.join(ARTIFACT_PATH, "scaler_young.joblib"))
        scaler = scaler_dict['scalar']
        cols_to_scale = scaler_dict['cols_to_scale']

        input_df[cols_to_scale] = scaler.transform(input_df[cols_to_scale])
        pred = model_young.predict(input_df)

    else:
        scaler_dict = load(os.path.join(ARTIFACT_PATH, "scaler_rest.joblib"))
        scaler = scaler_dict['scalar']
        cols_to_scale = scaler_dict['cols_to_scale']

        input_df[cols_to_scale] = scaler.transform(input_df[cols_to_scale])
        pred = model_rest.predict(input_df)

  
    return pred[0]





