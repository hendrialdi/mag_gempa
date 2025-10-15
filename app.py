import streamlit as st
import pandas as pd
import numpy as np
import random

# Judul aplikasi
st.title("🌋 Aplikasi Prediksi Gempa Indonesia")

st.markdown("""
Aplikasi ini merupakan prediksi gempa.
berdasarkan magnitude.
""")

# ============================
# Bagian 1: Prediksi Gempa Selanjutnya
# ============================
st.header("🔮 Prediksi Gempa Selanjutnya")

jumlah_prediksi = st.number_input(
    "Masukkan jumlah prediksi gempa yang ingin ditampilkan:",
    min_value=1, max_value=10, value=3
)

if st.button("Tampilkan Prediksi Gempa"):
    # Simulasi data gempa (acak)
    lokasi = ["Sumatera", "Jawa", "Bali", "NTT", "NTB", "Sulawesi", "Papua", "Maluku", "Kalimantan"]
    data = {
        "Wilayah": [random.choice(lokasi) for _ in range(jumlah_prediksi)],
        "Latitude": np.random.uniform(-10, 6, jumlah_prediksi),
        "Longitude": np.random.uniform(95, 141, jumlah_prediksi),
        "Kedalaman (km)": np.random.uniform(5, 200, jumlah_prediksi).round(1),
        "Magnitudo (Mw)": np.random.uniform(3.0, 7.0, jumlah_prediksi).round(2)
    }

    df_prediksi = pd.DataFrame(data)
    st.dataframe(df_prediksi)

# ============================
# Bagian 2: Prediksi Magnitudo dari Input
# ============================
st.header("📍 Prediksi Magnitudo Berdasarkan Koordinat")

lat = st.number_input("Masukkan Latitude (-10 s.d 6):", min_value=-10.0, max_value=6.0, value=-2.0)
lon = st.number_input("Masukkan Longitude (95 s.d 141):", min_value=95.0, max_value=141.0, value=120.0)
depth = st.number_input("Masukkan Kedalaman (km):", min_value=0.0, max_value=700.0, value=50.0)

if st.button("Prediksi Magnitudo"):
    # Simulasi prediksi magnitudo (acak berdasarkan depth)
    magnitude_pred = round(3 + np.random.rand() * (7 - 3) - (depth / 1000), 2)
    if magnitude_pred < 2.5:
        magnitude_pred = 2.5  # batas bawah magnitudo

    st.success(f"🔎 Prediksi Magnitudo: **{magnitude_pred} Mw**")

    st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}))

# Footer
st.markdown("---")

