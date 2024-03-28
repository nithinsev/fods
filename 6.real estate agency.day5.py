import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'number_of_bedrooms': [3, 4, 5, 3, 4],
    'area_sq_feet': [1500, 2000, 2500, 1800, 2200],
    'listing_price': [200000, 250000, 300000, 220000, 280000]
}
property_data = pd.DataFrame(data)
average_price_per_location = property_data.groupby('location')['listing_price'].mean()
print("Average listing price of properties in each location:\n", average_price_per_location)

properties_more_than_four_bedrooms = property_data[property_data['number_of_bedrooms'] > 4]
num_properties_more_than_four_bedrooms = properties_more_than_four_bedrooms.shape[0]
print("Number of properties with more than four bedrooms:", num_properties_more_than_four_bedrooms)

property_with_largest_area = property_data.loc[property_data['area_sq_feet'].idxmax()]
print("Property with the largest area:\n", property_with_largest_area)
