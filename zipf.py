# Para o dataframe
import pandas as pd

# Para o gráfico
import matplotlib.pyplot as plt
import seaborn as sns

# Para stopwords
import nltk

# Para a imagem
from PIL import Image
import numpy as np

# Para a nuvem de palavras
from wordcloud import WordCloud

# Extraindo e limpando os dados

texto = []

txt = open('/content/Salmos.txt', 'r')
for linha in txt:
  texto.append(linha)

sinais = ['\n', '.', ',', '(', ')', '?', '!', '\'', '[', ']', ';', ':']

for i in range(len(texto)):
  for j in sinais:
    texto[i] = texto[i].lower() # Mantendo o texto em letra minúscula
    texto[i] = texto[i].replace(j,'') # Retirando todos os sinais
    texto[i] = ''.join([i for i in texto[i] if not i.isdigit()]) # Retirando os dígitos
   
nltk.download() # Realizando o download do pacote stopwords

texto2 = ''.join(texto).split() # Unindo as frases e separando por palavras

stopwordsnltk = nltk.corpus.stopwords.words('portuguese') # Extraindo as Stopwords do NLTK
texto3 = [palavra for palavra in texto2 if palavra not in stopwordsnltk] # Retirando as Stopwords

print(texto3)

# Construindo o Dicionário de Palavras

contaPalavra = {}

# Contando as palavras
for i in texto3:
  contaPalavra[i] = texto3.count(i)

print(contaPalavra)

# Visualização Gráfica

pd.set_option('display.max_rows', None) # Para visualizar todas as linhas do Dataframe
df = pd.DataFrame(list(contaPalavra.items()), columns=['Palavra', 'Quantidade']) # Criando um Dataframe
df = df.sort_values(by='Quantidade', ascending=False, ignore_index=True) # Ordenando de forma decrescente o Dataframe pela coluna Quantidade 
df = df[df['Quantidade']>26] # Filtrando a coluna Quantidade para valores maiores que 26
df.head()

sns.set_theme(style='darkgrid') # Definindo a cor de fundo
plt.figure(figsize=(24,10)) # Definindo o tamanho do Dataframe
sns.barplot(x='Palavra', y='Quantidade', data=df, palette='ch:s=.25,rot=-.25') # Definindo os dados dos eixos x e y e a cor das barras
plt.xticks(rotation=90) # Alterando a posição dos nomes no gráfico
plt.show() # Plotando o gráfico

cristo = np.array(Image.open("/content/Cristo-Redentor.jpg")) # Extraindo a imagem

# Gerando uma wordcloud
wordcloud = WordCloud(background_color='Black', 
                      width=1000, height=1000, 
                      max_words=2000, mask=cristo, 
                      max_font_size=200,min_font_size=1
                      ).generate_from_frequencies(contaPalavra)
plt.subplots(figsize=(10,10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.show()
