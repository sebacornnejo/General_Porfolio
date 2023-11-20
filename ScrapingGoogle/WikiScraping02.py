import requests
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
from collections import Counter


def get_wikipedia_pages(search_query):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": search_query,
        "format": "json"
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    return data['query']['search']

def get_page_content(page_title):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": page_title,
        "format": "json"
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    return data['parse']['text']['*']

def generate_wordcloud(text):
    flag_mask = np.array(PIL.Image.open("Anarchy_Symbol.png"))
    colormap = ImageColorGenerator(flag_mask)
    wc = WordCloud(
        stopwords=STOPWORDS.update(
            [
                "view",
                "rosario",
                "picture",
                "pages",
                "january",
                "url",
                "tarefa",
                "T",
                "etc",
                "Jul",
                "Apr",
                "May",
                "Sep",
                "Feb",
                "Add",
                "et",
                "Jan",
                "Mar",
                "Dec",
                "Jun",
                "Aug",
                "Nov",
                "Oct",
                "July",
                "April",
                "September",
                "February",
                "March",
                "December",
                "June",
                "August",
                "November",
                "October",
            ]
        ),
        mask=flag_mask,
        # width=800,
        # height=400,
        background_color="white",
        min_font_size=3,
        max_words=400,
    ).generate(text)

    wc.recolor(color_func=colormap)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def generate_bar_chart(text):
    words = text.split()
    word_counter = Counter(words)
    common_words = word_counter.most_common(10)

    plt.figure(figsize=(10, 5))
    plt.bar([word[0] for word in common_words], [word[1] for word in common_words])
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Words related to anarchism in Wiki")
    plt.show()


def main():
    search_query = "Anarchism"
    pages = get_wikipedia_pages(search_query)

    all_text = ""
    for page in pages:
        title = page['title']
        content = get_page_content(title)

        # Use BeautifulSoup to extract text
        soup = BeautifulSoup(content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])

        all_text += text
        
    # Guardar el contenido en un archivo de texto
    with open('Wiki02_text.txt', 'w', encoding='utf-8') as file:
        file.write(all_text)

    # Plot Word Cloud
    generate_wordcloud(all_text)

    # Plot Bar Chart
    generate_bar_chart(all_text)

if __name__ == "__main__":
    main()
