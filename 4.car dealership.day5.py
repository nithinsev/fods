import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
data = {
    'mileage': [50000, 60000, 30000, 20000, 80000],
    'age': [5, 6, 3, 2, 8],
    'brand': ['Toyota', 'Honda', 'Toyota', 'BMW', 'Honda'],
    'engine_type': ['Petrol', 'Diesel', 'Petrol', 'Diesel', 'Petrol'],
    'price': [20000, 18000, 25000, 35000, 15000]
}
car_data = pd.DataFrame(data)
X = car_data[['mileage', 'age', 'brand', 'engine_type']] 
y = car_data['price']  
numeric_features = ['mileage', 'age']
numeric_transformer = Pipeline(steps=[('num', 'passthrough')])

categorical_features = ['brand', 'engine_type']
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))  
])
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', DecisionTreeRegressor(random_state=42))])
model.fit(X, y)
def predict_price(input_features):
    new_car = pd.DataFrame(input_features, index=[0])
    price_prediction = model.predict(new_car)
    return price_prediction[0]
mileage = float(input("Enter the mileage of the new car (in miles): "))
age = int(input("Enter the age of the new car (in years): "))
brand = input("Enter the brand of the new car: ")
engine_type = input("Enter the engine type of the new car: ")
input_features = {'mileage': [mileage], 'age': [age], 'brand': [brand], 'engine_type': [engine_type]}
predicted_price = predict_price(input_features)
print("Predicted price of the new car: ${:.2f}".format(predicted_price))
