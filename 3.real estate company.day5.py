import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
data = {
    'size': [1200, 1500, 1800, 2000, 1000, 1400, 1600, 1900, 2200, 1300],
    'bedrooms': [3, 4, 3, 4, 2, 3, 3, 4, 4, 3],
    'location': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C', 'A'],
    'price': [300000, 350000, 400000, 450000, 250000, 320000, 370000, 420000, 480000, 290000]
}
house_data = pd.DataFrame(data)
X = house_data[['size']]  
y = house_data['price']
plt.scatter(X, y, color='blue')
plt.title('House Price vs Size of the House')
plt.xlabel('Size of the House')
plt.ylabel('Price')
plt.show()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print("Model Performance:")
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared (R2):", r2)
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.title('House Price Prediction (Linear Regression)')
plt.xlabel('Size of the House')
plt.ylabel('Price')
plt.show()
