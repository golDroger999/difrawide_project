import streamlit as st



bb = 75
tb = 167
tb_m = 1.67
usia = 23
aktivitas = 0.5


#menghitung bbi
with st.expander('CARA MENGHITUNG BERAT BADAN IDEAL'):
    BBI = st.latex(r'''
    BBI = {TB} - 100 × 0.9  
    ''')
    
    st.latex(f'''
    BBI = {tb} - 100 × 0.9 = 57
    ''')

#menghitung imt
with st.expander('CARA MENGHITUNG INDEKS MASSA TUBUH'):
    IMT = st.latex(r'''
    IMT = \frac {BB}  {TB(meter) ^2}              
    ''')
    
    st.latex(f'''
    IMT = {bb} / {tb_m}^2 
    = 19.0          
    ''')
    