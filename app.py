import streamlit as st
import google.generativeai as genai

# 1. SETUP TAMPILAN
st.set_page_config(page_title="Buwana Karya AI", page_icon="🏢", layout="centered")
st.markdown("<h1 style='text-align: center; color: #b8860b;'>🛡️ BUWANA KARYA</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Mesin Intelijen Kelayakan Aset Warisan</h4>", unsafe_allow_html=True)
st.divider()

# 2. INPUT KUNCI MASTER
api_key = st.text_input("🔑 Masukkan Kode Otorisasi (API Key):", type="password")

# 3. FORM SURVEI LAPANGAN
st.subheader("📡 Radar Lapangan")
magnet = st.text_input("1. Jarak ke Magnet Area:", placeholder="Cth: 800m dari pintu belakang UMS")
luas_harga = st.text_input("2. Dimensi Lahan & Estimasi Harga:", placeholder="Cth: 100m2, total 1.2 Miliar")
jalan = st.text_input("3. Kondisi Akses & Logistik:", placeholder="Cth: Lebar 6 meter, gang")
kompetitor = st.text_input("4. Titik Lemah Kompetitor Sekitar:", placeholder="Cth: Kos pengap, jadul")

st.divider()

# 4. TOMBOL EKSEKUSI DENGAN AUTO-BYPASS
if st.button("🔥 GENERATE DOKUMEN EKSEKUSI", use_container_width=True):
    if not api_key:
        st.error("Masukkan Kode Otorisasi dulu sebelum mengeksekusi lahan!")
    elif not magnet or not luas_harga:
        st.warning("Data lahan belum lengkap. Isi radar lapangan!")
    else:
        try:
            # Autentikasi
            genai.configure(api_key=api_key)
            
            # TAKTIK BYPASS: Hack daftar model otomatis
            valid_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            
            if not valid_models:
                st.error("API Key lu valid, tapi Google memblokir akses model. Bikin API Key baru!")
            else:
                # Ambil mesin paling optimal (prioritas 1.5-flash, kalau gak ada ambil yang mana aja yang jalan)
                target_model = next((m for m in valid_models if '1.5-flash' in m), valid_models[0])
                model = genai.GenerativeModel(target_model)
                
                # PROMPT PREDATOR
                prompt_system = f"""
                Kamu adalah mesin AI strategis milik 'Buwana Karya', perusahaan konsultan investasi kos-kosan elit. 
                Tugasmu: Menganalisa data lahan ini dan membuat Laporan Eksekutif yang sangat agresif, elegan, dan manipulatif secara psikologis (menyerang ketakutan investor pada inflasi dan menawarkan kepastian warisan).
                
                Data Lahan dari Dema:
                - Magnet Area: {magnet}
                - Lahan & Harga: {luas_harga}
                - Akses: {jalan}
                - Kelemahan Saingan: {kompetitor}
                
                Buat laporan dengan struktur persis seperti ini:
                
                **DOKUMEN RAHASIA: KELAYAKAN ASET WARISAN BUWANA KARYA**
                *Status Lahan: SUPERIOR / LAYAK EKSEKUSI*

                **1. PEMETAAN ZONA DOMINASI**
                (Bahas monopoli area ini karena kompetitor lemah).
                **2. PROFIL PENYEWA & MESIN MARKETING**
                (Bahas garansi penuh kamar oleh strategi pemasaran Mona).
                **3. SIMULASI KETAKUTAN INFLASI VS. WARISAN NYATA**
                (Tekan bahwa uang di bank hangus dimakan inflasi).
                **4. PERLINDUNGAN JARINGAN ELIT (VIP CLEARANCE)**
                (Bahas dukungan elit untuk kemudahan perizinan).
                
                **KESIMPULAN EKSEKUTIF**
                
                Aturan: Bahasa Indonesia berkelas, tajam, tanpa basa-basi.
                """
                
                with st.spinner('Membedah kelayakan lahan...'):
                    response = model.generate_content(prompt_system)
                    st.success(f"Target Terkunci menggunakan mesin: {target_model}")
                    st.markdown(response.text)
        except Exception as e:
            st.error(f"Mesin gagal merespon: {e}")
