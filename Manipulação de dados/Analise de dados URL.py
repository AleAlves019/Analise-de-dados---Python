# Trabalhando com web Scraping 
# MANCHETE/ DESCRIÇÃO/ LINK / HORA_EXTRAÇÃO/ TIME_DELTA (TEMPO ATUAL - HORA DA EXTRAÇÃO)

''' As duas primeiras serão usadas para fazer a captura do 
conteúdo da página, pandas para entregar os resultados em forma estruturada 
e datetime para marcar o dia e hora da extração.
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime as dt


url = "https://globoesporte.globo.com/"

texto_string = requests.get(url).text #Convertendo a url em texto 
text_html = BeautifulSoup(texto_string, 'html.parser') #Converte o texto em HTML
lista_noticias = text_html.find_all("div",attrs={'class':'feed-post-body'}) #Vai localizar e retornar apenas as noticias

dados = []

for noticias in lista_noticias:
    titulo = noticias.contents[1].text.replace('"','')
    Descricao = noticias.contents[2].text
    link = noticias.find('a').get('href') # Ele busca o link da noticia 
    hora_extracao = dt.now().strftime("%d-%m-%Y %H:%M:%S") #Data atual da extração
    time_delta = noticias.find('span', attrs = {'class': 'feed-post-datetime'}).text
    
    dados.append((titulo, Descricao,link,hora_extracao,time_delta))

df = pd.DataFrame(dados, columns = ['Manchete','descrição', 'link', 'hora_extração', 'time_delta'])
print(df.head())






