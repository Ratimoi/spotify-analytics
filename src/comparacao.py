def comp_danca(df):

    comparacao = (
        df.sort_values(
            by="danceability",
            ascending=False
        )
        [["track_name", "track_artist", "danceability"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    print("=== MÚSICAS MAIS RITIMIZADAS ===\n")

    for i, row in comparacao.head(10).iterrows():

        print(
            f"{i+1:02d}. "
            f"{row['track_name']} - "
            f"{row['track_artist']} "
            f"({row['danceability']})"
        )

    print()


def comp_energia(df):

    comparacao = (
        df.sort_values(
            by="energy",
            ascending=False
        )
        [["track_name", "track_artist", "energy"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    print("=== MÚSICAS MAIS ENERGICAS ===\n")

    for i, row in comparacao.head(10).iterrows():

        print(
            f"{i+1:02d}. "
            f"{row['track_name']} - "
            f"{row['track_artist']} "
            f"({row['energy']})"
        )

    print()


def comp_fala(df):

    comparacao = (
        df.sort_values(
            by="speechiness",
            ascending=False
        )
        [["track_name", "track_artist", "speechiness"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    print("=== MÚSICAS MAIS CANTADAS ===\n")

    for i, row in comparacao.head(10).iterrows():

        print(
            f"{i+1:02d}. "
            f"{row['track_name']} - "
            f"{row['track_artist']} "
            f"({row['speechiness']})"
        )

    print()


def comp_acustico(df):

    comparacao = (
        df.sort_values(
            by="acousticness",
            ascending=False
        )
        [["track_name", "track_artist", "acousticness"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    print("=== MÚSICAS MAIS ACÚSTICAS ===\n")

    for i, row in comparacao.head(10).iterrows():

        print(
            f"{i+1:02d}. "
            f"{row['track_name']} - "
            f"{row['track_artist']} "
            f"({row['acousticness']})"
        )

    print()


def comp_instrumental(df):

    comparacao = (
        df.sort_values(
            by="instrumentalness",
            ascending=False
        )
        [["track_name", "track_artist", "instrumentalness"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    print("=== MÚSICAS MAIS INSTRUMENTAIS ===\n")

    for i, row in comparacao.head(10).iterrows():

        print(
            f"{i+1:02d}. "
            f"{row['track_name']} - "
            f"{row['track_artist']} "
            f"({row['instrumentalness']})"
        )

    print()


def comp_sentimental(df):

    comparacao = (
        df.sort_values(
            by="liveness",
            ascending=False
        )
        [["track_name", "track_artist", "liveness"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    print("=== MÚSICAS MAIS SENTIMENTAIS ===\n")

    for i, row in comparacao.head(10).iterrows():

        print(
            f"{i+1:02d}. "
            f"{row['track_name']} - "
            f"{row['track_artist']} "
            f"({row['liveness']})"
        )

    print()


def comp_tempo(df):

    comparacao = (
        df.sort_values(
            by="tempo",
            ascending=False
        )
        [["track_name", "track_artist", "tempo"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    print("=== MÚSICAS MAIS DURADOURAS ===\n")

    for i, row in comparacao.head(10).iterrows():

        print(
            f"{i+1:02d}. "
            f"{row['track_name']} - "
            f"{row['track_artist']} "
            f"({row['tempo']})"
        )

    print()