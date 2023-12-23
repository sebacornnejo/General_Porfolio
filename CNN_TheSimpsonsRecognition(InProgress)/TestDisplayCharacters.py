import warnings
warnings.simplefilter("ignore")
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
# import matplotlib.pyplot as plt
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objs as go
from keras.preprocessing.image import load_img


# Specify the paths to the training and validation data directories
train_data_dir = "TheSimpsonsDataset/train/"
val_data_dir = "TheSimpsonsDataset/validation/"

# Create a list to store the names of characters
name_character = []
for character in os.listdir(train_data_dir):
    data = [character]
    name_character.append(data)

# Crear una lista de diccionarios para almacenar la información de las imágenes
image_data = []

characters = os.listdir(train_data_dir)

for character in characters:
    image_dir = train_data_dir + character + "/" + os.listdir(train_data_dir + character)[0]
    image_data.append({"Character": character, "Image Path": image_dir})

# Crear subtramas con Plotly
columns = 5
rows = len(characters) // columns + 1

fig = sp.make_subplots(rows=rows, cols=columns,
                       vertical_spacing=0,)
    

for i, data in enumerate(image_data):
    character = data["Character"]
    image_dir = data["Image Path"]
    image = load_img(image_dir, target_size=(244, 244))
    image_trace = go.Image(z=image,hovertemplate=f'<extra></extra><b style="font-size:14px;">Name:</b> <span style="font-size:20px;">{character}</span><br>', hoverlabel=dict(bgcolor="#262626"))
    row = i // columns + 1
    col = i % columns + 1
    image_index = f'({i + 1})'
    fig.update_layout(height=row * 250, width=col * 250,)
    fig.add_trace(image_trace, row=row, col=col,)
    if col == 1:
        x = (col - 1) / columns + 0.42 / columns
    elif col == columns:
        x = (col - 1) / columns + 0.57 / columns
    else:
        x = (col - 1) / columns + 0.5 / columns
    fig.add_annotation(
        go.layout.Annotation(
            text=image_index,
            xref="paper", yref="paper",
            x=x,
            y=1 - (row - 1) / rows - 0.08 / rows,
            xanchor="center", yanchor="top",
            showarrow=False,
            font=dict(size=18),
        )
    )

fig.update_layout(title_text='<b style="font-size:24px;">The Simpsons Characters</b><br><span style="font-size:12px;">for the Recognition Model</span>', 
                  title_x=0.5, 
                  font=dict(family='Montserrat', 
                            color='#F2F2F2'),
                  template='plotly_dark')
fig.update_xaxes(showticklabels=False)
fig.update_yaxes(showticklabels=False)
fig.show()