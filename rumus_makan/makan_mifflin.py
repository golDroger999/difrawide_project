########### RUMUS KEBUTUHAN GIZI SEKALI MAKAN HARRIS BENEDICT ###############
class makan_mifflin():
    def __init__(self, bb=None, tb=None, usia=None, sex=None, aktivitas=None, stress=None):
        self.bb = bb 
        self.tb = tb 
        self.usia = usia 
        self.jenis_kelamin = sex
        self.aktivitas = aktivitas
        self.stress = stress

    
    
    def EnergiPagi(self):
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        energi = 0.35 * total_energi
        
        return round(energi,2)



    def ProteinPagi(self):
       
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        protein = (0.15 * total_energi)/4
        
        protein = 0.35 * protein
        
        return round(protein,2) 



    def LemakPagi(self):
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        lemak = (0.25 * total_energi)/9
        
        lemak = 0.35 * lemak
        
        return round(lemak,2)
    
    
    
    def KharbohidratPagi(self):
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        karbohidrat = (0.65 * total_energi)/4
         
        karbohidat = 0.35 * karbohidrat
         
        return round(karbohidat,2)
    
    
    
    def EnergiSiang(self):
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        energi = 0.35 * total_energi
        
        return round(energi,2)



    def ProteinSiang(self):
       
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        protein = (0.15 * total_energi)/4
        
        protein = 0.35 * protein
        
        return round(protein,2) 



    def LemakSiang(self):
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        lemak = (0.25 * total_energi)/9
        
        lemak = 0.35 * lemak
        
        return round(lemak,2)
    
    
    
    def KharbohidratSiang(self):
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        karbohidrat = (0.65 * total_energi)/4
         
        karbohidat = 0.35 * karbohidrat
         
        return round(karbohidat,2)
    
    
    def EnergiMalam(self):
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        energi = 0.30 * total_energi
        
        return round(energi,2)



    def ProteinMalam(self):
       
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        protein = (0.15 * total_energi)/4
        
        protein = 0.30 * protein
        
        return round(protein,2) 



    def LemakMalam(self):
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        lemak = (0.25 * total_energi)/9
        
        lemak = 0.30 * lemak
        
        return round(lemak,2)
    
    
    
    def KharbohidratMalam(self):
        if self.jenis_kelamin == 'pria':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) + 5        
    
        elif self.jenis_kelamin == 'wanita':
            bmr = (10 * self.bb) + (6.25 * self.tb) - (5 * self.usia) - 161
        
        total_energi = bmr * self.aktivitas * self.stress
        
        karbohidrat = (0.65 * total_energi)/4
         
        karbohidat = 0.30 * karbohidrat
         
        return round(karbohidat,2)
    
    