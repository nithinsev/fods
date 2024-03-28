import pandas as pd
property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4, 5],
    'location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'number_of_bedrooms': [3, 4, 5, 3, 6],
    'area_sq_ft': [1500, 1800, 2200, 1600, 2500],
    'listing_price': [200000, 250000, 300000, 220000, 350000]
})
average_price_per_location = property_data.groupby('location')['listing_price'].mean()
num_properties_more_than_four_bedrooms = (property_data['number_of_bedrooms'] > 4).sum()
property_largest_area = property_data.loc[property_data['area_sq_ft'].idxmax()]
print("Average listing price of properties in each location:")
print(average_price_per_location)
print("\nNumber of properties with more than four bedrooms:", num_properties_more_than_four_bedrooms)
print("\nProperty with the largest area:")
print(property_largest_area)
