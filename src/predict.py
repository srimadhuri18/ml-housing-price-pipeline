def predict_price(model, scaler, input_data):

    scaled = scaler.transform([input_data])

    prediction = model.predict(scaled)

    return prediction[0]