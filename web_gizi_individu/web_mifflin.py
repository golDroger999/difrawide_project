import streamlit as st 
import sys 

sys.path.append('')
from datetime import date
from rumus_gizi.rumus_mifflin import mifflin
from rumus_makan.makan_mifflin import makan_mifflin
from docxtpl import DocxTemplate

def web_mifflin():
    with st.form('mifflin'):
        
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
            aktivitas = st.number_input('faktor aktivitas')
            
        with kolom_usia  :
            usia   = st.number_input('masukan usia',1)
            stress = st.number_input('faktor stress')
        
         
         
        data = mifflin(bb=berat, tb=tinggi, usia=usia, jenis_kelamin=gender)
        imt = data.imt()
        bbi = data.bbi()
        bmr =  data.bmr()
        energi = data.total_energi(aktivitas=aktivitas, stress=stress)
        
        protein      = data.protein(aktivitas=aktivitas, stress=stress)
        lemak        = data.lemak(aktivitas=aktivitas, stress=stress)
        karbohidrat  = data.karbohidrat(aktivitas=aktivitas, stress=stress)
        # cairan       = data.cairan()
        
        energi_pagi       = makan_mifflin(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).EnergiPagi()
        protein_pagi      = makan_mifflin(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).ProteinPagi()
        lemak_pagi        = makan_mifflin(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).LemakPagi()
        kharbohidrat_pagi = makan_mifflin(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).KharbohidratPagi()
        
        energi_siang       = makan_mifflin(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).EnergiSiang()
        protein_siang      = makan_mifflin(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).ProteinSiang()
        lemak_siang        = makan_mifflin(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).LemakSiang()
        kharbohidrat_siang = makan_mifflin(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).KharbohidratSiang()
        
        energi_malam       = makan_mifflin(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).EnergiMalam()
        protein_malam      = makan_mifflin(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).ProteinMalam()
        lemak_malam        = makan_mifflin(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).LemakMalam()
        kharbohidrat_malam = makan_mifflin(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).KharbohidratMalam()

         
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
            # st.error('SEDANG DALAM PENGEMBANGAN')
            
            if gender == 'pria':
                plus = 5
            
            elif gender == 'wanita':
                plus = 161
                
            doc = DocxTemplate('web_gizi_individu/MIFFLIN.docx')
            
            context = {
                    'nama'    : nama, 
                    'usia'    : f'{usia} ',
                    'tanggal': tanggal,
                    'sex'     : gender , 
                    'berat'   : f'{berat} ', 
                    'tinggi'  : f'{tinggi} ',
                    
                    
                    'bbi'     : bbi,
                    'imt'     : imt,
                    'bmr'       : bmr,
                    'aktivitas' : aktivitas,
                    'energi'       : energi, 
                    'protein' : f'{protein}',
                    'lemak'   : f'{lemak}',
                    'kharbo'  : f'{karbohidrat}',
                    'plus'    : plus,
                    # 'cairan'  : f"{cairan}",
                    
                    
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
            

            