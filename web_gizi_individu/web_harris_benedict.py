import streamlit as st 
import sys
from docxtpl import DocxTemplate
sys.path.append('')

from datetime import date
from rumus_gizi.rumus_gizi_harrsibenedict import harrisbenedict
from rumus_makan.makan_harris_benedict import makan_harrisbenedict



def web_individu_harrisbenedict():
    with st.form('harris benedict'):
        st.info('''*CATATAN* 
            
aktivitas : 
                
    pria : (sangat ringan :1.3), (ringan : 1.65), (sedang : 1.76), (berat : 2.1)

    wanita : (sangat ringan :1.3), (ringan : 1.55), (sedang : 1.70), (berat : 2)
                ''')

        
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
            aktivitas = st.selectbox('faktor aktivitas', ('sangat ringan','ringan','sedang', 'berat'))
            
            if gender == 'pria':
                
                if aktivitas == 'sangat ringan':
                    aktivitas = 1.3
                
                elif aktivitas == 'ringan':
                    aktivitas = 1.65
                    
                elif aktivitas == 'sedang':
                    aktivitas = 1.76
                    
                elif aktivitas == 'berat':
                    aktivitas = 2.1
                    
                    
            elif gender == 'wanita':
                
                if aktivitas == 'sangat ringan':
                    aktivitas = 1.3
                
                elif aktivitas == 'ringan':
                    aktivitas = 1.55
                    
                elif aktivitas == 'sedang':
                    aktivitas = 1.7
                    
                elif aktivitas == 'berat':
                    aktivitas = 2
            
        
        with kolom_usia  :
            usia   = st.number_input('masukan usia',1)
        
            
            
        data = harrisbenedict(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender)
        imt = data.imt()
        bbi = data.bbi()
        bee =  data.bee()
        tee = data.tee(aktivitas=aktivitas)
        
        protein      = data.protein( aktivitas=aktivitas)
        lemak        = data.lemak(aktivitas=aktivitas)
        karbohidrat  = data.karbohidrat(aktivitas=aktivitas)
        cairan       = data.cairan()
        
        energi_pagi       = makan_harrisbenedict(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas).EnergiPagi()
        protein_pagi      = makan_harrisbenedict(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas).ProteinPagi()
        lemak_pagi        = makan_harrisbenedict(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas).LemakPagi()
        kharbohidrat_pagi = makan_harrisbenedict(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas).KharbohidratPagi()
        
        energi_siang       = makan_harrisbenedict(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas).EnergiSiang()
        protein_siang      = makan_harrisbenedict(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas).ProteinSiang()
        lemak_siang        = makan_harrisbenedict(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas).LemakSiang()
        kharbohidrat_siang = makan_harrisbenedict(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas).KharbohidratSiang()
        
        energi_malam       = makan_harrisbenedict(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas).EnergiMalam()
        protein_malam      = makan_harrisbenedict(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas).ProteinMalam()
        lemak_malam        = makan_harrisbenedict(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas).LemakMalam()
        kharbohidrat_malam = makan_harrisbenedict(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas).KharbohidratMalam()
        
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
                    st.success(f'BEE : {bee}')
                    st.success(f'TEE : {tee}')
                    st.success(f'PROTEIN : {protein}')
                    st.success(f'LEMAK : {lemak}')
                    st.success(f'KHARBOHIDRAT : {karbohidrat}')
                    st.success(f'KEBUTUHAN CAIRAN : {cairan}')
                
                
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
    
                    
        if gender == 'pria': 
            beecode = 66
            bbparam = 13.7
            tbparam = 5
            usiaparam = 6.8
        
        elif gender == 'wanita':
            beecode = 665
            bbparam = 9.6
            tbparam = 1.8
            usiaparam = 4.7
        
        st.write('------------------------------')     
         
        if st.form_submit_button('LAPORAN'):
            
            doc = DocxTemplate('web_gizi_individu/HARRIS BENEDICT.docx')
            
            context = {
                    'nama'    : nama, 
                    'usia'    : f'{usia} ',
                    'tanggal': tanggal,
                    'sex'     : gender , 
                    'berat'   : f'{berat} ', 
                    'tinggi'  : f'{tinggi} ',
                    
                    
                    'bbi'     : bbi,
                    'imt'     : imt,
                    'beecode' : beecode,
                    'bbparam' : bbparam,
                    'tbparam' : tbparam,
                    'usiaparam' : usiaparam,
                    
                    
                    'bee'       : bee,
                    'aktivitas' : aktivitas,
                    'tee'       : tee, 
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
                    
            }
            
            doc.render(context=context)
            doc.save(f'{nama}.docx', '..git/')
            st.success('SUKSES MEMBUAT LAPORAN')
            
