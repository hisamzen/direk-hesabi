import streamlit as st
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
try:
    import matplotlib.pyplot as plt
    PLOT_AVAILABLE = True
except ImportError:
    PLOT_AVAILABLE = False

st.set_page_config(page_title="Direk Tepe Kuvveti Hesaplayıcı v1.0", layout="centered")

# --- VERİ SETLERİ ---
AG_DATA = {
    "3R": {"1": 210.0, "2": 300.0, "3": 441.0, "4": 444.0},
    "4R": {"1": 280.0, "2": 400.0, "3": 588.0, "4": 592.0},
    "5R": {"1": 350.0, "2": 500.0, "3": 735.0, "4": 740.0},
    "3P+R/P": {"1": 490.0, "2": 654.0, "3": 899.0, "4": 908.0},
    "3Po+R/P": {"1": 535.0, "2": 695.0, "3": 968.0, "4": 956.0},
    "3A+R/P": {"1": 586.0, "2": 748.0, "3": 1025.0, "4": 1010.0},
    "3Ph+R/Po": {"1": 661.0, "2": 834.0, "3": 1135.0, "4": 1086.0},
    "3O+R/A": {"1": 713.0, "2": 923.0, "3": 1223.0, "4": 1167.0},
    "3x16/16+25 ALP": {"1": 201.8, "2": 236.84, "3": 306.0, "4": 302.2},
    "3x25/16+35 ALP": {"1": 250.0, "2": 272.9, "3": 345.8, "4": 335.7},
    "3x35/16+50 ALP": {"1": 301.3, "2": 327.1, "3": 410.6, "4": 388.9},
    "3x50/16+70 ALP": {"1": 371.24, "2": 383.9, "3": 477.86, "4": 440.7},
    "3x70/16+95 ALP": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4},
    "3x95/16+95 ALP": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4},
    "3x120/16+95 ALP": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4},
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
    "3x16+25 ALP": {"1": 201.8, "2": 236.84, "3": 306.0, "4": 302.2},
    "3x25+35 ALP": {"1": 250.0, "2": 272.9, "3": 345.8, "4": 335.7},
    "3x35+50 ALP": {"1": 301.3, "2": 327.1, "3": 410.6, "4": 388.9},
    "3x50+70 ALP": {"1": 371.24, "2": 383.9, "3": 477.86, "4": 440.7},
    "3x70+95 ALP": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4},
    "3x95+95 ALP": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4},
    "3x120+95 ALP": {"1": 460.8, "2": 469.4, "3": 573.9, "4": 512.4}
}

OG_DATA = {
    "3x3AWG": {"1": 273.0, "2": 381.0, "3": 525.0, "4": 525.0},
    "3x1/0 AWG": {"1": 411.0, "2": 525.0, "3": 705.0, "4": 678.0},
    "3x3/0 AWG": {"1": 513.0, "2": 662.0, "3": 870.0, "4": 810.0},
    "3x266 MCM": {"1": 660.0, "2": 854.0, "3": 1092.0, "4": 984.0},
    "3x477 MCM": {"1": 1014.0, "2": 1218.0, "3": 1500.0, "4": 1281.0}
}

if 'ag_cable_counts' not in st.session_state:
    st.session_state.ag_cable_counts = {}

st.title("⚡ Profesyonel Kablo Cer Hesaplayıcı")
st.markdown("---")

col_top1, col_top2 = st.columns(2)
with col_top1:
    hat_tipi = st.radio("Sistem Türü", ["AG Hat", "Müşterek Hat"], horizontal=True)
with col_top2:
    bolge = st.selectbox("Buz Yükü Bölgesi", ["1", "2", "3", "4"], index=1)

hat_sayisi = st.number_input("Toplam Hat Sayısı", min_value=1, max_value=10, value=1)
st.markdown("---")

total_rx, total_ry = 0.0, 0.0
results_data = []
cumulative_angle = 0 

