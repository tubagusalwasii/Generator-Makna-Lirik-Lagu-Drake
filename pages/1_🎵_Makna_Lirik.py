import streamlit as st
import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

# --- Fungsi untuk Memuat Model (Sudah Diperbaiki untuk CPU) ---
@st.cache_resource
def load_llm_model():
    base_model_id = "meta-llama/Llama-3.2-1B-Instruct"
    adapter_path = "llama3-drake-finetuned-v2"
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    base_model = AutoModelForCausalLM.from_pretrained(base_model_id)
    model = PeftModel.from_pretrained(base_model, adapter_path)
    model = model.to(device)
    
    tokenizer = AutoTokenizer.from_pretrained(adapter_path)
    
    return tokenizer, model

# --- Fungsi untuk memuat model evaluasi ---
@st.cache_resource
def load_evaluation_model():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

# --- Fungsi untuk Sistem RAG (Retrieval) menggunakan TF-IDF ---
@st.cache_resource
def setup_retriever():
    """Membaca dataset dan membangun sistem pencarian TF-IDF."""
    try:
        df = pd.read_csv("drake songs and meaning datasets.csv", delimiter=';', encoding='latin-1')
        # MEMASTIKAN KOLOM 'meaning_bait' ADA (SUDAH DIGANTI)
        if 'meaning_bait' not in df.columns:
            st.error("Dataset CSV harus memiliki kolom 'meaning_bait' untuk evaluasi.")
            return None, None, None
        # MENGGUNAKAN 'meaning_bait' SAAT MEMBERSIHKAN DATA (SUDAH DIGANTI)
        df.dropna(subset=['lyric_bait', 'song_title', 'album', 'meaning_bait'], inplace=True)
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(df['lyric_bait'])
        return df, vectorizer, tfidf_matrix
    except FileNotFoundError:
        st.error("File 'drake songs and meaning datasets.csv' tidak ditemukan.")
        return None, None, None

def retrieve_lyrics(query, df, vectorizer, tfidf_matrix):
    """Mencari lirik yang paling mirip dari database."""
    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, tfidf_matrix).flatten()
    best_index = similarity.argmax()
    return df.iloc[best_index]

# --- UI dan Logika Aplikasi Utama ---
st.set_page_config(page_title="Generator Makna Lirik", layout="centered")
st.title("🎵 Generator Makna Lirik Drake")
st.markdown("Masukkan potongan lirik lagu Drake, dan AI akan menghasilkan detail serta analisis maknanya.")

# Memuat semua model
with st.spinner("Memuat model AI, harap tunggu..."):
    tokenizer, model = load_llm_model()
    eval_model = load_evaluation_model()
st.toast("Semua model berhasil dimuat!", icon="✅") 

df, vectorizer, tfidf_matrix = setup_retriever()

if df is not None:
    lyrics = st.text_area(
        "Masukkan Lirik Lagu di Sini",
        height=150,
        placeholder="Contoh: Listen, seeing you got ritualistic"
    )

    if st.button("🔍 Hasilkan Makna"):
        if not lyrics.strip():
            st.warning("Mohon masukkan lirik terlebih dahulu.")
        else:
            # --- Proses RAG ---
            with st.spinner("Langkah 1/3: Mencari lagu di database..."):
                retrieved_data = retrieve_lyrics(lyrics, df, vectorizer, tfidf_matrix)
                title = retrieved_data['song_title']
                album = retrieved_data['album']
                sumber = retrieved_data['source']
                # MENGAMBIL MAKNA DARI KOLOM 'meaning_bait' (SUDAH DIGANTI)
                actual_meaning = retrieved_data['meaning_bait']

            # --- Proses Generasi ---
            with st.spinner("Langkah 2/3: Menganalisis makna..."):
                prompt = f"""
                 Tugas: Analisis makna dari lirik lagu Drake berikut ini.

                    Konteks Lagu:
                    - Judul: {title}
                    - Album: {album}
                    - Lirik: "{lyrics}"

                    Instruksi Format:
                    Berikan penjelasan mendalam dengan cara mengutip langsung bagian lirik spesifik dan jelaskan artinya.
                    Contoh: "Pada lirik '[kutipan lirik]', Drake tampaknya sedang membicarakan tentang... Hal ini didukung oleh baris berikutnya '[kutipan lirik lain]' yang menyiratkan..."

                    Mulai analisis Anda di bawah.
                    Makna:
                    """
                inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
                outputs = model.generate(
                    input_ids=inputs['input_ids'],
                    max_new_tokens=512,
                    num_beams=5,
                    early_stopping=True
                )
                decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
                generated_meaning = decoded_output.split("Makna:")[-1].strip() if "Makna:" in decoded_output else "Gagal menghasilkan makna."

            # --- PROSES EVALUASI ---
            with st.spinner("Langkah 3/3: Mengevaluasi hasil..."):
                embedding1 = eval_model.encode(generated_meaning, convert_to_tensor=True)
                embedding2 = eval_model.encode(actual_meaning, convert_to_tensor=True)
                cosine_scores = util.cos_sim(embedding1, embedding2)
                score = cosine_scores.item() * 100 # Jadikan persen

            # --- Menampilkan Hasil ---
            st.markdown("---")
            st.markdown("## 📄 Hasil Generate")
            st.markdown(f"**🎵 Judul Lagu:** `{title}`")
            st.markdown(f"**💿 Album:** `{album}`")
            st.markdown(f"**🔗 Sumber:** `{sumber}`")
            st.markdown("**🧠 Makna yang Dihasilkan:**")
            st.info(generated_meaning)

            st.markdown("---")
            st.markdown("## 📊 Hasil Evaluasi")
            st.markdown(f"**🎯 Makna Referensi (dari dataset):**")
            st.warning(actual_meaning)
            
            st.metric(
                label="Skor Kemiripan Semantik (Cosine Similarity)",
                value=f"{score:.2f}%"
            )
            st.progress(int(score))
            st.caption("Skor ini mengukur seberapa mirip makna yang dihasilkan AI dengan makna referensi dari dataset.")