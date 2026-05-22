import streamlit as st
import google.generativeai as genai

# 1. SETUP TAMPILAN (Biar Kelihatan Elite di HP Lu)
st.set_page_config(page_title="Buwana Karya AI", page_icon="🏢", layout="centered")

st.markdown("<h1 style='text-align: center; color: #b8860b;'>🛡️ BUWANA KARYA</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Mesin Intelijen Kelayakan Aset Warisan</h4>", unsafe_allow_html=True)
st.divider()

# 2. INPUT KUNCI MASTER
api_key = st.text_input("🔑 Masukkan Kode Otorisasi (API Key):", type="password")

# 3. FORM SURVEI LAPANGAN (Data yang lu ketik pas di lokasi)
st.subheader("📡 Radar Lapangan")
magnet = st.text_input("1. Jarak ke Magnet Area:", placeholder="Cth: 800m dari pintu belakang UMS")
luas_harga = st.text_input("2. Dimensi Lahan & Estimasi Harga:", placeholder="Cth: 400m2, total 1.2 Miliar")
jalan = st.text_input("3. Kondisi Akses & Logistik:", placeholder="Cth: Lebar 5 meter, aspal mulus")
kompetitor = st.text_input("4. Titik Lemah Kompetitor Sekitar:", placeholder="Cth: Kos tua, sirkulasi pengap, ibu kos galak")

st.divider()

# 4. TOMBOL EKSEKUSI
if st.button("🔥 GENERATE DOKUMEN EKSEKUSI", use_container_width=True):
    if not api_key:
        st.error("Masukkan Kode Otorisasi dulu sebelum mengeksekusi lahan!")
    elif not magnet or not luas_harga:
        st.warning("Data lahan belum lengkap. Isi radar lapangan!")
    else:
        # Nyalain mesin Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        
        # PROMPT PREDATOR (Ini yang bikin klien lu gemeteran ngeluarin duit)
        prompt_system = f"""
        Kamu adalah mesin AI strategis milik 'Buwana Karya', perusahaan konsultan investasi kos-kosan elit. 
        Tugasmu: Menganalisa data lahan ini dan membuat Laporan Eksekutif yang sangat agresif, elegan, dan manipulatif secara psikologis (menyerang ketakutan investor pada inflasi dan menawarkan kepastian warisan).
        
        Data Lahan dari Dema (Eksekutor Lapangan):
        - Magnet Area: {magnet}
        - Lahan & Harga: {luas_harga}
        - Akses: {jalan}
        - Kelemahan Saingan: {kompetitor}
        
        Buat laporan dengan struktur persis seperti ini:
        
        **DOKUMEN RAHASIA: KELAYAKAN ASET WARISAN BUWANA KARYA**
        *Status Lahan: SUPERIOR / LAYAK EKSEKUSI*

        **1. PEMETAAN ZONA DOMINASI**
        (Bahas bagaimana Buwana Karya akan melakukan hostile takeover / monopoli area ini karena kompetitor lemah).
        
        **2. PROFIL PENYEWA & MESIN MARKETING**
        (Bahas garansi penuh kamar. Sebutkan bahwa tim marketing Mona sudah menyiapkan perangkap digital dan pre-order bahkan sebelum fondasi digali).
        
        **3. SIMULASI KETAKUTAN INFLASI VS. WARISAN NYATA**
        (Tekan secara psikologis. Bahas bahwa uang yang diam di bank akan hangus dimakan inflasi. Tawarkan properti kos ini sebagai mesin pencetak uang anti-krisis yang bisa diwariskan ke anak).
        
        **4. PERLINDUNGAN JARINGAN ELIT (VIP CLEARANCE)**
        (Sebutkan secara eksplisit bahwa Buwana didukung jaringan elit—Dewan, Aparat, Pengusaha tingkat atas—sehingga semua perizinan dan keamanan proyek bebas dari gangguan preman atau birokrasi berbelit).
        
        **KESIMPULAN EKSEKUTIF**
        (Satu paragraf mematikan yang memaksa klien mengambil keputusan hari ini juga).
        
        Aturan: Gunakan bahasa Indonesia yang berkelas, tajam, tanpa basa-basi. Jangan ada kata "Berdasarkan data" atau sapaan AI standar. Langsung hantam ke isi.
        """
        
        with st.spinner('Membedah kelayakan lahan... Mengekstrak simulasi profit...'):
            try:
                response = model.generate_content(prompt_system)
                st.success("Target Terkunci. Laporan Eksekutif Siap Disajikan:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Mesin gagal merespon: {e}")
