import streamlit as st 
from docxtpl import DocxTemplate
from datetime import date 

import sys 

sys.path.append('')

from rumus_gizi.rumus_gizi_assesmen import AssesmenGizi 
from rumus_makan.makan_assesmen import makan_assesmen
from rumus_gizi.cek_biokimia import cek_biokimia
    
    
def web_individu_form_dietetik():
    
    with st.form('form dietetik penyakit'):
        st.subheader('DATA ANTROPOMETRI')
        
        with st.expander('DATA ANTROPOMETRI'):
        
            max_width_str = f"max-width: 10000px;"
            st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""",
            unsafe_allow_html=True,)     


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
                stress = st.number_input('faktor stress',1.00)


            with kolom_usia  :
                usia   = st.number_input('masukan usia',1)
                aktivitas = st.number_input('faktor aktivitas',1.00)
            
        

            data = AssesmenGizi(bb=berat, tb=tinggi, jenis_kelamin=gender, usia =usia)
            imt = data.imt()
            bbi = data.bbi()
            bee =  data.bee()
            tee = data.tee(aktivitas=aktivitas, stress=stress)      
    
            protein = data.protein(aktivitas=aktivitas, stress=stress)
            lemak = data.lemak(aktivitas=aktivitas, stress=stress)
            karbohidrat = data.karbohidrat(aktivitas=aktivitas, stress=stress)
            cairan = data.cairan()
            
            energi_pagi       = makan_assesmen(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).EnergiPagi()
            protein_pagi      = makan_assesmen(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).ProteinPagi()
            lemak_pagi        = makan_assesmen(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).LemakPagi()
            kharbohidrat_pagi = makan_assesmen(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas, stress=stress).KharbohidratPagi()
        
            
            energi_siang       = makan_assesmen(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas,stress=stress).EnergiSiang()
            protein_siang      = makan_assesmen(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas,stress=stress).ProteinSiang()
            lemak_siang        = makan_assesmen(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas,stress=stress).LemakSiang()
            kharbohidrat_siang = makan_assesmen(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas,stress=stress).KharbohidratSiang()
    
    
            energi_malam       = makan_assesmen(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas,stress=stress).EnergiMalam()
            protein_malam      = makan_assesmen(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas,stress=stress).ProteinMalam()
            lemak_malam        = makan_assesmen(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas,stress=stress).LemakMalam()
            kharbohidrat_malam = makan_assesmen(bb=berat, tb=tinggi, usia=usia, sex=gender, aktivitas=aktivitas,stress=stress).KharbohidratMalam()
            
            
            if st.form_submit_button('ANALISA'):
                
                
                
                    st.write('''---------------------------------''')
                    st.subheader('HASIL PERHITUNGAN KEBUTUHAN GIZI')
                    st.write('''---------------------------------''')
    
                    
                    hasil1, hasil2 = st.columns(2)
                    with hasil1:
                        st.subheader('ANTROPOMETRI')
                        berat_badan = st.success(f'BERAT BADAN : {berat} kg')
                        berat_badan = st.success(f'TINGGI BADAN : {tinggi} cm')
                        jenis_kelamin = st. success(f'GENDER/SEX : {gender}') 
                        umur = st.success(f'UMUR : {usia} tahun')
                        imt = st.success(f'IMT : {imt}')
                        bbi = st.success(f'BBI : {bbi}')
                        
                    
                    with hasil2:
                        st.subheader('KEBUTUHAN GIZI')
                        st.success(f'BEE : {bee}')
                        st.success(f'TEE : {tee}')
                        st.success(f'PROTEIN : {protein}')
                        st.success(f'LEMAK : {lemak}') 
                        st.success(f'KHARBOHIDRAT : {karbohidrat}')
                        st.success(f'KEBUTUHAN CAIRAN : {cairan}')
                    
                    
                    
                    st.write('-------------------------')
                    st.subheader('KEBUTUHAN GIZI SEKALI MAKAN')    
                    # st.write('-------------------------')
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
                
        
        st.write('-------------------------')
        
        
        
        
        st.subheader('CEK BIOKIMIA')
        with st.expander('CEK BIOKIMIA'):
            
            kolomHB, kolomGLUKOSA, kolomKOLESTEROL = st.columns(3)
            
            with kolomHB:
                hb = st.number_input('HB')
                cek = st.form_submit_button('CEK HB') 
                if cek:
                    st.error('SEDANG DALAM PENGEMBANGAN')

            with kolomGLUKOSA:
                glukosa = st.number_input('GLUKOSA mg/dl', 0)
                cek = st.form_submit_button('CEK GUKOSA') 
                if cek:
                    hasil = cek_biokimia.cek_glukosa(glukosa=glukosa)
                    st.success(hasil)
        
            with kolomKOLESTEROL:
                kolesterol = st.number_input('KOLESTEROL TOTAL mg/dl', 0)
                cek = st.form_submit_button('CEK KOLESTEROL') 
                if cek:
                    hasil = cek_biokimia.cek_kolesterol(kolesterol=kolesterol)
                    st.success(hasil)
                    
                    
            kolomALBUMIN, kolomSGOT, kolomSGPT = st.columns(3)
        
            with kolomALBUMIN:
                albumin = st.number_input('ALBUMIN g/dl')
                cek = st.form_submit_button('CEK ALBUMIN') 
                if cek:
                    hasil = cek_biokimia.cek_albumin(albumin)
                    st.success(hasil)

            with kolomSGOT:
                sgot = st.number_input('SGOT')
                cek = st.form_submit_button('CEK SGOT') 
                if cek:
                    st.error('SEDANG DALAM PENGEMBANGAN')
        
            with kolomSGPT:
                sgpt = st.number_input('SGPT')
                cek = st.form_submit_button('CEK SGPT') 
                if cek:
                    st.error('SEDANG DALAM PENGEMBANGAN')
                    
            kolomKOLESTEROL_LDL, kolomKOLESTEROL_HDL, kolomGLUKOSA_PUASA  = st.columns(3)
            
            with kolomKOLESTEROL_LDL:
                ldl = st.number_input('KOLESTEROL LDL mg/dl', 0)
                cek = st.form_submit_button('CEK KOLESTEROL LDL')
                if cek:
                    hasil = cek_biokimia.ldl(ldl)
                    st.success(hasil)
                
            with kolomKOLESTEROL_HDL:
                hdl = st.number_input('KOLESTEROL HDL mg/dl', 0)
                cek = st.form_submit_button('CEK KOLESTEROL HDL') 
            
            with kolomGLUKOSA_PUASA:
                gpuasa = st.number_input('GLUKOSA PUASA', 0)
                cek = st.form_submit_button('CEK GLUKOSA PUASA') 
                
            
        
        st.write('-------------------------')
       
       
       
        
        st.subheader('DATA KLINIS ')
        with st.expander('DATA KLINIS '):
            
            kolom1, kolom2 = st.columns(2)
            with kolom1:
                antropometri = st.text_area('antropometri')
                biokimia     = st.text_area('biokimia')
                riwayat_diet = st.text_area('riwayat dietary')
                fisik_klinis = st.text_area('fisik klinis')
                riwayat_individu = st.text_area('riwayat individu')

            with kolom2:
                perbandinga_antropometri = st.text_area('perbandingan antropometri normal')
                perbandingan_biokimia    = st.text_area('perbandingan biokimia normal')
                perbandingan_diet        = st.text_area('perbandingan riwayat dietary')
                perbandingan_klinis      = st.text_area('perbandingan fisik klinis normal')
                perbandingan_riwayat_individu = st.text_area('perbandingan riwayat individu normal ')


            st.write('-------------------------')
            st.subheader('PERMASALAHAN KLINIS')
            
            kolom3, kolom4 = st.columns(2)

            with kolom3:
                 masalah_antropometri = st.text_area('permasalahan antropometri') 
                 masalah_biokimia = st.text_area('permasalahan biokimia')
                 masalah_diet = st.text_area('permasalahan riwayat gizi/diet')


            with kolom4:
                masalah_klinis = st.text_area('permasalahan fisik klinis')
                masalah_individu = st.text_area('permasalahan riwayat individu')     

        
            
        st.write('---------------------------')
        
        
        
        
        st.subheader('DIAGNOSA GIZI') 
        with st.expander('DIAGNOSA GIZI'):   
            kolom5 , kolom6, kolom7 = st.columns(3)
            with kolom5: 
                problem = st.text_area('problem')

            with kolom6: 
                etiologi = st.text_area('etiologi')

            with kolom7: 
                gejala = st.text_area('gejala')
                
                
            
        st.write('------------------------------')
       
       
       
       
        st.subheader('INTERVENSI GIZI') 
        with st.expander('INTERVENSI GIZI'):
            kolom8, kolom9 = st.columns(2)
            with kolom8: 
                p = st.text_area('P (problem)')
                e = st.text_area('E (etiologi)')
                s = st.text_area('S (Sign/Simptom)')

            with kolom9:
                p_intervensi = st.text_area('(P) intervensi')
                e_intervensi = st.text_area('(E) intervensi')
                s_intervensi = st.text_area('(S) intervensi')


                
        st.write('-------------------------')
        
        
        
        
        st.subheader('RENCANA DIET ')
        
        with st.expander('RENCANA DIET'):
            kolom10, kolom11 = st.columns(2)
            with kolom10: 
                penyakit   = st.text_input('penyakit')

            with kolom11 :
                jenis_diet = st.text_input('jenis diet untuk pasien')

            kolom12, kolom13, kolom14 = st.columns(3)
            with kolom12: 
                jalur_pemberian = st.text_input('jalur pemberian')


            with kolom13: 
                frekuensi = st.number_input('frekuensi',1)

            with kolom14:
                bentuk_makanan = st.text_input('bentuk makanan')

            kolom15, kolom16 = st.columns(2)
            with kolom15:
                tujuan_diet = st.text_area('tujuan diet')

            with kolom16: 
                syarat_diet  = st.text_area('syarat diet')
            
            prinsip_diet = st.text_area('penjelasan diet')
        

        st.write('-------------------------')

        
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
        
        if st.form_submit_button('LAPORAN'):
            doc = DocxTemplate('ASSASMEN GIZI.docx')
            
            context = {
                
                    'nama'    : nama, 
                    'usia'    : f'{usia} ',
                    'tanggal': tanggal,
                    'sex'     : gender , 
                    'berat'   : f'{berat} ', 
                    'tinggi'  : f'{tinggi} ',
                    
                    
                    'antropometri' : antropometri,
                    'biokimia' : biokimia,
                    'riwayat_diet' : riwayat_diet,
                    'fisik_klinis' : fisik_klinis,
                    'riwayat_individu' : riwayat_individu,
                    
                    
                    'antropometri_normal' : perbandinga_antropometri,
                    'biokimia_normal' : perbandingan_biokimia,
                    'riwayatdiet_normal' : perbandingan_diet,
                    'fisikklinis_normal' : perbandingan_klinis,
                    'individu_normal' : perbandingan_riwayat_individu,
                    
                    
                    'masalah_antro' : masalah_antropometri,
                    'malalah_biokimia' : masalah_biokimia,
                    'masalah_diet' : masalah_diet,
                    'masalah_klinis' : masalah_klinis,
                    'masalah_individu' : masalah_individu,
                    
                    
                    'problem' : problem,
                    'etiologi' : etiologi,
                    'gejala' : gejala,
                    
                    
                    'p' : p,
                    'e' : e,
                    's' : s,
                    
                    
                    'p_intervensi' : p_intervensi,
                    'e_intervensi' : e_intervensi,
                    's_intervensi' : s_intervensi,
                    
                    
                    'penyakkit' : penyakit,
                    'jenis_diet' : jenis_diet,
                    'tujuan_diet' : tujuan_diet,
                    'syarat_diet' : syarat_diet,
                    'jalur_pemberian' : jalur_pemberian,
                    'frekuensi' : frekuensi,
                    'bentuk' : bentuk_makanan,
                    'prinsip' : prinsip_diet,
                    
                    
                    'bbi'     : bbi,
                    'imt'     : imt,
                    'beecode' : beecode,
                    'bbparam' : bbparam,
                    'tbparam' : tbparam,
                    'usiaparam' : usiaparam,
                    
                    
                    'bee'       : bee,
                    'aktivitas' : aktivitas,
                    'stress'    : stress,
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
            doc.save(f'{nama}.docx')
            st.success('SUKSES MEMBUAT LAPORAN')

