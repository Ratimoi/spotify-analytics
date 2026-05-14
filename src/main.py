from menus import (
    menu_principal,
    menu_pesquisas,
    menu_rankings,
    menu_comparacoes,
    menu_graficos,
    menu_circular,
    menu_colunas
)

from rankings import (
    rank_musicas,
    rank_artistas,
    rank_genero,
    rank_album
)

from comparacao import (
    comp_danca,
    comp_energia,
    comp_fala,
    comp_acustico,
    comp_instrumental,
    comp_sentimental,
    comp_tempo
)

from circulares import (
    circ_musica,
    circ_artista,
    circ_genero,
    circ_album
)

from colunas import (
    col_bpm,
    col_genero
)

from utils import limpar_console

from loader import carregar_dados

# ------------------
# Carregamento do CSV
# ------------------

df = carregar_dados()


# ---------------
# Fluxo principal
# ---------------

limpar_console()

while True:

    menu_principal()

    choice = input("\nOpção: ")

    match choice:

        # ----------------
        # Menu Pesquisas
        # ----------------

        case "1":

            limpar_console()

            while True:

                menu_pesquisas()

                choice = input("\nOpção: ")

                match choice:

                    # ----------
                    # Rankings
                    # ----------

                    case "1":

                        limpar_console()

                        while True:

                            menu_rankings()

                            choice = input("\nOpção: ")

                            match choice:

                                case "1":
                                    limpar_console()
                                    rank_musicas(df)

                                case "2":
                                    limpar_console()
                                    rank_artistas(df)

                                case "3":
                                    limpar_console()
                                    rank_genero(df)

                                case "4":
                                    limpar_console()
                                    rank_album(df)

                                case "9":
                                    limpar_console()
                                    break

                                case _:
                                    limpar_console()
                                    print("Opção inválida...\n")

                    # -------------
                    # Comparações
                    # -------------

                    case "2":

                        limpar_console()

                        while True:

                            menu_comparacoes()

                            choice = input("\nOpção: ")

                            match choice:

                                case "1":
                                    limpar_console()
                                    comp_danca(df)

                                case "2":
                                    limpar_console()
                                    comp_energia(df)

                                case "3":
                                    limpar_console()
                                    comp_fala(df)

                                case "4":
                                    limpar_console()
                                    comp_acustico(df)

                                case "5":
                                    limpar_console()
                                    comp_instrumental(df)

                                case "6":
                                    limpar_console()
                                    comp_sentimental(df)

                                case "7":
                                    limpar_console()
                                    comp_tempo(df)

                                case "9":
                                    limpar_console()
                                    break

                                case _:
                                    limpar_console()
                                    print("Opção inválida...\n")

                    case "9":
                        limpar_console()
                        break

                    case _:
                        limpar_console()
                        print("Opção inválida...\n")

        # ---------------
        # Menu Gráficos
        # ---------------

        case "2":

            limpar_console()

            while True:

                menu_graficos()

                choice = input("\nOpção: ")

                match choice:

                    # -------------------
                    # Gráficos circulares
                    # -------------------

                    case "1":

                        limpar_console()

                        while True:

                            menu_circular()

                            choice = input("\nOpção: ")

                            match choice:

                                case "1":
                                    limpar_console()
                                    circ_musica(df)

                                case "2":
                                    limpar_console()
                                    circ_artista(df)

                                case "3":
                                    limpar_console()
                                    circ_genero(df)

                                case "4":
                                    limpar_console()
                                    circ_album(df)

                                case "9":
                                    limpar_console()
                                    break

                                case _:
                                    limpar_console()
                                    print("Opção inválida...\n")

                    # ----------------
                    # Gráficos coluna
                    # ----------------

                    case "2":

                        limpar_console()

                        while True:

                            menu_colunas()

                            choice = input("\nOpção: ")

                            match choice:

                                case "1":
                                    limpar_console()
                                    col_bpm(df)

                                case "2":
                                    limpar_console()
                                    col_genero(df)

                                case "9":
                                    limpar_console()
                                    break

                                case _:
                                    limpar_console()
                                    print("Opção inválida...\n")

                    case "9":
                        limpar_console()
                        break

                    case _:
                        limpar_console()
                        print("Opção inválida...\n")

        # -----
        # Sair
        # -----

        case "9":
            limpar_console()
            break

        case _:
            limpar_console()
            print("Opção inválida...\n")