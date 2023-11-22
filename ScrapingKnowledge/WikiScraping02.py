# -----------------------------------------------------------------------------------------#
# This Python script retrieves content from multiple Wikipedia pages related to a search query, extracts text from each page, combines the text, and then generates a word cloud and a bar chart based on the aggregated text.
# -----------------------------------------------------------------------------------------#


import requests
from bs4 import BeautifulSoup
import os
from scraping_wordcloud import generate_wordcloud, generate_bar_chart

search_query = "Anarchy"  # Update this to your search query
mask_path = "Anarchy_Symbol.png"  # Image for wordcloud mask
custom_stopwords_path = (
    "custom_stopwords.txt"  # Update this to your custom stopwords file path
)
output_png_path = "./Images/WordsonmultiWikipediapage.png"  # Update this to your desired output PNG path
output_html_path = "./HTMLs/WordsonmultiWikipediapage.html"  # Update this to your desired output HTML path
main_title = "Top 20 words related to Anarchy"  # Update this to your desired main title
subtitle = "on multi Wikipedia pages"  # Update this to your desired subtitle

# -----------------------------------------------------------------------------------------#
# 1) 'get_wikipedia_pages' Function:
# Takes a search query.
# Sends a request to the Wikipedia API's search endpoint.
# Returns a list of pages related to the search query.
# -----------------------------------------------------------------------------------------#


def get_wikipedia_pages(search_query):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": search_query,
        "format": "json",
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    return data["query"]["search"]


# -----------------------------------------------------------------------------------------#
# 2) 'get_page_content' Function:
# Takes the title of a Wikipedia page.
# Sends a request to the Wikipedia API's parse endpoint to get the content of the specified page.
# Returns the HTML content of the page.
# -----------------------------------------------------------------------------------------#


def get_page_content(page_title):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {"action": "parse", "page": page_title, "format": "json"}

    response = requests.get(base_url, params=params)
    data = response.json()
    return data["parse"]["text"]["*"]


# -----------------------------------------------------------------------------------------#
# 'main' Section:

# Checks if a file named "Wiki02_text.txt" exists. If it does, it reads the content from the file.
# If the file doesn't exist, it calls get_wikipedia_pages to fetch a list of Wikipedia pages related to the search query.
# For each page, it calls get_page_content to retrieve the HTML content and uses BeautifulSoup to extract text from paragraphs.
# The extracted text from all pages is saved to "Wiki02_text.txt."
# Calls generate_wordcloud and generate_bar_chart functions to generate the word cloud and bar chart based on the aggregated text.
# -----------------------------------------------------------------------------------------#


def main():
    # Check if the file already exists
    # NOTE: IF THE SEARCH_QUERY IS CHANGED, YOU MUST DELETE THE PREVIOUS FILE
    if os.path.exists("Wiki02_text.txt"):
        with open("Wiki02_text.txt", "r", encoding="utf-8") as file:
            all_text = file.read()
    else:
        pages = get_wikipedia_pages(search_query)

        all_text = ""
        for page in pages:
            title = page["title"]
            content = get_page_content(title)

            # Use BeautifulSoup to extract text
            soup = BeautifulSoup(content, "html.parser")
            paragraphs = soup.find_all("p")
            text = " ".join([p.get_text() for p in paragraphs])

            all_text += text

        # Save the content to a text file
        with open("Wiki02_text.txt", "w", encoding="utf-8") as file:
            file.write(all_text)

    # Plot Word Cloud
    word_freq = generate_wordcloud(
        all_text, mask_path, custom_stopwords_path, output_png_path
    )

    # Plot Bar Chart
    generate_bar_chart(word_freq, output_html_path, main_title, subtitle)


if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------------------#
# NOTE:
# Web scraping Wikipedia pages should comply with Wikipedia's terms of service. Always check and adhere to the website's terms of use.
# -----------------------------------------------------------------------------------------#
