import streamlit as st
import random

st.title("Selamat Datang di Web Informatika !")
st.write(
    "ngodingseru bersama Bapak Hendri Setiadi"
)
st.image("miku.jpg", width=200)

###########
st.title("Aplikasi Sederhana")
c1, c2 = st.columns(2)
with c1:
    st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
    angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)
    
    if (angka % 2) == 0:
      st.write(f"{angka} adalah Bilangan Genap")
    else:
      st.write(f"{angka} adalah Bilangan Ganjil")

###########################

with c2:
    # Inisialisasi angka rahasia di session_state
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 50)
    
    st.header("Game Tebak Angka")
    
    guess = st.number_input("Masukkan tebakan angka (1-50):", min_value=1, max_value=50, step=1)
    if st.button("Tebak"):
        if guess == st.session_state.secret_number:
            st.success("Tebakan kamu benar! 🎉")
            st.balloons() 
            # Reset angka rahasia untuk permainan baru
            st.session_state.secret_number = random.randint(1,50)
        else:
            st.warning("Tebakan salah, coba lagi!")
    
    st.write("Tebak angka antara 1 sampai 50.")
