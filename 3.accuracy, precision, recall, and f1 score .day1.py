import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 
data = {
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [0.5, 1.5, 2.5, 3.5, 4.5],
    'target': [0, 1, 0, 1, 1]
}
df = pd.DataFrame(data)
print("Available features:")
print(df.columns[:-1]) 
features = input("Enter names of features (comma-separated): ").split(',')
target_variable = input("Enter name of target variable: ")
X = df[features]
y = df[target_variable]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression() 
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print("\nEvaluation Metrics:")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
