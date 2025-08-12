import streamlit as st

st.set_page_config(
    page_title="Home - Analisis Lirik Drake",
    page_icon="👋",
)

st.title("Selamat Datang di Aplikasi Analisis Makna Lirik Drake! 👋")
st.sidebar.success("Pilih halaman di atas untuk memulai.")

st.markdown(
    """
    Aplikasi ini adalah portofolio berbasis AI yang dirancang untuk menganalisis dan 
    menghasilkan interpretasi makna dari lirik-lirik lagu Drake. 
    
    """
)

st.subheader("Fitur Utama Aplikasi")
st.markdown(
    """
    - **Generator Makna Lirik**: Masukkan potongan lirik dan dapatkan analisis mendalam mengenai maknanya.
    - **Evaluasi Model**: Setiap makna yang dihasilkan akan dievaluasi performanya menggunakan metrik kemiripan semantik (Cosine Similarity) dibandingkan dengan makna referensi.
"""
)

st.subheader("Cara Penggunaan")
st.info(
    """
    1.  Buka halaman **🎵 Makna Lirik** dari menu di sebelah kiri.
    2.  Masukkan potongan lirik lagu Drake di area teks yang tersedia.
    3.  Klik tombol "Hasilkan Makna".
    4.  Tunggu beberapa saat hingga AI selesai menganalisis dan menampilkan hasilnya, lengkap dengan skor evaluasi.
    5.  Kunjungi halaman **👤 Profil** untuk mengetahui lebih lanjut tentang penulis aplikasi ini.
"""
)