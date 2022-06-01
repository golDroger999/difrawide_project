import streamlit as st 
import sys 

sys.path.append('')

from rumus_gizi.rumus_gizi_khusus_wanita_hamil import wanita_hamil
from rumus_gizi.rumus_gizi_khusus_wanita_hamil import makan_pagi_hamil
from rumus_gizi.rumus_gizi_khusus_wanita_hamil import makan_siang_hamil
from rumus_gizi.rumus_gizi_khusus_wanita_hamil import makan_malam_hamil
from docxtpl import DocxTemplate 

def web_gizi_wanita_hamil():
    
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
            trisemester = st.selectbox('tri semester', ['TRI SEMESTER 1', 'TRI SEMESTER 2', 'TRI SEMESTER 3'])

        with kolom4:
            tinggi = st.number_input('masukan tinggi badan', 1)
            usia_kehamilan = st.number_input('usia kehamilan dalam minggu', 1)
            lila = st.number_input('lila / lingkar lengan atas', 1)
            
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
        
            
            
        data = wanita_hamil(bb=berat, tb=tinggi, usia=usia, trimester=trisemester, usia_kehamilan=usia_kehamilan) 
        imt  = data.imt()
        bbi  = data.bbi()
        bbih = data.bbih()
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
        
        energi_pagi = makan_pagi_hamil.energi(bb=berat, tb=tinggi, usia=usia, trimester=trisemester, usia_kehamilan=usia_kehamilan, aktifitas=persen_aktivitas, tidur=tidur)
        protein_pagi = makan_pagi_hamil.protein(bb=berat, tb=tinggi, usia=usia, trimester=trisemester, usia_kehamilan=usia_kehamilan, aktifitas=persen_aktivitas, tidur=tidur)
        lemak_pagi = makan_pagi_hamil.lemak(bb=berat, tb=tinggi, usia=usia, trimester=trisemester, usia_kehamilan=usia_kehamilan, aktifitas=persen_aktivitas, tidur=tidur)
        kharbohidrat_pagi = makan_pagi_hamil.kharbohidrat(bb=berat, tb=tinggi, usia=usia, trimester=trisemester, usia_kehamilan=usia_kehamilan, aktifitas=persen_aktivitas, tidur=tidur)
        
        energi_siang = makan_pagi_hamil.energi(bb=berat, tb=tinggi, usia=usia, trimester=trisemester, usia_kehamilan=usia_kehamilan, aktifitas=persen_aktivitas, tidur=tidur)
        protein_siang = makan_pagi_hamil.protein(bb=berat, tb=tinggi, usia=usia, trimester=trisemester, usia_kehamilan=usia_kehamilan, aktifitas=persen_aktivitas, tidur=tidur)
        lemak_siang = makan_pagi_hamil.lemak(bb=berat, tb=tinggi, usia=usia, trimester=trisemester, usia_kehamilan=usia_kehamilan, aktifitas=persen_aktivitas, tidur=tidur)
        kharbohidrat_siang = makan_pagi_hamil.kharbohidrat(bb=berat, tb=tinggi, usia=usia, trimester=trisemester, usia_kehamilan=usia_kehamilan, aktifitas=persen_aktivitas, tidur=tidur)
        
        energi_malam = makan_malam_hamil.energi(bb=berat, tb=tinggi, usia=usia, trimester=trisemester, usia_kehamilan=usia_kehamilan, aktifitas=persen_aktivitas, tidur=tidur)
        protein_malam = makan_malam_hamil.protein(bb=berat, tb=tinggi, usia=usia, trimester=trisemester, usia_kehamilan=usia_kehamilan, aktifitas=persen_aktivitas, tidur=tidur)
        lemak_malam = makan_malam_hamil.lemak(bb=berat, tb=tinggi, usia=usia, trimester=trisemester, usia_kehamilan=usia_kehamilan, aktifitas=persen_aktivitas, tidur=tidur)
        kharbohidrat_malam = makan_malam_hamil.kharbohidrat(bb=berat, tb=tinggi, usia=usia, trimester=trisemester, usia_kehamilan=usia_kehamilan, aktifitas=persen_aktivitas, tidur=tidur)
        
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
                    bbih = st.success(f'BBIH : {bbih}')
                    
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
            
            if trisemester == 'TRI SEMESTER 1':
                energiplus = 180
                proteinplus = 1
                lemakplus = 2.3
                karboplus = 25
                
            elif trisemester == 'TRI SEMESTER 2':
                energiplus = 300
                proteinplus = 10
                lemakplus = 2.3
                karboplus = 40
                
            elif trisemester == 'TRI SEMESTER 3':
                energiplus = 300
                proteinplus = 30
                lemakplus = 2.3
                karboplus = 40
                
            
            if tinggi <=160:
                tb_code = 105
                
            elif tinggi >=160:
                tb_code = 110
                                
                 
        
            doc    = DocxTemplate('IBU HAMIL.docx')
            
            context = {
                    'nama'    : nama, 
                    'usia'    : f'{usia} ',  
                    'berat'   : f'{berat} ', 
                    'tinggi'  : f'{tinggi} ',
                    'tb_code' : f'{tb_code}',
                  
                  
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
                    'trimester' : f'{trisemester}',
                    'usia_hamil' : f'{usia_kehamilan}',
                  
                  
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
