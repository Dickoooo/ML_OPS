from flask import Flask, render_template, request
import pickle
import pandas as pd
import logging

app = Flask(__name__)

# Configurez le logging
logging.basicConfig(level=logging.ERROR)

# Chargement du modèle depuis le fichier pickle
model = pickle.load(open("regressionlogistic.pkl", "rb"))

def model_pred(features):
    """Fonction pour prédire le résultat basé sur les features fournies"""
    test_data = pd.DataFrame([features])
    prediction = model.predict(test_data)
    return int(prediction[0])

@app.route("/")
def index():
    """Route pour la page d'accueil"""
    return render_template("index.html")  # Assurez-vous d'avoir un fichier index.html dans le dossier templates

@app.route("/predict", methods=["POST"])
def predict():
    """Route pour gérer les prédictions basées sur les données soumises via un formulaire"""
    if request.method == "POST":
        try:
            # Extraction des données du formulaire
            credit_lines_outstanding = int(request.form["credit_lines_outstanding"])
            income = float(request.form["income"])
            years_employed = int(request.form["years_employed"])
            fico_score = int(request.form["fico_score"])

            # Constante pour la prédiction
            constant = 8.0913

            # Prédiction du modèle
            prediction = model.predict(
                [[constant, credit_lines_outstanding, income, years_employed, fico_score]]
            )

            # Rendre le template en fonction du résultat de la prédiction
            if prediction[0] == 1:
                return render_template(
                    "index.html",
                    prediction_text="Vous faites défaut, le crédit ne sera pas accordé."
                )
            else:
                return render_template(
                    "index.html", prediction_text="Tout va bien, crédit accordé ! :)"
                )

        except ValueError as e:
            logging.error(f"Erreur dans les valeurs numériques : {e}")
            return render_template("index.html", prediction_text=f"Erreur dans les valeurs numériques : {e}")
        
        except KeyError as e:
            logging.error(f"Clé manquante dans le formulaire : {e}")
            return render_template("index.html", prediction_text=f"Clé manquante dans le formulaire : {e}")
        
        except Exception as e:
            logging.error(f"Une erreur inattendue est survenue : {e}")
            return render_template("index.html", prediction_text=f"Une erreur inattendue est survenue : {e}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
