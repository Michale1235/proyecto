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
    st.write('Se busca realizar un análisis exploratorio de los datos de la huella ecológica per cápita departamental y por componentes, organizándolos para su mejor lectura. Estos datos, que abarcan el período de 2009 a 2016, fueron extraídos de la plataforma del Ministerio del Ambiente.')

#pagina 1



#pagina 2



#pagina 3
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

###pagina 4
    
elif st.session_state.page=="Página 4: Mapa":
    st.image("huella ecologica.jpg", use_column_width=True)
    st.title('Conclusiones')
    st.write('Puntos principales')
    st.write('Con base en los datos presentados en las gráficas, se concluye que la región de Lima muestra la mayor huella ecológica per cápita durante el período analizado. Esta conclusión se fundamenta en varios factores clave como alto consumo de recursos, densidad poblacional elevada, infraestructura y movilidad, y la creciente actividad económica y comercial.')


     
