

class AssesmenGizi():
    
    def __init__(self, bb=None, tb=None, usia=None, jenis_kelamin=None):
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
    
    
    
    def bee(self):
        
        if self.jenis_kelamin == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
        
        elif self.jenis_kelamin == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
                        
        return round(bmr,2) 
            
            
    
    def tee(self, aktivitas, stress):
        
        if self.jenis_kelamin == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
        
        elif self.jenis_kelamin == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
        
        tee = bmr * aktivitas * stress
        
        return round(tee,2)
    
    
    
    def protein(self,  aktivitas, stress):
        if self.jenis_kelamin == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
        
        elif self.jenis_kelamin == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
        
        tee = bmr * aktivitas * stress
        
        protein = (0.15 * tee)/4
        
        return round(protein,2)



    def lemak(self, aktivitas, stress):
        
       if self.jenis_kelamin == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
            
       elif self.jenis_kelamin == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
      
       tee = bmr * aktivitas * stress
          
       lemak = (0.25 * tee)/9
        
       return round(lemak,2)
        


    def karbohidrat(self, aktivitas, stress):
        
        if self.jenis_kelamin == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
            
        elif self.jenis_kelamin == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
      
        tee = bmr * aktivitas * stress
              
        karbohidrat  = (0.65 * tee)/4 
        
        return round(karbohidrat,2)
    
    
    
    def cairan(self):
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        cairan = (bbi * 50)/1000
        
        return cairan
