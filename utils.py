from dataset import df
import pandas as pd
import streamlit as st
import time
#Essa funcao é pra formatar os numeros para melhor vizualização
def format_number(value, prefix = ''):
    for unit in ['','mil']:
        if value <1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'

#Receita por Estado
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum() # esse comando vai agrupar o local da compra e o somatorio de cada local de compra, assim vamos saber qual local que vendeu mais
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)
# Aqui nós vamos tirar as duplicidade do local de compra, latitude e longitude, vamos fazer um merge com os dados que ja tinhamos no df_rec_estado(fd, receita por estado), a esquerda trouxe o local da compra e fez um sort (organizacao) de cima pra baixo (ascemding false) do total de vendas em cada local  

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].sum().reset_index()

# Adiciona colunas de Ano e Mês
df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
df_rec_mensal['Mês'] = df_rec_mensal['Data da Compra'].dt.month_name()

# Mostra o DataFrame com a receita mensal, o ano e o mês

df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)

#dataframes vendedores
df_vendedores = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))
# Aqui fez a junção de Vendedor e preco e agrupou em cada um, depois juntou nesse DF a soma dos precos e um contador pra saber quantas vendas fez
# Função para converter arquivo csv
@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def mensagem_sucesso():
    success = st.success(
        'Arquivo baixado com sucesso',
        icon="✅"
        )
    time.sleep(3)
    success.empty()