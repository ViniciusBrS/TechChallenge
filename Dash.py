import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import pandas_gbq

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    # query_job = client.query(query)
    # rows_raw = query_job.result()
    # # Convert to list of dicts. Required for st.cache_data to hash the return value.
    # rows = [dict(row) for row in rows_raw]
    # return rows

    df = pandas_gbq.read_gbq(query, project_id="postech-414800", credentials=credentials)
    return df

v_qry = """
SELECT  x1.ANO,  x1.MES,  COUNT(*) qtd_populacao_entrevistada,  SUM( IF   (CAST(x1.B002 AS int64) = 1, 1, 0)) qtd_populacao_internada,
SUM( IF (CAST(x1.B002 AS int64) = 2, 1, 0)) qtd_populacao_nao_internada,
ROUND( (SUM(  IF  (CAST(x1.B002 AS int64) = 1, 1, 0)) / COUNT(*))*100,2) perc_populacao_internada
FROM `basedosdados.br_ibge_pnad_covid.microdados` x1
WHERE ( CAST(x1.B0011 AS int64) = 1 OR CAST(x1.B0012 AS int64) = 1 OR CAST(x1.B0013 AS int64) = 1 OR CAST(x1.B0014 AS int64) = 1 OR CAST(x1.B0015 AS int64) = 1
OR CAST(x1.B0016 AS int64) = 1 OR CAST(x1.B0017 AS int64) = 1 OR CAST(x1.B0018 AS int64) = 1 OR CAST(x1.B0019 AS int64) = 1 OR CAST(x1.B00110 AS int64) = 1
OR CAST(x1.B00111 AS int64) = 1 OR CAST(x1.B00112 AS int64) = 1 OR CAST(x1.B00113 AS int64) = 1 )
GROUP BY x1.ANO, x1.MES
ORDER BY  1, 2
"""

dados = run_query(v_qry)




# Print results.
st.write("Tabela de dados:")
st.write(dados)