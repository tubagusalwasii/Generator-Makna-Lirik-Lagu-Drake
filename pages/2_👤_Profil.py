import streamlit as st
from PIL import Image

st.set_page_config(page_title="Profil Penulis", page_icon="👤")

st.title("Profil Penulis")

# --- Ganti dengan informasi Anda ---
NAMA_ANDA = "Tubagus Alwasi'i"
BIO_ANDA = """
Nama saya Tubagus Alwasi'i, dan saat ini saya berada di penghujung perjalanan studi saya sebagai mahasiswa semester 8 di Universitas Islam Sultan Agung (Unissula). Sejak awal, saya selalu tertarik pada dunia teknologi, terutama pada bagaimana Kecerdasan Buatan (AI) dapat digunakan untuk memecahkan masalah-masalah unik.

Di sisi lain, musik adalah "soundtrack" dalam kehidupan saya. Saya menghabiskan banyak waktu mendengarkan berbagai genre, namun saya memiliki ketertarikan khusus pada lirik yang cerdas dan puitis. Ada kepuasan tersendiri ketika berhasil menangkap makna tersembunyi di balik barisan kata dalam sebuah lagu.

Aplikasi web generator makna lirik Drake ini adalah proyek yang lahir dari titik temu kedua gairah saya tersebut. Idenya muncul dari sebuah pertanyaan sederhana: "Apa sebenarnya yang ingin Drake sampaikan di sini?" Liriknya sering kali berlapis-lapis, membuatnya menarik sekaligus menantang untuk dipahami sepenuhnya. Saya melihat ini sebagai sebuah peluang. Saya ingin membangun sesuatu yang bisa memperkaya pengalaman mendengarkan musik bagi banyak orang. Dengan memanfaatkan kekuatan AI, aplikasi ini bertujuan untuk mengurai kompleksitas lirik Drake, memberikan konteks, dan mengungkap cerita di baliknya. Ini adalah cara saya menggunakan keahlian teknologi untuk merayakan seni dan memperdalam koneksi kita dengan musik.
"""
LINK_LINKEDIN = "https://www.linkedin.com/in/tubagus-alwasi-i-727200295/"
LINK_GITHUB = "https://github.com/tubagusalwasii"
LINK_LAINNYA = "https://www.instagram.com/tbagusz/" 
PATH_FOTO_PROFIL = "assets/foto.jpeg"
# --- Batas edit ---


try:
    image = Image.open(PATH_FOTO_PROFIL)
    st.image(image, width=200, caption=NAMA_ANDA)
except FileNotFoundError:
    st.error(f"Foto profil tidak ditemukan. Pastikan file '{PATH_FOTO_PROFIL}' ada.")


st.header(NAMA_ANDA)
st.info(BIO_ANDA)

st.subheader("Tentang Saya")
st.markdown(f"""
- 💼 [LinkedIn]({LINK_LINKEDIN})
- 💻 [GitHub]({LINK_GITHUB})
- 📸 [Instagram]({LINK_LAINNYA})
""")