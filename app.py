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
    .glow-button.blue:hover {
        box-shadow: 0 0 20px rgba(0, 198, 255, 1);
        transform: translateY(-1px);
    }
    .glow-button.red {
        background: linear-gradient(135deg, #ff1744, #ff5252);
        color: #ffffff;
        box-shadow: 0 0 16px rgba(255, 23, 68, 0.9);
    }
    .glow-button.red:hover {
        box-shadow: 0 0 24px rgba(255, 82, 82, 1);
        transform: translateY(-1px);
    }
    .section-card {
        background: radial-gradient(circle at top left, rgba(0, 153, 255, 0.12), rgba(0,0,0,0.9));
        border-radius: 18px;
        padding: 18px 18px 14px 18px;
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
    .warning-footer strong {
        color: #ffb3b3;
    }
    .map-block {
        margin-top: 8px;
        padding: 10px 12px;
        border-radius: 12px;
        background: rgba(0, 0, 0, 0.55);
        border: 1px solid rgba(0, 153, 255, 0.3);
        font-size: 0.85rem;
    }
    .tel-link {
        color: #7dd3fc;
        text-decoration: none;
    }
    .tel-link:hover {
        text-decoration: underline;
        color: #e0f2fe;
    }
    .chat-bubble-user {
        background: rgba(0, 153, 255, 0.2);
        padding: 8px 10px;
        border-radius: 10px;
        margin-bottom: 4px;
        font-size: 0.9rem;
    }
    .chat-bubble-ai {
        background: rgba(0, 255, 153, 0.12);
        padding: 8px 10px;
        border-radius: 10px;
        margin-bottom: 8px;
        font-size: 0.9rem;
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

st.markdown(
    "<h3>ACİL DURUM · YAPAY ZEKA SOHBET · KONUM TABANLI HASTANE & ECZANE</h3>",
    unsafe_allow_html=True,
)

# ------------------ ACİL DURUM BÖLÜMÜ ------------------ #
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🚨 Acil Durum")
    st.write(
        "Hayati risk, göğüs ağrısı, nefes darlığı, bilinç kaybı, ağır travma gibi durumlarda "
        "**beklemeden 112 Acil Çağrı Merkezi’ni arayın.**"
    )
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        if st.button("📞 112’yi Ara", type="primary"):
            st.markdown("[Telefonla 112’yi ara](tel:112)", unsafe_allow_html=True)
            st.info("Telefonunuzdan 112’yi arayabilirsiniz.")
    with col_a2:
        st.write("Konumunuza göre en yakın acil servis için aşağıdaki harita bölümünü kullanın.")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ YAPAY ZEKA SOHBET (GEMINI ENTEGRASYON NOKTASI) ------------------ #
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markmarkdown("### 🤖 Yapay Zeka Sağlık Asistanı (Demo)")

    st.write(
        "Bu bölüm, arka planda **Gemini** veya benzeri bir büyük dil modeli ile entegre olacak şekilde "
        "tasarlanmıştır. Şu an örnek bir kural tabanlı cevaplayıcı çalışıyor."
    )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_msg = st.text_input("Şikayetini veya sorununu yaz (ör: başım ağrıyor, ateşim var vb.)")

    def simple_triage_answer(text: str) -> str:
        t = text.lower()
        if any(k in t for k in ["göğüs", "nefes", "zor nefes", "kalp", "baygın"]):
            return (
                "Bu tarif, potansiyel olarak **hayati risk** içerebilir. "
                "Derhal 112’yi araman veya en yakın acil servise başvurman gerekir."
            )
        if any(k in t for k in ["ateş", "üşüme", "titreme"]):
            return (
                "Ateş ve enfeksiyon bulguları olabilir. Bol sıvı al, dinlen; "
                "durumun kötüleşirse aile hekimi veya acil servise başvur."
            )
        if any(k in t for k in ["başım ağrıyor", "baş ağrısı", "migren"]):
            return (
                "Baş ağrısı birçok nedene bağlı olabilir. Işık ve sesten uzak dur, "
                "gerekirse basit ağrı kesici kullan; ani, çok şiddetli ve farklı bir ağrıysa acile git."
            )
        return (
            "Şikayetini anladım. Bu uygulama tıbbi tanı koyamaz; "
            "durumun seni endişelendiriyorsa bir hekime başvurman en doğrusudur."
        )

    if st.button("Asistanla Konuş (Demo)"):
        if user_msg.strip():
            ai_answer = simple_triage_answer(user_msg)
            st.session_state.chat_history.append(("Kullanıcı", user_msg))
            st.session_state.chat_history.append(("AIHEALTH", ai_answer))
        else:
            st.warning("Lütfen önce bir mesaj yaz.")

    for sender, msg in st.session_state.chat_history:
        if sender == "Kullanıcı":
            st.markdown(f"<div class='chat-bubble-user'><strong>Sen:</strong> {msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-bubble-ai'><strong>AIHEALTH:</strong> {msg}</div>", unsafe_allow_html=True)

    st.info(
        "Not: Buradaki mantık örnektir. Gerçek sistemde bu kısım Gemini API veya benzeri bir modele bağlanacaktır."
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ FOTOĞRAF ÇEKME / YARA ANALİZİ MOCK ------------------ #
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 📷 Yaralı Bölgenin Fotoğrafını Çek")

    st.write(
        "Yaralı veya hasar görmüş bölgenin fotoğrafını çekerek, ileride **Gemini Vision** gibi "
        "görsel yapay zeka modellerine gönderilecek bir akış tasarlanmıştır."
    )

    img = st.camera_input("Yaralı bölgenin fotoğrafını çek")

    def mock_vision_analysis(image_bytes: bytes) -> str:
        # Buraya gerçek Gemini Vision entegrasyonu eklenecek.
        return (
            "Örnek analiz: Yüzeysel deri lezyonu benzeri bir görünüm tespit edildi. "
            "Gerçek tanı için mutlaka hekim muayenesi gereklidir."
        )

    if img is not None:
        bytes_data = img.getvalue()
        with st.spinner("Görüntü analiz ediliyor... (Gemini Vision entegrasyon noktası)"):
            result = mock_vision_analysis(bytes_data)
        st.markdown("#### Yapay Zeka Analiz Sonucu")
        st.write(result)
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ KONUM TABANLI HASTANE & ECZANE ------------------ #
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 📍 Konum Tabanlı Hastane ve Eczane Bul")

    st.write(
        "Cihaz konumunu kullanarak en yakın hastane ve eczaneleri harita üzerinde açmak için aşağıdaki "
        "konum alma butonunu kullanın."
    )

    loc = geolocation()

    if loc:
        lat = loc["latitude"]
        lon = loc["longitude"]
        st.success(f"Konum alındı: {lat:.5f}, {lon:.5f}")

        now = datetime.now()
        hour = now.hour

        # Hastane
        hospital_url = f"https://www.google.com/maps/search/hospital/@{lat},{lon},15z"
        st.markdown(
            f"<div class='map-block'><strong>En Yakın Hastaneler</strong><br/>"
            f"<a href='{hospital_url}' target='_blank'>🧭 Haritada Hastaneleri Aç</a></div>",
            unsafe_allow_html=True,
        )

        # Eczane / Nöbetçi eczane
        if hour >= 19 or hour < 8:
            eczane_title = "En Yakın Nöbetçi Eczaneler"
            keyword = "n%C3%B6bet%C3%A7i+eczane"
        else:
            eczane_title = "En Yakın Eczaneler"
            keyword = "eczane"

        pharmacy_url = f"https://www.google.com/maps/search/{keyword}/@{lat},{lon},15z"

        st.markdown(
            f"<div class='map-block'><strong>{eczane_title}</strong><br/>"
            f"<a href='{pharmacy_url}' target='_blank'>💊 Haritada Eczaneleri Aç</a><br/>"
            f"<small style='opacity:0.8;'>Gerçek telefon ve adres bilgileri için harita üzerindeki "
            f"eczane kartlarını kullanın.</small></div>",
            unsafe_allow_html=True,
        )
    else:
        st.warning("Konum alınamadı. Lütfen tarayıcıdan konum izni verin.")

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ KAYIT OL BÖLÜMÜ ------------------ #
st.markdown('<div id="kayit-ol"></div>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 📝 Kayıt Ol")

    col1, col2 = st.columns(2)
    with col1:
        ad = st.text_input("Ad Soyad")
        tc = st.text_input("T.C. / Kimlik Numarası")
        tel = st.text_input("Telefon Numarası")
    with col2:
        email = st.text_input("E-posta")
        yas = st.number_input("Yaş", min_value=0, max_value=120, step=1)
        kronik = st.text_area("Kronik Hastalık / Düzenli İlaç Bilgisi", height=80)

    if st.button("Kaydımı Tamamla", type="primary"):
        if ad and tel:
            st.success(
                "Kayıt talebiniz alındı. Bu demo sürümde veriler kalıcı olarak saklanmamaktadır; "
                "gerçek sistemde güvenli sunucu altyapısı ile işlenecektir."
            )
        else:
            st.warning("Lütfen en az Ad Soyad ve Telefon alanlarını doldurun.")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ HUKUKİ UYARI ------------------ #
st.markdown(
    """
    <div class="warning-footer">
      <strong>Hukuki Uyarı:</strong> AIHEALTH, yapay zeka destekli bir sağlık asistanı prototipidir. 
      Acil durumlarda <strong>112 Acil Çağrı Merkezi</strong> ve en yakın sağlık kuruluşunun yerini <u>kesinlikle tutmaz</u>. 
      Buradaki tüm bilgiler yalnızca bilgilendirme amaçlıdır; tıbbi tanı ve tedavi için mutlaka hekim değerlendirmesi gereklidir.
    </div>
    """,
    unsafe_allow_html=True,
)
