import pandas as pd
import plotly.express as px


def col_bpm(df):

    bins = range(0, 241, 10)

    df["faixa_bpm"] = pd.cut(
        df["tempo"],
        bins=bins
    )

    bpm = (
        df["faixa_bpm"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    bpm.columns = ["Faixa BPM", "Quantidade"]

    bpm["Faixa BPM"] = bpm["Faixa BPM"].astype(str)

    fig = px.bar(
        bpm,
        x="Faixa BPM",
        y="Quantidade",
        title="Distribuição de BPM das músicas",
        text_auto=True
    )

    fig.show()


def col_genero(df):

    genero = (
        df["playlist_genre"]
        .value_counts()
        .reset_index()
    )

    genero.columns = ["Gênero", "Quantidade"]

    fig = px.bar(
        genero,
        x="Gênero",
        y="Quantidade",
        title="Quantidade de músicas por gênero",
        text_auto=True
    )

    fig.show()