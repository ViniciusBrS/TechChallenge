# Tech Challenge Fase 3 - Pós Tech Data Analytics (2DTAT)

## Analise dos dados PNAD - Covid19

- Estudo nas pesquisas realizadas pelo IBGE via telefone, entre Maio/20 e Novembro/20 com o objetivo de coletar informações econômicas e sociais sobre o impacto da pandemia da Covid-19.
- Utilizamos os dados disponibilizados pelo datalake do portal [A Base dos dados](https://basedosdados.org/) via [BigQuery](https://basedosdados.org/dataset/c747a59f-b695-4d19-82e4-fef703e74c17?table=5894e1ac-dc08-465d-91a3-703683da85ba)
- Foi realizada a extração das tabelas: basedosdados.br_ibge_pnad_covid.dicionario e basedosdados.br_ibge_pnad_covid.microdados

## Tratamento das bases

  Para o ETL, seguimos em 3 passos:

- Fazer o download das bases do BigQuery para manipulação
- Realizar ajuste dos códigos que estão na tabela de microdados, com o dado correspondente contido no dicionário
- Incluir informações adicionais para enriquecimento da base

## Análise

    1. Pessoas que tiveram pelo menos 1 sintoma de COVID foram à algum estabelecimento de saúde?
        R.Através da nossa análise, percebemos que muitas pessoas que apresentaram pelo menos um sintoma de COVID-19 não 
          procuraram atendimento em um estabelecimento de saúde. Isso pode ter várias implicações, incluindo a possibilidade 
          de subnotificação de casos de COVID-19.
## Conclusão
