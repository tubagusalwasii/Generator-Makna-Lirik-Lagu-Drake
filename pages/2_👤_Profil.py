import streamlit as st
import math

st.set_page_config(
    page_title="Profil Drake",
    page_icon="🎤",
    layout="wide"
)


URL_FOTO_PROFIL = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Drake_July_2016.jpg/800px-Drake_July_2016.jpg"
URL_MORE_LIFE = "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/71/97/d0/7197d021-de0f-9548-3f31-40b8294d3242/17UMGIM85032.rgb.jpg/1200x630bb.jpg"
URL_SCORPION = "https://upload.wikimedia.org/wikipedia/en/9/90/Scorpion_by_Drake.jpg"
URL_CARE_PACKAGE = "https://i.scdn.co/image/ab67616d0000b2739c1e02d4becb7c5bbca01e2a"
URL_DARK_LANE = "https://i.scdn.co/image/ab67616d0000b273bba7cfaf7c59ff0898acba1f"



st.title("Profil Artis: Drake")
st.write("---")

# --- Bagian Biografi ---
col1, col2 = st.columns([2, 3])  

with col1:
    st.image(URL_FOTO_PROFIL, caption="Aubrey 'Drake' Graham")

with col2:
    st.header("Drake")
    st.info(
        """
        Aubrey Drake Graham (lahir 24 Oktober 1986) adalah seorang rapper, penyanyi, penulis lagu, 
        dan aktor asal Kanada. Seorang tokoh berpengaruh dalam musik populer kontemporer, 
        Drake dikreditkan karena mempopulerkan suara Toronto ke panggung dunia.
        
        Awalnya ia dikenal sebagai aktor dalam serial drama remaja *Degrassi: The Next Generation* pada awal 2000-an. Mengejar karir musik, ia merilis mixtape pertamanya, *Room for Improvement*, 
        pada tahun 2006. Drake telah memenangkan empat Grammy Awards, enam American Music Awards, 
        dan memegang beberapa rekor tangga lagu Billboard.
        """
    )
    st.markdown(f"""
    - **Nama Lengkap:** Aubrey Drake Graham
    - **Asal:** Toronto, Ontario, Kanada
    - **Genre:** Hip hop, R&B, pop rap
    - **Label:** OVO Sound, Republic Records
    """)


# --- Bagian Diskografi ---
st.write("---")
st.header("💽 Diskografi (Album dalam Laporan)")
st.write("") 


## --- Album: More Life ---
st.subheader("More Life (2017)")
tracklist_more_life = [
    "Free Smoke", "No Long Talk (feat. Giggs)", "Passionfruit", "Jorja Interlude",
    "Get It Together (feat. Black Coffee & Jorja Smith)", "Madiba Riddim", "Blem",
    "4422 (feat. Sampha)", "Gyalchester", "Skepta Interlude", "Portland (feat. Quavo & Travis Scott)",
    "Sacrifices (feat. 2 Chainz & Young Thug)", "Nothings Into Somethings", "Teenage Fever",
    "KMT (feat. Giggs)", "Lose You", "Can't Have Everything", "Glow (feat. Kanye West)",
    "Since Way Back (feat. Partynextdoor)", "Fake Love", "Ice Melts (feat. Young Thug)", "Do Not Disturb"
]
col1_ml, col2_ml = st.columns([1, 2])
with col1_ml:
    st.image(URL_MORE_LIFE, caption="More Life - A Playlist by October Firm")
with col2_ml:
    st.markdown("**Daftar Lagu:**")
    mid_point = math.ceil(len(tracklist_more_life) / 2)
    list_1 = tracklist_more_life[:mid_point]
    list_2 = tracklist_more_life[mid_point:]
    track_col_1, track_col_2 = st.columns(2)
    with track_col_1:
        for i, track in enumerate(list_1, 1):
            st.write(f"{i}. {track}")
    with track_col_2:
        for i, track in enumerate(list_2, mid_point + 1):
            st.write(f"{i}. {track}")
