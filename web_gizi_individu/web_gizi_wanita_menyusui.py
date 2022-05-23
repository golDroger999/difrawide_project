import streamlit as st 
import sys 

sys.path.append('')

from rumus_gizi.rumus_gizi_khusus_wanita_menyusui import wanita_menyusui
from rumus_gizi.rumus_gizi_khusus_wanita_menyusui import makan_pagi_menyusui
from rumus_gizi.rumus_gizi_khusus_wanita_menyusui import makan_siang_menyusui
from rumus_gizi.rumus_gizi_khusus_wanita_menyusui import makan_malam_menyusui
from docxtpl import DocxTemplate 



def web_gizi_wanita_menyusui():
    
    with st.form(key='ANALISA GIZI WANITA'):
    
        kolom1, kolom2, = st.columns(2)
        with kolom1:
            nama = st.text_input('masukan nama')

        with kolom2:
            tanggal = st.date_input('masukan tanggal ')

        kolom3, kolom4, kolom5 = st.columns(3)

        with kolom3:
            berat = st.number_input('masukan berat badan', 1)
            aktivitas = st.selectbox('aktivitas', ['ringan', 'sedang', 'berat', 'sangat berat'])
            

        with kolom4:
            tinggi = st.number_input('masukan tinggi badan', 1)
            fase = st.selectbox('fase menyusui', ['6 BULAN PERTAMA', '6 BULAN KEDUA'])
        
        with kolom5:
            usia = st.number_input('masukan usia', 1)
            tidur = st.number_input('waktu tidur', 1)
            
        
         
        if aktivitas   == 'ringan'  : 
            persen_aktivitas = 0.30
        
        elif aktivitas == 'sedang':
            persen_aktivitas = 0.50
        
        elif aktivitas == 'berat' : 
            persen_aktivitas = 0.75
        
        elif aktivitas == 'sangat berat' : 
            persen_aktivitas = 1
        
            
            
        data = wanita_menyusui(bb=berat, tb=tinggi, usia=usia, lama_menyusui=fase) 
        imt  = data.imt()
        bbi  = data.bbi()
        # bbih = data.bbih()
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
        
        energi_pagi = makan_pagi_menyusui.energi(bb=berat, tb=tinggi, usia=usia, lama_menyusui=fase, aktifitas=persen_aktivitas, tidur=tidur)
        protein_pagi = makan_pagi_menyusui.protein(bb=berat, tb=tinggi, usia=usia, lama_menyusui=fase, aktifitas=persen_aktivitas, tidur=tidur)
        lemak_pagi = makan_pagi_menyusui.lemak(bb=berat, tb=tinggi, usia=usia, lama_menyusui=fase, aktifitas=persen_aktivitas, tidur=tidur)
        kharbohidrat_pagi = makan_pagi_menyusui.kharbohidrat(bb=berat, tb=tinggi, usia=usia, lama_menyusui=fase, aktifitas=persen_aktivitas, tidur=tidur)
        
        energi_siang = makan_siang_menyusui.energi(bb=berat, tb=tinggi, usia=usia, lama_menyusui=fase, aktifitas=persen_aktivitas, tidur=tidur)
        protein_siang = makan_siang_menyusui.protein(bb=berat, tb=tinggi, usia=usia, lama_menyusui=fase, aktifitas=persen_aktivitas, tidur=tidur)
        lemak_siang = makan_siang_menyusui.lemak(bb=berat, tb=tinggi, usia=usia, lama_menyusui=fase, aktifitas=persen_aktivitas, tidur=tidur)
        kharbohidrat_siang = makan_siang_menyusui.kharbohidrat(bb=berat, tb=tinggi, usia=usia, lama_menyusui=fase, aktifitas=persen_aktivitas, tidur=tidur)
        
        energi_malam = makan_malam_menyusui.energi(bb=berat, tb=tinggi, usia=usia, lama_menyusui=fase, aktifitas=persen_aktivitas, tidur=tidur)
        protein_malam = makan_malam_menyusui.protein(bb=berat, tb=tinggi, usia=usia, lama_menyusui=fase, aktifitas=persen_aktivitas, tidur=tidur)
        lemak_malam = makan_malam_menyusui.lemak(bb=berat, tb=tinggi, usia=usia, lama_menyusui=fase, aktifitas=persen_aktivitas, tidur=tidur)
        kharbohidrat_malam = makan_malam_menyusui.kharbohidrat(bb=berat, tb=tinggi, usia=usia, lama_menyusui=fase, aktifitas=persen_aktivitas, tidur=tidur)
        
        analisa = st.form_submit_button('ANALISA ')
        
        if analisa:
            with st.expander('HASIL PERHITUNGAN DENGAN RUMUS DUBOIS'):
                st.write('''---------------------------------''')
                st.subheader('HASIL PERHITUNGAN KEBUTUHAN GIZI')
                st.write('''---------------------------------''')
                
                
                kolom1, kolom2 = st.columns(2)
                with kolom1:
                    st.subheader('ANTROPOMETRI')
                    berat_badan = st.success(f'BERAT BADAN : {berat} kg')
                    berat_badan = st.success(f'TINGGI BADAN : {tinggi} cm')
                    # jenis_kelamin = st. success(f'GENDER/SEX : {jenis_kelamin}') 
                    umur = st.success(f'UMUR : {usia} tahun')
                    imt = st.success(f'IMT : {imt}')
                    bbi = st.success(f'BBI : {bbi}')
                    # bbih = st.success(f'BBIH : {bbih}')
                    
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
        
        if st.form_submit_button('LAPORAN'):
            
            if fase == '6 BULAN PERTAMA':
                energiplus = 330
                proteinplus = 20
                lemakplus = 2.2
                karboplus = 45
                
            elif fase == '6 BULAN KEDUA':
                energiplus = 400
                proteinplus = 15
                lemakplus = 2.2
                karboplus = 55
            
                
            doc    = DocxTemplate('/home/gol/Documents/koding/difrawide_project/web_gizi_individu/IBU MENYUSUI.docx')
            
            context = {
                    'nama'    : nama, 
                    'usia'    : f'{usia} ',  
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
                    'fase' : f'{fase}',
                  
                  
                    'energi'  : f'{total_energi}',
                    'protein' : f'{protein}',
                    'lemak'   : f'{lemak}',
                    'kharbo'  : f'{karbohidrat}',
                    'energiplus' : f'{energiplus}',
                    'proteinplus' : f'{proteinplus}',
                    'lemakplus' : f'{lemakplus}',
                    'karboplus' : f'{karboplus}',
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
                    'tanggal'      : tanggal
                    }
                
            doc.render(context=context)
            doc.save(f'{nama}.docx')
            st.success('SUKSES MEMBUAT LAPORAN')
    
        