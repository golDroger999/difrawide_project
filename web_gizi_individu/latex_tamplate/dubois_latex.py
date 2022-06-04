import streamlit as st


def bbi(tb, hasil):
    rumus = st.latex(r'''
    BBI = TB - 100 × 0,9             
    ''')
    hitung = st.latex(f'''
    BBI = {tb} - 100 × 0,9 = {hasil} kg
    ''')
    

def imt(bb, tb, hasil):
    tb_m = tb /100
    
    rumus = st.latex(r'''
    \frac {BB}{TB (meter)^2}                 
    ''')
    hitung = st.latex(f'''
    IMT = {bb} / {tb_m}^2 = {hasil}
    ''')


def bmr(sex, bbi, hasil):
    if sex == 'pria':
        code = 1
        rumus = st.latex(r'''
        BMR = 1 × 24 jam × BBI
        ''')
            
    elif sex == 'wanita':
        code = 0.9
        rumus = st.latex(r'''
        BMR = 0.9 × 24 jam × BBI
        ''')
    
    BMR = st.latex(f'''
    BMR = {code} × 24 jam × {bbi} = {hasil}           
    ''')
         
    
def energi(bbi, persen_aktifitas, waktu_tidur, sex, hasil_bmr):
    st.subheader('RUMUS MENCARI ENEGRI DALAM RUMUS DUBOIS')
    
    # menghitung bmr 
    if sex == 'pria':
        code = 1
        rumus = st.markdown(r'''
        BMR = 1 × 24 jam × BBI (A)
        ''')
            
    elif sex == 'wanita':
        code = 0.9
        rumus = st.latex(r'''
        BMR = 0.9 × 24 jam × BBI (A)
        ''')
    
    # BMR = st.markdown(f'''
    # BMR = {code} × 24 jam × {bbi} = {hasil_bmr} (A)           
    # ''')
    
    #menghitung koreksi tidur
    koreksi_tidur_rumus = st.markdown(r'''
    KOREKSI TIDUR = 10% × lama tidur(jam) × BBI (B)
    ''')
    
    c = st.markdown(r'''
    C = (A) - (B) atau BMR - KOREKSI TIDUR (C)
    ''')
    
    aktivitas = st.markdown(r'''
    AKTIVITAS = % aktivitas × C (D) 
    ''')
    return 0
    


energi(bbi=57, persen_aktifitas=0.5, waktu_tidur=8, sex='pria', hasil_bmr=1340)