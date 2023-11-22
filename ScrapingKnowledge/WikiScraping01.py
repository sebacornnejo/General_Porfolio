# -----------------------------------------------------------------------------------------#
# This Python script uses web scraping to extract text from a Wikipedia page related to a search query and then generates a word cloud and a bar chart based on the extracted text.
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
output_png_path = (
    "./Images/WordsonaWikipediapage.png"  # Update this to your desired output PNG path
)
output_html_path = (
    "./HTMLs/WordsonaWikipediapage.html"  # Update this to your desired output HTML path
)
main_title = "Top 20 words related to Anarchy"  # Update this to your desired main title
subtitle = "on a Wikipedia page"  # Update this to your desired subtitle

# -----------------------------------------------------------------------------------------#
# 1) 'get_wikipedia_page' Function:
# Takes a search query.
# Sends a request to the Wikipedia search page with the provided query.
# Returns the HTML content of the search results page.
# -----------------------------------------------------------------------------------------#


def get_wikipedia_page(search_query):
    base_url = "https://en.wikipedia.org/w/index.php"
    params = {"search": search_query, "title": "Special:Search", "go": "Go", "ns0": 1}

    response = requests.get(base_url, params=params)
    return response.text


# -----------------------------------------------------------------------------------------#
# 2) 'extract_text_from_page' Function:
# Takes the HTML content of a Wikipedia page.
# Uses BeautifulSoup to parse the HTML and extract text from all paragraphs (<p> elements).
# Returns the concatenated text from all paragraphs.
# -----------------------------------------------------------------------------------------#


def extract_text_from_page(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    paragraphs = soup.find_all("p")
    text = " ".join([p.get_text() for p in paragraphs])
    return text


# -----------------------------------------------------------------------------------------#
# 'main' Section:

# Checks if a file named "Wiki01_text.txt" exists. If it does, it reads the content from the file.
# If the file doesn't exist, it calls get_wikipedia_page to fetch the Wikipedia search page content, then uses extract_text_from_page to extract text from the page.
# The extracted text is saved to "Wiki01_text.txt".
# Calls generate_wordcloud and generate_bar_chart functions to generate the word cloud and bar chart based on the extracted text.
# -----------------------------------------------------------------------------------------#


def main():
    # Check if the file already exists
    # NOTE: IF THE SEARCH_QUERY IS CHANGED, YOU MUST DELETE THE PREVIOUS FILE
    if os.path.exists("Wiki01_text.txt"):
        with open("Wiki01_text.txt", "r", encoding="utf-8") as file:
            text = file.read()
    else:
        # Perform scraping if file does not exist
        page_content = get_wikipedia_page(search_query)
        text = extract_text_from_page(page_content)

        # Save the content to a text file
        with open("Wiki01_text.txt", "w", encoding="utf-8") as file:
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
# Web scraping Wikipedia pages should comply with Wikipedia's terms of service, which generally permit automated access but discourage scraping excessively or disruptively. Always check and adhere to the website's terms of use.
# -----------------------------------------------------------------------------------------#
