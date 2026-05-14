import plotly.express as px


def circ_musica(df):

    total = df["track_popularity"].sum()

    top10 = (
        df.sort_values(
            by="track_popularity",
            ascending=False
        )[["track_name", "track_popularity"]]
        .drop_duplicates(subset="track_name")
        .head(10)
        .copy()
    )

    outros = total - top10["track_popularity"].sum()

    top10.loc[len(top10)] = ["Outros", outros]

    top10["percentual"] = (
        top10["track_popularity"] / total
    ) * 100

    fig = px.pie(
        top10,
        names="track_name",
        values="percentual",
        hole=0.45,
        title="Top 10 músicas mais populares"
    )

    fig.show()


def circ_artista(df):

    total = df["track_popularity"].sum()

    top10 = (
        df.groupby("track_artist")["track_popularity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    outros = total - top10["track_popularity"].sum()

    top10.loc[len(top10)] = ["Outros", outros]

    top10["percentual"] = (
        top10["track_popularity"] / total
    ) * 100

    fig = px.pie(
        top10,
        names="track_artist",
        values="percentual",
        hole=0.45,
        title="Top 10 artistas mais populares"
    )

    fig.show()


def circ_genero(df):

    total = df["track_popularity"].sum()

    top10 = (
        df.groupby("playlist_genre")["track_popularity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    outros = total - top10["track_popularity"].sum()

    top10.loc[len(top10)] = ["Outros", outros]

    top10["percentual"] = (
        top10["track_popularity"] / total
    ) * 100

    fig = px.pie(
        top10,
        names="playlist_genre",
        values="percentual",
        hole=0.45,
        title="Top gêneros mais populares"
    )

    fig.show()


def circ_album(df):

    total = df["track_popularity"].sum()

    top10 = (
        df.groupby("track_album_name")["track_popularity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    outros = total - top10["track_popularity"].sum()

    top10.loc[len(top10)] = ["Outros", outros]

    top10["percentual"] = (
        top10["track_popularity"] / total
    ) * 100

    fig = px.pie(
        top10,
        names="track_album_name",
        values="percentual",
        hole=0.45,
        title="Top álbuns mais populares"
    )

    fig.show()