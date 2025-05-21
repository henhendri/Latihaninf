import streamlit as st

st.title("Selamat Datang di Web Informatika !")
st.write(
    "ngodingseru bersama Bapak Hendri Setiadi"
)
st.image("miku.jpg", width=200)

st.title("Aplikasi Sederhana")

# Menggunakan layout kolom###
#col1, col2 = st.columns(2)

#with col1:
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