for h in range(int(hat_sayisi)):
    st.subheader(f"📍 {h+1}. Hat Ayarları")
    if h not in st.session_state.ag_cable_counts: st.session_state.ag_cable_counts[h] = 1
    
    col_line1, col_line2 = st.columns([3, 1])
    cer_og, cer_ag = 0.0, 0.0
    
    with col_line1:
        if hat_tipi == "Müşterek Hat":
            og_s = st.selectbox(f"OG (Hat {h+1})", ["- YOK -"] + list(OG_DATA.keys()), key=f"og_{h}")
            if og_s != "- YOK -": cer_og = OG_DATA[og_s][bolge]
        
        for a in range(st.session_state.ag_cable_counts[h]):
            ag_s = st.selectbox(f"AG {a+1} (Hat {h+1})", ["- YOK -"] + list(AG_DATA.keys()), key=f"ag_{h}_{a}")
            if ag_s != "- YOK -": cer_ag += AG_DATA[ag_s][bolge]
        
        st.button(f"➕ AG Ekle (Hat {h+1})", key=f"btn_{h}", on_click=lambda idx=h: st.session_state.ag_cable_counts.update({idx: st.session_state.ag_cable_counts[idx]+1}))

    with col_line2:
        if h == 0:
            st.info("Referans Hat (0°)")
            input_aci = 0
        else:
            input_aci = st.number_input(f"Hat {h} ile {h+1} arasındaki açı (°)", 0, 360, 0, key=f"aci_{h}")
    
    cumulative_angle += input_aci
    # Başlangıç: Hat 1 her zaman 180 derecedir (-x yönü)
    math_angle = 180 + cumulative_angle
    rad = math.radians(math_angle)
    
    f_ag = cer_ag * 0.81 if (hat_tipi == "Müşterek Hat" and cer_og > 0 and cer_ag > 0) else cer_ag
    h_cer = cer_og + f_ag
    
    rx = h_cer * math.cos(rad)
    ry = h_cer * math.sin(rad)
    
    total_rx += rx
    total_ry += ry
    
    results_data.append({
        "Hat": h+1, 
        "Girdi_Açı": input_aci, 
        "Mutlak_Açı": math_angle, 
        "Cer": h_cer, 
        "Rx": rx, 
        "Ry": ry
    })
    st.markdown("---")

if st.button("HESAPLA", type="primary", use_container_width=True):
    v_r = math.sqrt(total_rx**2 + total_ry**2)
    s_t = abs(total_rx) + abs(total_ry)
    
    st.header("📊 Sonuçlar")
    c1, c2, c3 = st.columns(3)
    c1.metric("Vektörel Bileşke (R)", f"{v_r:.2f} kgf")
    c2.write(f"**ΣRx (Bileşen):** {total_rx:.2f}\n\n**ΣRy (Bileşen):** {total_ry:.2f}")
    c3.metric("Skaler Toplam", f"{s_t:.2f} kgf")

    if PLOT_AVAILABLE:
        fig, ax = plt.subplots(figsize=(10, 10), facecolor='white')
        
        # Görselleştirme için sabit uzunluk
        PLOT_MAG = 100 
        
        for i, d in enumerate(results_data):
            p_rad = math.radians(d["Mutlak_Açı"])
            p_rx = PLOT_MAG * math.cos(p_rad)
            p_ry = PLOT_MAG * math.sin(p_rad)
            
            # Vektörler
            ax.quiver(0, 0, p_rx, p_ry, angles='xy', scale_units='xy', scale=1, color='black', width=0.005)
            # Hat İsimleri
            ax.text(p_rx * 1.15, p_ry * 1.15, f"Hat {d['Hat']}", fontsize=12, fontweight='bold', ha='center', va='center')

        # TÜM AÇILARI YAYLARLA VE ETİKETLERLE ÇİZ
        for i in range(len(results_data) - 1):
            h_start = results_data[i]
            h_end = results_data[i+1]
            sapma = h_end["Girdi_Açı"]
            
            if sapma != 0:
                # Yay yarıçapı kademeli olarak artar
                arc_radius = (i + 1) * (PLOT_MAG * 0.25)
                
                # Arc çizimi
                arc = Arc((0, 0), arc_radius*2, arc_radius*2, angle=0, 
                          theta1=h_start["Mutlak_Açı"], 
                          theta2=h_end["Mutlak_Açı"], 
                          color='red', linewidth=1.5, linestyle='--')
                ax.add_patch(arc)
                
                # Açı Yazısı (Yayın tam ortasına ve biraz dışına)
                text_angle_deg = h_start["Mutlak_Açı"] + (sapma / 2)
                text_angle_rad = math.radians(text_angle_deg)
                
                # Yazıyı yayın biraz dışına yerleştirmek için yarıçapı %20 artırıyoruz
                tx = arc_radius * 1.2 * math.cos(text_angle_rad)
                ty = arc_radius * 1.2 * math.sin(text_angle_rad)
                
                ax.text(tx, ty, f"{sapma}°", color='red', fontweight='bold', fontsize=11, 
                        ha='center', va='center', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1))

        ax.set_axis_off()
        lim = PLOT_MAG * 2.0
        ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim)
        st.pyplot(fig)
    
    st.subheader("📝 Hat Detayları")
    st.table([{"Hat": d["Hat"], "Sapma Açısı (°)": d["Girdi_Açı"], "Cer (kgf)": f"{d['Cer']:.2f}"} for d in results_data])

st.markdown("<p style='text-align: center;'>Hazırlayan: Hişam Zengin Elk. Müh.</p>", unsafe_allow_html=True)