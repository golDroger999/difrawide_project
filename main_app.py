import streamlit as st
import sys
import pandas as pd 



sys.path.append('')
from web_gizi_individu.menu_individu import pilihan_rumus_gizi_individu
from web_gizi_kelompok.menu_kelompok import pilihan_analisa_gizi_kelompok
from hardware_iot.dashboard_timbangan import dashboard




def main():
    st.sidebar.header('POLTEKKES KEMENKES DENPASAR JURUSAN GIZI')
    option = st.sidebar.selectbox('', ('ANALISA GIZI INDIVIDU', 'ANALISA GIZI KELOMPOK', 'HARDWARE TOOLS (IOT)' ))

    if option == 'ANALISA GIZI INDIVIDU':
        st.write('----------------------------')
        st.header('DIETETIC FRAMEWORK WITH DEADLINES') 
        pilihan_rumus_gizi_individu()


    elif option == 'ANALISA GIZI KELOMPOK' :
        st.write('----------------------------')
        st.header('DIETETIC FRAMEWORK WITH DEADLINES') 
        pilihan_analisa_gizi_kelompok()

        
    elif option == 'HARDWARE TOOLS (IOT)':
        st.write('----------------------------')
        st.header('DIETETIC FRAMEWORK WITH DEADLINES')
        st.write('----------------------------')
        dashboard()
        st.error('SEDANG DALAM PENGEMBANGAN')
        
    
   

if __name__ == '__main__':
    main()