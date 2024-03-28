import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'total_amount_spent': [100, 200, 150, 300, 250, 120, 180, 220, 280, 230],
    'frequency_of_visits': [5, 8, 6, 10, 7, 4, 6, 7, 9, 8]
}
transaction_data = pd.DataFrame(data)
X = transaction_data[['total_amount_spent', 'frequency_of_visits']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
inertia_values = []
k_range = range(1, 11)  
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia_values.append(kmeans.inertia_)
plt.plot(k_range, inertia_values, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal K')
plt.show()
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(X_scaled)
transaction_data['cluster'] = kmeans.labels_
plt.scatter(transaction_data['total_amount_spent'], transaction_data['frequency_of_visits'], c=transaction_data['cluster'], cmap='viridis')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.title('Customer Segmentation based on Spending Patterns')
plt.show()
print(transaction_data)
