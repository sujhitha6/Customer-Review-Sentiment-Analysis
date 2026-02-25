import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("flipkart_reviews.csv")

print("Dataset Preview:")
print(data.head())
print("Total rows:", len(data))


# Sentiment function
def get_sentiment(review):
    polarity = TextBlob(str(review)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


# Apply sentiment
data["Sentiment"] = data["Review"].apply(get_sentiment)

print("\nSentiment Counts:")
print(data["Sentiment"].value_counts())


# Plot graph
plt.figure(figsize=(6,4))
sns.countplot(x=data["Sentiment"])
plt.title("Sentiment Distribution")
plt.show()


data["Sentiment"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Sentiment Percentage")
plt.ylabel("")
plt.show()