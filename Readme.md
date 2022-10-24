## DATA SOURCING
----------------------------------------------

This data was sourced from Kaggle - https://www.kaggle.com/datasets/gaurav2022/mobile-health


## AIM 
-----------------------------------
The aim of the project is to predict a person's physical activity fro their different body part motion.

## Context
-------------------------------------------------
The MHEALTH (Mobile HEALTH) dataset comprises body motion and vital signs recordings for ten volunteers of diverse profile while performing several physical activities. Sensors placed on the subject's chest, right wrist and left ankle are used to measure the motion experienced by diverse body parts, namely, acceleration, rate of turn and magnetic field orientation. The sensor positioned on the chest also provides 2-lead ECG measurements, which can be potentially used for basic heart monitoring, checking for various arrhythmias or looking at the effects of exercise on the ECG.

##  DATASET SUMMARY
-----------------------------------
Activities: 12
Sensor devices: 3
Subjects: 10
EXPERIMENTAL SETUP

## EXPERIMENTAL SETUP
-------------------------------------------
The collected dataset comprises body motion and vital signs recordings for ten volunteers of diverse profile while performing 12 physical activities (Table 1). Shimmer2 [BUR10] wearable sensors were used for the recordings. The sensors were respectively placed on the subject's chest, right wrist and left ankle and attached by using elastic straps (as shown in the figure in attachment). The use of multiple sensors permits us to measure the motion experienced by diverse body parts, namely, the acceleration, the rate of turn and the magnetic field orientation, thus better capturing the body dynamics. The sensor positioned on the chest also provides 2-lead ECG measurements which are not used for the development of the recognition model but rather collected for future work purposes. This information can be used, for example, for basic heart monitoring, checking for various arrhythmias or looking at the effects of exercise on the ECG. All sensing modalities are recorded at a sampling rate of 50 Hz, which is considered sufficient for capturing human activity. Each session was recorded using a video camera. This dataset is found to generalize to common activities of the daily living, given the diversity of body parts involved in each one (e.g., frontal elevation of arms vs. knees bending), the intensity of the actions (e.g., cycling vs. sitting and relaxing) and their execution speed or dynamicity (e.g., running vs. standing still). The activities were collected in an out-of-lab environment with no constraints on the way these must be executed, with the exception that the subject should try their best when executing them.

## ACTIVITY SET
------------------------------------------------
The activity set is listed in the following:
L1: Standing still (1 min)
L2: Sitting and relaxing (1 min)
L3: Lying down (1 min)
L4: Walking (1 min)
L5: Climbing stairs (1 min)
L6: Waist bends forward (20x)
L7: Frontal elevation of arms (20x)
L8: Knees bending (crouching) (20x)
L9: Cycling (1 min)
L10: Jogging (1 min)
L11: Running (1 min)
L12: Jump front & back (20x)
NOTE: In brackets are the number of repetitions (Nx) or the duration of the exercises (min).

## Data Preparation
------------------------------------------
I have only taken acceleration and gyroscope data for the classification of the given activity and convert it into csv file provided here. If you are also interested in ECG and magnetometer data you can download it from here.

Follow this notebook to see how I fetch this data from UCI.

https://www.kaggle.com/gaurav2022/download-data-from-ucs/output
## Acknowledgements
----------------------------------------------
All credits goes to UCI Machine Learning repository for providing this dataset (Link)
