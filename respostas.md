# Trabalho 01 - Fundamentos de Machine Learning

**Aluno:** Caren Teva das Neves
**Data:** 08/07/2026  

---

## 1. Explique, com suas palavras, o que é machine learning?

Machine Learning (Aprendizado de Máquina) é uma área da Inteligência Artificial que permite que computadores aprendam padrões a partir de dados sem serem explicitamente programados para cada tarefa. Em vez de seguir regras fixas definidas por humanos, o sistema identifica relações nos dados e faz previsões ou toma decisões baseadas nesse aprendizado.

**Exemplo prático:** Ao invés de programar manualmente regras para identificar spam ("se tem palavra X ou Y, é spam"), um modelo de ML analisa milhares de e-mails já classificados e aprende sozinho quais padrões indicam spam.

**Principais tipos:**
- **Supervisionado:** Aprende com dados rotulados (ex: prever preços de casas)
- **Não-supervisionado:** Encontra padrões em dados sem rótulos (ex: segmentar clientes)
- **Por reforço:** Aprende por tentativa e erro com recompensas (ex: jogos)

---

## 2. Explique o conceito de conjunto de treinamento, conjunto de validação e conjunto de teste em machine learning.

São divisões do conjunto total de dados usados em diferentes fases do desenvolvimento do modelo:

### Conjunto de Treinamento (Training Set)
- **Tamanho típico:** 60-80% dos dados
- **Função:** O modelo aprende os padrões a partir desses dados. É aqui que os pesos e parâmetros são ajustados.
- **Analogia:** É como os "exercícios" que um aluno faz para aprender a matéria.

### Conjunto de Validação (Validation Set)
- **Tamanho típico:** 10-20% dos dados
- **Função:** Usado para ajustar os hiperparâmetros do modelo (taxa de aprendizado, número de camadas, etc.) e evitar overfitting. Não é usado para treinar, apenas para avaliar durante o desenvolvimento.
- **Analogia:** É como as "provas simuladas" que ajudam o aluno a saber se está pronto.

### Conjunto de Teste (Test Set)
- **Tamanho típico:** 10-20% dos dados
- **Função:** Avalia o desempenho final do modelo em dados nunca vistos antes. É a "prova final" que mede a real capacidade de generalização.
- **Analogia:** É como a "prova oficial" - o aluno nunca viu as questões antes.

**Observação importante:** O modelo NUNCA deve ver os dados de teste durante o treinamento, para não contaminar a avaliação.

---

## 3. Explique como você lidaria com dados ausentes em um conjunto de dados de treinamento.

Dados ausentes são comuns em problemas reais e precisam ser tratados. Minha abordagem seria:

### 1. Análise Exploratória
Primeiro, entenderia:
- **Quantos dados estão faltando?**
- **O padrão é aleatório (MCAR) ou sistemático (MAR/NMAR)?**
- **Qual coluna tem mais dados faltantes?**

### 2. Estratégias de Tratamento

| Estratégia | Quando usar | Como fazer |
|------------|-------------|------------|
| **Remoção** | Poucos dados faltantes (<5%) | Remover linhas com NA ou colunas com >50% NA |
| **Imputação com Média/Mediana** | Dados numéricos, distribuição normal | Substituir NA pela média ou mediana da coluna |
| **Imputação com Moda** | Dados categóricos | Substituir pela categoria mais frequente |
| **Imputação por Regressão** | Dados com correlações fortes | Usar outras features para prever o valor faltante |
| **KNN Imputation** | Dados com padrões similares | Usar os K vizinhos mais próximos para estimar |
| **Criação de Indicador** | Quando o fato de faltar é relevante | Criar coluna binária indicando se faltava |

### 📊 Exemplo prático em Python:

```python
# Usando pandas
import pandas as pd
from sklearn.impute import SimpleImputer

# Remoção simples
df_clean = df.dropna()

# Imputação com média
imputer = SimpleImputer(strategy='mean')
df['idade'] = imputer.fit_transform(df[['idade']])

# Imputação com mediana (mais robusta para outliers)
imputer = SimpleImputer(strategy='median')
