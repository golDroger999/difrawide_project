import streamlit as st
import sys 

sys.path.append('')

from web_gizi_kelompok.kelompok import kalkulasi_gizi_kelompok


def pilihan_analisa_gizi_kelompok():
    
    pilihan = st.selectbox('', ['GIZI KELOMPOK DUBOIS', 'PSG KELOMPOK'])
    st.write('-----------------------------------------------------------------------')
    
    if pilihan == 'GIZI KELOMPOK DUBOIS':
        st.subheader('GIZI KELOMPOK DUBOIS')
        kalkulasi_gizi_kelompok()
        
    elif pilihan == 'PSG KELOMPOK':
        st.subheader('PSG KELOMPOK')
        st.error('SEDANG DALAM PENGEMBANGAN')
