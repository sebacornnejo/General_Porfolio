import requests
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
from collections import Counter
import os
# import pandas as pd
import plotly.graph_objects as go

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
        access = response.json()["items"]

        if "items" in data:
            snippets = [item["snippet"] for item in data["items"]]
            # Combina los snippets en un solo texto
            combined_text = " ".join(snippets)
            return combined_text

    except Exception as e:
        print(f"Error: {e}")
        return []


def generate_wordcloud(text):
    flag_mask = np.array(PIL.Image.open("Anarchy_Symbol.png"))
    colormap = ImageColorGenerator(flag_mask)
    wc = WordCloud(
        width=800,
        height=800,
        stopwords=STOPWORDS.update(
            [
                "view",
                "rosario",
                "picture",
                "pages",
                "url",
                "tarefa",
                "T",
                "etc",
                "Add",
                "et",
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
                "thus",
                "often",
                "generally",
                "specifically",
                "described",
                "defined",
                "without",
                "based",
                "αναρχία",
                "αν",
                "αρχία",
                "first",
                "one",
                "later",
                "two",
                "refer",
                "use",
                "due",
                "ago",
            ]
        ),
        mask=flag_mask,
        # width=800,
        # height=400,
        background_color="white",
        min_font_size=3,
        max_words=400,
        font_path="Montserrat-Regular.ttf",
    ).generate(text)

    wc.recolor(color_func=colormap)
    plt.figure(figsize=(10, 10))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")

    plt.savefig("./Images/WordsonaGooglesearch.png", dpi=300, bbox_inches="tight")

    plt.show()

    word_freq = Counter(text.split())
    wc_data = wc.words_

    # Filtrar word_freq para incluir solo las palabras presentes en wc_data
    word_freq = {word: freq for word, freq in word_freq.items() if word in wc_data}

    # Crear un DataFrame para las palabras
    # wordf = pd.DataFrame(wc_data.items(), columns=['word', 'freq'])
    # wordf['count'] = wordf['word'].apply(lambda w: f"{word_freq[w]}")

    return Counter(word_freq)


def generate_bar_chart(word_counter):
    common_words = word_counter.most_common(20)

    # Crear el gráfico de barras con Plotly
    figbar = go.Figure()
    figbar.add_trace(
        go.Bar(
            x=[word[0] for word in common_words],
            y=[word[1] for word in common_words],
            marker_color="#6331C5",
        )
    )  # Utiliza el color principal que hemos estado usando

    # Personalizar el diseño del gráfico
    figbar.update_layout(
        xaxis_title="Words",
        yaxis_title="Count",
        title='<b style="font-size:16px;">Top 20 words related to Anarchy</b><br><span style="font-size:12px;">on a Google search</span>',
        template="plotly_dark",  # Utiliza el tema oscuro que hemos estado utilizando
        font_family="Montserrat",  # Utiliza la fuente que hemos estado utilizando
    )

    figbar.update_traces(
        marker=dict(line=dict(color="#F2F2F2")),
        hovertemplate="Word: %{x}<br>Count: %{y}",
        name="",
    )

    # Mostrar el gráfico
    figbar.show()

    # Add custom styles and links to the head of the HTML file
    styles = """
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Montserrat', sans-serif;
            }
        </style>
    """

    # Save the interactive HTML chart
    # Uncomment the following line to save the interactive HTML chart:
    figbar.write_html("./HTMLs/WordsonaGooglesearch.html")

    # Add Montserrat font style to the generated HTML
    # Read the content of the generated HTML file with UTF-8 encoding
    with open("./HTMLs/WordsonaGooglesearch.html", "r", encoding="utf-8") as file:
        content = file.read()

    # Insert the styles in the head of the HTML file
    content = content.replace("</head>", styles + "</head>")

    # Escribir el contenido modificado de nuevo al archivo HTML
    with open("./HTMLs/WordsonaGooglesearch.html", "w", encoding="utf-8") as file:
        file.write(content)


def main():
    # Reemplaza "api_key" y "cx" con tus propias credenciales
    api_key = open("API_KEY").read()
    cx = open("SEARCH_ENGINE_ID").read()
    search_query = "Anarchy"
    # Verificar si el archivo ya existe
    # OJO: SI EL SEARCH_QUERY ES CAMBIADO, DEBE ELIMINAR EL ARCHIVO ANTERIOR
    if os.path.exists("Google01_text.txt"):
        with open("Google01_text.txt", "r", encoding="utf-8") as file:
            text = file.read()
    else:
        # Realizar scraping si el archivo no existe
        # Realiza la búsqueda y obtén los snippets de los resultados
        text = words_google_search(search_query, api_key, cx)

        # Guardar el contenido en un archivo de texto
        with open("Google01_text.txt", "w", encoding="utf-8") as file:
            file.write(text)

    # Plot Word Cloud and return frequency words to bar plot
    word_freq = generate_wordcloud(text)

    # Plot Bar Chart
    generate_bar_chart(word_freq)


if __name__ == "__main__":
    main()