import streamlit as st
import pandas as pd
from data_processing import fetch_and_process_data
from analysis import analyze_performance
from rank_prediction import predict_neet_rank

st.set_page_config(page_title="Quiz Performance Analysis", layout="wide")

st.title("Quiz Performance Analysis & NEET Rank Prediction")

# Fetch and process data
submission_data, historical_data = fetch_and_process_data()

if submission_data is not None:
    # Analyze performance
    analysis_results = analyze_performance(submission_data, historical_data)

    st.subheader("Performance Insights")
    st.json(analysis_results)

    # Predict NEET rank
    predicted_rank = predict_neet_rank(analysis_results)
    st.subheader("Predicted NEET Rank")
    st.write(predicted_rank)
else:
    st.error("Failed to fetch data. Please check API endpoints.")

