# Spotify Analytics

Sistema desenvolvido em Python para análise e visualização de dados musicais utilizando um dataset do Spotify.

O projeto permite explorar informações sobre músicas, artistas, gêneros e álbuns através de rankings, comparações estatísticas e gráficos interativos.

---

# Tecnologias utilizadas

* Python
* Pandas
* Plotly

---

# Estrutura do projeto

```text
spotify-analytics/
│
├── data/
│   └── spotify_songs.csv
│
├── docs/
│   └── dataset_readme.md
│
├── src/
│   ├── main.py
│   ├── loader.py
│   ├── menus.py
│   ├── utils.py
│   ├── rankings.py
│   ├── comparacao.py
│   ├── circulares.py
│   └── colunas.py
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

# Funcionalidades

## Rankings

* Músicas mais ouvidas
* Artistas mais ouvidos
* Gêneros mais ouvidos
* Álbuns mais ouvidos

## Comparações musicais

* Danceability
* Energy
* Speechiness
* Acousticness
* Instrumentalness
* Liveness
* Tempo

## Gráficos

### Circulares

* Músicas
* Artistas
* Gêneros
* Álbuns

### Colunas

* Distribuição de BPM
* Quantidade de músicas por gênero

---

# Instalação

Clone o repositório:

```bash
git clone https://github.com/Ratimoi/spotify-analytics.git
```

Entre na pasta:

```bash
cd spotify-analytics
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# Executar o projeto

```bash
python src/main.py
```

---

# Objetivo do projeto

Aplicar conceitos de:

* análise de dados
* visualização de dados
* manipulação de datasets
* modularização em Python
* organização de projetos
* gráficos interativos

---

# Licença

Este projeto está sob a licença MIT.
