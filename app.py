import streamlit as st
import pandas as pd
import joblib

pipeline = joblib.load(r"model.pkl")
Model = pipeline["Model"]
vectorizer = pipeline["vectorizer"]

st.title("Just A Small Web App For Your Message's Sentiment Analysis...",anchor=False)
msg = st.text_input("Enter Your Text Message Here To Check Your Mood...")
if st.button("Know",type="primary"):
    if msg !="":
        raw_msg = vectorizer.transform([msg])
        Prediction = Model.predict(raw_msg)[0]
        if Prediction == "positive":
            st.success(f"Your Mood Is {Prediction}")
        if Prediction == "negative":
            st.warning(f"Your Mood Is {Prediction}")
        if Prediction == "neutral":
            st.toast(f"Your Mood Is {Prediction}")
    else:
        st.toast("Please Enter Something Msg In Box...",duration="long")