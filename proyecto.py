import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import datetime
import matplotlib.pyplot as plt
import PyPDF2


def sidebar_menu():
    st.sidebar.title("Huella ecológica per cápita departamental y por componentes - Ministerio del Ambiente")
    if st.sidebar.button('Página Principal'):
        st.session_state.page = "Página Principal"
    if st.sidebar.button('Página 2: Grafico por Departamento'):
        st.session_state.page = "Página 2: Grafico por Departamento"
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
    st.title('Huella Ecológica')
    pdf_file=open('huellaecologica.pdf','rb')
    pdf_reader=PyPDF2.PdfReader(pdf_file)
    page_obj=pdf_reader.pages[0]
    texto=page_obj.extract_text()
    st.write(texto)
elif st.session_state.page == "Página 2: Grafico por Departamento":
    option1 = st.selectbox('seleciona el año que quieres visualizar los datos',
                          ['Área de Cultivos','Área de Pastoreo','Área de Bosques',
                           'Zonas de Pescas','Huella de Carbono','Áreas Urbanas'])
    st.write('seleccionó:', option1)
    option =st.selectbox('Seleciona un año',
                         ['2009', '2010', '2011','2012','2013','2014','2015','2016'])
    st.write('Seleccionó:', option)
    st.title('Grafico por departamentos')
    excel_file='prueba.xlsx'
    sheet_name= option
    sheet_name1=option1

    df=pd.read_excel(excel_file,
                     sheet_name=sheet_name,
                     usecols='A:H',
                     header=6)
    
    df_filtred=df[df['Ámbito']!='Total']



    bar_chart=px.bar(df_filtred,
                     x='Ámbito',
                     y=option1,
                     color_discrete_sequence=['green']*len(df_filtred)
                     )
    

    linea_chart=px.line(df_filtred,
                     x='Ámbito',
                     y=option1,
                     color_discrete_sequence=['green']*len(df_filtred)
                     )
    st.plotly_chart(linea_chart)


    
    for i, v in enumerate(df_filtred[option1]):
        bar_chart.add_annotation(
        x=df_filtred['Ámbito'].iloc[i],
        y=v,
        text=f'{v:.3f}',
        showarrow=False,
        font=dict(color='blue'),
        align='center',
        yshift=6 )

    st.plotly_chart(bar_chart)
    
 


    pie_chart=px.pie(df_filtred,
                     title='Porcentaje de Huella Regional Per capita por Region',
                     values=option1,
                     names='Ámbito')
    st.plotly_chart(pie_chart)
    








elif st.session_state.page == "Página 3: Gráfico":
    option = st.selectbox('seleciona el año que quieres visualizar los datos',
                          ('2009', '2010', '2011','2012','2013','2014','2015','2016'))
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

    Total_departamentos=df['Ámbito'].nunique()
    total_ambito=df['Huella Regional Per Capita'].mean()

    col1,col2=st.columns(2)
    col1.metric('Departamentos', str(Total_departamentos))
    col2.metric('Total de Huella ecológia en el peru', f'{total_ambito:,.5f}')

    pie_chart=px.pie(df_filtred,
                     title='Porcentaje de Huella Regional Per capita',
                     values='Huella Regional Per Capita',
                     names='Ámbito')
    st.plotly_chart(pie_chart)
    






