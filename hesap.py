import streamlit as st

st.set_page_config(page_title="Kablo Cer Hesaplayıcı v1.0", layout="centered")

# --- VERİ SETLERİ ---
AG_DATA = {
    "ROSE": {"1": 70.0, "2": 100.0, "3": 147.0, "4": 148.0},
    "PANSY": {"1": 105.0, "2": 139.0, "3": 188.0, "4": 190.0},
    "POPPY": {"1": 120.0, "2": 150.0, "3": 211.0, "4": 206.0},
    "ASTER": {"1": 137.0, "2": 170.0, "3": 230.0, "4": 224.0},
    "PHLOX": {"1": 157.0, "2": 194.0, "3": 259.0, "4": 244.0},
    "OXLİP": {"1": 169.0, "2": 218.0, "3": 282.0, "4": 265.0},	
    "1x16+16 ALP": {"1": 100.9, "2": 118.42, "3": 153.0, "4": 151.1},
"1x16+35 ALP": {"1": 100.9, "2": 118.42, "3": 153.0, "4": 151.1},
"1x16+50 ALP": {"1": 100.9, "2": 118.42, "3": 153.0, "4": 151.1},
"1x16+70 ALP": {"1": 100.9, "2": 118.42, "3": 153.0, "4": 151.1},
"1x16+95 ALP": {"1": 100.9, "2": 118.42, "3": 153.0, "4": 151.1},
"1x10+16 ALP": {"1": 80.0, "2": 100.0, "3": 120.0, "4": 120.0},
"1x16+25 ALP": {"1": 100.9, "2": 118.42, "3": 153.0, "4": 151.1},
"1x25+35 ALP": {"1": 125.0, "2": 136.45, "3": 172.9, "4": 167.85},
"1x35+50 ALP": {"1": 150.65, "2": 163.55, "3": 205.3, "4": 194.45},
"1x50+70 ALP": {"1": 185.62, "2": 191.95, "3": 238.93, "4": 220.35},
"1x70+95 ALP": {"1": 230.4, "2": 234.7, "3": 286.95, "4": 256.2},
"1x10/16+16 ALP": {"1": 80.0, "2": 100.0, "3": 120.0, "4": 120.0},
"1x16/16+25 ALP": {"1": 100.9, "2": 118.42, "3": 153.0, "4": 151.1},
"1x25/16+35 ALP": {"1": 125.0, "2": 136.45, "3": 172.9, "4": 167.85},
"1x35/16+50 ALP": {"1": 150.65, "2": 163.55, "3": 205.3, "4": 194.45},
"1x50/16+70 ALP": {"1": 185.62, "2": 191.95, "3": 238.93, "4": 220.35},
"1x70/16+95 ALP": {"1": 230.4, "2": 234.7, "3": 286.95, "4": 256.2},
"2x10 ALP": {"1": 55.0, "2": 69.0, "3": 91.0, "4": 87.0},
"2x16 ALP": {"1": 67.0, "2": 79.0, "3": 102.0, "4": 101.0},
"3x16+25 ALP": {"1": 201.8, "2": 236.84, "3": 306.0, "4": 302.2},
"3x25+35 ALP": {"1": 250.0, "2": 272.9, "3": 345.8, "4": 335.7},
"3x35+50 ALP": {"1": 301.3, "2": 327.1, "3": 410.6, "4": 388.9},
"3x50+70 ALP": {"1": 371.24, "2": 383.9, "3": 477.86, "4": 440.7},
"3x70+95 ALP": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4},
"3x95+95 ALP": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4},
"3x120+95 ALP": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4},
"3x16/16+25 ALP": {"1": 201.8, "2": 236.84, "3": 306.0, "4": 302.2},
"3x25/16+35 ALP": {"1": 250.0, "2": 272.9, "3": 345.8, "4": 335.7},
"3x35/16+50 ALP": {"1": 301.3, "2": 327.1, "3": 410.6, "4": 388.9},
"3x50/16+70 ALP": {"1": 371.24, "2": 383.9, "3": 477.86, "4": 440.7},
"3x70/16+95 ALP": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4},
"3x95/16+95 ALP": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4},
"3x120/16+95 ALP": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4},
"3x10 ALP": {"1": 165.4, "2": 205.55, "3": 270.8, "4": 268.0},
"3x16/25+25 ALP": {"1": 211.8, "2": 248.6, "3": 321.3, "4": 317.3},
"3x25/25+35 ALP": {"1": 262.5, "2": 286.5, "3": 363.1, "4": 352.4},
"3x35/25+50 ALP": {"1": 316.3, "2": 343.4, "3": 431.1, "4": 408.3},
"3x50/25+70 ALP": {"1": 389.8, "2": 403.1, "3": 501.7, "4": 462.7},
"3x70/25+95 ALP": {"1": 483.8, "2": 492.8, "3": 602.5, "4": 538.1},
"3x95/25+95 ALP": {"1": 483.8, "2": 492.8, "3": 602.5, "4": 538.1},
"3x120/25+95 ALP": {"1": 483.8, "2": 492.8, "3": 602.5, "4": 538.1},
"3x16/35+25 ALP": {"1": 222.4, "2": 261.1, "3": 337.3, "4": 333.1},
"3x25/35+35 ALP": {"1": 275.6, "2": 300.8, "3": 381.2, "4": 370.1},
"3x35/35+50 ALP": {"1": 332.1, "2": 360.6, "3": 452.6, "4": 428.7},
"3x50/35+70 ALP": {"1": 409.2, "2": 423.2, "3": 526.8, "4": 485.8},
"3x70/35+95 ALP": {"1": 508.1, "2": 517.5, "3": 632.7, "4": 564.9},
"3x95/35+95 ALP": {"1": 508.1, "2": 517.5, "3": 632.7, "4": 564.9},
"3x120/35+95 ALP": {"1": 508.1, "2": 517.5, "3": 632.7, "4": 564.9},
"3x16/50+25 ALP": {"1": 233.6, "2": 274.1, "3": 354.2, "4": 349.8},
"3x25/50+35 ALP": {"1": 289.4, "2": 315.9, "3": 400.3, "4": 388.6},
"3x35/50+50 ALP": {"1": 348.7, "2": 378.6, "3": 475.3, "4": 450.2},
"3x50/50+70 ALP": {"1": 429.7, "2": 444.4, "3": 553.1, "4": 510.1},
"3x70/50+95 ALP": {"1": 533.4, "2": 543.3, "3": 664.3, "4": 593.1},
"3x95/50+95 ALP": {"1": 533.4, "2": 543.3, "3": 664.3, "4": 593.1},
"3x120/50+95 ALP": {"1": 533.4, "2": 543.3, "3": 664.3, "4": 593.1}
    
}

