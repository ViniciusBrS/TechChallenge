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
          procuraram atendimento em um estabelecimento de saúde. Isso pode ter várias implicações, incluindo a possibilidade de subnotificação de casos de COVID-19.
  2. Em relação a trabalho, podemos perceber que houve uma adaptação para o modelo de trabalho remoto durante o lockdown para as pessoas funções que permitiam tal mudança, para funções que exigem o trabalho presencial, houveram afastamentos temporários de até 1 ano, durante a primeira grande onda de infecções.
  3. No âmbito financeiro, percebemos que o auxílio emergencial foi o rendimento mais presente nas famílias pesquisadas, para suportar a falta de rendimentos devido a estagnação econômica gerada pela pandemia.
  
  Link do [dashboard](https://lookerstudio.google.com/reporting/07d2431d-fd3f-4b9d-9d36-8e1c7940d239)
   
## Conclusão

  Com base na análise, sugere-se que pode haver uma subnotificação significativa de casos de COVID-19. Isso pode ser devido a vários fatores, incluindo a falta de acesso a serviços de saúde, medo de estigmatização, ou simplesmente a falta de consciência sobre a gravidade dos sintomas.

  Esta subnotificação pode ter várias implicações. Por um lado, pode levar a uma compreensão imprecisa da extensão e gravidade da pandemia. Por outro lado, pode resultar em pessoas infectadas não recebendo o tratamento de que necessitam, potencialmente levando a resultados de saúde piores.

  Portanto, é crucial que as autoridades de saúde e os formuladores de políticas levem em consideração essa possível subnotificação ao planejar e implementar respostas à pandemia. Isso pode incluir medidas para aumentar o acesso aos testes de COVID-19, campanhas de educação pública para aumentar a conscientização sobre os sintomas da COVID-19 e a importância de procurar atendimento médico, e esforços para reduzir o estigma associado à doença.
  
  Além disso, os hospitais e outros estabelecimentos de saúde devem estar preparados para um possível aumento na demanda por seus serviços se mais pessoas começarem a procurar atendimento para os sintomas de COVID-19. Isso pode exigir o aumento da capacidade de atendimento, a contratação de mais pessoal de saúde, ou a implementação de medidas para controlar a propagação do vírus dentro dos estabelecimentos de saúde.
