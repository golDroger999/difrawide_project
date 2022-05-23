class perkeni():
    
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
            bmr = 30 * bbi
        
        elif self.jenis_kelamin == 'wanita':
            bmr = 25 * bbi
        
        return round(bmr,2)



    
    def total_energi(self, aktivitas, faktor_usia):
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        if self.jenis_kelamin == 'pria'   :
            bmr = 30 * bbi
        
        elif self.jenis_kelamin == 'wanita':
            bmr = 25 * bbi
        
        energi = (bmr + aktivitas) - faktor_usia
        
        return round(energi,2)
    
    
    
    
    
    def protein(self, aktivitas, faktor_usia):
        
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        if self.jenis_kelamin == 'pria'   :
            bmr = 30 * bbi
        
        elif self.jenis_kelamin == 'wanita':
            bmr = 25 * bbi
        
        energi = (bmr + aktivitas) - faktor_usia
    
        protein = (0.15 * energi)/4
        
        return round(protein,2)
    
    
    
    
    
    def lemak(self, aktivitas, faktor_usia):
    
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        if self.jenis_kelamin == 'pria'   :
            bmr = 30 * bbi
        
        elif self.jenis_kelamin == 'wanita':
            bmr = 25 * bbi
        
        energi = (bmr + aktivitas) - faktor_usia

        lemak = (0.25 * energi)/9
        
        return round(lemak,2)
    
    
    
    
    def karbohidrat(self, aktivitas, faktor_usia):
    
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        if self.jenis_kelamin == 'pria'   :
            bmr = 30 * bbi
        
        elif self.jenis_kelamin == 'wanita':
            bmr = 25 * bbi
        
        energi = (bmr + aktivitas) - faktor_usia

        karbohidrat = (0.65 * energi)/4
        
        return round(karbohidrat,2)

    