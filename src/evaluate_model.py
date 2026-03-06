from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


def evaluate_models(models, X_test, y_test):

    results = {}

    for name, model in models.items():

        predictions = model.predict(X_test)

        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        r2 = r2_score(y_test, predictions)

        results[name] = {
            "RMSE": rmse,
            "R2 Score": r2
        }

    return results