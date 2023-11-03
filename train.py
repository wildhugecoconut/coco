import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("dataset.csv")

features = df.drop(["id", "has_event"], axis=1)
print(features)
target = df["qty_sold"]

random = RandomForestRegressor(n_estimators=11)
random.fit(features, target)

with open("model.pkl", "wb") as file:
    pickle.dump(random, file)
    print("Model saved successfully")
