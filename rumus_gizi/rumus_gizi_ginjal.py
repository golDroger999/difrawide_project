class gizi_ginjal():
    
    def __init__(self, bb, tb, usia, jenis_kelamin):
        self.bb = bb
        self.tb = tb
        self.usia = usia
        self.jenis_kelamin = jenis_kelamin
        
        
        
            
    def imt(self):
        imt = self.bb / (self.tb/100)**2
        return round(imt,2)




    def bbi(self):
        
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100) 
        
        return round(bbi,2)
    
    
    
    
    def bmr(self):
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        if self.jenis_kelamin == 'pria'   :
            bmr = 1 * 24 * bbi
        
        elif self.jenis_kelamin == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        return round(bmr,2)
    
    
    
     
    def total_energi(self):
        
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100) 
        
        
        if self.usia <= 60: 
            energi = 35 * bbi
            
        elif self.usia > 60 :
            energi = 30 * bbi
            
        return round(energi, 2)
    
    
    
    
    
    def protein(self, kondisi):
        
        if kondisi == 'Haemodialisa':
            protein = 0.8 * self.bb
            
        elif kondisi == 'tanpa Haemodialisa':
            protein = 1.2 * self.bb
           
        return round(protein,2)
    
    
    
    
    
    def lemak(self):
        
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100) 
        
        
        if self.usia <= 60: 
            energi = 35 * bbi
            
        elif self.usia > 60 :
            energi = 35 * bbi
        
        lemak = lemak = (0.25 * energi)/9
        
        return round(lemak, 2)   
    
    
    
    
    def karbohidrat(self):

        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100) 
        
        
        if self.usia <= 60: 
            energi = 35 * bbi
            
        elif self.usia > 60 :
            energi = 35 * bbi
        
        karbohidrat = (0.65 * energi)/4
        
        return round(karbohidrat, 2)   