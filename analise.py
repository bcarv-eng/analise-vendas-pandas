# analise.py
# Análise exploratória de dados de vendas utilizando Pandas
# Desenvolvido por Barbara Carvalho

import pandas as pd

ARQUIVO_DADOS = "vendas.csv"

def executar_analise():
    try:
        df = pd.read_csv(ARQUIVO_DADOS)
    except FileNotFoundError:
        print(f"Erro: o arquivo '{ARQUIVO_DADOS}' não foi encontrado.")
        return

    df["Receita"] = df["Quantidade"] * df["Preco_Unitario"]

    receita_total = df["Receita"].sum()
    produto_mais_vendido = df.groupby("Produto")["Quantidade"].sum().idxmax()
    produto_maior_receita = df.groupby("Produto")["Receita"].sum().idxmax()

    print("=" * 50)
    print("RELATÓRIO GERENCIAL DE VENDAS".center(50))
    print("=" * 50)
    print(f"Receita total: R$ {receita_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print(f"Produto com maior volume de vendas: {produto_mais_vendido}")
    print(f"Produto com maior receita: {produto_maior_receita}")
    print("=" * 50)

    print("\nResumo por produto:")
    resumo = df.groupby("Produto").agg({"Quantidade": "sum", "Receita": "sum"}).round(2)
    print(resumo)

if __name__ == "__main__":
    executar_analise()
    input("\nPressione Enter para encerrar...")
