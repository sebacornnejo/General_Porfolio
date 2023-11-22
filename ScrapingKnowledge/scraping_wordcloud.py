# -----------------------------------------------------------------------------------------#
# This Python script uses the WordCloud library to generate a word cloud from input text, customizes the appearance, and then creates a bar chart to visualize word frequencies. Additionally, it saves the bar chart as an interactive HTML file.
# -----------------------------------------------------------------------------------------#


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
from collections import Counter
import plotly.graph_objects as go


# -----------------------------------------------------------------------------------------#
# 1) 'generate_wordcloud' Function:

# This function takes input text, a mask image, a file containing custom stopwords, and an output path for saving the generated word cloud PNG.
# It creates a WordCloud object, customizes its appearance, and generates the word cloud using the input text.
# The word cloud is displayed, saved as a PNG file, and the word frequencies are counted.
# The function returns a Counter object containing word frequencies.
# -----------------------------------------------------------------------------------------#


def generate_wordcloud(text, mask_path, custom_stopwords_path, output_png_path):
    # Load a mask image and create a colormap
    flag_mask = np.array(PIL.Image.open(mask_path))
    colormap = ImageColorGenerator(flag_mask)

    # Load custom stopwords from a file
    with open(custom_stopwords_path, "r", encoding="utf-8") as file:
        custom_stopwords = [line.strip() for line in file]

    # Generate WordCloud
    wc = WordCloud(
        width=800,
        height=800,
        stopwords=STOPWORDS.update(custom_stopwords),
        mask=flag_mask,
        background_color="white",
        min_font_size=3,
        max_words=400,
        font_path="Montserrat-Regular.ttf",
    ).generate(text)

    # Recolor the WordCloud based on the colormap
    wc.recolor(color_func=colormap)

    # Display the WordCloud
    plt.figure(figsize=(10, 10))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")

    # Save the WordCloud as a PNG file
    plt.savefig(output_png_path, dpi=300, bbox_inches="tight")
    plt.show()

    # Count the frequency of words in the text
    word_freq = Counter(text.split())
    wc_data = wc.words_
    word_freq = {word: freq for word, freq in word_freq.items() if word in wc_data}

    return Counter(word_freq)


# -----------------------------------------------------------------------------------------#
# 2) 'generate_bar_chart' Function:

# This function takes a Counter object with word frequencies, an output path for saving the interactive HTML chart, main title, and subtitle.
# It creates a bar chart using Plotly with the 20 most common words and their frequencies.
# The layout and appearance of the chart are customized.
# The chart is displayed, and an HTML file is generated and saved with custom styles.
# -----------------------------------------------------------------------------------------#


def generate_bar_chart(word_counter, output_html_path, main_title, subtitle):
    # Get the most common 20 words and their frequencies
    common_words = word_counter.most_common(20)

    # Create a bar chart using Plotly
    figbar = go.Figure()
    figbar.add_trace(
        go.Bar(
            x=[word[0] for word in common_words],
            y=[word[1] for word in common_words],
            marker_color="#6331C5",
        )
    )

    # Customize the layout of the bar chart
    figbar.update_layout(
        xaxis_title="Words",
        yaxis_title="Count",
        title=f'<b style="font-size:16px;">{main_title}</b><br><span style="font-size:12px;">{subtitle}</span>',
        template="plotly_dark",
        font_family="Montserrat",
    )

    # Customize trace appearance
    figbar.update_traces(
        marker=dict(line=dict(color="#F2F2F2")),
        hovertemplate="Word: %{x}<br>Count: %{y}",
        name="",
    )

    # Display the bar chart
    figbar.show()

    # Add custom styles with Montserrat font to the HTML file
    styles = """
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Montserrat', sans-serif;
            }
        </style>
    """

    # Write the HTML file and add custom styles
    figbar.write_html(output_html_path)

    with open(output_html_path, "r", encoding="utf-8") as file:
        content = file.read()

    content = content.replace("</head>", styles + "</head>")

    with open(output_html_path, "w", encoding="utf-8") as file:
        file.write(content)


# -----------------------------------------------------------------------------------------#
# These functions can be used together to analyze and visualize word frequencies in a given text. Adjustments can be made to parameters such as font style, colors, and other visualization preferences as required.
# -----------------------------------------------------------------------------------------#
