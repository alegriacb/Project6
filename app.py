import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Venta de vehículos usados en USA')

# crear un botón para la creación de un histograma
hist_button = st.button('Construir histograma')

if hist_button:  # al hacer clic en el botón se despliega un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches respecto al kilometraje')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear un boton para la creacion de un diagrama de dispersión
scat_button = st.button('Contruir un diagrama de dispersion')

if scat_button:
    st.write("Creación de un diagrama de dispersión entre kilometraje y precio")

    # crear el diagrama de dispersión
    fig2 = px.scatter(car_data, x='odometer', y='price',
                      title='Kilimetraje vs Precio')

    # mostar gráfico interactivo
    st.plotly_chart(fig2, use_container_width=True)
