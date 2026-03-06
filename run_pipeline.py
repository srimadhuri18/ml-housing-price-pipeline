from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.train_model import train_models
from src.evaluate_model import evaluate_models


def main():

    print("Loading dataset...")
    df = load_data()

    print("Preprocessing data...")
    X_train, X_test, y_train, y_test, scaler = preprocess_data(df)

    print("Training models...")
    models = train_models(X_train, y_train)

    print("Evaluating models...")
    results = evaluate_models(models, X_test, y_test)

    for model, metrics in results.items():
        print(f"\nModel: {model}")
        print("RMSE:", metrics["RMSE"])
        print("R2 Score:", metrics["R2 Score"])


if __name__ == "__main__":
    main()