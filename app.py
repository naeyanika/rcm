import streamlit as st
import pandas as pd

@st.cache_data
def muat_data_dari_github(url):
    data = pd.read_excel(url)
    return data


#Link Github
url_github = 'https://github.com/naeyanika/rcm/blob/master/RCM.xlsx'

#Muat Data
data = muat_data_dari_github(url_github)

st.title('Pencarian Data Risk Control Matrix')

# Input user kata kunci
kata_kunci = st.text_input("Masukkan kata kunci yang ingin dicari:")

# Fungsi Pencarian
def cari_data(data, kata_kunci):
    hasil = data[
        data['KC/KR/KP'].str.contains(kata_kunci, case=False, na=False) |
        data['Judul Temuan'].str.contains(kata_kunci, case=False, na=False) |
        data['Kode Risk Issue'].str.contains(kata_kunci, case=False, na=False) |
        data['Judul Risk Issue'].str.contains(kata_kunci, case=False, na=False) |
        data['Kategori'].str.contains(kata_kunci, case=False, na=False) |
        data['Kelemahan'].str.contains(kata_kunci, case=False, na=False) 
    ]
    return hasil

# Jika ada input kata kunci, lakukan pencarian
if kata_kunci:
    hasil_pencarian = cari_data(data, kata_kunci)
    
    # Tampilkan hasil pencarian
    if not hasil_pencarian.empty:
        st.write(hasil_pencarian)
    else:
        st.write("Tidak ada hasil yang cocok dengan kata kunci.")

