import pandas as pd
customer_demographics_data = {
    'customer_id': [1, 2, 3, 4, 5],
    'age': [25, 30, 35, 40, 45],
    'gender': ['M', 'F', 'M', 'F', 'M'],
    'location': ['CityA', 'CityB', 'CityA', 'CityC', 'CityB']
}
customer_demographics = pd.DataFrame(customer_demographics_data)

user_activity_logs_data = {
    'customer_id': [1, 2, 3, 4, 5],
    'timestamp': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'page_views': [10, 15, 20, 25, 30],
    'interaction_duration': [60, 75, 90, 105, 120]
}
user_activity_logs = pd.DataFrame(user_activity_logs_data)

customer_support_data = {
    'customer_id': [1, 2, 3, 4, 5],
    'support_tickets': [2, 1, 3, 2, 4],
    'satisfaction_score': [4, 5, 3, 4, 2]
}
customer_support = pd.DataFrame(customer_support_data)

consolidated_data = pd.merge(customer_demographics, user_activity_logs, on='customer_id', how='inner')
consolidated_data = pd.merge(consolidated_data, customer_support, on='customer_id', how='inner')

print("Consolidated Dataset:")
print(consolidated_data)
