"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    os.makedirs("files/plots", exist_ok=True)

    df = pd.read_csv("files/input/news.csv", index_col=0)

    plt.figure()

    colors = {
        "Television": "dimgray",
        "Newspaper": "gray",
        "Internet": "blue",
        "Radio": "lightgray",
    }

    zorder = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }

    linewidths = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 4,
        "Radio": 2,
    }

    for col in df.columns:
        plt.plot(
            df[col],
            color=colors[col],
            label=col,
            zorder=zorder[col],
            linewidth=linewidths[col],
        )

    plt.title("how people get their news", fontsize=16)

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        first_year = df.index[0]

        plt.scatter(
            x=first_year,
            y=df.loc[first_year, col],
            color=colors[col],
            zorder=zorder[col],
        )

        plt.text(
            x=first_year - 0.2,
            y=df.loc[first_year, col],
            s=col + " " + str(df.loc[first_year, col]) + "%",
            ha="right",
            va="center",
            color=colors[col],
        )

        last_year = df.index[-1]

        plt.scatter(
            x=last_year,
            y=df.loc[last_year, col],
            color=colors[col],
            zorder=zorder[col],
        )

        plt.text(
            x=last_year + 0.2,
            y=df.loc[last_year, col],
            s=str(df.loc[last_year, col]) + "%",
            ha="left",
            va="center",
            color=colors[col],
        )

    plt.tight_layout()
    plt.savefig("files/plots/news.png")
    plt.close()
"""
Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
generar el archivo `files/plots/news.png`.

Un ejemplo de la grafica final esta ubicado en la raíz de
este repo.

El gráfico debe salvarse al archivo `files/plots/news.png`.

"""
