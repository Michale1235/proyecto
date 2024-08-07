import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import PyPDF2
from streamlit_option_menu import option_menu

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded")
selecionar=option_menu(
    menu_title='Menu de opciones',
    options=['Página Principal','Gráfico 1: Áreas y departamentos','Gráfico 2: Departamentos y años','Gráfico 3: Huella ecológica anual','Conclusión',
             'Sobre nosotros'],
    icons=['house','cloud-upload','kanban','activity','book','person'],
    orientation='horizontal')
departamentos=['AMAZONAS', 'ÁNCASH', 'APURÍMAC','AREQUIPA','AYACUCHO','CAJAMARCA','CUSCO','HUANCAVELICA','HUÁNUCO','ICA','JUNÍN',
                'LA LIBERTAD','LAMBAYEQUE','LIMA','LORETO','MADRE DE DIOS','MOQUEGUA','PASCO','PIURA','PUNO',
                'SAN MARTÍN','TACNA','TUMBES','UCAYALI']
años=['2009', '2010', '2011','2012','2013','2014','2015','2016']
areas=['Área de Cultivos','Área de Pastoreo','Área de Bosques','Zonas de pesca','Huella de Carbono','Áreas Urbanas']

excel_file='excels/huellaecologicaregional.xlsx'
excel_file1='excels/datos.xlsx'

if selecionar=='Página Principal':
    st.image("Principal.jpg", use_column_width=True)
    st.title('Huella ecológica')
    st.subheader("¡Acompáñanos a explorar este mundo del conocimiento!:wave:")
    pdf=open("pdfs/Text1.pdf","rb")
    pdf7=PyPDF2.PdfReader(pdf)
    page_obj=pdf7.pages[0]
    texto7=page_obj.extract_text()
    st.write(texto7)
    with st.container():
        st.write("---")
        left_column, right_column= st.columns((2))
    with left_column:
        st.header("Definición")
        pdf=open("pdfs/Concepto2.pdf","rb")
        pdf0=PyPDF2.PdfReader(pdf)
        page_obj=pdf0.pages[0]
        texto0=page_obj.extract_text()
        st.write(texto0)
        st.write("[Fuente:](https://sinia.minam.gob.pe/sites/default/files/sinia/archivos/public/docs/2078.pdf)")
    with right_column:
        st.image("imgen/Definición.jpg", use_column_width=True)
        st.image("imgen/Definición2.png", use_column_width=True)
    with st.container():
        st.write("---")
        st.header("Componentes")
        image_column, text_column = st.columns((1,2))
    with image_column:
        st.image("imgen/Carbono.jpg", use_column_width=True)
    with text_column:
        st.subheader("Área para absorción del carbono")
        pdf=open("pdfs/Área1.pdf","rb")
        pdf1=PyPDF2.PdfReader(pdf)
        page_obj=pdf1.pages[0]
        texto1=page_obj.extract_text()
        st.write(texto1)
        st.write("[Fuente: ](https://www.ciudad.org.pe/wp-content/uploads/2014/11/huella_ecologica.pdf)")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
    with image_column:
        st.image("imgen/Pastoreo.png", use_column_width=True)
    with text_column:
        st.subheader("Área de las tierras de pastoreo")
        pdf=open("pdfs/Área2.pdf","rb")
        pdf2=PyPDF2.PdfReader(pdf)
        page_obj=pdf2.pages[0]
        texto2=page_obj.extract_text()
        st.write(texto2)
        st.write("[Fuente: ](https://repositorio.uncp.edu.pe/bitstream/handle/20.500.12894/6399/T010_72320900_T.pdf?sequence=1)")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
    with image_column:
        st.image("imgen/Forestal.jpg", use_column_width=True)
    with text_column:
        st.subheader("Área forestal")
        pdf=open("pdfs/Área3.pdf","rb")
        pdf3=PyPDF2.PdfReader(pdf)
        page_obj=pdf3.pages[0]
        texto3=page_obj.extract_text()
        st.write(texto3)
        st.write("[Fuente: ](https://coeeci.org.pe/calcula-tu-huella-forestal/)")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
    with image_column:
        st.image("imgen/zonas pesqueras.jpg", use_column_width=True)
    with text_column:
        st.subheader("Área de las zonas pesqueras")
        pdf=open("pdfs/Área4.pdf","rb")
        pdf4=PyPDF2.PdfReader(pdf)
        page_obj=pdf4.pages[0]
        texto4=page_obj.extract_text()
        st.write(texto4)
        st.write("[Fuente: ](https://perusostenible.org/wp-content/uploads/2023/06/Hojas-de-Ruta-Sectoriales-informe-pesca.pdf)")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
    with image_column:
        st.image("imgen/Cultivos.jpg", use_column_width=True)
    with text_column:
        st.subheader("Área de los cultivos")
        pdf=open("pdfs/Área5.pdf","rb")
        pdf5=PyPDF2.PdfReader(pdf)
        page_obj=pdf5.pages[0]
        texto5=page_obj.extract_text()
        st.write(texto5)
        st.write("[Fuente: ](https://www.redalyc.org/journal/5717/571763394006/html/)")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
    with image_column:
        st.image("imgen/Urbanización.jpg", use_column_width=True)
    with text_column:
        st.subheader("Área de la tierra urbanizada")
        pdf=open("pdfs/Área6.pdf","rb")
        pdf6=PyPDF2.PdfReader(pdf)
        page_obj=pdf6.pages[0]
        texto6=page_obj.extract_text()
        st.write(texto6)
        st.write("[Fuente: ](https://www.euskadi.eus/contenidos/documentacion/huella_ecologica/es_def/adjuntos/Huella-Ecologica_pais_vasco_WEB.pdf)")
