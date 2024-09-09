from app import model_pred

new_data = {'constante':8.0913,
            'loan_amt_outstanding': 4000,
            'income': 50000,
            'years_employed': 4,
            'fico_score': 600,
            }


def test_predict():
    prediction = model_pred(new_data)
    assert prediction == 1, "incorrect prediction"