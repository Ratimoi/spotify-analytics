import pandas as pd


def carregar_dados():

    df = pd.read_csv("../data/spotify_songs.csv")

    return df