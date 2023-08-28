from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    analysis = TextBlob(text)
    
    # Get the polarity score (-1 to 1, where < 0 is negative, > 0 is positive)
    polarity = analysis.sentiment.polarity

    # Determine the sentiment based on the polarity score
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Get user input for the text string
text_input = input("Enter a text string: ")

# Analyze the sentiment and print the result
sentiment = analyze_sentiment(text_input)
print(f"The sentiment of the text is: {sentiment}")
