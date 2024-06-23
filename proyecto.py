import requests
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import PyPDF2

st.set_page_config(page_title="Página Principal", page_icon="🤖", layout="wide")

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
    st.image("principal.jpg", use_column_width=True)
    st.title('Huella ecológica')
    st.subheader("¡Acompáñanos a explorar este mundo del conocimiento!:wave:")
    pdf=open("Text1.pdf","rb")
    pdf7=PyPDF2.PdfReader(pdf)
    page_obj=pdf7.pages[0]
    texto7=page_obj.extract_text()
    st.write(texto7)
    
    with st.container():
      st.write("---")
    left_column, right_column= st.columns((2))
    with left_column:
        st.header("Definición")
        pdf=open("Concepto2.pdf","rb")
        pdf0=PyPDF2.PdfReader(pdf)
        page_obj=pdf0.pages[0]
        texto0=page_obj.extract_text()
        st.write(texto0)
        st.write("[Saber más](https://sinia.minam.gob.pe/sites/default/files/sinia/archivos/public/docs/2078.pdf)")
    with right_column:
        st.image("Definición.png", use_column_width=True)
        st.image("Definición2.png", use_column_width=True)
    with st.container():
       st.write("---")
       st.header("Componentes")
       st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
         st.image("Carbono.jpg", use_column_width=True)
    with text_column:
        st.subheader("Área para absorción del carbono")
        pdf=open("Área1.pdf","rb")
        pdf1=PyPDF2.PdfReader(pdf)
        page_obj=pdf1.pages[0]
        texto1=page_obj.extract_text()
        st.write(texto1)
        st.write("[Ver más >](https://www.ciudad.org.pe/wp-content/uploads/2014/11/huella_ecologica.pdf)")

    with st.container():
      st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
         st.image("Pastoreo.png", use_column_width=True)
    with text_column:
        st.subheader("Área de las tierras de pastoreo")
        pdf=open("Área2.pdf","rb")
        pdf2=PyPDF2.PdfReader(pdf)
        page_obj=pdf2.pages[0]
        texto2=page_obj.extract_text()
        st.write(texto2)
        st.write("[Ver más >](https://repositorio.uncp.edu.pe/bitstream/handle/20.500.12894/6399/T010_72320900_T.pdf?sequence=1)")

    with st.container():
     st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image("Forestal.jpg", use_column_width=True)
    with text_column:
        st.subheader("Área forestal")
        pdf=open("Área3.pdf","rb")
        pdf3=PyPDF2.PdfReader(pdf)
        page_obj=pdf3.pages[0]
        texto3=page_obj.extract_text()
        st.write(texto3)
        st.write("[Ver más >](https://coeeci.org.pe/calcula-tu-huella-forestal/)")
    with st.container():
     st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image("zonas pesqueras.jpg", use_column_width=True)
    with text_column:
        st.subheader("Área de las zonas pesqueras")
        pdf=open("Área4.pdf","rb")
        pdf4=PyPDF2.PdfReader(pdf)
        page_obj=pdf4.pages[0]
        texto4=page_obj.extract_text()
        st.write(texto4)
        st.write("[Ver más >](https://perusostenible.org/wp-content/uploads/2023/06/Hojas-de-Ruta-Sectoriales-informe-pesca.pdf)")
    with st.container():
     st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image("Cultivos.jpg", use_column_width=True)
    with text_column:
        st.subheader("Área de los cultivos")
        pdf=open("Área5.pdf","rb")
        pdf5=PyPDF2.PdfReader(pdf)
        page_obj=pdf5.pages[0]
        texto5=page_obj.extract_text()
        st.write(texto5)
        st.write("[Ver más >](https://www.redalyc.org/journal/5717/571763394006/html/)")
    with st.container():
     st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image("Urbanización.jpg", use_column_width=True)
    with text_column:
        st.subheader("Área de la tierra urbanizada")
        pdf=open("Área6.pdf","rb")
        pdf6=PyPDF2.PdfReader(pdf)
        page_obj=pdf6.pages[0]
        texto6=page_obj.extract_text()
        st.write(texto6)
        st.write("[Ver más >](https://www.euskadi.eus/contenidos/documentacion/huella_ecologica/es_def/adjuntos/Huella-Ecologica_pais_vasco_WEB.pdf)")
    with st.container():
     st.write("---")
    st.header("Sigue explorando!")
   

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
    st.image("Pisada.png", use_column_width=True)
    st.write("---")
    st.title('Conclusiones')
    st.write('Puntos principales')
    st.write('Se concluye que la región de Lima muestra la mayor huella ecológica per cápita...')
    st.write("[Ver más >](https://siar.regioncajamarca.gob.pe/indicador/1208)")
    st.write("Youtube >](https://youtu.be/g-V9CS-MHrI)")

     
