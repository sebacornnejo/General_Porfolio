# Scraping through internet knowledge

This project provides versatile web scraping scripts for extracting information from Google, Wikipedia, and Twitter, and visualizing word frequencies through word clouds and bar charts.
The example project "What is Anarchy for the Internet?" demonstrates how to utilize these scripts.

## Table of Contents

- [GoogleScraping01.py](#googlescraping01py)
- [GoogleScraping02.py](#googlescraping02py)
- [WikiScraping01.py](#wikiscraping01py)
- [WikiScraping02.py](#wikiscraping02py)
- [XScraping01.py](#xscraping01py)
- [scraping_wordcloud.py](#scraping_wordcloudpy)
- [How to Use](#how-to-use)
- [Example Project](#example-project)
- [Acknowledgments](#acknowledgments)

## [GoogleScraping01.py](GoogleScraping01.py)

This Python script utilizes the Google Custom Search JSON API to perform a search query and extract snippets from the results. It then generates a word cloud and a bar chart to visualize the word frequencies.

For detailed comments and code, view the [GoogleScraping01.py](GoogleScraping01.py).

## [GoogleScraping02.py](GoogleScraping02.py)

This Python script is an extension of GoogleScraping01.py, with added functionality for paginating through multiple search result pages.

For detailed comments and code, view the [GoogleScraping02.py](GoogleScraping02.py).

## [WikiScraping01.py](WikiScraping01.py)

This Python script uses web scraping to extract text from a Wikipedia page related to the search query "Anarchy" and generates a word cloud and a bar chart based on the extracted text.

For detailed comments and code, view the [WikiScraping01.py](WikiScraping01.py).

## [WikiScraping02.py](WikiScraping02.py)

This Python script retrieves content from multiple Wikipedia pages related to the search query, extracts text from each page, combines the text, and generates a word cloud and a bar chart based on the aggregated text.

For detailed comments and code, view the [WikiScraping02.py](WikiScraping02.py).

## [XScraping01.py](XScraping01.py)

This Python script performs web scraping of tweets related to the search query "Anarchy" using the ntscraper library and generates a word cloud and a bar chart based on the extracted tweet text.

For detailed comments and code, view the [XScraping01.py](XScraping01.py).

## [scraping_wordcloud.py](scraping_wordcloud.py)

This Python script uses the WordCloud library to generate a word cloud from input text, customizes the appearance, and then creates a bar chart to visualize word frequencies. Additionally, it saves the bar chart as an interactive HTML file.

For detailed comments and code, view the [scraping_wordcloud.py](scraping_wordcloud.py).

These scripts are designed for versatile scraping applications. Adjustments can be made to parameters for different use cases.

## How to Use

1. Clone the repository: `git clone --depth=1 --filter=blob:none https://github.com/sebacornnejo/General_Porfolio.git/ScrapingKnowledge`
2. Install the required libraries: `pip install -r requirements.txt`
3. Run the individual analysis scripts or the full dashboard script.
4. Explore the generated charts and dashboard HTML files.

## Example Project

Explore the example project "What is Anarchy for the Internet?" that showcases the usage of these scripts. The generated files include:

### Google search

#### A simple search

- [Word cloud image](./Images/WordsonaGooglesearch.png)
- [Bar chart HTML](https://sebacornnejo.github.io/WordsonaGooglesearch.html)
- [Combined text from Google scraping](Google01_text.txt)

#### Multi simple search

- [Word cloud image](./Images/WordsonmultiGooglesearch.png)
- [Bar chart HTML](https://sebacornnejo.github.io/WordsonmultiGooglesearch.html)
- [Combined text from Multi-Google scraping](Google02_text.txt)

### Wikipedia search

#### On a page

- [Word cloud image](./Images/WordsonaWikipediapage.png)
- [Bar chart HTML](https://sebacornnejo.github.io/WordsonaWikipediapage.html)
- [Combined text from Wikipedia scraping](Wiki01_text.txt)

#### On multi pages

- [Word cloud image](./Images/WordsonmultiWikipediapage.png)
- [Bar chart HTML](https://sebacornnejo.github.io/WordsonmultiWikipediapage.html)
- [Combined text from Multi-Wikipedia scraping](Wiki02_text.txt)

### Twitter tweets

#### 1000 tweets

- [Word cloud image](./Images/WordsonX.png)
- [Bar chart HTML](https://sebacornnejo.github.io/WordsonX.html)
- [Combined text from Twitter scraping](X01_text.txt)

## Acknowledgments

This project leverages several libraries and tools that contribute to its functionality. We would like to express our gratitude to the following:

- [Google Custom Search JSON API](https://developers.google.com/custom-search): Used in [GoogleScraping01.py](GoogleScraping01.py) and [GoogleScraping02.py](GoogleScraping02.py) for performing search queries and extracting snippets from the results.

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/): Applied in [WikiScraping01.py](WikiScraping01.py) and [WikiScraping02.py](WikiScraping02.py) for web scraping Wikipedia pages.

- [ntscraper](https://github.com/bocchilorenzo/ntscraper): A Python library used in [XScraping01.py](XScraping01.py) for scraping tweets related to the search query on Twitter.

- [WordCloud](https://github.com/amueller/word_cloud): Employed in [scraping_wordcloud.py](scraping_wordcloud.py) for generating word clouds based on the extracted text.

- [Plotly](https://plotly.com/): Utilized for creating interactive bar charts in [scraping_wordcloud.py](scraping_wordcloud.py).

I extend me appreciation to the developers and contributors behind these tools and APIs, as they significantly contributed to the success of this project.
