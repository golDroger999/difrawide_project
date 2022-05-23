import streamlit as st 
import pandas as pd
import numpy as np 
import plotly.express as px

import sys 

sys.path.append('')

from rumus_gizi.rumus_gizi_dubois import dubois


def kalkulasi_gizi_kelompok():
    # st.title('ANALISA GIZI KELOMPOK')
    st.info(
        
    
    
            '''
        
        *CATATAN* : perhitungan menggunakan rumus dubois, dengan koreksi tidur 8 jam, persen aktivitas 50% atau aktivitas sedang, sda 10 %
            
            untuk format kolom pada file csv : 
            1. kolom berat badan bernama bb, 
            2. kolom tinggi badan bernama tb, 
            3. kolom umur bernama usia, 
            4. kolom gender bernama jenis_kelamin(format pria dan wanita)
            5. menggunakan huruf kecil semua
    
    
            '''
)
    
    
    upload = st.file_uploader('masukan file berformat csv')
    if upload:
        read = pd.read_csv(upload)
        df   = pd.DataFrame(read)
        st.subheader('datasets')
        show, stats = st.columns(2)
        
        with show:
            show  = st.dataframe(df)

        with stats:
            stats = df.describe()
            stats = st.dataframe(stats)


        rumus = dubois(bb=df['bb'], tb=df['tb'], usia=df['usia'], jenis_kelamin=df['jenis_kelamin'])
        df['imt'] = rumus.imt_group()
        df['bbi'] = rumus.bbi_group()
        df['bmr'] = rumus.bmr_group()
        df['energi']     = rumus.total_energi_group()
        df['protein']    = rumus.protein_group()
        df['lemak']      = rumus.lemak_group()
        df['karbohidat'] = rumus.karbohidrat_group()
        
        
        data = [
                (df['imt'] <  18.5),
                (df['imt'] > 18.5 ) & (df['imt'] <= 25),
                (df['imt'] > 25 ) & (df['imt'] <= 30),
                (df['imt'] > 30 ) 
                ]

        value = ['kurus', 'ideal', 'gemuk', 'obesitas']
        status = np.select(data, value)
        df['status']=status     
        
        
        with st.expander('HASIL ANALISA'):
            st.subheader('hasil perhitungan')
            group = df.groupby('status')['bb', 'usia', 'tb'].agg(['mean', 'std'])
            stats = df.describe().T
            st.dataframe(df)
            st.dataframe(group)
            st.dataframe(stats)
            
            

        
        with st.expander('PLOTTING DATASETS'):
            st.header('PLOTTING DATASETS')

            fig = px.pie(df,  names='status')# pie plot status
            st.plotly_chart(fig)
            

            fig = px.pie(df, names='jenis_kelamin')# pie plot jenis kelamin
            st.plotly_chart(fig)
            
            fig = px.histogram(df,x='usia', facet_col='jenis_kelamin', color='jenis_kelamin')
            st.plotly_chart(fig)
            

            fig = px.scatter(df, x='usia', y='imt', color='status', facet_col='jenis_kelamin', size='imt')# scatterplot imt
            st.plotly_chart(fig)
            

            fig = px.box(df, x='status', y='usia', color='jenis_kelamin')# boxplot usia
            st.plotly_chart(fig)


            fig = px.box(df, x='status', y='bb', color='jenis_kelamin')# boxplot bb
            st.plotly_chart(fig)
            
            
            fig = px.box(df, x='status', y='tb', color='jenis_kelamin')# boxplot bb
            st.plotly_chart(fig)


            fig = px.box(df, x='jenis_kelamin', y='usia', color='status')# boxplot jenis kelamin
            st.plotly_chart(fig)
            
            
        
        

def psg_kelompok():
    upload =  st.file_uploader('silahkan masukan file berformat csv')
 
 
 
 
 
 
    