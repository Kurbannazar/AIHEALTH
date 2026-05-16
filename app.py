import streamlit as st
from datetime import datetime
from io import BytesIO
import base64

# ------------------ GENEL AYARLAR ------------------ #
st.set_page_config(page_title="AIHEALTH", page_icon="💠", layout="centered")

# Özel tema (siyah + mavi glow)
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
    .top-right-buttons {
        position: fixed;
        top: 12px;
        right: 16px;
        z-index: 9999;
        display: flex;
        gap: 8px;
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
    .map-btn {
        margin-top: 6px;
        padding: 6px 10px;
        border-radius: 999px;
        border: 1px solid rgba(0, 153, 255, 0.4);
        background: radial-gradient(circle at top, #003b6f, #001322);
        color: #e0f4ff;
        cursor: pointer;
        font-size: 0.8rem;
        box-shadow: 0 0 10px rgba(0, 153, 255, 0.7);
    }
    .map-btn.red {
        border-color: rgba(255, 82, 82, 0.7);
        background: radial-gradient(circle at top, #5c0000, #1a0000);
        box-shadow: 0 0 12px rgba(255, 82, 82, 0.9);
    }
    .tel-link {
        color: #7dd3fc;
        text-decoration: none;
    }
    .tel-link:hover {
        text-decoration: underline;
        color: #e0f2fe;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sağ üst butonlar
st.markdown(
    """
    <div class="top-right-buttons">
        <a class="glow-button blue" href="#kayit-ol">Kayıt Ol</a>
        <a class="glow-button red" href="tel:112">ACİL</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------ BAŞLIK ------------------ #
st.markdown("<h1>AIHEALTH</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3>Akıllı Sağlık Asistanı · Kamera ve Konum Entegrasyonlu</h3>",
    unsafe_allow_html=True,
)

# ------------------ FOTOĞRAF ÇEK / GEMINI VISION ------------------ #
st.markdown("### Donanım Bazlı Fotoğraf Analizi")

with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.write(
        "Yaralı bölgenin fotoğrafını cihaz kamerası ile çekin. Görüntü, "
        "Gemini Vision benzeri bir yapay zeka analiz motoruna gönderilecek şekilde tasarlanmıştır."
    )

    img = st.camera_input("Yaralı bölgenin fotoğrafını çekin")

    def send_to_gemini_vision(image_bytes: bytes) -> str:
        """
        Burada gerçek Gemini Vision API entegrasyonu yapılmalıdır.
        Örnek akış:
        - image_bytes -> base64 encode
        - Google AI / Gemini Vision endpoint'ine POST isteği
        - Dönen JSON içinden özet / teşhis önerisi alınır
        """
        # --- ÖRNEK / MOCK CEVAP ---
        return (
            "Örnek analiz: Yüzeysel deri lezyonu benzeri bir görünüm tespit edildi. "
            "Gerçek teşhis için mutlaka hekim muayenesi gereklidir."
        )

    if img is not None:
        # Görüntüyü bytes olarak al
        bytes_data = img.getvalue()
        # (İsteğe bağlı) base64 gösterimi
        b64_preview = base64.b64encode(bytes_data).decode("utf-8")

        with st.spinner("Görüntü analiz ediliyor... (Gemini Vision entegrasyon noktası)"):
            analysis_result = send_to_gemini_vision(bytes_data)

        st.markdown("#### Yapay Zeka Analiz Sonucu")
        st.write(analysis_result)

        with st.expander("Teknik Detay (Base64 Örneği)"):
            st.code(b64_preview[:300] + "...", language="text")

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ KONUM / HASTANE & ECZANE ------------------ #
st.markdown("### Canlı Konum Entegrasyonu")

st.markdown(
    """
    <div class="section-card">
    <p>AIHEALTH, cihazınızın konum servislerini kullanarak en yakın sağlık merkezlerini bulmak üzere tasarlanmıştır.</p>
    """,
    unsafe_allow_html=True,
)

# JS ile navigator.geolocation kullanarak harita açan HTML/JS köprüsü
hospital_html = """
<div class="map-block">
  <strong>En Yakın Hastane</strong><br/>
  <small>Butona bastığınızda tarayıcı konum izni isteyebilir. Onayladığınızda, harita uygulaması mevcut konumunuzdan en yakın hastaneleri gösterecek şekilde açılır.</small><br/>
  <button class="map-btn" onclick="openNearestHospital()">En Yakın Hastaneyi Aç</button>
</div>

<script>
function openNearestHospital() {
    if (!navigator.geolocation) {
        alert("Konum servisi tarayıcı tarafından desteklenmiyor.");
        return;
    }
    navigator.geolocation.getCurrentPosition(function(pos) {
        var lat = pos.coords.latitude;
        var lon = pos.coords.longitude;
        // Google Maps: konuma göre 'hospital' araması
        var url = "https://www.google.com/maps/search/hospital/@"
                  + lat + "," + lon + ",15z";
        window.open(url, "_blank");
    }, function(err) {
        alert("Konum alınamadı. Lütfen tarayıcı konum iznini kontrol edin.");
    });
}
</script>
"""

st.components.v1.html(hospital_html, height=150)

# ECZANE / NÖBETÇİ ECZANE
now = datetime.now()
hour = now.hour

if hour >= 19:
    eczane_title = "En Yakın Nöbetçi Eczaneler"
    eczane_desc = (
        "Saat 19:00 sonrası olduğu için, konumunuza en yakın nöbetçi eczaneler "
        "listelenecek şekilde harita açılacaktır."
    )
    search_keyword = "n%C3%B6bet%C3%A7i+eczane"
else:
    eczane_title = "En Yakın Eczaneler"
    eczane_desc = (
        "Şu an 19:00 öncesi. Konumunuza en yakın eczaneler listelenecek şekilde harita açılacaktır."
    )
    search_keyword = "eczane"

eczane_html = f"""
<div class="map-block">
  <strong>{eczane_title}</strong><br/>
  <small>{eczane_desc}</small><br/>
  <button class="map-btn red" onclick="openNearestPharmacy()">Eczane Haritasını Aç</button>

  <div style="margin-top:8px;">
    <small style="opacity:0.8;">Örnek telefon arama linkleri (gerçek veriler için eczane API entegrasyonu eklenmelidir):</small><br/>
    <a class="tel-link" href="tel:+9002120000001">📞 Örnek Eczane 1</a><br/>
    <a class="tel-link" href="tel:+9002120000002">📞 Örnek Eczane 2</a>
  </div>
</div>

<script>
function openNearestPharmacy() {
    if (!navigator.geolocation) {
        alert("Konum servisi tarayıcı tarafından desteklenmiyor.");
        return;
    }
    navigator.geolocation.getCurrentPosition(function(pos) {
        var lat = pos.coords.latitude;
        var lon = pos.coords.longitude;
        // Google Maps: konuma göre eczane / nöbetçi eczane araması
        var url = "https://www.google.com/maps/search/{search_keyword}/@"
                  + lat + "," + lon + ",15z";
        window.open(url, "_blank");
    }, function(err) {
        alert("Konum alınamadı. Lütfen tarayıcı konum iznini kontrol edin.");
    });
}
</script>
"""

st.components.v1.html(eczane_html, height=210)

st.markdown("</div>", unsafe_allow_html=True)

# ------------------ KAYIT OL BÖLÜMÜ ------------------ #
st.markdown('<div id="kayit-ol"></div>', unsafe_allow_html=True)
st.markdown("### Kayıt Ol")

with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
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
        st.success("Kayıt talebiniz alındı. Bilgileriniz güvenli bir şekilde işlenmektedir.")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ HUKUKİ UYARI ------------------ #
st.markdown(
    """
    <div class="warning-footer">
      <strong>Hukuki Uyarı:</strong> AIHEALTH bir yapay zeka destekli sağlık asistanıdır; 
      acil durumlarda <strong>112 Acil Çağrı Merkezi</strong> ve en yakın sağlık kuruluşunun yerini <u>kesinlikle tutmaz</u>. 
      Tüm çıktılar bilgilendirme amaçlıdır, tıbbi tanı ve tedavi için mutlaka hekim görüşü gereklidir.
    </div>
    """,
    unsafe_allow_html=True,
)
