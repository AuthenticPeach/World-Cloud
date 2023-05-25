import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the NLTK stopword data
nltk.download('stopwords')
nltk.download('punkt')

def generate_word_cloud(text):
    # Tokenize the text and remove stopwords
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word.lower() for word in tokens if word.lower() not in stop_words and word.isalpha()]

    # Create the word cloud
    word_cloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(' '.join(filtered_tokens))

    # Display the word cloud
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

if __name__ == "__main__":
    sample_text = "Die by the blade for the one you love."
    generate_word_cloud(sample_text)
