import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
data = {
    'age': [45, 50, 35, 40, 60, 55, 65, 30, 50, 70],
    'gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male'],
    'blood_pressure': ['High', 'Normal', 'Normal', 'Normal', 'High', 'High', 'Normal', 'High', 'Normal', 'High'],
    'cholesterol_levels': ['High', 'Normal', 'Normal', 'High', 'High', 'Normal', 'High', 'Normal', 'Normal', 'High'],
    'treatment_outcome': ['Good', 'Bad', 'Good', 'Good', 'Bad', 'Good', 'Good', 'Bad', 'Good', 'Bad']
}
medical_data = pd.DataFrame(data)
X = medical_data[['age', 'gender', 'blood_pressure', 'cholesterol_levels']]
y = medical_data['treatment_outcome']
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='Good')
recall = recall_score(y_test, y_pred, pos_label='Good')
f1 = f1_score(y_test, y_pred, pos_label='Good')
print("Model Performance:")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)
predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("\nPredictions on the test set:")
print(predictions_df)
