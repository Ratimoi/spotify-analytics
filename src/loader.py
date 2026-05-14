import pandas as pd
from pathlib import Path


def carregar_dados():

    caminho = (
        Path(__file__)
        .resolve()
        .parent.parent
        / "data"
        / "spotify_songs.csv"
    )

    df = pd.read_csv(caminho)

    return df