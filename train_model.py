import pandas as pd, pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv("train.csv")
df["Age"] = df["YrSold"] - df["YearBuilt"]

X = df[["GrLivArea", "BedroomAbvGr", "FullBath", "Age", "OverallQual"]]
y = df["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("R2:", r2_score(y_test, pred))
print("MAE:", mean_absolute_error(y_test, pred))

pickle.dump(model, open("model.pkl", "wb"))
