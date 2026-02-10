import streamlit as st
import pickle
import pandas as pd
import numpy as np

model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("encoders.pkl", "rb"))

st.markdown("<h1 style='text-align:center;'>✈️ Flight Price Prediction System</h1>", unsafe_allow_html=True)

st.info("""
Please enter the flight details below.
The system will predict the estimated flight ticket price.
""")

airline = st.selectbox("Airline", ["IndiGo","Air India","Jet Airways","SpiceJet","Multiple carriers"])
source = st.selectbox("Source", ["Delhi","Kolkata","Mumbai","Chennai","Banglore"])
destination = st.selectbox("Destination", ["Cochin","Delhi","Banglore","Hyderabad","Kolkata"])
stops = st.selectbox("Total Stops", [0,1,2,3])
journey_day = st.number_input("Journey Day", 1, 31)
journey_month = st.number_input("Journey Month", 1, 12)
dep_hour = st.number_input("Departure Hour", 0, 23)
dep_min = st.number_input("Departure Minute", 0, 59)
arr_hour = st.number_input("Arrival Hour", 0, 23)
arr_min = st.number_input("Arrival Minute", 0, 59)
duration = st.number_input("Duration (minutes)")

if st.button("Predict Price"):
    input_df = pd.DataFrame(np.zeros((1, len(columns))), columns=columns)

    input_df["Total_Stops"] = stops
    input_df["Journey_Day"] = journey_day
    input_df["Journey_Month"] = journey_month
    input_df["Dep_Hour"] = dep_hour
    input_df["Dep_Min"] = dep_min
    input_df["Arrival_Hour"] = arr_hour
    input_df["Arrival_Min"] = arr_min
    input_df["Duration"] = duration

    for col in input_df.columns:
        if airline in col or source in col or destination in col:
            input_df[col] = 1

    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Flight Price: ₹ {int(prediction)}")
