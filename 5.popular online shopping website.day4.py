import pandas as pd
import numpy as np
from scipy import stats
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E',
             'Product F', 'Product G', 'Product H', 'Product I', 'Product J'],
    'categories': ['electronics', 'electronics', 'electronics', 'electronics', 'electronics',
                   'electronics', 'electronics', 'electronics', 'electronics', 'electronics'],
    'manufacturer': ['Manufacturer X', 'Manufacturer X', 'Manufacturer Y', 'Manufacturer Y', 'Manufacturer Z',
                     'Manufacturer Z', 'Manufacturer X', 'Manufacturer Y', 'Manufacturer Z', 'Manufacturer X'],
    'manufacturer_number': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'reviews_date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05',
                     '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10'],
    'reviews_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'reviews_rating': [4.5, 3.8, 4.2, 4.0, 3.9, 4.6, 4.3, 4.1, 3.7, 4.4],
    'reviews_text': ['Great product!', 'Could be better.', 'Awesome!', 'Not bad.', 'Good value for money.',
                     'Excellent!', 'Satisfied with purchase.', 'Needs improvement.', 'Disappointed.', 'Highly recommended.']
}
customer_reviews = pd.DataFrame(data)
product_category = 'electronics'
reviews_ratings = customer_reviews[customer_reviews['categories'] == product_category]['reviews_rating']
mean_rating = reviews_ratings.mean()
std_dev = reviews_ratings.std()
n = len(reviews_ratings)
sem = std_dev / np.sqrt(n)
confidence_level = 0.95
z_score = stats.norm.ppf((1 + confidence_level) / 2)
margin_of_error = z_score * sem
confidence_interval = (mean_rating - margin_of_error, mean_rating + margin_of_error)
print("Mean Rating for {}:".format(product_category), mean_rating)
print("Standard Deviation:", std_dev)
print("Confidence Interval ({}%):".format(confidence_level * 100), confidence_interval)
