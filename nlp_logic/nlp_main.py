from textblob import TextBlob
import wikipedia
import nltk

nltk.download("punkt")


def search_wikipedia(name):
    """Search Wikipedia for a given name."""
    print(f"Searching for name: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Find and summarize Wikipedia content for a given name."""
    print(f"Finding Wikipedia summary for the name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Create a TextBlob object from the provided text."""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Search Wikipedia for a name, summarize the content, and extract noun phrases."""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