elif selecionar=='Gráfico 1: Áreas y departamentos':
    st.title('Análisis por áreas y departamentos')
    col1,col2=st.columns(2)
    with col1:
        option1 = st.selectbox('Seleciona el área que quieres visualizar los datos',areas)
        st.write('seleccionó:', option1)
    with col2:
        option =st.selectbox('Selecciona un departamento',departamentos)
        st.write('Seleccionó:', option)
        sheet_name= años
        sheet_name1=option1
        df=pd.read_excel(excel_file,
                     sheet_name=sheet_name,
                     usecols='A:H',
                     header=6)
        df = pd.concat([df.assign(Años=años) for años, df in df.items()], ignore_index=True)
        df_filtered3 = df[df['Ámbito'] == option][['Años', option1]]
    fig, ax = plt.subplots(figsize=(10, 4))
    df_filtered3.plot(x='Años',
            y=option1,
            ax=ax,
            color='red',
            marker='o')
    ax.set_ylabel('hectáreas globales (hag)')
    plt.tight_layout(pad=3.0)
    st.pyplot(fig)
elif selecionar== "Gráfico 2: Departamentos y años":
    st.title('Análisis por departamentos y años')
    col1,col2=st.columns(2)
    with col1:
        option1 = st.selectbox('seleciona el departamento que quieres visualizar los datos',departamentos)
        st.write('Seleccionó:', option1)
    with col2:
        option =st.selectbox('Seleciona un año',años)
        st.write('Seleccionó:', option)
        sheet_name= option
        sheet_name1=option1
        df=pd.read_excel(excel_file1,
                     sheet_name=sheet_name,
                     usecols='A:Y',
                     header=2)
        paleta_continua=px.colors.sequential.Jet
        df_filtred=df[df['Ámbito']!='Huella Regional Per Capita']
    c1,c2=st.columns(2)
    Total_departamentos=df['Ámbito'].nunique()
    total_ambito=df_filtred[option1].sum()
    col1,col2=st.columns(2)
    col1.metric('Numero de huellas ecologicas', value=df_filtred.Ámbito.count(), delta='Ámbito')
    col2.metric('Total de Huella ecológia en el departamento', f'{total_ambito:,.4f}', delta='total')
    df_filtred1=df_filtred.groupby('Ámbito')[option1].sum().reset_index().sort_values(by=option1)
    bar_chart=px.bar(df_filtred1,
                     x=option1,
                     y='Ámbito',
                     text_auto=True,
                     color=option1,
                     color_continuous_scale=paleta_continua)
    st.plotly_chart(bar_chart,use_container_width=True)
elif selecionar == "Gráfico 3: Huella ecológica anual":
    st.title('Análisis de la huella ecológica en el Perú')
    option = st.selectbox('Seleciona el año que quieres visualizar los datos',
                          ('2009', '2010', '2011','2012','2013','2014','2015','2016'))
    st.write('Seleccionó:', option)
    st.title('Gráfico de Huella Ecológica')
    sheet_name= option
    df=pd.read_excel(excel_file,
                     sheet_name=sheet_name,
                     usecols='A:H',
                     header=6)
    df.dropna(inplace=True)

    df_filtred=df[df['Ámbito']!='Total']
    Total_departamentos=df['Ámbito'].nunique()
    total_ambito=df['Huella Regional Per Capita'].mean()

    col1,col2=st.columns(2)
    col1.metric('Total de departamentos', str(Total_departamentos))
    col2.metric('Promedio de Huella ecológia en el peru', f'{total_ambito:,.5f}')
    pie_chart=px.pie(df_filtred,
                     title='Porcentaje de Huella Regional Per capita',
                     values='Huella Regional Per Capita',
                     names='Ámbito')
    st.plotly_chart(pie_chart) 
    huellas='Huella Regional Per Capita'
    paleta_continua=px.colors.sequential.Jet
    df_filtred11 = df.sort_values(by=huellas, ascending=False)
    bar_chart=px.bar(df_filtred11,
                             x='Ámbito',
                             y=huellas,
                             color='Ámbito',
                             color_continuous_scale=paleta_continua)
    st.plotly_chart(bar_chart) 
    with st.expander('Mi base de datos'):
        st.dataframe(df_filtred, use_container_width=True)
        df_filtred.describe()

elif selecionar=='Conclusión':
    pdf_file=open('pdfs/interpretacion.pdf','rb')
    pdf_reader=PyPDF2.PdfReader(pdf_file)
    page_obj=pdf_reader.pages[0]
    texto=page_obj.extract_text()
    st.write(texto)
    st.write("---")
    st.header('Acciones para minimizar la huella ecológica')
    st.write("---")
    st.subheader("¡Preserva la biodiversidad peruana!")
    st.image("imgen/Progra.png", use_column_width=True)
    st.write("""
             *Fuente: Grupo N°3*
             """)
    pdf=open("pdfs/frase.pdf","rb")
    pdf12=PyPDF2.PdfReader(pdf)
    page_obj=pdf12.pages[0]
    texto12=page_obj.extract_text()
    st.write(texto12)
    st.write("[Ver más](https://youtu.be/g-V9CS-MHrI)")
elif selecionar=='Sobre nosotros':
    st.title('Colaboradores')
    video=open('Integrantes/equipo.mp4', 'rb')
    video1=video.read()
    st.video(video1)
    
