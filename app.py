import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the trained model (Ensure you train and save your model as 'model.pkl' first)
# model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

st.title("🏠 Real Estate Price Predictor")
st.write("Enter the property details below to estimate its estimated market value using Machine Learning.")

# Create input fields for user parameters
col1, col2 = st.columns(2)

with col1:
    sq_ft = st.number_input("Square Footage (sq. ft)", min_value=500, max_value=10000, value=1500, step=50)
    bedrooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5, 6])
    bathrooms = st.selectbox("Number of Bathrooms", [1, 2, 3, 4, 5])

with col2:
    age = st.number_input("Age of Property (Years)", min_value=0, max_value=100, value=10)
    location_score = st.slider("Location Rating (1-10)", min_value=1, max_value=10, value=7)

# Prediction button
if st.button("Predict Price", type="primary"):
    # Dummy calculation for template purpose (Replace with: model.predict([[sq_ft, bedrooms, bathrooms, age, location_score]]))
    estimated_price = (sq_ft * 120) + (bedrooms * 15000) - (age * 1000) + (location_score * 20000)
    
    st.success(f"Estimated Property Price: **${estimated_price:,.2f}**")
    st.balloons()