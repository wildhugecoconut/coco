import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

model = None
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/predict", methods=["POST"])
def predict():
    parameters = request.get_json(force=True)
    f1 = int(parameters["item"])
    f2 = int(parameters["category"])
    f3 = int(parameters["department"])
    f4 = int(parameters["store"])
    f5 = int(parameters["store_code"])
    f6 = int(parameters["region"])
    f7 = int(parameters["yearweek"])
    f8 = float(parameters["sell_price"])
    f9 = int(parameters["weekday_int"])
    f10 = int(parameters["event"])
    qty_sold = model.predict([[f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]])[0]
    print(qty_sold)
    return jsonify(qty_sold)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
