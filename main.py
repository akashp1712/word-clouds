# Start with loading all necessary libraries
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

def transform_format(val):
    if val == 0:
        return 255
    else:
        return val

def show_word_cloud():
    # Start with one review:
    text = "Hello World, I'm Akash Panchal 👋A passionate Software Engineer with experience of building Microservices based applications with Python, JavaScript and some other cool projects for Mobile, Machine Learning and NLP." \
           "Hello World, I'm Akash Panchal 👋A passionate Software Engineer with experience of building Microservices based applications with Python, JavaScript and some other cool projects for Mobile, Machine Learning and NLP."

    # Generate a word cloud image
    mask = np.array(Image.open("akash.jpg"))
    wordcloud_usa = WordCloud(stopwords=set(), background_color="white", mode="RGBA", max_words=2000,
                              mask=mask).generate(text)

    # create coloring from image
    image_colors = ImageColorGenerator(mask)
    plt.figure(figsize=[10, 10])
    plt.imshow(wordcloud_usa.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")

    # store to file
    plt.savefig("akash_wc.png", format="png")

    plt.show()


if __name__ == '__main__':
    show_word_cloud()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
