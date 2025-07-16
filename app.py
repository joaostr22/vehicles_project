import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')

st.header('Análise de venda de carros')

hist_button = st.checkbox('Criar histograma')

scatter_button = st.checkbox('Criar gráfico de dispersão')

if hist_button:
    st.write('Criando um histograma para analisar o ano do modelo por condição')

    fig = px.histogram(
    car_data,
    x='model_year',
    color='condition',
    barmode='stack',
    title='Distribuição de condição dos veículos por ano do modelo'
    )

    fig.update_layout(
    xaxis_title='Ano do Modelo',
    yaxis_title='Quantidade de Veículos',
    legend_title='Condição'
    )

    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write('Criando um gráfico de dispersão para analisar como o preço de um veículo varia com a quilometragem (odômetro) e o tipo de câmbio.')

    fig2 = px.scatter(
        car_data,
        x='odometer',
        y='price',
        color='transmission',
        title='Preço VS quilometragem por tipo de câmbio'
    )

    fig2.update_layout(
        xaxis_title='Quilometragem',
        yaxis_title='Preço',
        legend_title='Tipo de câmbio'
    )

    st.plotly_chart(fig2, use_container_width=True)
