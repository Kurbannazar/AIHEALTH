import streamlit as st
from datetime import datetime
from streamlit_geolocation import geolocation

st.set_page_config(page_title="AIHEALTH", page_icon="💠", layout="centered")

st.markdown("<h1>AIHEALTH</h1>", unsafe_allow_html=True)
st.markdown("<h3>Akıllı Sağlık Asistanı · Kamera ve Konum Entegrasyonlu</h3>", unsafe_allow_html=True)

# ---------------- FOTOĞRAF ---------------- #
st.markdown("### Yaralı Bölgenin Fotoğrafını Çekin")
img = st.camera_input("Fotoğraf çek")

if img:
    st.success("Fotoğraf alındı. Yapay zeka analizi burada çalışacak.")
    st.write("Örnek analiz: Yüzeysel deri lezyonu benzeri bir görünüm tespit edildi.")

# ---------------- KONUM ---------------- #
st.markdown("### Konum Bilgisi")

loc = geolocation()

if loc:
    lat = loc["latitude"]
    lon = loc["longitude"]

    st.success(f"Konum alındı: {lat}, {lon}")

    maps_hospital = f"https://www.google.com/maps/search/hospital/@{lat},{lon},15z"
    maps_pharmacy = f"https://www.google.com/maps/search/eczane/@{lat},{lon},15z"

    st.markdown(f"[📍 En Yakın Hastaneleri Aç]({maps_hospital})")
    st.markdown(f"[💊 En Yakın Eczaneleri Aç]({maps_pharmacy})")
else:
    st.warning("Konum alınamadı. Lütfen izin verin.")

# ---------------- KAYIT ---------------- #
st.markdown("### Kayıt Ol")

ad = st.text_input("Ad Soyad")
tc = st.text_input("T.C. / Kimlik No")
tel = st.text_input("Telefon")
email = st.text_input("E-posta")
yas = st.number_input("Yaş", 0, 120)
kronik = st.text_area("Kronik Hastalıklar")

if st.button("Kaydı Tamamla"):
    st.success("Kayıt başarıyla alındı.")
