"""
Trabalho 2 - Python e Pandas
Bootcamp Machine Learning - Avanti
"""

import pandas as pd
import numpy as np


# ---------------------------------------------------------------------------
# 1. Função que recebe uma lista de números e retorna outra lista
#    apenas com os números ímpares.
# ---------------------------------------------------------------------------
def filtrar_impares(numeros):
    """Retorna uma nova lista contendo apenas os números ímpares."""
    return [n for n in numeros if n % 2 != 0]


# ---------------------------------------------------------------------------
# 2. Função que recebe uma lista de números e retorna outra lista
#    com os números primos presentes.
# ---------------------------------------------------------------------------
def eh_primo(n):
    """Verifica se um número é primo."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def filtrar_primos(numeros):
    """Retorna uma nova lista contendo apenas os números primos."""
    return [n for n in numeros if eh_primo(n)]


# ---------------------------------------------------------------------------
# 3. Função que recebe duas listas e retorna outra lista com os elementos
#    que estão presentes em apenas uma das listas (diferença simétrica).
# ---------------------------------------------------------------------------
def elementos_unicos(lista1, lista2):
    """Retorna os elementos que aparecem em apenas uma das duas listas."""
    return list(set(lista1) ^ set(lista2))


# ---------------------------------------------------------------------------
# 4. Função para encontrar o segundo maior valor em uma lista de inteiros.
# ---------------------------------------------------------------------------
def segundo_maior(numeros):
    """Retorna o segundo maior valor distinto de uma lista de inteiros."""
    valores_unicos = list(set(numeros))
    if len(valores_unicos) < 2:
        raise ValueError("A lista precisa ter pelo menos 2 valores distintos.")
    valores_unicos.sort(reverse=True)
    return valores_unicos[1]


# ---------------------------------------------------------------------------
# 5. Função que recebe uma lista de tuplas (nome, idade) e retorna a lista
#    ordenada pelo nome em ordem alfabética.
# ---------------------------------------------------------------------------
def ordenar_por_nome(pessoas):
    """Ordena uma lista de tuplas (nome, idade) pelo nome, em ordem alfabética."""
    return sorted(pessoas, key=lambda pessoa: pessoa[0])


# ---------------------------------------------------------------------------
# 6. Como identificar e tratar outliers em uma coluna numérica usando
#    desvio padrão ou quartis?
# ---------------------------------------------------------------------------
"""
Existem duas abordagens comuns para identificar outliers:

a) Método do desvio padrão (Z-score):
   - Calcula-se a média e o desvio padrão da coluna.
   - Um valor é considerado outlier se estiver a mais de (geralmente) 2 ou 3
     desvios padrão de distância da média.
   - Fórmula do z-score: z = (x - média) / desvio_padrão

b) Método dos quartis (IQR - Intervalo Interquartil):
   - Calcula-se Q1 (25º percentil) e Q3 (75º percentil).
   - IQR = Q3 - Q1
   - Um valor é considerado outlier se estiver abaixo de (Q1 - 1.5 * IQR)
     ou acima de (Q3 + 1.5 * IQR).
   - É o método mais usado, pois é menos sensível a distribuições assimétricas.

Depois de identificados, os outliers podem ser tratados de várias formas:
removendo as linhas, substituindo pelos limites (capping/winsorização),
substituindo pela mediana, ou mantendo-os caso façam sentido para o problema
(ex: fraudes, que são "outliers" por natureza).
"""


def identificar_outliers_zscore(df, coluna, limite=3):
    """Identifica outliers em uma coluna usando o método do z-score (desvio padrão)."""
    media = df[coluna].mean()
    desvio = df[coluna].std()
    z_scores = (df[coluna] - media) / desvio
    return df[z_scores.abs() > limite]


def identificar_outliers_iqr(df, coluna):
    """Identifica outliers em uma coluna usando o método do IQR (quartis)."""
    q1 = df[coluna].quantile(0.25)
    q3 = df[coluna].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    return df[(df[coluna] < limite_inferior) | (df[coluna] > limite_superior)]


def tratar_outliers_iqr(df, coluna):
    """Remove os outliers de uma coluna usando o método do IQR."""
    q1 = df[coluna].quantile(0.25)
    q3 = df[coluna].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    return df[(df[coluna] >= limite_inferior) & (df[coluna] <= limite_superior)]


# ---------------------------------------------------------------------------
# 7. Como concatenar vários DataFrames (empilhando linhas ou colunas),
#    mesmo que tenham colunas diferentes?
# ---------------------------------------------------------------------------
"""
Utiliza-se pd.concat() especificando o parâmetro axis:

