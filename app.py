from flask import Flask, render_template, request
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open("pipeline/regressionlogistic.pkl", "rb"))


def model_pred(features):
    test_data = pd.DataFrame([features])
    prediction = model.predict(test_data)
    return int(prediction[0])


@app.route("/", methods=["GET"])
def Home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        credit_lines_outstanding = int(request.form["credit_lines_outstanding"])
        income = float(request.form["income"])
        years_employed = int(request.form["years_employed"])
        fico_score = int(request.form["fico_score"])
    # Constante pour la prédiction (vous pouvez adapter cette valeur si nécessaire)
        constant = 8.0913
        prediction = model.predict(
            [[constant, credit_lines_outstanding, income, years_employed,fico_score]]
        )

        if prediction[0] == 1:
            return render_template(
                "index.html",
                prediction_text="accordé",
            )

        else:
            return render_template(
                "index.html", prediction_text="pas accordé"
            )

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)