# dashboard.py
# Geração de gráfico de barras a partir dos dados de vendas
# Desenvolvido por Barbara Carvalho

import pandas as pd
import matplotlib.pyplot as plt

ARQUIVO_DADOS = "vendas.csv"
ARQUIVO_GRAFICO = "dashboard_vendas.png"

def gerar_dashboard():
    try:
        df = pd.read_csv(ARQUIVO_DADOS)
    except FileNotFoundError:
        print(f"Erro: o arquivo '{ARQUIVO_DADOS}' não foi encontrado.")
        return

    df["Receita"] = df["Quantidade"] * df["Preco_Unitario"]
    receita_por_produto = df.groupby("Produto")["Receita"].sum().sort_values()

    plt.style.use("ggplot")
    fig, ax = plt.subplots(figsize=(10, 6))

    barras = ax.barh(receita_por_produto.index, receita_por_produto.values,
                     color="#6A9FB5", edgecolor="#2C3E50")

    for i, valor in enumerate(receita_por_produto.values):
        ax.text(valor + 5, i, f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                va="center", fontsize=9)

    ax.set_title("Receita Total por Produto", fontsize=14, pad=20)
    ax.set_xlabel("Receita (R$)", fontsize=11)
    ax.set_ylabel("Produto", fontsize=11)

    plt.tight_layout()
    plt.savefig(ARQUIVO_GRAFICO, dpi=150)
    print(f"Gráfico salvo como '{ARQUIVO_GRAFICO}'.")
    plt.show()

if __name__ == "__main__":
    gerar_dashboard()
    input("\nPressione Enter para sair...")
