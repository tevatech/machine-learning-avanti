# Trabalho 01 - Fundamentos de Machine Learning

**Aluno:** Caren Teva das Neves
**Data:** 08/07/2026  

---

## 1. Explique, com suas palavras, o que é machine learning?

Machine learning é basicamente ensinar o computador a aprender sozinho, sem ter que programar todas as regras manualmente. Em vez de ficar escrevendo "se isso acontecer, faça aquilo" para cada situação possível, você mostra um monte de exemplos para o computador e deixa ele descobrir os padrões por conta própria, exatamente como a gente aprende na vida real. Por exemplo, ao invés de você programar regras do tipo "se o email tem a palavra oferta ou grátis, então é spam", você simplesmente mostra 10 mil emails que já estão classificados como spam ou não, e o computador vai analisando esses exemplos até aprender sozinho quais características indicam que um email é spam. O legal é que quanto mais exemplos você mostra, melhor ele fica, porque ele vai refinando o entendimento dele com cada novo dado que recebe. No dia a dia, a gente usa machine learning sem nem perceber: é o que faz a Netflix recomendar filmes que você provavelmente vai gostar, o Instagram mostrar posts que te interessam, o Google Maps prever quanto tempo você vai levar no trânsito e até o seu email separar automaticamente as mensagens importantes das propagandas. No fundo, machine learning se resume a uma coisa bem simples: você alimenta o computador com dados, ele encontra os padrões escondidos nesses dados e usa esses padrões para fazer previsões ou tomar decisões sozinho, sem precisar de instruções explícitas para cada nova situação que aparece.

---

## 2. Explique o conceito de conjunto de treinamento, conjunto de validação e conjunto de teste em machine learning.

Quando a gente vai ensinar um modelo de machine learning, a gente não pode simplesmente jogar todos os dados que tem e esperar que ele aprenda direitinho, a gente precisa dividir esses dados em três grupos que têm funções bem diferentes. O primeiro é o conjunto de treinamento, que é a maior parte dos dados e é onde o modelo realmente aprende, tipo quando você estuda a matéria fazendo exercícios, ele fica ali olhando os exemplos, ajustando os parâmetros dele e tentando entender os padrões. Depois tem o conjunto de validação, que serve como um simulado, a gente usa ele durante o desenvolvimento para ir testando o modelo e ajustando as configurações, tipo a taxa de aprendizado ou o número de camadas, pra garantir que ele não está só decorando os dados de treinamento mas tá realmente aprendendo padrões que funcionam pra qualquer situação. E por último, o mais importante, é o conjunto de teste, que é a prova final, aquele grupo de dados que o modelo nunca viu antes e que a gente só usa no final para avaliar se ele realmente aprendeu ou se só decorou os exemplos, porque se ele for bem nesses dados novos significa que ele consegue generalizar e fazer previsões boas no mundo real, mas se ele for mal é sinal de que ele decorou os dados de treinamento mas não entendeu o conceito, o que a gente chama de overfitting.

---

## 3. Explique como você lidaria com dados ausentes em um conjunto de dados de treinamento.

Quando encontro dados faltando em um conjunto de dados, primeiro avalio a gravidade: se uma coluna tem muitos dados vazios, eu descarto ela, mas se são poucos, parto pra outras estratégias. A mais comum é preencher esses espaços com algum valor, como a média ou mediana para números ou a moda para categorias, mas também posso usar técnicas mais avançadas onde outras colunas ajudam a estimar o valor que falta, como a regressão ou o KNN, que olha exemplos parecidos pra fazer essa estimativa. Às vezes, o fato do dado estar faltando já é uma informação relevante, então crio uma coluna extra indicando que aquele campo estava vazio. O cuidado mais importante é nunca fazer esse preenchimento antes de dividir os dados em treino e teste, porque isso vaza informações e engana a avaliação do modelo, então sempre trato os dados faltantes primeiro no treino e aplico a mesma regra no teste depois.

---

## 4. O que é uma matriz de confusão e como ela é usada para avaliar o desempenho de um modelo preditivo?

A matriz de confusão é uma tabelinha que compara as previsões do modelo com os valores reais, mostrando quatro tipos de resultado: acertos e erros para cada classe, como verdadeiros positivos, verdadeiros negativos, falsos positivos e falsos negativos. A partir dela a gente calcula métricas como precisão, recall e F1-score, que contam histórias diferentes sobre o desempenho do modelo, porque a acurácia sozinha pode enganar, principalmente quando os dados são desbalanceados. Dependendo do problema, a gente prioriza uma métrica diferente, por exemplo, na saúde a gente quer um recall alto pra não deixar nenhum doente passar, mesmo que isso gere alguns falsos alarmes, já em sistemas de spam a gente prefere uma precisão alta pra não classificar emails importantes como lixo.

---

## 5. Áreas interessantes para aplicação de machine learning

Algumas áreas em que considero especialmente interessante aplicar machine learning:

- **Saúde:** apoio ao diagnóstico médico (análise de imagens, exames), previsão de risco de doenças, otimização de tratamentos personalizados.
- **Agricultura:** previsão de safras, detecção de pragas e doenças em plantações por imagem, otimização do uso de água e insumos.
- **Construção civil:** previsão de custos e prazos de obras, manutenção preditiva de equipamentos, otimização logística de materiais.
- **Manufatura:** manutenção preditiva de máquinas (evitando paradas inesperadas), controle de qualidade automatizado via visão computacional.

Dentre essas, a área de **saúde** me parece a mais interessante, pelo impacto direto que pode ter na qualidade de vida das pessoas desde diagnósticos mais rápidos e precisos até a personalização de tratamentos, embora também seja uma das áreas que exige mais cuidado ético e responsabilidade no uso dos dados.
