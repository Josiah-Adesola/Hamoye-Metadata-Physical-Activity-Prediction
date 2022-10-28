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
    st.title('Mobile Health  Human Behavior Prediction  App')
    st.markdown("This project was developed by Team Metadata")
    st.header("Human Activity Recognition")
    st.markdown("The MHEALTH (Mobile HEALTH) dataset comprises body motion and vital signs recordings for ten volunteers of diverse profile while performing several physical activities. Sensors placed on the subject's chest, right wrist and left ankle are used to measure the motion experienced by diverse body parts, namely, acceleration, rate of turn and magnetic field orientation. The sensor positioned on the chest also provides 2-lead ECG measurements, which can be potentially used for basic heart monitoring, checking for various arrhythmias or looking at the effects of exercise on the ECG.")

    st.image("exercise.png")

    #get data from user
    alx = st.number_input("Acceleration from the left-ankle sensor (X-axis)", min_value=-15.00, max_value=20.00, value=8.00)
    aly = st.number_input("Acceleration from the left-ankle sensor (Y axis)", min_value=-20.00, max_value=4.00, value=1.00)
    alz = st.number_input("Acceleration from the left-ankle sensor (Z axis)", min_value=-20.00, max_value=20.00, value=-10.00)
    glx = st.number_input("Gyro from the left-ankle sensor (X axis)", min_value=-0.13, max_value=1.00, value=0.46)

    gly = st.number_input("Gyro from the left-ankle sensor (Y axis)", min_value=-2.00, max_value=2.00, value=1.50)
    glz = st.number_input("Gyro from the left-ankle sensor (Z axis)", min_value=-2.00, max_value=1.50, value=0.60)

    arx = st.number_input("Acceleration from the right-lower-arm sensor (X axis)", min_value=-31.00, max_value=15.00, value=3.00)
    ary = st.number_input("Acceleration from the right-lower-arm sensor (Y axis)", min_value=-19.00, max_value=13.00, value=5.00)

    arz = st.number_input("Acceleration from the right-lower-arm sensor (Z axis)", min_value=-14.00, max_value=15.00, value=-6.00)
    grx = st.number_input("Gyro from the right-lower-arm sensor (X axis)",  min_value=-1.70, max_value=2.00, value=1.00)

    gry = st.number_input("Gyro from the right-lower-arm sensor (Y axis)", min_value= - 3.00, max_value=2.00, value=1.00)
    grz = st.number_input("Gyro from the right-lower-arm sensor (Z axis)",min_value=-0.40, max_value=2.40, value=1.05)
         

    #code for prediction
    prediction = ''

    #creating the button for prediction

    if st.button('Physical Activity Prediction'):
        prediction = mhealth_prediction(alx, aly, alz, glx, gly, glz, arx, ary, arz, grx,
       gry, grz)

        if (prediction[0] == 1):
            st.success("Standing Still")

        elif (prediction[0] == 2):
            st.success("Still and relaxing")
        elif (prediction[0] == 3):
            st.success("Lying Down")

        elif (prediction[0] == 4):
            st.success("Walking")
        elif (prediction[0] == 5):
            st.success("Climbing stairs")

        elif (prediction[0] == 6):
            st.success("Waist bends forward")
        elif (prediction[0] == 7):
            st.success("Standing Still")

        elif (prediction[0] == 8):
            st.success("Knees bending (crouching)")
        elif (prediction[0] == 9):
            st.success("Cycling")

        elif (prediction[0] == 10):
            st.success("Jogging")
        elif (prediction[0] == 11):
            st.success("Running")

        elif (prediction[0] == 12):
            st.success("Jump front & back")
        else: 
            st.success("There's no exercise")

        return prediction

if __name__ == '__main__':
    main()