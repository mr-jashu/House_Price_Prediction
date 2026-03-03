import streamlit as st
import pandas as pd
import sys
import os

# Add src to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.pipeline.prediction_pipeline import PredictPipeline, CustomData

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("House Price Prediction App 🏠")
st.write("Enter the house details to predict the price:")

usd_to_inr_rate = st.number_input(
    "USD to INR Exchange Rate",
    min_value=1.0,
    max_value=200.0,
    value=83.0,
    step=0.1,
)

# Input Fields
col1, col2 = st.columns(2)

with col1:
    MedInc = st.number_input("Median Income (in $10k)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
    HouseAge = st.number_input("House Age (Years)", min_value=1, max_value=100, value=30)
    AveRooms = st.number_input("Average Rooms", min_value=1.0, max_value=20.0, value=6.0, step=0.5)
    AveBedrms = st.number_input("Average Bedrooms", min_value=0.5, max_value=10.0, value=1.0, step=0.5)

with col2:
    Population = st.number_input("Population", min_value=0, max_value=5000, value=1500)
    AveOccup = st.number_input("Average Occupancy", min_value=1.0, max_value=10.0, value=3.0, step=0.1)
    Latitude = st.number_input("Latitude", min_value=30.0, max_value=45.0, value=35.0, step=0.01)
    Longitude = st.number_input("Longitude", min_value=-130.0, max_value=-110.0, value=-120.0, step=0.01)

if st.button("Predict Price"):
    data = CustomData(
        MedInc=MedInc,
        HouseAge=HouseAge,
        AveRooms=AveRooms,
        AveBedrms=AveBedrms,
        Population=Population,
        AveOccup=AveOccup,
        Latitude=Latitude,
        Longitude=Longitude
    )
    
    pred_df = data.get_data_as_dataframe()
    
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    predicted_price_usd = float(results[0])
    predicted_price_inr = predicted_price_usd * usd_to_inr_rate

    st.success(f"Predicted House Price (USD): ${predicted_price_usd:,.2f}")
    st.success(f"Predicted House Price (INR): ₹{predicted_price_inr:,.2f}")