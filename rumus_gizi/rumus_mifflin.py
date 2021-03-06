class mifflin():
    
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
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
            
        return round(bmr,2)
    
    
    
    
    def total_energi(self, aktivitas, stress):
        
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * aktivitas * stress
        
        return round(total_energi,2)
    
    
    
    def protein(self, aktivitas, stress):
        
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * aktivitas * stress
        
        protein = (0.15 * total_energi)/4
        
        return round(protein,2)
    
    
    
    def lemak(self, aktivitas, stress):
        
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * aktivitas * stress
        
        lemak = (0.25 * total_energi)/9
        
        return round(lemak,2)
    
    
    
    def karbohidrat(self, aktivitas, stress):
        
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * aktivitas * stress
        
        karbohidrat = (0.65 * total_energi)/4
        
        return round(karbohidrat,2)
    
    

    
    