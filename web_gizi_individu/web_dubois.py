import pandas as pd 
import numpy as np 
import streamlit as st
import sys 
from docxtpl import DocxTemplate 
# from docx2pdf import convert
import base64
from datetime import date

sys.path.append('')


from rumus_gizi.rumus_gizi_dubois import dubois
from rumus_makan.makan_dubois import makan_pagi_dubois
from rumus_makan.makan_dubois import makan_siang_dubois
from rumus_makan.makan_dubois import makan_malam_dubois




def web_individu_dubois():
    
    def download_laporan(file):
        bs64 = base64
    
    # with st.form(key='kalkulator gizi individu'):
    st.info('*CATATAN* persentase aktivitas : (ringan : 30%), (sedang : 50%), (berat : 75%), (sangat berat : 100%)... sda = 10%')
    
    nama, tanggal = st.columns(2)
    with nama :
        nama = st.text_input('masukan nama anda')
    
    with tanggal : 
        tanggal = st.date_input('tanggal konseling :', date.today()) 
    
    
    kolom_berat, kolom_tinggi, kolom_usia = st.columns(3)
    with kolom_berat :
        berat  = st.number_input('masukan berat badan',1)
    
    with kolom_tinggi:
        tinggi = st.number_input('masukan tinggi badan',1)
    
    with kolom_usia  :
        usia   = st.number_input('masukan usia',1)
    
    
    sex, tidur, aktivitas = st.columns(3)
    with sex:
        jenis_kelamin = st.selectbox('jenis kelamin' ,('pria', 'wanita'))
    
    with tidur:
        tidur = st.number_input('waktu tidur',1)
    
    with aktivitas: 
        aktivitas =st.selectbox('aktivitas fisik' ,('ringan', 'sedang' , 'berat', 'sangat berat'))
    
    keluhan = st.text_area('keluhan / masalah')
    
    
    if aktivitas   == 'ringan'  : 
        persen_aktivitas = 0.30
    
    elif aktivitas == 'sedang':
        persen_aktivitas = 0.50
    
    elif aktivitas == 'berat' : 
        persen_aktivitas = 0.75
    
    elif aktivitas == 'sangat berat' : 
        persen_aktivitas = 1
    
    
    data = dubois(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=jenis_kelamin) 
    imt  = data.imt()
    bbi  = data.bbi()
    bmr  = data.bmr()
    ktidur = data.koreksi_tidur(tidur=tidur)
    
    c  = data.c_kalori(tidur=tidur)
    aktivitas_fisik = data.aktivitas(tidur=tidur, aktivitas=persen_aktivitas)
    e = data.e_kalori(tidur=tidur, aktivitas=persen_aktivitas)
    
    sda          = data.sda(tidur=tidur, aktivitas=persen_aktivitas)
    total_energi = data.total_energi(tidur=tidur,aktivitas=persen_aktivitas)
    protein      = data.protein(tidur=tidur, aktivitas=persen_aktivitas)
    lemak        = data.lemak(tidur=tidur, aktivitas=persen_aktivitas)
    karbohidrat  = data.karbohidrat(tidur=tidur, aktivitas=persen_aktivitas)
    cairan       = data.cairan() 
    
    
    energi_pagi       = makan_pagi_dubois.energi(bb=berat, tb=tinggi, usia=usia, sex=jenis_kelamin, aktivitas=persen_aktivitas, tidur=tidur)
    protein_pagi      = makan_pagi_dubois.protein(bb=berat, tb=tinggi, usia=usia, sex=jenis_kelamin, aktivitas=persen_aktivitas, tidur=tidur)
    lemak_pagi        = makan_pagi_dubois.lemak(bb=berat, tb=tinggi, usia=usia, sex=jenis_kelamin, aktivitas=persen_aktivitas, tidur=tidur)
    kharbohidrat_pagi = makan_siang_dubois.kharbohidrat(bb=berat, tb=tinggi, usia=usia, sex=jenis_kelamin, aktivitas=persen_aktivitas, tidur=tidur)
    
    energi_siang       = makan_siang_dubois.energi(bb=berat, tb=tinggi, usia=usia, sex=jenis_kelamin, aktivitas=persen_aktivitas, tidur=tidur)
    protein_siang      = makan_siang_dubois.protein(bb=berat, tb=tinggi, usia=usia, sex=jenis_kelamin, aktivitas=persen_aktivitas, tidur=tidur)
    lemak_siang        = makan_siang_dubois.lemak(bb=berat, tb=tinggi, usia=usia, sex=jenis_kelamin, aktivitas=persen_aktivitas, tidur=tidur) 
    kharbohidrat_siang = makan_siang_dubois.kharbohidrat(bb=berat, tb=tinggi, usia=usia, sex=jenis_kelamin, aktivitas=persen_aktivitas, tidur=tidur)
    
    energi_malam       = makan_malam_dubois.energi(bb=berat, tb=tinggi, usia=usia, sex=jenis_kelamin, aktivitas=persen_aktivitas, tidur=tidur)
    protein_malam      = makan_malam_dubois.protein(bb=berat, tb=tinggi, usia=usia, sex=jenis_kelamin, aktivitas=persen_aktivitas, tidur=tidur)
    lemak_malam        = makan_malam_dubois.lemak(bb=berat, tb=tinggi, usia=usia, sex=jenis_kelamin, aktivitas=persen_aktivitas, tidur=tidur)
    kharbohidrat_malam = makan_malam_dubois.kharbohidrat(berat, tinggi, usia, jenis_kelamin, persen_aktivitas, tidur)
    
    if(st.button('HITUNG')):
        
        with st.expander('HASIL PERHITUNGAN DENGAN RUMUS DUBOIS'):
            
            
            st.write('''---------------------------------''')
            st.subheader('HASIL PERHITUNGAN KEBUTUHAN GIZI')
            st.write('''---------------------------------''')
            
            
            kolom1, kolom2 = st.columns(2)
            with kolom1:
                st.subheader('ANTROPOMETRI')
                berat_badan = st.success(f'BERAT BADAN : {berat} kg')
                berat_badan = st.success(f'TINGGI BADAN : {tinggi} cm')
                jenis_kelamin = st. success(f'GENDER/SEX : {jenis_kelamin}') 
                umur = st.success(f'UMUR : {usia} tahun')
                imt = st.success(f'IMT : {imt}')
                bbi = st.success(f'BBI : {bbi}')
                
                
            with kolom2:
                st.subheader('KEBUTUHAN GIZI')
                bmr     = st.success(f'BMR : {bmr}')
                energi  = st.success(f'KEBUTUHAN ENERGI : {total_energi}')
                protein = st.success(f'KEBUTUHAN PROTEIN : {protein}')
                lemak   = st.success(f'KEBUTUHAN LEMAK : {lemak}')
                kharbo  = st.success(f'KEBUTUHAN KHARBOHIDRAT : {karbohidrat}')
                cairan  = st.success(f'KEBUTUHAN CAIRAN : {cairan}')
                
                
                
        with st.expander('KEBUTUHAN ZAT GIZI SEKALI MAKAN '):
            
            pagi, siang, malam = st.columns(3)
            with pagi:
                st.subheader('pagi')
                energi  = st.success(f'ENERGI : {energi_pagi}')
                protein = st.success(f'PROTEIN : {protein_pagi}')
                lemak   = st.success(f'LEMAK : {lemak_pagi}')
                kharbo  = st.success(f'KHARBOHIDRAT : {kharbohidrat_pagi}') 
            
            with siang:
                st.subheader('siang')
                energi  = st.success(f'ENERGI : {energi_siang}')
                protein = st.success(f'PROTEIN : {protein_siang}')
                lemak   = st.success(f'LEMAK : {lemak_siang}')
                kharbo  = st.success(f'KHARBOHIDRAT : {kharbohidrat_siang}')
            
            with malam:
                st.subheader('malam')
                energi  = st.success(f'ENERGI : {energi_malam}')
                protein = st.success(f'PROTEIN : {protein_malam}')
                lemak   = st.success(f'LEMAK : {lemak_malam}')
                kharbo  = st.success(f'KHARBOHIDRAT : {kharbohidrat_malam}')
    
    st.write('---------------------------------------------------------')
    
    
    if st.button('LAPORAN'):
        
        if jenis_kelamin == 'pria':
            bmr_code = 1
            
        elif jenis_kelamin == 'wanita':
                bmr_code = 0.9
                    
                    
        doc    = DocxTemplate('web_gizi_individu/DUBOIS.docx')
        context = {
            'nama'    : nama, 
            'usia'    : f'{usia} ', 
            'sex'     : jenis_kelamin , 
            'bmr_code': f'{bmr_code}',
            'berat'   : f'{berat} ', 
            'tinggi'  : f'{tinggi} ',
          
          
            'imt'     : imt,
            'bbi'     : f'{bbi}',
            'bmr'     : f'{bmr}',
            'tidur'   : f'{tidur}',
            'ktidur'  : f'{ktidur}',
            'c'       : f'{c}',
            'aktivitas' : f'{persen_aktivitas}',
            'aktivitas_fisik' : f'{aktivitas_fisik}',
            "e"       : f'{e}',
            'sda'     : f'{sda}',
          
          
            'energi'  : f'{total_energi}',
            'protein' : f'{protein}',
            'lemak'   : f'{lemak}',
            'kharbo'  : f'{karbohidrat}',
            'cairan'  : f"{cairan}",
          
          
            'energi_pagi'  :energi_pagi,
            'protein_pagi' : protein_pagi,
            'lemak_pagi'   : lemak_pagi,
            'kharbo_pagi'  : kharbohidrat_pagi,
          
          
            'energi_siang' :energi_siang,
            'protein_siang': protein_siang,
            'lemak_siang'  : lemak_siang,
            'kharbo_siang' : kharbohidrat_siang,
            'energi_malam' :energi_malam,
          
          
            'protein_malam': protein_malam,
            'lemak_malam'  : lemak_malam,
            'kharbo_malam' : kharbohidrat_malam,
            'keluhan'      : keluhan,
            'tanggal'      : tanggal
            }
                
        doc.render(context=context)
        out = doc.save(f'{nama}.docx')
        # convert(input_path)
    
        st.download_button(
        'DOWNLOAD LAPORAN',
        data = out,
        file_name=f'{nama}'    
        )
                
        st.success('SUKSES MEMBUAT LAPORAN')
                
            
            
            # hasil = base64.b64encode(out.encode()).decode()  # some strings <-> bytes conversions necessary here
            # href = f'<a href="data:file/csv;base64,{hasil}">Download csv file</a>'