st.write("---")


# --- Album: Scorpion ---
st.subheader("Scorpion (2018)")
col1_sc, col2_sc = st.columns([1, 2])
with col1_sc:
    st.image(URL_SCORPION, caption="Scorpion")
with col2_sc:
    st.markdown("**Daftar Lagu (Double Album):**")
    a_side_col, b_side_col = st.columns(2) 
    a_side_scorpion = ["Survival", "Nonstop", "Elevate", "Emotionless", "God's Plan", "I'm Upset", "8 Out of 10", "Mob Ties", "Can't Take a Joke", "Sandra's Rose", "Talk Up (feat. Jay-Z)", "Is There More"]
    b_side_scorpion = ["Peak", "Summer Games", "Jaded", "Nice for What", "Finesse", "Ratchet Happy Birthday", "That's How You Feel", "Blue Tint", "In My Feelings", "Don't Matter to Me (feat. Michael Jackson)", "After Dark (feat. Static Major & Ty Dolla Sign)", "Final Fantasy", "March 14"]
    with a_side_col:
        st.markdown("**A Side**")
        for i, track in enumerate(a_side_scorpion, 1):
            st.write(f"{i}. {track}")
    with b_side_col:
        st.markdown("**B Side**")
        for i, track in enumerate(b_side_scorpion, 1):
            st.write(f"{i}. {track}")
st.write("---")


# --- Album: Care Package ---
st.subheader("Care Package (2019)")
tracklist_care_package = [
    "Dreams Money Can Buy", "The Motion", "How Bout Now", "Trust Issues", "Days in the East", 
    "Draft Day", "4PM in Calabasas", "5 AM in Toronto", "I Get Lonely", "My Side", 
    "Jodeci Freestyle (feat. J. Cole)", "Club Paradise", "Free Spirit (feat. Rick Ross)", 
    "Heat of the Moment", "Girls Love Beyoncé (feat. James Fauntleroy)", "Paris Morton Music", "Can I"
]
col1_cp, col2_cp = st.columns([1, 2])
with col1_cp:
    st.image(URL_CARE_PACKAGE, caption="Care Package")
with col2_cp:
    st.markdown("**Daftar Lagu:**")
    mid_point = math.ceil(len(tracklist_care_package) / 2)
    list_1 = tracklist_care_package[:mid_point]
    list_2 = tracklist_care_package[mid_point:]
    track_col_1, track_col_2 = st.columns(2)
    with track_col_1:
        for i, track in enumerate(list_1, 1):
            st.write(f"{i}. {track}")
    with track_col_2:
        for i, track in enumerate(list_2, mid_point + 1):
            st.write(f"{i}. {track}")
st.write("---")


# --- Album: Dark Lane Demo Tapes ---
st.subheader("Dark Lane Demo Tapes (2020)")
tracklist_dark_lane = [
    "Deep Pockets", "When to Say When", "Chicago Freestyle (feat. Giveon)",
    "Not You Too (feat. Chris Brown)", "Toosie Slide", "Desires (feat. Future)",
    "Time Flies", "Landed", "D4L (with Future & Young Thug)",
    "Pain 1993 (feat. Playboi Carti)", "Losses", "From Florida With Love",
    "Demons (feat. Fivio Foreign & Sosa Geek)", "War"
]
col1_dl, col2_dl = st.columns([1, 2])
with col1_dl:
    st.image(URL_DARK_LANE, caption="Dark Lane Demo Tapes")
with col2_dl:
    st.markdown("**Daftar Lagu:**")
    mid_point = math.ceil(len(tracklist_dark_lane) / 2)
    list_1 = tracklist_dark_lane[:mid_point]
    list_2 = tracklist_dark_lane[mid_point:]
    track_col_1, track_col_2 = st.columns(2)
    with track_col_1:
        for i, track in enumerate(list_1, 1):
            st.write(f"{i}. {track}")
    with track_col_2:
        for i, track in enumerate(list_2, mid_point + 1):
            st.write(f"{i}. {track}")

