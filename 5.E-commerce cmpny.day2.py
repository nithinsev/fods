import pandas as pd
order_data = pd.DataFrame({
    'customer_id': [1, 1, 2, 2, 3],
    'order_date': ['2024-01-01', '2024-01-03', '2024-01-02', '2024-01-04', '2024-01-05'],
    'product_name': ['A', 'B', 'A', 'C', 'B'],
    'order_quantity': [5, 3, 2, 4, 6]
})
orders_per_customer = order_data.groupby('customer_id').size()
print("Total number of orders made by each customer:")
print(orders_per_customer)
print()
avg_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
print("Average order quantity for each product:")
print(avg_order_quantity_per_product)
print()
order_data['order_date'] = pd.to_datetime(order_data['order_date'])
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()
print("Earliest Order Date:", earliest_order_date)
print("Latest Order Date:", latest_order_date)
