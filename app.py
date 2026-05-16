import streamlit as st
from datetime import datetime
from streamlit_geolocation import geolocation
import base64

# ------------------ GENEL AYARLAR ------------------ #
st.set_page_config(page_title="AIHEALTH", page_icon="💠", layout="centered")

# ------------------ TEMA & STİL ------------------ #
st.markdown(
    """
    <style>
    body {
        background-color: #02040a;
        color: #e0f4ff;
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background: radial-gradient(circle at top, #04152b 0, #02040a 45%, #000000 100%);
    }
    h1, h2, h3 {
        color: #e6f7ff;
        text-shadow: 0 0 12px rgba(0, 153, 255, 0.8);
    }
    .logo-title {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .logo-circle {
        width: 42px;
        height: 42px;
        border-radius: 50%;
        border: 2px solid #00c6ff;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 0 18px rgba(0, 198, 255, 0.9);
        font-size: 22px;
        color: #00e5ff;
    }
    .top-right-buttons {
        position: fixed;
        top: 12px;
        right: 16px;
        z-index: 9999;
        display: flex;
        gap: 8px;
    }
    .glow-button {
        padding: 0.5rem 1.2rem;
        border-radius: 999px;
        border: 1px solid rgba(255,255,255,0.15);
        cursor: pointer;
        font-weight: 600;
        font-size: 0.9rem;
        letter-spacing: 0.03em;
        box-shadow: 0 0 12px rgba(0, 153, 255, 0.8);
        transition: all 0.2s ease-out;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        justify-content: center;
    }
    .glow-button.blue {
        background: linear-gradient(135deg, #0b6bff, #00c6ff);
        color: #ffffff;
    }
    .glow-button.red {
        background: linear-gradient(135deg, #ff1744, #ff5252);
        color: #ffffff;
        box-shadow: 0 0 16px rgba(255, 23, 68, 0.9);
    }
    .section-card {
        background: radial-gradient(circle at top left, rgba(0, 153, 255, 0.12), rgba(0,0,0,0.9));
        border-radius: 18px;
        padding: 18px;
        border: 1px solid rgba(0, 153, 255, 0.25);
        box-shadow: 0 0 24px rgba(0, 153, 255, 0.25);
        margin-bottom: 18px;
    }
    .warning-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        padding: 8px 16px;
        background: linear-gradient(90deg, #1a0000, #3b0000);
        color: #ff6b6b;
        font-size: 0.75rem;
        text-align: center;
        border-top: 1px solid rgba(255, 0, 0, 0.5);
        z-index: 9999;
    }
    .chat-bubble-user {
        background: rgba(0, 153, 255, 0.2);
        padding: 8px 10px;
        border-radius: 10px;
        margin-bottom: 4px;
    }
    .chat-bubble-ai {
        background: rgba(0, 255, 153, 0.12);
        padding: 8px 10px;
        border-radius: 10px;
        margin-bottom: 8px;
        border: 1px solid rgba(0, 255, 153, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------ SAĞ ÜST BUTONLAR ------------------ #
st.markdown(
    """
    <div class="top-right-buttons">
        <a class="glow-button blue" href="#kayit-ol">Kayıt Ol</a>
        <a class="glow-button red" href="tel:112">ACİL</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------ BAŞLIK / LOGO ------------------ #
st.markdown(
    """
    <div class="logo-title">
        <div class="logo-circle">⚕️</div>
        <div>
            <h1 style="margin-bottom:2px;">AIHEALTH</h1>
            <p style="margin-top:0;font-size:0.9rem;opacity:0.8;">
                Yapay Zeka Destekli Sağlık Asistanı
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------ ACİL DURUM ------------------ #
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🚨 Acil Durum")
    st.write("Hayati risk durumunda **112’yi arayın**.")
    if st.button("📞 112’yi Ara"):
        st.markdown("[Telefonla 112’yi ara](tel:112)", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ YAPAY ZEKA SOHBET ------------------ #
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🤖 Yapay Zeka Sağlık Asistanı (Demo)")

    if "chat" not in st.session_state:
        st.session_state.chat = []

    user_msg = st.text_input("Şikayetini yaz (ör: başım ağrıyor)")

    def triage(msg):
        msg = msg.lower()
        if "nefes" in msg or "göğüs" in msg:
            return "Bu ciddi olabilir. Derhal 112’yi arayın."
        if "ateş" in msg:
            return "Ateş enfeksiyon belirtisi olabilir. Dinlen, sıvı al."
        if "baş" in msg:
            return "Baş ağrısı yaygındır. Işık-sesten uzak dur."
        return "Durumunu anladım. Gerekirse bir doktora başvur."

    if st.button("Asistanla Konuş"):
        if user_msg.strip():
            ai = triage(user_msg)
            st.session_state.chat.append(("Sen", user_msg))
            st.session_state.chat.append(("AIHEALTH", ai))

    for sender, msg in st.session_state.chat:
        bubble = "chat-bubble-user" if sender == "Sen" else "chat-bubble-ai"
        st.markdown(f"<div class='{bubble}'><strong>{sender}:</strong> {msg}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ FOTOĞRAF ÇEKME ------------------ #
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 📷 Yaralı Bölgenin Fotoğrafını Çek")
    img = st.camera_input("Fotoğraf çek")

    if img:
        st.success("Fotoğraf alındı. Yapay zeka analizi burada çalışacak.")
        st.write("Örnek analiz: Yüzeysel deri lezyonu benzeri bir görünüm tespit edildi.")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ KONUM TABANLI HASTANE & ECZANE ------------------ #
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 📍 En Yakın Hastane & Eczane")

    loc = geolocation()

    if loc:
        lat = loc["latitude"]
        lon = loc["longitude"]
        st.success(f"Konum alındı: {lat}, {lon}")

        hospital = f"https://www.google.com/maps/search/hospital/@{lat},{lon},15z"
        st.markdown(f"[🏥 En Yakın Hastaneler]({hospital})")

        hour = datetime.now().hour
        keyword = "nöbetçi eczane" if hour >= 19 else "eczane"
        pharmacy = f"https://www.google.com/maps/search/{keyword}/@{lat},{lon},15z"
        st.markdown(f"[💊 En Yakın Eczaneler]({pharmacy})")
    else:
        st.warning("Konum alınamadı. Lütfen izin verin.")

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ KAYIT OL ------------------ #
st.markdown('<div id="kayit-ol"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 📝 Kayıt Ol")

    ad = st.text_input("Ad Soyad")
    tel = st.text_input("Telefon")
    email = st.text_input("E-posta")

    if st.button("Kaydı Tamamla"):
        if ad and tel:
            st.success("Kayıt alındı. Teşekkürler.")
        else:
            st.warning("Ad ve telefon zorunludur.")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ HUKUKİ UYARI ------------------ #
st.markdown(
    """
    <div class="warning-footer">
      <strong>Hukuki Uyarı:</strong> AIHEALTH bir sağlık profesyoneli değildir. 
      Acil durumlarda 112’yi arayın. Tüm bilgiler bilgilendirme amaçlıdır.
    </div>
    """,
    unsafe_allow_html=True,
)
