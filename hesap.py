import streamlit as st

# Sayfa yapılandırması
st.set_page_config(page_title="Direk Tepe Kuvveti v3", layout="centered")

# CSS ile buton ve tasarım özelleştirme
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Başlık ve Alt Başlıklar
st.title("⚡ Direk Tepe Kuvveti Hesaplayıcı")
st.subheader("Güncel TEDAŞ Cer Cetveli Verileriyle")
st.markdown("##### Hazırlayan: &nbsp;&nbsp;**Hişam Zengin**")
st.markdown("##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Elektrik Müh.")
st.markdown("---")

# TÜM ALPEK LİSTESİ
alpek_verileri = {
    "1x16+16 ALP.": {"1": 100.9, "2": 118.42, "3": 153.0, "4": 151.1},
    "1x10+16 ALP.": {"1": 80.0, "2": 100.0, "3": 120.0, "4": 120.0},
    "1x25+35 ALP.": {"1": 125.0, "2": 136.45, "3": 172.9, "4": 167.85},
    "1x35+50 ALP.": {"1": 150.65, "2": 163.55, "3": 205.3, "4": 194.45}, 
    "1x50+70 ALP.": {"1": 185.62, "2": 191.95, "3": 238.93, "4": 220.35},
    "1x70+95 ALP.": {"1": 230.4, "2": 234.7, "3": 286.95, "4": 256.2},
    "2x10 ALP.": {"1": 55.0, "2": 69.0, "3": 91.0, "4": 87.0},
    "2x16 ALP.": {"1": 67.0, "2": 79.0, "3": 102.0, "4": 101.0},
    "3x10 ALP.": {"1": 165.4, "2": 205.55, "3": 270.8, "4": 268.0},
    "3x16+25 ALP.": {"1": 201.8, "2": 236.84, "3": 306.0, "4": 302.2},
    "3x25+35 ALP.": {"1": 250.0, "2": 272.9, "3": 345.8, "4": 335.7},
    "3x35+50 ALP.": {"1": 301.3, "2": 327.1, "3": 410.6, "4": 388.9},
    "3x50+70 ALP.": {"1": 371.24, "2": 383.9, "3": 477.86, "4": 440.7},
    "3x70+95 ALP.": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4},
    "3x95+95 ALP.": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4},
    "3x120+95 ALP.": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4},
    "3x50/50+70 ALP.": {"1": 429.7, "2": 444.4, "3": 553.1, "4": 510.1},
    "3x70/50+95 ALP.": {"1": 533.4, "2": 543.3, "3": 664.3, "4": 593.1},
    "3x95/50+95 ALP.": {"1": 533.4, "2": 543.3, "3": 664.3, "4": 593.1},
    "3x120/50+95 ALP.": {"1": 533.4, "2": 543.3, "3": 664.3, "4": 593.1}
}

# Giriş Bölümü
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        kesit = st.selectbox("İletken Kesiti", list(alpek_verileri.keys()))
        bolge = st.radio("Buz Yükü Bölgesi", ["1", "2", "3", "4"], horizontal=True)
    with col2:
        hat_sayisi = st.number_input("Bağlı Hat Sayısı", min_value=1, max_value=10, value=1)
        st.write("") # Boşluk
        clear = st.button("TEMİZLE")

if clear:
    st.rerun()

st.markdown("---")

# Hesapla
if st.button("HESAPLA"):
    cer_degeri = alpek_verileri[kesit][bolge]
    toplam_tepe = cer_degeri * hat_sayisi
    
    st.success(f"### Hesaplanan Toplam Tepe Kuvveti: {toplam_tepe:.2f} kgf")
    
    # Detay Kartı
    st.info(f"""
    **Seçim Detayları:**
    - Kesit: {kesit}
    - Bölge: {bolge}. Bölge
    - Birim Cer: {cer_degeri} kgf
    - Toplam Hat: {hat_sayisi} Adet
    """)