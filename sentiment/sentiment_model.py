# sentiment/sentiment_model.py

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Returns compound sentiment score between -1 (neg) and +1 (pos).
    """
    if not text:
        return 0.0
    score = analyzer.polarity_scores(text)
    return score["compound"]

# Example usage
if __name__ == "__main__":
    print(analyze_sentiment("Bitcoin is going to the moon!"))
    print(analyze_sentiment("I lost everything in crypto."))