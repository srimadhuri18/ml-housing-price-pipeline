from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


def train_models(X_train, y_train):

    models = {}

    lr = LinearRegression()
    lr.fit(X_train, y_train)
    models["LinearRegression"] = lr

    dt = DecisionTreeRegressor()
    dt.fit(X_train, y_train)
    models["DecisionTree"] = dt

    rf = RandomForestRegressor()
    rf.fit(X_train, y_train)
    models["RandomForest"] = rf

    return models