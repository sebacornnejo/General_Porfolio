# -----------------------------------------------------------------------------------------#
# This Python script utilizes the Google Custom Search JSON API to perform a search query and extract snippets from the results. It then generates a word cloud and a bar chart to visualize the word frequencies.
# -----------------------------------------------------------------------------------------#


import requests
import os
from scraping_wordcloud import generate_wordcloud, generate_bar_chart

search_query = "Anarchy"  # Update this to your search query
mask_path = "Anarchy_Symbol.png"  # Image for wordcloud mask
custom_stopwords_path = (
    "custom_stopwords.txt"  # Update this to your custom stopwords file path
)
output_png_path = (
    "./Images/WordsonaGooglesearch.png"  # Update this to your desired output PNG path
)
output_html_path = (
    "./HTMLs/WordsonaGooglesearch.html"  # Update this to your desired output HTML path
)
main_title = "Top 20 words related to Anarchy"  # Update this to your main title
subtitle = "on a Google search"  # Update this to your subtitle

# -----------------------------------------------------------------------------------------#
# 'words_google_search' Function:

# This function performs a Google search using the Google Custom Search JSON API.
# It takes the search query, API key, and custom search engine ID (cx).
# The API response is parsed, and snippets from the search results are extracted and combined into a single text.
# The combined text is returned.
# -----------------------------------------------------------------------------------------#


def words_google_search(search_query, api_key, cx):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "q": search_query,
        "key": api_key,
        "cx": cx,
        # "searchType" : "image",
        # "fileType" : "pdf",
        "lr": "lang_en",
        # "gl" : "us",
        # "dateRestrict": "2021-01-01:2021-12-31",
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        # access = response.json()["items"]

        if "items" in data:
            snippets = [item["snippet"] for item in data["items"]]
            # Combine the snippets into a single text
            combined_text = " ".join(snippets)
            return combined_text

    except Exception as e:
        print(f"Error: {e}")
        return []


# -----------------------------------------------------------------------------------------#
# 'main' Section:

# The main function reads the API key and search engine ID from files.
# It checks if a text file (Google01_text.txt) containing search results exists. If not, it performs the Google search and saves the results.
# The generate_wordcloud function is called to create a word cloud, and the word frequencies are obtained.
# The generate_bar_chart function is then called to create a bar chart with the word frequencies.
# -----------------------------------------------------------------------------------------#


def main():
    # Replace "api_key" and "cx" with your own credentials
    api_key = open("API_KEY").read()
    cx = open("SEARCH_ENGINE_ID").read()

    # Check if the file already exists
    # NOTE: IF THE SEARCH_QUERY IS CHANGED, YOU MUST DELETE THE PREVIOUS FILE
    if os.path.exists("Google01_text.txt"):
        with open("Google01_text.txt", "r", encoding="utf-8") as file:
            text = file.read()
    else:
        # Perform scraping if file does not exist
        # Perform the search and get snippets of the results
        text = words_google_search(search_query, api_key, cx)

        # Save content to a text file
        with open("Google01_text.txt", "w", encoding="utf-8") as file:
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
# - Replace "API_KEY" and "SEARCH_ENGINE_ID" with your actual API key and custom search engine ID.
# - The script saves the combined text of snippets in a file (Google01_text.txt) to avoid unnecessary API requests.
# - If the search query is changed, delete the existing text file to perform a new search.
# - Ensure the necessary libraries (requests, os, scraping_wordcloud) are installed.
# - This script demonstrates a simple example of web scraping and data visualization using Python. Adjustments can be made for customization and further enhancements.
# -----------------------------------------------------------------------------------------#
