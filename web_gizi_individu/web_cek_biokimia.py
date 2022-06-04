import streamlit as st
from rumus_gizi.cek_biokimia import cek_biokimia

def web_cek_biokimia():    
    with st.form('cek biokimia'):
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