OG_DATA = {
    "3AWG": {"1": 91.0, "2": 127.0, "3": 175.0, "4": 175.0},
    "1/0 AWG": {"1": 137.0, "2": 175.0, "3": 235.0, "4": 226.0},
    "3/0 AWG": {"1": 171.0, "2": 220.73, "3": 290.0, "4": 270.0},
    "266 MCM": {"1": 220.0, "2": 284.5, "3": 364.0, "4": 328.0},
    "477 MCM": {"1": 338.0, "2": 406.13, "3": 500.0, "4": 427.0}
}

# --- SESSION STATE (Dinamik Liste Yönetimi) ---
if 'ag_rows' not in st.session_state:
    st.session_state.ag_rows = [{"kablo": "- YOK -", "adet": 0}]

def add_ag_row():
    st.session_state.ag_rows.append({"kablo": "- YOK -", "adet": 0})

def clear_all():
    st.session_state.ag_rows = [{"kablo": "- YOK -", "adet": 0}]
    st.rerun()

# --- ARAYÜZ ---
st.title("⚡ Kablo Cer Hesaplayıcı")
st.markdown("---")

bolge = st.selectbox("Buz Yükü Bölgesi", ["1", "2", "3", "4"], index=1)

# OG Bölümü
st.subheader("🔹 OG (Orta Gerilim)")
col_og1, col_og2 = st.columns([3, 1])
with col_og1:
    og_secim = st.selectbox("OG İletkeni", ["- YOK -"] + list(OG_DATA.keys()))
with col_og2:
    og_adet = st.number_input("OG Adet", min_value=0, value=0, key="og_count")

st.markdown("---")

# AG Bölümü (Dinamik)
st.subheader("🔸 AG (Alçak Gerilim) Listesi")
ag_toplam_cer = 0

for i, row in enumerate(st.session_state.ag_rows):
    c1, c2 = st.columns([3, 1])
    with c1:
        st.session_state.ag_rows[i]["kablo"] = st.selectbox(f"AG İletkeni {i+1}", ["- YOK -"] + list(AG_DATA.keys()), key=f"ag_k_{i}")
    with c2:
        st.session_state.ag_rows[i]["adet"] = st.number_input(f"Adet {i+1}", min_value=0, value=row["adet"], key=f"ag_a_{i}")

col_btn1, col_btn2 = st.columns(2)
with col_btn1:
    st.button("➕ Yeni AG Kablo Ekle", on_click=add_ag_row, use_container_width=True)
with col_btn2:
    st.button("🗑️ Tümünü Temizle", on_click=clear_all, use_container_width=True)

st.markdown("---")

# --- HESAPLAMA ---
if st.button("HESAPLA", type="primary", use_container_width=True):
    og_toplam = 0
    ag_ham_toplam = 0
    
    # OG Hesapla
    if og_secim != "- YOK -" and og_adet > 0:
        og_toplam = OG_DATA[og_secim][bolge] * og_adet
        
    # AG Hesapla (Tüm satırları topla)
    for row in st.session_state.ag_rows:
        if row["kablo"] != "- YOK -" and row["adet"] > 0:
            ag_ham_toplam += AG_DATA[row["kablo"]][bolge] * row["adet"]
    
    # Müşterek Hat Zayıflatma
    katsayi = 1.0
    if og_toplam > 0 and ag_ham_toplam > 0:
        katsayi = 0.81
        ag_final_cer = ag_ham_toplam * katsayi
        st.warning("⚠️ Müşterek hat: Tüm AG kablolarının toplamına 0.81 zayıflatma uygulandı.")
    else:
        ag_final_cer = ag_ham_toplam

    toplam_Pt = og_toplam + ag_final_cer
    
    # SONUÇLAR
    st.success(f"### Toplam Tepe Kuvveti ($P_t$): {toplam_Pt:.2f} kgf")
    
    st.table({
        "Bileşen": ["OG Toplam", "AG Toplam (Zayıflatılmış)", "GENEL TOPLAM"],
        "Kuvvet (kgf)": [f"{og_toplam:.2f}", f"{ag_final_cer:.2f}", f"{toplam_Pt:.2f}"]
    })
st.markdown("<p style='text-align: center;'>Hazırlayan: Hişam Zengin Elk. Müh.</p>", unsafe_allow_html=True)