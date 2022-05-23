import streamlit as st 


def dashboard():
    
    bb, tb , imt = st.columns(3)
    
    with bb:
        bb = st.metric('BERAT BADAN', value=0, delta_color="inverse")
        bbi = st.metric('BERAT BADAN IDEAL', value=0, delta_color="inverse")
    
    with tb:
        tb = st.metric('TINGGI BADAN', value=0, delta_color="inverse" )
        energi =  st.metric('ENERGI', value=0, delta_color='inverse')
        
    with imt: 
        imt = st.metric('INDEKS MASSA TUBUH', value=0, delta_color='inverse')
        protein = st.metric('PROTEIN', value=0, delta_color='inverse')
        
    
    