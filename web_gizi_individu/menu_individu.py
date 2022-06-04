import streamlit as st 
import sys 

sys.path.append('')

from web_gizi_individu.web_dubois import web_individu_dubois
from web_gizi_individu.web_harris_benedict import web_individu_harrisbenedict
# from web_gizi_individu.web_form_dietetik import web_individu_form_dietetik
from web_gizi_individu.web_gizi_wanita_hamil import web_gizi_wanita_hamil
from web_gizi_individu.web_gizi_wanita_menyusui import web_gizi_wanita_menyusui
from web_gizi_individu.web_mifflin import web_mifflin
from web_gizi_individu.web_perkeni_2015 import web_perkeni_2015
from web_gizi_individu.web_gizi_ginjal import web_ginjal



def pilihan_rumus_gizi_individu():
    pilihan = st.selectbox('', ['DUBOIS', 'HARRIS BENEDICT', 'RUMUS DIETETIK PENYAKIT', 'PSG BALITA', 'ANALISA GIZI KHUSUS WANITA'])
    st.write('-----------------------------------------------------------------------')
    
    if pilihan == 'DUBOIS':
        st.subheader('KALKULATOR GIZI DUBOIS')
        web_individu_dubois()
        
    elif pilihan == 'HARRIS BENEDICT':
        st.subheader('KALKULATOR GIZI HARRIS BENEDICT')
        web_individu_harrisbenedict()
    
    
    elif pilihan == 'RUMUS DIETETIK PENYAKIT':
        
        with st.expander('PILIH JENIS RUMUS'):

            pilih_form = st.radio('',  'RUMUS PERKENI 2015 (DIABETES)',
                                       'RUMUS MIFFLIN (BIASA DIGUNAKAN DIETESIAN RS)',
                                       'RUMUS GGK/CKD/CRF (RUMUS KEBUTUHAN GIZI UNTUK PENYAKIT GINJAL)'
                                )
        
        st.write('-----------------------------------------------------------')
    
        if pilih_form == 'RUMUS PERKENI 2015 (DIABETES)':
            st.subheader('RUMUS PERKENI 2015 (DIABETES)')
            web_perkeni_2015()
        
        elif pilih_form == 'RUMUS MIFFLIN (BIASA DIGUNAKAN DIETESIAN RS)':
            st.subheader('RUMUS MIFFLIN (BIASA DIGUNAKAN DIETESIAN RS)')
            web_mifflin()
            
        elif pilih_form =='RUMUS GGK/CKD/CRF (RUMUS KEBUTUHAN GIZI UNTUK PENYAKIT GINJAL)':
            st.subheader('RUMUS GGK/CKD/CRF (RUMUS KEBUTUHAN GIZI UNTUK PENYAKIT GINJAL)')
            web_ginjal() 
            
            
    elif pilihan == 'PSG BALITA':
        st.subheader('PSG BALITA') 
        st.error('SEDANG DALAM PENGEMBANGAN')
        
        
    elif pilihan == 'ANALISA GIZI KHUSUS WANITA':
        
        with st.expander('PILIH JENIS FORM'):
            pilih_form = st.radio('', ('HAMIL', 'MENYUSUI')) 
        st.write('-----------------------------------------------------------')

        if pilih_form == 'HAMIL':
            st.subheader('ANALISA GIZI KHUSUS WANITA HAMIL')
            web_gizi_wanita_hamil()
            
        elif pilih_form == 'MENYUSUI':
            st.subheader('ANALISA GIZI KHUSUS WANITA MENYUSUI')
            web_gizi_wanita_menyusui()
            
    
    
        