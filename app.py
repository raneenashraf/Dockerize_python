import nltk

# Importing necessary modules from NLTK
from nltk.corpus import webtext
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK data for stopwords
nltk.download('stopwords')

# Create a set of English stopwords
english_stops = set(stopwords.words('english'))
print(english_stops)

# Download NLTK data for tokenization
nltk.download('punkt')

# Open and read the text file
with open("paragraphs.txt", "r") as file:
    text = file.read()

# Tokenize the text into words
words = word_tokenize(text)

# Remove stopwords from the list of words
filtered_words = [word for word in words if word not in english_stops]

# Import Counter from collections module to count word frequencies
from collections import Counter

# Count the frequency of each word in the filtered list
word_freq = Counter(filtered_words)

# Print the frequency of each word
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
