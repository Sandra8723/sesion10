import pandas as pd
import streamlit as st


data = pd.read_csv('educacionvial_2018.csv', delimiter=";")

data = data.dropna()
data

st.header("Filtro 1")
st.write ("Mostrar todas las acciones diferentes a las de Instituciones Educativas")
filtro1 = data[data["ACCIONES"] != "Otros_Instituciones_Educativas"]
st.dataframe(filtro1)

st.header("Filtro 2")
st.write ("Mostrar todas Lineas de trabajo de Incidencia y Gestión Ejecución de Experiencias")
filtro2 = data[data["LÍNEAS DE TRABAJO - COMPONENTE"] == "Incidencia_y_Gestion_Ejecucion_de_Experiencias"]
st. dataframe(filtro2)

st.header("Filtro 3")
st.write ("Mostrar todas Lineas de trabajo de Incidencia que se encuentran en la Comuna San Antonio de prado")
filtro3 = data[(data["LÍNEAS DE TRABAJO - COMPONENTE"] == "Incidencia_y_Gestion_Ejecucion_de_Experiencias") & (data["COMUNA"]=='San_Antonio_de_Prado')]
st. dataframe(filtro3)

st.header("Filtro 4")
st.write ("Seleccionar todas las filas de los datos donde la columna Barrio coincide con alguna de las palabras clave especificadas en la lista")
palabras_clave = ['Perpetuo Socorro','La Candelaria']
filtro4 = data[data["BARRIO"].isin(palabras_clave)]
st. dataframe(filtro4)

st.header("Filtro 5")
st.write ("Mostrar la comuna con codigo 10 (La Candelaria)")
filtro5 = data[(data["COD_COMUNA"]==10) & (data["COMUNA"]=='La_Candelaria')]
st. dataframe(filtro5)

st.header("Filtro 6")
st.write ("Mostrar mas de 100 del Total de mujeres sensibilizadas de la comuna Poblado")
filtro6 = data[(data["COMUNA"]=='Poblado') & (data["TOTAL MUJER"]>100)]
st. dataframe(filtro6)

st.header("Filtro 7")
st.write ("Mostrar el público objetivo diferente a los Peatones")
filtro7 = data[data["PUBLICO OBJETIVO"] != "Peatones"]
st. dataframe(filtro7)

st.header("Filtro 8")
st.write ("Mostrar el Total de Hombre igual a 52")
filtro8 = data[data['TOTAL HOMBRE']==52]
st. dataframe(filtro8)

st.header("Filtro 9")
st.write ("Mostrar las palabras claves de la lista de datos columna Verificación")
palabras_clave = ['Incidencia','Experiencias_Empresas']
filtro9 = data[data['VERIFICACIÓN'].isin(palabras_clave)]
st. dataframe(filtro9)

st.header("Filtro 10")
st.write ("Mostrar total personas sensibilizadas en la comuna con codigo 5, Bario Caribe")
filtro10 = data[(data['TOTAL PERSONAS SENSIBILIZADAS']) & (data['COD_COMUNA']==5) & (data["BARRIO"]== 'Caribe')]
st. dataframe(filtro10)