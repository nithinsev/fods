import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load the dataset from CSV file
df = pd.read_csv("C:/Users/SysSoft/Documents/lex programs/New folder/data.csv")

# Preprocess the text data
def preprocess_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert text to lowercase
    text = text.lower()
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

# Apply preprocessing to each feedback
df['preprocessed_feedback'] = df['feedback'].apply(preprocess_text)

# Flatten the list of preprocessed tokens
all_tokens = [token for sublist in df['preprocessed_feedback'] for token in sublist]

# Calculate the frequency distribution of words
word_freq = Counter(all_tokens)

# Display the top N most frequent words and their corresponding frequencies
def display_top_words(word_freq, top_n):
    top_words = word_freq.most_common(top_n)
    for word, freq in top_words:
        print(f"{word}: {freq}")

# Get user input for N
top_n = int(input("Enter the number of top words to display: "))

# Display the top N most frequent words and their frequencies
print(f"\nTop {top_n} most frequent words and their frequencies:")
display_top_words(word_freq, top_n)

# Plot a bar graph to visualize the top N most frequent words and their frequencies
top_words_df = pd.DataFrame(word_freq.most_common(top_n), columns=['Word', 'Frequency'])
plt.figure(figsize=(10, 6))
plt.bar(top_words_df['Word'], top_words_df['Frequency'], color='skyblue')
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.title(f'Top {top_n} Most Frequent Words')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
