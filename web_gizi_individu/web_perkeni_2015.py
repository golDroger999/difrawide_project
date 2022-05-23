import streamlit as st 
import sys 

sys.path.append('')
from datetime import date
from rumus_gizi.rumus_perkeni_2015 import perkeni
from rumus_makan.makan_perkeni_2015 import makan_perkeni_2015
from docxtpl import DocxTemplate


def web_perkeni_2015():
    with st.form('perkeni'):
        
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
            aktivitas =st.selectbox('aktivitas fisik' ,('bedrest','ringan', 'sedang' , 'berat'))
            if aktivitas   == 'bedrest'  : 
                persen_aktivitas = 0.10
        
            elif aktivitas == 'ringan':
                persen_aktivitas = 0.20
        
            elif aktivitas == 'sedang' : 
                persen_aktivitas = 0.30
        
            elif aktivitas == 'berat' : 
                persen_aktivitas = 50
            
        
        with kolom_usia  :
            usia  = st.number_input('masukan usia',1)
            
            if usia <= 0 and usia >= 40:
                usia = 0 

            elif usia <=40 and usia >= 59:
                usia = 0.05

            elif usia <=59 and usia >= 69:
                usia = 0.10

            elif usia >69:
                usia = 0.15
        
        
         
        data = perkeni(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender)
        imt = data.imt()
        bbi = data.bbi()
        bmr =  data.bmr()
        energi = data.total_energi(aktivitas=persen_aktivitas, faktor_usia=usia)
        
        protein      = data.protein(aktivitas=persen_aktivitas, faktor_usia=usia)
        lemak        = data.lemak(aktivitas=persen_aktivitas, faktor_usia=usia)
        karbohidrat  = data.karbohidrat(aktivitas=persen_aktivitas, faktor_usia=usia)
        # cairan       = data.cairan()
        
        energi_pagi       = makan_perkeni_2015.energi_pagi(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender, aktivitas=persen_aktivitas, faktor_usia=usia)
        protein_pagi      = makan_perkeni_2015.protein_pagi(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender, aktivitas=persen_aktivitas, faktor_usia=usia)
        lemak_pagi        = makan_perkeni_2015.lemak_pagi(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender, aktivitas=persen_aktivitas, faktor_usia=usia)
        kharbohidrat_pagi = makan_perkeni_2015.karbohidrat_pagi(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender, aktivitas=persen_aktivitas, faktor_usia=usia)
        
        energi_siang       = makan_perkeni_2015.energi_siang(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender, aktivitas=persen_aktivitas, faktor_usia=usia)
        protein_siang      = makan_perkeni_2015.protein_siang(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender, aktivitas=persen_aktivitas, faktor_usia=usia)
        lemak_siang        = makan_perkeni_2015.lemak_siang(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender, aktivitas=persen_aktivitas, faktor_usia=usia)
        kharbohidrat_siang = makan_perkeni_2015.karbohidrat_siang(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender, aktivitas=persen_aktivitas, faktor_usia=usia)
        
        energi_malam       =makan_perkeni_2015.energi_malam(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender, aktivitas=persen_aktivitas, faktor_usia=usia)
        protein_malam      =makan_perkeni_2015.protein_malam(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender, aktivitas=persen_aktivitas, faktor_usia=usia)
        lemak_malam        =makan_perkeni_2015.lemak_malam(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender, aktivitas=persen_aktivitas, faktor_usia=usia)
        kharbohidrat_malam =makan_perkeni_2015.karbohidrat_malam(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender, aktivitas=persen_aktivitas, faktor_usia=usia)

         
        if st.form_submit_button('HITUNG'): 
            
            
            with st.expander('HASIL PERHITUNGAN'):
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
                    st.success(f'BMR : {bmr}')
                    st.success(f'ENERGI : {energi}')
                    st.success(f'PROTEIN : {protein}')
                    st.success(f'LEMAK : {lemak}')
                    st.success(f'KHARBOHIDRAT : {karbohidrat}')
                
                
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
    
        
        
        st.write('''---------------------------------''')
        
        if st.form_submit_button('LAPORAN'):
        
            if gender == 'pria':
                bmrcode = 30
                
            elif gender == 'wanita':
                bmrcode = 25 
                
                
                
                
            
            doc = DocxTemplate('/home/gol/Documents/koding/difrawide_project/web_gizi_individu/PERKENI.docx')
            
            context = {
                    'nama'    : nama, 
                    'usia'    : f'{usia}',
                    'tanggal': tanggal,
                    'sex'     : gender , 
                    'berat'   : f'{berat} ', 
                    'tinggi'  : f'{tinggi} ',
                    
                    
                    'bbi'     : bbi,
                    'imt'     : imt,
                    'faktor_usia' : usia,
                    'bmr' : bmr,
                    'bmrcode' : bmrcode,
                    'aktivitas' : persen_aktivitas,
                    
                    
                    
                    'energi' : energi,
                    'protein' : f'{protein}',
                    'lemak'   : f'{lemak}',
                    'kharbo'  : f'{karbohidrat}',
                    
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
            
            }
            
            doc.render(context=context)
            doc.save(f'{nama}.docx')
            st.success('SUKSES MEMBUAT LAPORAN')
            
