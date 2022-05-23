import pandas as pd
import datetime as dt    
from datetime import date        
            
            
class psg():
    def __init__(self, umur, bb, pb_tb):

        self.umur = umur
        self.bb = bb 
        self.pb_tb = pb_tb 
     
     
     
     
    def bbu(self):
        bbudata  = pd.DataFrame(pd.read_csv('/home/gol/Documents/koding/difrawide_project/datasets/bbperu.csv'))
        umur     = pd.Series(bbudata['umur bulan'])
        min_1sd  = pd.Series(bbudata['-1 SD'])
        median   = pd.Series(bbudata['Median'])
        plus_1sd = pd.Series(bbudata['+1 SD'])
        dictbbu  = {'umur':umur, '-1sd':min_1sd, 'median':median, '+1sd':plus_1sd}
        usia     = list(dictbbu['umur'])
        plus1sd  = list(dictbbu['+1sd'])
        median   = list(dictbbu['median'])
        mins1sd  = list(dictbbu['-1sd'])
    
        umur = self.umur
        
        if self.bb < median[umur]:
            bbu = (self.bb - median[umur]) / (median[umur] - mins1sd[umur])
            z_score = bbu   
        
        elif self.bb > median[umur]:
            bbu = (self.bb - median[umur]) / (median[umur] - plus1sd[umur])
            z_score = bbu   
            
                 
        return round(z_score,2)




    def pb_tb_u(self):
        bbudata  = pd.DataFrame(pd.read_csv('/home/gol/Documents/koding/difrawide_project/datasets/pbtbperu.csv'))
        umur     = pd.Series(bbudata['umur bulan'])
        min_1sd  = pd.Series(bbudata['-1 SD'])
        median   = pd.Series(bbudata['Median'])
        plus_1sd = pd.Series(bbudata['+1 SD'])
        dictbbu  = {'umur':umur, '-1sd':min_1sd, 'median':median, '+1sd':plus_1sd}
        usia     = list(dictbbu['umur'])
        plus1sd  = list(dictbbu['+1sd'])
        median   = list(dictbbu['median'])
        mins1sd  = list(dictbbu['-1sd'])
        
        umur = self.umur
        
        if self.pb_tb < median[umur]:
            pbtb_u = (self.pb_tb - median[umur]) / (median[umur] - mins1sd[umur])
            z_score = pbtb_u
        
        elif self.pb_tb > median[umur]:
            pbtb_u = (self.pb_tb - median[umur]) / (median[umur] - plus1sd[umur])
            z_score = pbtb_u
        
        return round(z_score, 2)

  


    def bb_pb(self):
        bbudata  = pd.DataFrame(pd.read_csv('/home/gol/Documents/koding/difrawide_project/datasets/bbperpb.csv'))
        pb     = pd.Series(bbudata['panjang badan'])
        min_1sd  = pd.Series(bbudata['-1 SD'])
        median   = pd.Series(bbudata['Median'])
        plus_1sd = pd.Series(bbudata['+1 SD'])
        dictbbu  = {'panjang_badan':pb, '-1sd':min_1sd, 'median':median, '+1sd':plus_1sd}
        usia     = list(dictbbu['panjang_badan'])
        plus1sd  = list(dictbbu['+1sd'])
        median   = list(dictbbu['median'])
        mins1sd  = list(dictbbu['-1sd'])
        
        panjang_badan = self.pb_tb
        
        if self.bb < median[panjang_badan]:
            bbpb = (self.bb - median[panjang_badan]) / (median[panjang_badan] - mins1sd[panjang_badan])
            z_score = pbtb_u
        
        elif self.bb > median[panjang_badan]:
            bbpb = (self.bb - median[panjang_badan]) / (median[panjang_badan] - plus1sd[panjang_badan])
            z_score = bbpb
        
        return round(z_score, 2)   
    
    
    
        

print(f'hasil = {psg(umur=30, bb=5.7, pb_tb=92).bb_pb()}')
