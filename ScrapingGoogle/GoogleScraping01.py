import requests
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
from collections import Counter


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
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            if "items" in data:
                snippets.extend([item["snippet"] for item in data["items"]])

        except Exception as e:
            print(f"Error: {e}")

    return snippets


# def words_google_search(search_query, api_key, cx):
#     url = f"https://www.googleapis.com/customsearch/v1"
#     params = {
#         "q": search_query,
#         "key": api_key,
#         "cx": cx,
#         # "searchType" : "image",
#         # "fileType" : "pdf",
#         "lr": "lang_en",
#         # "gl" : "us",
#         # "dateRestrict": "2021-01-01:2021-12-31",
#     }

#     try:
#         response = requests.get(url, params=params)
#         data = response.json()
#         access = response.json()["items"]

#         if "items" in data:
#             snippets = [item["snippet"] for item in data["items"]]
#             return snippets

#     except Exception as e:
#         print(f"Error: {e}")
#         return []


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
    plt.title("Words related to anarchism in Google")
    plt.show()


# Reemplaza "api_key" y "cx" con tus propias credenciales
api_key = open("API_KEY").read()
cx = open("SEARCH_ENGINE_ID").read()
search_query = "Anarchism"

# Realiza la búsqueda y obtén los snippets de los resultados
search_results = words_google_search(search_query, api_key, cx)
# search_results = words_google_search(search_query, api_key, cx, num_pages=30)

# Combina los snippets en un solo texto
combined_text = " ".join(search_results)

# Genera y muestra el word cloud
generate_wordcloud(combined_text)

# Genera y muestra el gráfico de barras
generate_bar_chart(combined_text)
