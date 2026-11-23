# House Price Predictor 🏠

A machine learning web app that estimates a house's sale price from its size, rooms, age and overall quality.

## Dataset
[Kaggle: House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) (Ames, Iowa housing data, 1,460 rows).

## How it works
1. Features used: living area (`GrLivArea`), bedrooms (`BedroomAbvGr`), full bathrooms (`FullBath`), property age (`YrSold - YearBuilt`) and overall quality (`OverallQual`).
2. Data split 80% train / 20% test.
3. Model: Random Forest Regressor (200 trees) built with scikit-learn.
4. The trained model is saved as `model.pkl` and loaded by the Streamlit app.

## Results (on the held-out 20% test set)
- R² score: **0.87**
- Mean Absolute Error: **about $21,900**

## Tech used
Python, pandas, NumPy, scikit-learn, Streamlit

## Run it locally
pip install -r requirements.txt
python train_model.py   # optional: retrain and regenerate model.pkl
streamlit run app.py

## Limitations
The model learned from Iowa houses, so its estimates won't be accurate for other cities. It uses only 5 features, so it's a learning project and not a valuation tool.

## Future improvements
- Add more features (neighborhood, garage, lot size)
- Compare other models (XGBoost, Gradient Boosting)
- Deploy the app online
