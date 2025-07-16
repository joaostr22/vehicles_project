import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv') # lendo os dados

st.header('Título provisório')

hist_button = st.button('Criar histograma') # criar um botão

scatter_button = st.button('Criar gráfico de dispersão')

if hist_button: # se o botão for clicado       
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write('Criando um gráfico de dispersão')

    fig2 = px.scatter(car_data, x='odometer', y='price')

    st.plotly_chart(fig2, use_container_width=True)
