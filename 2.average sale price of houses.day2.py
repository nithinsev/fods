import numpy as np
import pandas as pd
data = {
    'Bedrooms': [3, 4, 5, 4, 6],
    'SquareFootage': [1500, 2000, 2500, 2200, 2800],
    'SalePrice': [200000, 250000, 300000, 280000, 350000]
}
house_data = pd.DataFrame(data)
filtered_data = house_data[house_data['Bedrooms'] > 4]
sale_prices = filtered_data['SalePrice'].values
average_sale_price = np.mean(sale_prices)
print("Average sale price of houses with more than four bedrooms:", average_sale_price)
