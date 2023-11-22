# -----------------------------------------------------------------------------------------#
# This Python script is similar to GoogleScraping01.py, with the main difference being the modification of the words_google_search function to allow for pagination through multiple search result pages.
# -----------------------------------------------------------------------------------------#


import requests
import os
from scraping_wordcloud import generate_wordcloud, generate_bar_chart

search_query = "Anarchy"  # Update this to your search query
npages = 50  # Number of pages to retrieve
mask_path = "Anarchy_Symbol.png"  # Image for wordcloud mask
custom_stopwords_path = (
    "custom_stopwords.txt"  # Update this to your custom stopwords file path
)
output_png_path = "./Images/WordsonmultiGooglesearch.png"  # Update this to your desired output PNG path
output_html_path = "./HTMLs/WordsonmultiGooglesearch.html"  # Update this to your desired output HTML path
main_title = "Top 20 words related to Anarchy"  # Update this to your desired main title
subtitle = "on multi Google search"  # Update this to your desired subtitle

# -----------------------------------------------------------------------------------------#
# 'words_google_search' Function:

# The words_google_search function now takes two additional parameters, start_page and num_pages. These parameters control the starting page and the number of pages to retrieve.
# It iterates over the specified number of pages, adjusting the start parameter in the API request to fetch results from different pages.
# Snippets from each page are added to the snippets list.
# The combined text of all snippets is returned.
# -----------------------------------------------------------------------------------------#


def words_google_search(search_query, api_key, cx, start_page=1, num_pages=30):
    snippets = []
    for page in range(start_page, start_page + num_pages):
        start_index = (page - 1) * 10 + 1
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
            "start": start_index,
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            if "items" in data:
                snippets.extend([item.get("snippet", "") for item in data["items"]])

        except Exception as e:
            print(f"Error: {e}")

    # Combine the fragments into a single text
    combined_text = " ".join(snippets)
    return combined_text


# -----------------------------------------------------------------------------------------#
# 'main' Section:

# The main function now calls words_google_search with the num_pages parameter set to the specified number of pages (npages).
# The script then continues with the word cloud and bar chart generation as GoogleScraping01.py.
# -----------------------------------------------------------------------------------------#


def main():
    # Replace "api_key" and "cx" with your own credentials
    api_key = open("API_KEY").read()
    cx = open("SEARCH_ENGINE_ID").read()
    # Check if the file already exists
    # NOTE: IF THE SEARCH_QUERY IS CHANGED, YOU MUST DELETE THE PREVIOUS FILE
    if os.path.exists("Google02_text.txt"):
        with open("Google02_text.txt", "r", encoding="utf-8") as file:
            text = file.read()
    else:
        # Perform scraping if file does not exist
        # Perform the search and get snippets of the results
        text = words_google_search(search_query, api_key, cx, num_pages=int(npages))

        # Guardar el contenido en un archivo de texto
        with open("Google02_text.txt", "w", encoding="utf-8") as file:
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
# Remember to replace "API_KEY" and "SEARCH_ENGINE_ID" with your actual API key and custom search engine ID. Additionally, ensure that the necessary libraries (requests, os, scraping_wordcloud) are installed.
# -----------------------------------------------------------------------------------------#
