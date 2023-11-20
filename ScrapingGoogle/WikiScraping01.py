import requests
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
from collections import Counter
import plotly.graph_objects as go


def get_wikipedia_page(search_query):
    base_url = "https://en.wikipedia.org/w/index.php"
    params = {
        "search": search_query,
        "title": "Special:Search",
        "go": "Go",
        "ns0": 1
    }

    response = requests.get(base_url, params=params)
    return response.text

def extract_text_from_page(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join([p.get_text() for p in paragraphs])
    return text


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
    
    # word_freq = Counter(text.split())
    # wc_data = wc.words_

    
    # import plotly.express as px
    # import pandas as pd
    # # Crear un DataFrame para Plotly Express
    # df = pd.DataFrame(wc_data.items(), columns=['word', 'freq'])

    # fig = px.scatter(df,
    #                  x='word',
    #                  y='freq',
    #                  size='freq',
    #                  hover_name='word',
    #                  color='freq',
    #                  color_continuous_scale='viridis',
    #                  text=df['word'].apply(lambda w: f"{w}: {word_freq[w]}"))

    # fig.update_layout(title='Word Cloud',
    #                   xaxis={'showgrid': False, 'showticklabels': False, 'zeroline': False},
    #                   yaxis={'showgrid': False, 'showticklabels': False, 'zeroline': False})

    # return fig


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
    page_content = get_wikipedia_page(search_query)
    text = extract_text_from_page(page_content)
    
    # Guardar el contenido en un archivo de texto
    with open('Wiki01_text.txt', 'w', encoding='utf-8') as file:
        file.write(text)

    # Plot Word Cloud
    generate_wordcloud(text)
    # plotly_fig = generate_wordcloud(text)
    
    # plotly_fig.show()

    # Plot Bar Chart
    generate_bar_chart(text)

if __name__ == "__main__":
    main()
