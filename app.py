import streamlit as st
from src.predict_pipeline import PredictPipeline

st.title("SMS Spam Classifier")

message = st.text_area("Enter message")

if st.button("Predict"):

    obj = PredictPipeline()

    prediction = obj.predict(message)

    if prediction == 1:
        st.error("Spam Message")
    else:
        st.success("Ham Message")