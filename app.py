import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")
st.title("🏠 House Price Predictor")
st.write("Enter the property details to estimate its sale price (trained on the Ames, Iowa housing dataset).")

col1, col2 = st.columns(2)

with col1:
    sq_ft = st.number_input("Living Area (sq. ft)", min_value=500, max_value=5000, value=1500)
    bedrooms = st.selectbox("Bedrooms above ground", [1, 2, 3, 4, 5, 6], index=2)
    bathrooms = st.selectbox("Full Bathrooms", [1, 2, 3, 4], index=1)

with col2:
    age = st.number_input("Age of Property (Years)", min_value=0, max_value=100, value=20)
    quality = st.slider("Overall Quality (1-10)", min_value=1, max_value=10, value=5)

if st.button("Predict Price", type="primary"):
    features = pd.DataFrame(
        [[sq_ft, bedrooms, bathrooms, age, quality]],
        columns=["GrLivArea", "BedroomAbvGr", "FullBath", "Age", "OverallQual"])
    price = model.predict(features)[0]
    st.success(f"Estimated Property Price: **${price:,.0f}**")