- axis=0 -> empilha as linhas (um DataFrame "embaixo" do outro).
  Se os DataFrames tiverem colunas diferentes, as colunas que não existem
  em um deles são preenchidas com NaN automaticamente.

- axis=1 -> empilha as colunas (um DataFrame "ao lado" do outro),
  alinhando pelos índices. Se os índices não baterem, também surgem NaN.

Exemplo:
    df_concatenado_linhas = pd.concat([df1, df2], axis=0, ignore_index=True)
    df_concatenado_colunas = pd.concat([df1, df2], axis=1)
"""


def concatenar_dataframes(lista_dfs, eixo=0):
    """Concatena uma lista de DataFrames empilhando linhas (axis=0) ou colunas (axis=1)."""
    return pd.concat(lista_dfs, axis=eixo, ignore_index=(eixo == 0))


# ---------------------------------------------------------------------------
# 8. Como ler um arquivo CSV em um DataFrame e exibir as primeiras linhas?
# ---------------------------------------------------------------------------
def ler_csv_e_mostrar_head(caminho_arquivo, n_linhas=5):
    """Lê um arquivo CSV e exibe as primeiras n linhas do DataFrame."""
    df = pd.read_csv(caminho_arquivo)
    print(df.head(n_linhas))
    return df


# ---------------------------------------------------------------------------
# 9. Como selecionar uma coluna específica e filtrar linhas em um DataFrame
#    com base em uma condição?
# ---------------------------------------------------------------------------
def selecionar_coluna(df, nome_coluna):
    """Seleciona uma única coluna do DataFrame (retorna uma Series)."""
    return df[nome_coluna]


def filtrar_linhas(df, coluna, valor_minimo):
    """Filtra as linhas do DataFrame em que a coluna é maior que um valor mínimo."""
    return df[df[coluna] > valor_minimo]


# Exemplo de uso combinado (seleção de coluna + filtro):
# idades_maiores_18 = df.loc[df["idade"] > 18, "idade"]


# ---------------------------------------------------------------------------
# 10. Como lidar com valores ausentes (NaN) em um DataFrame?
# ---------------------------------------------------------------------------
"""
Principais formas de lidar com valores ausentes usando pandas:

- Verificar onde estão os valores ausentes:
    df.isnull().sum()

- Remover linhas ou colunas com valores ausentes:
    df.dropna(axis=0)   # remove linhas com qualquer NaN
    df.dropna(axis=1)   # remove colunas com qualquer NaN

- Preencher valores ausentes (imputação):
    df.fillna(0)                        # preenche com um valor fixo
    df.fillna(df.mean(numeric_only=True))  # preenche com a média da coluna
    df.fillna(method="ffill")           # preenche com o valor anterior
    df.fillna(method="bfill")           # preenche com o valor seguinte

- Interpolar valores (útil em séries temporais):
    df.interpolate()
"""


def tratar_valores_ausentes(df, estrategia="media"):
    """
    Trata valores ausentes em um DataFrame numérico.

    estrategia pode ser:
        'remover' -> remove linhas com valores ausentes
        'media'   -> preenche com a média de cada coluna numérica
        'mediana' -> preenche com a mediana de cada coluna numérica
        'zero'    -> preenche com 0
    """
    if estrategia == "remover":
        return df.dropna()
    elif estrategia == "media":
        return df.fillna(df.mean(numeric_only=True))
    elif estrategia == "mediana":
        return df.fillna(df.median(numeric_only=True))
    elif estrategia == "zero":
        return df.fillna(0)
    else:
        raise ValueError("Estratégia inválida. Use: remover, media, mediana ou zero.")


# ---------------------------------------------------------------------------
# Exemplos rápidos de teste (executados apenas se o arquivo for rodado
# diretamente, não quando for importado como módulo).
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17]

    print("Ímpares:", filtrar_impares(numeros))
    print("Primos:", filtrar_primos(numeros))

    lista_a = [1, 2, 3, 4, 5]
    lista_b = [4, 5, 6, 7]
    print("Elementos únicos:", elementos_unicos(lista_a, lista_b))

    print("Segundo maior:", segundo_maior([10, 4, 7, 22, 22, 3]))

    pessoas = [("Carlos", 30), ("Ana", 25), ("Bruno", 40)]
    print("Ordenado por nome:", ordenar_por_nome(pessoas))

    df_exemplo = pd.DataFrame({
        "valor": [10, 12, 11, 13, 500, 9, 10, 12, -300, 11]
    })
    print("Outliers (IQR):")
    print(identificar_outliers_iqr(df_exemplo, "valor"))