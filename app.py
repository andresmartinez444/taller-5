import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Gráfica de datos aleatorios")

# Slider para elegir la cantidad de datos
num_datos = st.slider("Selecciona el número de datos", min_value=5, max_value=50, value=10)

# Generar datos aleatorios
tiempo = np.sort(np.random.uniform(0, 10, num_datos))  # Tiempos entre 0 y 10 segundos
voltaje = np.random.uniform(0, 5, num_datos)  # Voltajes entre 0 y 5V (puedes ajustar el rango)

# Crear DataFrame
df = pd.DataFrame({
    "Tiempo (s)": tiempo,
    "Voltaje (V)": voltaje
})

# Mostrar datos en una tabla
st.write("Datos generados aleatoriamente:")
st.dataframe(df)

# Graficar los datos
fig, ax = plt.subplots()
ax.plot(df["Tiempo (s)"], df["Voltaje (V)"], marker="o", linestyle="-")
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Voltaje (V)")
ax.set_title("Voltaje vs. Tiempo")
st.pyplot(fig)
