from collections import Counter
likes_data = [10, 15, 20, 10, 25, 15, 10, 30, 20, 25, 15, 20, 10, 30, 25, 20]
likes_distribution = Counter(likes_data)
print("Frequency distribution of likes:")
for likes, frequency in likes_distribution.items():
    print(f"Likes: {likes}, Frequency: {frequency}")
