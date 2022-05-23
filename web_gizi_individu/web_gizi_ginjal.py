import sys 
import streamlit as st

sys.path.append("")

from datetime import date
from rumus_gizi.rumus_gizi_ginjal import gizi_ginjal
from rumus_makan.makan_ginjal import makan_pagi_ginjal
from rumus_makan.makan_ginjal import makan_siang_ginjal
from rumus_makan.makan_ginjal import makan_malam_ginjal
from docxtpl import DocxTemplate

def web_ginjal():
    with st.form(key='web ginjal'):
        nama, tanggal = st.columns(2)
        with nama :
            nama   = st.text_input('masukan nama anda')

        with tanggal : 
            tanggal = st.date_input('tanggal konseling :', date.today()) 


        kolom_berat, kolom_tinggi, kolom_usia = st.columns(3)
        with kolom_berat :
            berat  = st.number_input('masukan berat badan',1)
            gender = st.selectbox('jenis kelamin', ('pria', 'wanita')) 

        with kolom_tinggi:
            tinggi = st.number_input('masukan tinggi badan',1)
            kondisi = st.selectbox('kondisi', ('Haemodialisa', 'tanpa Haemodialisa'))

        with kolom_usia:
            usia = st.number_input('masukan usia', 1)
            



        data = gizi_ginjal(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender)
        
        imt = data.imt()
        bbi = data.bbi()
        bmr = data.bmr()
        energi = data.total_energi()
        protein = data.protein(kondisi=kondisi)
        lemak = data.lemak()
        karbohidrat = data.karbohidrat()
        
        
        energi_pagi = makan_pagi_ginjal.energi(bb=berat, tb=tinggi, usia=usia, sex=gender)
        protein_pagi =  makan_pagi_ginjal.protein(bb=berat, tb=tinggi, usia=usia, sex=gender, kondisi=kondisi)
        lemak_pagi = makan_pagi_ginjal.lemak(bb=berat, tb=tinggi, usia=usia, sex=gender)
        karbohidrat_pagi = makan_pagi_ginjal.kharbohidrat(bb=berat, tb=tinggi, usia=usia, sex=gender)
        
        energi_siang = makan_siang_ginjal.energi(bb=berat, tb=tinggi, usia=usia, sex=gender)
        protein_siang =  makan_siang_ginjal.protein(bb=berat, tb=tinggi, usia=usia, sex=gender, kondisi=kondisi)
        lemak_siang = makan_siang_ginjal.lemak(bb=berat, tb=tinggi, usia=usia, sex=gender)
        karbohidrat_siang = makan_siang_ginjal.kharbohidrat(bb=berat, tb=tinggi, usia=usia, sex=gender)
        
        energi_malam = makan_malam_ginjal.energi(bb=berat, tb=tinggi, usia=usia, sex=gender)
        protein_malam =  makan_malam_ginjal.protein(bb=berat, tb=tinggi, usia=usia, sex=gender, kondisi=kondisi)
        lemak_malam = makan_malam_ginjal.lemak(bb=berat, tb=tinggi, usia=usia, sex=gender)
        karbohidrat_malam = makan_malam_ginjal.kharbohidrat(bb=berat, tb=tinggi, usia=usia, sex=gender)
        
        
                
        if(st.form_submit_button('HITUNG')):
            
            with st.expander('HASIL PERHITUNGAN DENGAN RUMUS DUBOIS'):
                st.write('''---------------------------------''')
                st.subheader('HASIL PERHITUNGAN KEBUTUHAN GIZI')
                st.write('''---------------------------------''')
                
                
                kolom1, kolom2 = st.columns(2)
                with kolom1:
                    st.subheader('ANTROPOMETRI')
                    berat_badan = st.success(f'BERAT BADAN : {berat} kg')
                    berat_badan = st.success(f'TINGGI BADAN : {tinggi} cm')
                    jenis_kelamin = st. success(f'GENDER/SEX : {gender}') 
                    umur = st.success(f'UMUR : {usia} tahun')
                    imt = st.success(f'IMT : {imt}')
                    bbi = st.success(f'BBI : {bbi}')
                    
                    
                with kolom2:
                    st.subheader('KEBUTUHAN GIZI')
                    bmr     = st.success(f'BMR : {bmr}')
                    energi  = st.success(f'KEBUTUHAN ENERGI : {energi}')
                    protein = st.success(f'KEBUTUHAN PROTEIN : {protein}')
                    lemak   = st.success(f'KEBUTUHAN LEMAK : {lemak}')
                    kharbo  = st.success(f'KEBUTUHAN KHARBOHIDRAT : {karbohidrat}')
                
            with st.expander('KEBUTUHAN ZAT GIZI SEKALI MAKAN '):
                
                pagi, siang, malam = st.columns(3)
                with pagi:
                    st.subheader('pagi')
                    energi  = st.success(f'ENERGI : {energi_pagi}')
                    protein = st.success(f'PROTEIN : {protein_pagi}')
                    lemak   = st.success(f'LEMAK : {lemak_pagi}')
                    kharbo  = st.success(f'KHARBOHIDRAT : {karbohidrat_pagi}') 
                
                with siang:
                    st.subheader('siang')
                    energi  = st.success(f'ENERGI : {energi_siang}')
                    protein = st.success(f'PROTEIN : {protein_siang}')
                    lemak   = st.success(f'LEMAK : {lemak_siang}')
                    kharbo  = st.success(f'KHARBOHIDRAT : {karbohidrat_siang}')
                
                with malam:
                    st.subheader('malam')
                    energi  = st.success(f'ENERGI : {energi_malam}')
                    protein = st.success(f'PROTEIN : {protein_malam}')
                    lemak   = st.success(f'LEMAK : {lemak_malam}')
                    kharbo  = st.success(f'KHARBOHIDRAT : {karbohidrat_malam}')
                    
                    
        st.write('------------------------------')
        
        
        if(st.form_submit_button('LAPORAN')):
            # st.error('SEDANG DALAM PENGEMBANGAN')
            
            if kondisi == 'Haemodialisa':
                kondisicode = 0.8
                
            elif kondisi == 'tanpa Haemodialisa':
                kondisicode = 1.2
                
                
            if gender == 'pria':
                    bmrcode = 1
                
            elif gender == "wanita":
                bmrcode = 0.9
                
                
            if usia <= 60:
                energicode = 35
                
            elif usia > 60:
                energicode = 30
                
            doc    = DocxTemplate('/home/gol/Documents/koding/difrawide_project/web_gizi_individu/GINJAL.docx')

            context = {
                    'nama'    : nama, 
                    'usia'    : f'{usia} ', 
                    'sex'     : gender, 
                    'kondisicode' : kondisicode,
                    'bmrcode' : bmrcode,
                    'energicode' : energicode,
                    'berat'   : f'{berat} ', 
                    'tinggi'  : f'{tinggi} ',
                    
                    'tanggal' : tanggal,
                    'imt'     : imt,
                    'bbi'     : f'{bbi}',
                    'bmr'     : f'{bmr}',
                    
                    
                    'energi'  : f'{energi}',
                    'protein' : f'{protein}',
                    'lemak'   : f'{lemak}',
                    'kharbo'  : f'{karbohidrat}',
                    
                    'energi_pagi'  :energi_pagi,
                    'protein_pagi' : protein_pagi,
                    'lemak_pagi'   : lemak_pagi,
                    'kharbo_pagi'  : karbohidrat_pagi,
                  
                  
                    'energi_siang' :energi_siang,
                    'protein_siang': protein_siang,
                    'lemak_siang'  : lemak_siang,
                    'kharbo_siang' : karbohidrat_siang,
                    'energi_malam' :energi_malam,
                  
                  
                    'protein_malam': protein_malam,
                    'lemak_malam'  : lemak_malam,
                    'kharbo_malam' : karbohidrat_malam,
                    
                    
                    
            }    
        
            doc.render(context=context)
            doc.save(f'{nama}.docx')
            st.success('SUKSES MEMBUAT LAPORAN')
