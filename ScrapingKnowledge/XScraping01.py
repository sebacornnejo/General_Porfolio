# -----------------------------------------------------------------------------------------#
# This Python script performs web scraping of tweets related to a search query using the ntscraper library, and then generates a word cloud and a bar chart based on the extracted tweet text.
# -----------------------------------------------------------------------------------------#


import os
from scraping_wordcloud import generate_wordcloud, generate_bar_chart

search_query = "Anarchy"  # Update this to your search query
no_tweets = "1000"  # Update this to the number of tweets you want to retrieve
mask_path = "Anarchy_Symbol.png"  # Image for wordcloud mask
custom_stopwords_path = (
    "custom_stopwords.txt"  # Update this to your custom stopwords file path
)
output_png_path = "./Images/WordsonX.png"  # Update this to your desired output PNG path
output_html_path = (
    "./HTMLs/WordsonX.html"  # Update this to your desired output HTML path
)
main_title = "Top 20 words related to Anarchy"  # Update this to your desired main title
subtitle = "on X"  # Update this to your desired subtitle

# -----------------------------------------------------------------------------------------#
# 'get_tweets' Function:
# Uses the ntscraper library to retrieve tweets related to a specified query.
# Parameters:
#           query: The search query (e.g., "Anarchy").
#           modes: The search mode (e.g., "term").
#           no: The number of tweets to retrieve.
# Returns the combined text of the tweets.
# -----------------------------------------------------------------------------------------#


def get_tweets(query, modes, no):
    from ntscraper import (
        Nitter,
    )  # Read more at https://github.com/bocchilorenzo/ntscraper

    # If you want to extract a table from scraping, uncomment the pandas import and the commented content within the function
    # import pandas as pd

    scrapper = Nitter()
    tweets = scrapper.get_tweets(query, mode=modes, number=float(no), language="en")
    final_tweets = []
    # full_tweets = []
    for tweet in tweets["tweets"]:
        # full_data = [tweet["link"],tweet["text"],tweet["date"],tweet["stats"]["likes"],tweet["stats"]["comment"]]
        data = tweet["text"]
        # full_tweets.append(full_data)
        final_tweets.append(data)
    # full_data = pd.DataFrame(full_tweets, columns=["link","text","date","No_of_Likes","No_of_tweets"])
    data = " ".join(final_tweets)
    return data  # full_data


# -----------------------------------------------------------------------------------------#
# 'main' Section:

# Checks if a file named "X01_text.txt" exists. If it does, it reads the content from the file.
# If the file doesn't exist, it calls the get_tweets function to fetch tweets related to the search query.
# The extracted tweet text is saved to "X01_text.txt."
# Calls the generate_wordcloud and generate_bar_chart functions to generate the word cloud and bar chart based on the tweet text.
# -----------------------------------------------------------------------------------------#


def main():
    # Check if the file already exists
    # NOTE: IF THE SEARCH_QUERY IS CHANGED, YOU MUST DELETE THE PREVIOUS FILE
    if os.path.exists("X01_text.txt"):
        with open("X01_text.txt", "r", encoding="utf-8") as file:
            text = file.read()
    else:
        # Scrapes tweets if the file doesn't exist
        text = get_tweets(search_query, "term", no_tweets)

        # Saves the tweet content to a text file
        with open("X01_text.txt", "w", encoding="utf-8") as file:
            file.write(text)

    # Plot Word Cloud and return frequency words to bar plot
    word_freq = generate_wordcloud(
        text, mask_path, custom_stopwords_path, output_png_path
    )

    # Plot Bar Chart
    generate_bar_chart(word_freq, output_html_path, main_title, subtitle)


if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------------------#
# NOTE:
# - Make sure to comply with the terms of service of the platform you are scraping (in this case, Twitter) and respect their usage policies.
# - Ntscraper library can only be used for academic purposes.
# - Also, consider handling potential exceptions that might occur during the scraping process.
# -----------------------------------------------------------------------------------------#
