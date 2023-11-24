import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
import requests


df_selic = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json')
data_extracao = date.today()
df_selic['data extracao'] = data_extracao
df_selic['responsavel'] = 'Autora'
df_selic['data'] =pd.to_datetime(df_selic['data'], dayfirst=True) #converte a coluna do tipo objeto e sobrescreve nela com a nova tipagem

df_selic['data extracao'] = pd.to_datetime(df_selic['data extracao'], dayfirst=True)
df_selic_ord =  df_selic.sort_values(by='data', ascending=False, inplace=True)
df_selic.reset_index(drop=True, inplace=True) #reseta o indice depois da ordenação

novo_index= (f'selic_{index}' for index in df_selic.index) #muda a nomenclatura do indice
df_selic.set_index(keys=[novo_index], inplace= True)
funcao_loc = df_selic.iloc[:4]


Teste = df_selic['data'] <= '2019-01-31'
Filtro = df_selic.loc[Teste]
print(Filtro)