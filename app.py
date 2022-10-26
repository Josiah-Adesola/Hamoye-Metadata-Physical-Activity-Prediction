import streamlit as st
import pandas as pd
import pickle
import numpy as np


#Load the saved model
filename = "rf_model.pkl"
loaded_model = pickle.load(open(filename, 'rb'))

def mhealth_prediction(alx, aly, alz, glx, gly, glz, arx, ary, arz, grx,
       gry, grz):
    
    prediction = loaded_model.predict(pd.DataFrame([[alx, aly, alz, glx, gly, glz, arx, ary, arz, grx,
       gry, grz]]))

    if (prediction[0] == 1):
        print("Standing Still")

    elif (prediction[0] == 2):
        print("Still and relaxing")
    elif (prediction[0] == 3):
        print("Lying Down")

    elif (prediction[0] == 4):
        print("Walking")
    elif (prediction[0] == 5):
        print("Climbing stairs")

    elif (prediction[0] == 6):
        print("Waist bends forward")
    elif (prediction[0] == 7):
        print("Standing Still")

    elif (prediction[0] == 8):
        print("Knees bending (crouching)")
    elif (prediction[0] == 9):
        print("Cycling")

    elif (prediction[0] == 10):
        print("Jogging")
    elif (prediction[0] == 11):
        print("Running")

    elif (prediction[0] == 12):
        print("Jump front & back")
    else: 
        print("There's no exercise")

    return prediction


def main():

    add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"))
    st.title('Mobile Health  Human Behavior Prediction  App')
    st.markdown("This project was developed by Team Metadata")
    st.header("Human Activity Recognition")
    st.markdown("The MHEALTH (Mobile HEALTH) dataset comprises body motion and vital signs recordings for ten volunteers of diverse profile while performing several physical activities. Sensors placed on the subject's chest, right wrist and left ankle are used to measure the motion experienced by diverse body parts, namely, acceleration, rate of turn and magnetic field orientation. The sensor positioned on the chest also provides 2-lead ECG measurements, which can be potentially used for basic heart monitoring, checking for various arrhythmias or looking at the effects of exercise on the ECG.")

    st.image("exercise.png")

    #get data from user
    age = st.number_input("Age", min_value=18, max_value=85, value=18)
    sex = st.selectbox("Gender", ["Female", "Male"])
    cp = st.selectbox("Chest Pain type", ['Typical angina', 'Atypical angina', 'Non-angina', 'Asymptomatic'])
    trestbps = st.number_input("Resting Blood Pressure (mm/Hg)", min_value=90, max_value=300, value=90)
    chol = st.number_input("Serum Cholesterol in mg/dl", min_value=100, max_value=650, value=150)
    fbs = st.selectbox("Fastig Blood Sugar", ["True", "False"])
    st.caption("Is it greater than 120mg/dl")
    restecg = st.selectbox("Resting Electrocardiographic Results", ["Normal","Stt abnormality","Iv hypertrophy"])
    thalach = st.number_input("Maximum heart rate achieved", min_value=50, max_value=250, value=60)
    exang = st.selectbox("Exercise Induced Angina?", ["True", "False"])
    oldpeak = st.number_input("ST Depression induced by exercise relative to rest",  min_value=0.0, max_value=6.5, value=1.0)
    slope = st.number_input("Slope of the peak", min_value=1, max_value=3, value=1)
    ca = st.number_input("Number of major vessels colored by flourosopy",min_value=0, max_value=3, value=1)
    thal = st.selectbox("Stage of Thalassemia Blood disorder", ["Normal", "Fixed", "Defect", "Reversible Defect"])       

    #code for prediction
    prediction = ''

    #creating the button for prediction

    if st.button('Heart Disease Test Result'):
        prediction = mhealth_prediction(alx, aly, alz, glx, gly, glz, arx, ary, arz, grx,
       gry, grz)

        if (prediction[0] == 1):
            print("Standing Still")

        elif (prediction[0] == 2):
            print("Still and relaxing")
        elif (prediction[0] == 3):
            print("Lying Down")

        elif (prediction[0] == 4):
            print("Walking")
        elif (prediction[0] == 5):
            print("Climbing stairs")

        elif (prediction[0] == 6):
            print("Waist bends forward")
        elif (prediction[0] == 7):
            print("Standing Still")

        elif (prediction[0] == 8):
            print("Knees bending (crouching)")
        elif (prediction[0] == 9):
            print("Cycling")

        elif (prediction[0] == 10):
            print("Jogging")
        elif (prediction[0] == 11):
            print("Running")

        elif (prediction[0] == 12):
            print("Jump front & back")
        else: 
            print("There's no exercise")

        return prediction

if __name__ == '__main__':
    main()