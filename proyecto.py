import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def sidebar_menu():
    st.sidebar.title("Huella ecológica per cápita departamental y por componentes - Ministerio del Ambiente")
    if st.sidebar.button('Página Principal'):
        st.session_state.page = "Página Principal"
    if st.sidebar.button('Página 2: Datos de Usuario'):
        st.session_state.page = "Página 2: Datos de Usuario"
    if st.sidebar.button('Página 3: Gráfico'):
        st.session_state.page = "Página 3: Gráfico"
    if st.sidebar.button('Página 4: Mapa'):
        st.session_state.page = "Página 4: Mapa"

if 'page' not in st.session_state:
    st.session_state.page = "Página Principal"

sidebar_menu()

if st.session_state.page == "Página Principal":
    st.image("logoproyecto.jpeg", use_column_width=True)
    st.title('Huella ecológica')
    st.write('BIENVENIDOS')
    st.write('La huella ecológica es un indicador del impacto ambiental generado por la demanda humana que se hace de los recursos existentes en los ecosistemas del planeta, relacionándola con la capacidad ecológica de la Tierra de regenerar sus recursos.')

elif st.session_state.page == "Página 3: Gráfico":
    option = st.selectbox('seleciona el año que quieres visualizar los datos',
                          ('2009', '2010', '2011','2012'))
    st.write('Seleccionó:', option)
    st.title('Gráfico de Huella Ecológica')
    excel_file='prueba.xlsx'
    sheet_name= option

    df=pd.read_excel(excel_file,
                     sheet_name=sheet_name,
                     usecols='A:H',
                     header=6)
    st.dataframe(df)
    df_filtred=df[df['Ámbito']!='Total']

    pie_chart=px.pie(df_filtred,
                     title='Porcentaje de Huella Regional Per capita',
                     values='Huella Regional Per Capita',
                     names='Ámbito')
    st.plotly_chart(pie_chart)
    


     
