class cek_biokimia:
    
    def cek_hb(hb):
        # if hb < 13.0:
        #     hasil = 'NORMAL'
            
        # elif hb > 11:
            
            
            
        return 0 
    
    
    
    def cek_glukosa(glukosa=70):
        
        if glukosa <=1:
            hasil = 'TOLONG MASUKAN DATA DENGAN BENAR'
            
        elif glukosa > 1 and glukosa <=40:
            hasil = 'hasil : RENDAH... normal : 80 - 112 mg/dl'
        
        
        if glukosa >= 80 and glukosa <= 112:
            hasil = 'NORMAL'
        
        elif glukosa < 80 and glukosa >= 40:
            hasil = 'hasil : RENDAH... normal : 80 - 112 mg/dl'
        
        elif glukosa > 112:
            hasil = 'hasil : TINGGI... normal : 80 - 112 mg/dl'  
        
        return hasil
    
    
    
    def cek_albumin(albumin):
        
        if albumin >= 3.5 and albumin <=5.5:
            hasil = 'NORMAL'
            
        elif albumin > 5.5:
            hasil = 'HYPERALBUMINEMIA... normal : 3.5 - 5.5 g/dl'
            
        elif albumin < 3.5:
            hasil = 'HIPOALBUMINEMIA... normal : 3.5 - 5.5 g/dl'
        return hasil
    
    
    
    
    def cek_kolesterol(kolesterol):
        
        if kolesterol <= 200:
            hasil = 'NORMAL'
            
        elif kolesterol > 200 and kolesterol <=239:
            hasil = 'hasil : BATAS TINGGI... normal : <200 mg/dl'
            
        elif kolesterol > 239:
            hasil = 'hasil : TINGGI... normal : <200 mg/dl'
        
        return hasil
    
    
    
    def ldl(ldl):
        if ldl <= 100:
            hasil = "NORMAL" 
        
        elif ldl > 100 and ldl <=160:
            hasil = 'hasil : BATAS TINGGI... normal: < 100 mg/dl'
            
        elif ldl > 160:
            hasil = 'hasil : TINGGI... normal : < 100 mg/dl'
    
        return hasil
    
    
    
    
    def hdl(hdl):
        if hdl < 200:
            pass
        return 'masih dikembangkan'
    
    
    
    def cek_sgot(sgot):
        return 0
    
    
    
    def cek_sgpt(sgpt):
        return 0