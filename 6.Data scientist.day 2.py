import pandas as pd
sales_data = pd.DataFrame({
    'order_date': ['2024-02-05', '2024-02-10', '2024-02-15', '2024-02-20', '2024-03-01'],
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B'],
    'order_quantity': [10, 5, 8, 12, 6]
})
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'])
current_date = pd.to_datetime('today').normalize()
start_date = current_date - pd.DateOffset(months=1)
filtered_data = sales_data[sales_data['order_date'] >= start_date]
product_sales = filtered_data.groupby('product_name')['order_quantity'].sum()
top_products = product_sales.sort_values(ascending=False).head(5)
print("Top 5 products sold the most in the past month:")
print(top_products)
