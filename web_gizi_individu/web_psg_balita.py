import streamlit as st 
import pandas as pd
from datetime import date
import datetime as dt  

import sys 
sys.path.append('')

from rumus_psg.psg import penilaian_status_gizi_beta



def psg_individu():
    # st.title('KALKULATOR PSG BALITA')
    st.info('*CATATAN :* digunakan untuk rentang usia 0 - 60 bulan... menggunakan standar deviasi dari PMK No 2 Th 2020 ttg Standar Antropometri Anak')
    st.write('---------------------------------------------------')
    
    anak, ortu = st.columns(2)
    with anak: 
        anak = st.text_input('masukan nama anak')
     
    with ortu:
        ortu = st.text_input('masukan nama orang tua')
    
    
    lahir, kunjungan = st.columns(2)
    with lahir:
        lahir = st.date_input('tanggal lahir', dt.datetime(2020,1,1)) 
    
    with kunjungan:
        kunjungan = st.date_input('tanggal kunjungan', dt.datetime.now())
    
    umur_hitung = (kunjungan - lahir)/30
    umur = umur_hitung.days
    
    bb, pbtb, sex = st.columns(3)
    with bb : bb = st.number_input('masukan berat badan',1.00)
    
    with pbtb:
        
        if umur < 24   :
            pbtb = st.number_input('masukan panjang badan',1.00)
            pb = pbtb
            label = 'PB'
        
        elif umur > 24 : 
            pbtb = st.number_input('masukan tinggi badan',1.00)
            tb = pbtb
            label = 'TB' 
            
            
             
    with sex : 
        sex = st.selectbox('jenis kelamin', ['pria', 'wanita'])
    
    asuhan = st.text_area('asuhan')

    bbu = penilaian_status_gizi_beta.hitung_bbu(bb=bb, tahun=int(lahir.year), bulan=int(lahir.month), hari=int(lahir.day), tanggal_ukur = kunjungan)
    pbtbu = penilaian_status_gizi_beta.hitung_pbtbu(pbtb=pbtb, tahun=int(lahir.year), bulan=int(lahir.month), hari=int(lahir.day)) 
    imtu = penilaian_status_gizi_beta.hitung_imtu(bb=bb,pbtb=pbtb, usia=umur,tahun=int(lahir.year), bulan=int(lahir.month), hari=int(lahir.day)) 

    if st.button('HITUNG'):
        
        with st.expander('STATUS GIZI BALITA'):
            
            kolom1 , kolom2, kolom3 = st.columns(3)
            with kolom1:
                umur = st.success(f'UMUR : {umur}')
                imtu = st.success((f'IMT/U : {imtu}'))
            
            with kolom2:
                bbu = st.success(f'BB/U : {bbu}') 
            
            with kolom3:
                pbtb = st.success(f'{label}/U : {pbtbu}')
            
            
    st.write('-------------------------')
    if st.button('LAPORAN'):
        st.warning('DALAM PENGEMBANGAN')
            
        
        
    st.write('---------------------------------------------------')
psg_individu()