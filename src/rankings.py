def rank_musicas(df):

    ranking = (
        df.sort_values(
            by="track_popularity",
            ascending=False
        )
        [["track_name", "track_artist", "track_popularity"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    print("=== MÚSICAS MAIS OUVIDAS ===\n")

    for i, row in ranking.head(10).iterrows():

        print(
            f"{i+1:02d}. "
            f"{row['track_name']} - "
            f"{row['track_artist']} "
            f"({row['track_popularity']})"
        )

    print()


def rank_artistas(df):

    ranking = (
        df.groupby("track_artist")["track_popularity"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    print("=== ARTISTAS MAIS OUVIDOS ===\n")

    for i, row in ranking.head(10).iterrows():

        print(
            f"{i+1:02d}. "
            f"{row['track_artist']} - "
            f"({row['track_popularity']:.2f})"
        )

    print()


def rank_genero(df):

    ranking = (
        df.groupby("playlist_genre")["track_popularity"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    print("=== GÊNEROS MAIS OUVIDOS ===\n")

    for i, row in ranking.head(10).iterrows():

        print(
            f"{i+1:02d}. "
            f"{row['playlist_genre']} - "
            f"({row['track_popularity']:.2f})"
        )

    print()


def rank_album(df):

    ranking = (
        df.groupby("track_album_name")
        .agg({
            "track_popularity": "mean",
            "track_artist": "first"
        })
        .sort_values(by="track_popularity", ascending=False)
        .reset_index()
    )

    print("=== ÁLBUNS MAIS OUVIDOS ===\n")

    for i, row in ranking.head(10).iterrows():

        print(
            f"{i+1:02d}. "
            f"{row['track_album_name']} - "
            f"{row['track_artist']} - "
            f"({row['track_popularity']:.2f})"
        )

    print()