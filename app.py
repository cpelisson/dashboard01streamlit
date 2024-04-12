import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from graphics import grafico_map_estado, grafico_rec_mensal,grafico_rec_estado,grafico_rec_categoria, grafico_rec_vendedores, grafico_vendas_vendedores


#config da pagina
st.set_page_config(layout="wide")
st.title('Dashboard de Vendas')
#criar filtros side bar
st.sidebar.title('Filtro de Vendedores')
filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique(),
    
)
if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]
    #se o vendedor da coluna vendedor estiver no filtro vendedor vai mostar apenas esse vendedor

#criar aba
aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
#inserindo dados na aba
with aba1:
    st.dataframe(df)#aqui importou todos os dados do DF para a primeira aba (Dataset)
    
with aba2:
    coluna1, coluna2, = st.columns(2) #vai criar duas colunas na pagina
    with coluna1:
        #st.metric('Receita Total', df['Preço'].sum())# Aqui vai fazer uma métrica, onde vai somar toda a coluna de preço atraves do .sum para trazer a receita total.
        # Agora vem o codigo certo depois que fizemos a funcao de formatar o numero
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))
        st.plotly_chart(grafico_map_estado, use_container_width=True)# aqui chamou o grafico criado no graphics
        st.plotly_chart(grafico_rec_estado, use_container_width=True)
    with coluna2:
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))
        st.plotly_chart(grafico_rec_mensal, use_container_width=True) #aqui chamou o grafico criado no graphics
        st.plotly_chart(grafico_rec_categoria, use_container_width=True) #aqui chamou o grafico criado no graphics
        #PRESTE ATENCAO, o df shape serviu pra filtrar a tabela de baixo pra cima, isso fez com o que a tabela ficasse de ponta cabeça, assim trazendo o ultimo item e o seu ID, sabendo assim qual foi o ID da ultima venda e logicamente a quantidade de venda
        #aqui tambem usou a funcao format_number
    with aba3:
        coluna1, coluna2 = st.columns(2)
        with coluna1:
            st.plotly_chart(grafico_rec_vendedores, use_container_width=True)
        with coluna2 :   
            st.plotly_chart(grafico_vendas_vendedores, use_container_width=True)


