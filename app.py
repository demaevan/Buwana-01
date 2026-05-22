import streamlit as st
import google.generativeai as genai
import googlemaps
import folium
from streamlit_folium import st_folium

# 1. UI/UX PREDATOR MODE (Dark & Gold)
st.set_page_config(page_title="Buwana Karya AI | Radar Lahan", page_icon="🎯", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #FFFFFF; }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; font-family: 'Helvetica Neue', sans-serif;}
    .stTextInput>div>div>input { background-color: #2C2C2C; color: #D4AF37; border: 1px solid #D4AF37; }
    .stButton>button { background-color: #D4AF37; color: #121212; font-weight: bold; border-radius: 5px; width: 100%; }
    .stButton>button:hover { background-color: #B8860B; color: #FFFFFF; }
    .metric-card { background-color: #1E1E1E; padding: 20px; border-radius: 10px; border-left: 5px solid #D4AF37; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("🎯 BUWANA KARYA: RADAR LAHAN")
st.markdown("### Sistem Intelijen & Akuisisi Proyek Kost")
st.divider()

# 2. BRANKAS KUNCI API
col_key1, col_key2 = st.columns(2)
with col_key1:
    gmaps_api = st.text_input("🔑 Google Maps API Key:", type="password")
with col_key2:
    gemini_api = st.text_input("🧠 Gemini API Key:", type="password")

st.markdown("---")

# 3. INPUT KOORDINAT SATELIT
st.markdown("<h4 style='text-align: center; color: #FFF;'>Masukkan Titik Kordinat Lahan Target</h4>", unsafe_allow_html=True)
col_lat, col_lng = st.columns(2)
with col_lat:
    lat = st.text_input("Latitude (Lat):", placeholder="Contoh: -7.558123")
with col_lng:
    lng = st.text_input("Longitude (Lng):", placeholder="Contoh: 110.768654")

# 4. MESIN EKSEKUSI
if st.button("🚀 SCAN LAHAN & RANCANG CETAK BIRU BISNIS"):
    if not gmaps_api or not gemini_api or not lat or not lng:
        st.error("Bongkar brankas dulu! Masukkan semua API Key dan Kordinat Lahan.")
    else:
        try:
            # Inisialisasi Kunci
            gmaps = googlemaps.Client(key=gmaps_api)
            genai.configure(api_key=gemini_api)
            target_location = (float(lat), float(lng))
            
            with st.spinner("🛰️ Menyedot data satelit... Meretas demografi area..."):
                # SCRAPING DATA AREA (Radius 2 KM)
                radius = 2000 
                kompetitor = gmaps.places_nearby(location=target_location, radius=radius, keyword='kost OR homestay')
                kampus = gmaps.places_nearby(location=target_location, radius=radius, keyword='universitas OR kampus')
                pabrik = gmaps.places_nearby(location=target_location, radius=radius, keyword='pabrik OR industri')
                minimarket = gmaps.places_nearby(location=target_location, radius=radius, type='convenience_store')
                
                jml_kompetitor = len(kompetitor.get('results', []))
                jml_kampus = len(kampus.get('results', []))
                jml_pabrik = len(pabrik.get('results', []))
                jml_minimarket = len(minimarket.get('results', []))

                # VISUALISASI DASHBOARD
                st.markdown("### 📊 STATUS TERITORI (Radius 2 KM)")
                col1, col2, col3, col4 = st.columns(4)
                col1.markdown(f"<div class='metric-card'>🏢 Kompetitor (Kost): <h2>{jml_kompetitor}</h2></div>", unsafe_allow_html=True)
                col2.markdown(f"<div class='metric-card'>🎓 Magnet Kampus: <h2>{jml_kampus}</h2></div>", unsafe_allow_html=True)
                col3.markdown(f"<div class='metric-card'>⚙️ Magnet Industri: <h2>{jml_pabrik}</h2></div>", unsafe_allow_html=True)
                col4.markdown(f"<div class='metric-card'>🛒 Minimarket: <h2>{jml_minimarket}</h2></div>", unsafe_allow_html=True)
                
                # VISUALISASI PETA INTERAKTIF
                st.markdown("### 🗺️ PETA AKUISISI LAHAN")
                m = folium.Map(location=[float(lat), float(lng)], zoom_start=15, tiles="CartoDB dark_matter")
                folium.Marker([float(lat), float(lng)], popup="LAHAN TARGET BUWANA", icon=folium.Icon(color='red', icon='star')).add_to(m)
                
                # Plot kompetitor di peta
                for place in kompetitor.get('results', [])[:10]: # Tampilkan max 10 kompetitor terdekat
                    p_lat = place['geometry']['location']['lat']
                    p_lng = place['geometry']['location']['lng']
                    folium.CircleMarker([p_lat, p_lng], radius=5, color='orange', fill=True, popup=place.get('name')).add_to(m)
                
                st_folium(m, width=1200, height=400)

                # AKTIVASI OTAK ANALIS BISNIS (GEMINI)
                st.markdown("### 📑 CETAK BIRU EKSEKUSI BUWANA KARYA")
                
                # Auto-bypass model
                valid_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                target_model = next((m for m in valid_models if '1.5-flash' in m), valid_models[0])
                model = genai.GenerativeModel(target_model)
                
                prompt = f"""
                Kamu adalah analis properti dan perencana bisnis elit dari 'Buwana Karya'.
                Ini adalah data scraping Google Maps dari lahan target klien:
                - Koordinat: {lat}, {lng}
                - Kompetitor terdeteksi: {jml_kompetitor} kost
                - Universitas terdekat: {jml_kampus}
                - Kawasan Industri/Kantor: {jml_pabrik}
                - Akses minimarket: {jml_minimarket}
                
                Buat cetak biru bisnis yang TACTICAL, MENDALAM, dan REALISTIS dengan bahasa Indonesia yang tegas, analitis, dan profesional. Pisahkan dalam struktur berikut:
                
                **1. TARGET MARKET & DEMOGRAFI (Berdasarkan dominasi kampus/pabrik)**
                Jelaskan segmentasi secara psikografi, behavior, umur, dan tentukan HARGA JUAL/SEWA yang paling optimal untuk membunuh saingan.
                
                **2. ANALISA GEOGRAFI & TANTANGAN KONSTRUKSI**
                Bahas potensi masalah pembangunan di lahan ini (logistik, sempadan, kontur) dan solusi Dema sebagai perencana fisik.
                
                **3. MITIGASI RISIKO OPERASIONAL**
                Apa masalah yang pasti terjadi saat kost berjalan dan apa SOP/sistem yang harus dipasang sejak awal.
                
                **4. STRATEGI MARKETING BUWANA (The Mona Protocol)**
                Bagaimana Mona akan menarik penghuni pertama. Bahas teknik presale, garansi okupansi, dan pembajakan penyewa dari kompetitor.
                
                Tulis dalam format Markdown tanpa basa-basi intro. Ini adalah dokumen resmi Buwana Karya.
                """
                
                with st.spinner("Mencetak strategi akuisisi..."):
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                    
        except Exception as e:
            st.error(f"Sistem gagal mengeksekusi: {e}\nPastikan API Key Google Maps memiliki akses ke 'Places API'.")
