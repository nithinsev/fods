import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
data = {
    'usage_minutes': [300, 400, 200, 500, 600],
    'contract_duration': [12, 24, 6, 18, 36],
    'age': [30, 40, 25, 45, 50],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'churn': [0, 1, 0, 1, 0]  
}
customer_data = pd.DataFrame(data)
X = customer_data[['usage_minutes', 'contract_duration', 'age', 'gender']]
y = customer_data['churn']
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)
def predict_churn(usage_minutes, contract_duration, age, gender):
    gender_male = 1 if gender.lower() == 'male' else 0
    gender_female = 1 if gender.lower() == 'female' else 0
    new_customer = [[usage_minutes, contract_duration, age, gender_male, gender_female]]
    new_customer_scaled = scaler.transform(new_customer)
    churn_prediction = model.predict(new_customer_scaled)
    return churn_prediction[0]
usage_minutes = int(input("Enter the usage minutes: "))
contract_duration = int(input("Enter the contract duration (in months): "))
age = int(input("Enter the age of the customer: "))
gender = input("Enter the gender of the customer (Male/Female): ")
churn_prediction = predict_churn(usage_minutes, contract_duration, age, gender)
if churn_prediction == 1:
    print("The new customer is predicted to churn.")
else:
    print("The new customer is predicted not to churn.")
