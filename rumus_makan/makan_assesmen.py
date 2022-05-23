
############### RUMUS KEBUTUHAN GIZI SEKALI MAKAN ASSASMEN GIZI ###############

class makan_assesmen():
    def __init__(self, bb=None, tb=None, usia=None, sex=None, aktivitas=None, stress=None):
        self.bb = bb 
        self.tb = tb 
        self.usia = usia 
        self.sex = sex
        self.aktivitas = aktivitas
        self.stress = stress

    
    
    def EnergiPagi(self):
        if self.sex == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
        
        elif self.sex == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
        
        tee = bmr * self.aktivitas * self.stress
        
        energi = 0.35 * tee
        
        return round(energi,2)



    def ProteinPagi(self):
        if self.sex == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
        
        elif self.sex == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
        
        tee = bmr * self.aktivitas * self.stress
        
        protein = (0.15 * tee)/4
        
        protein = 0.35 * protein
        
        return round(protein,2) 



    def LemakPagi(self):
        if self.sex == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
            
        elif self.sex == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
      
        tee = bmr * self.aktivitas * self.stress
          
        lemak = (0.25 * tee)/9
        
        lemak = 0.35 * lemak
        
        return round(lemak,2)
    
    
    
    def KharbohidratPagi(self):
         if self.sex == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
            
         elif self.sex == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
      
         tee = bmr * self.aktivitas * self.stress
              
         karbohidrat  = (0.65 * tee)/4 
         
         karbohidat = 0.35 * karbohidrat
         
         return round(karbohidat,2)
    
    
    
    def EnergiSiang(self):
        if self.sex == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
        
        elif self.sex == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
        
        tee = bmr * self.aktivitas * self.stress
        
        energi = 0.35 * tee
        
        return round(energi,2)



    def ProteinSiang(self):
        if self.sex == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
        
        elif self.sex == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
        
        tee = bmr * self.aktivitas * self.stress
        
        protein = (0.15 * tee)/4
        
        protein = 0.35 * protein
        
        return round(protein,2) 



    def LemakSiang(self):
        if self.sex == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
            
        elif self.sex == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
      
        tee = bmr * self.aktivitas * self.stress
          
        lemak = (0.25 * tee)/9
        
        lemak = 0.35 * lemak
        
        return round(lemak,2)
    
    
    
    def KharbohidratSiang(self):
         if self.sex == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
            
         elif self.sex == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
      
         tee = bmr * self.aktivitas * self.stress
              
         karbohidrat  = (0.65 * tee)/4 
         
         karbohidat = 0.35 * karbohidrat
         
         return round(karbohidat,2)
    
    
    def EnergiMalam(self):
        if self.sex == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
        
        elif self.sex == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
        
        tee = bmr * self.aktivitas * self.stress
        
        energi = 0.30 * tee
        
        return round(energi,2)



    def ProteinMalam(self):
        if self.sex == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
        
        elif self.sex == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
        
        tee = bmr * self.aktivitas * self.stress
        
        protein = (0.15 * tee)/4
        
        protein = 0.30 * protein
        
        return round(protein,2) 



    def LemakMalam(self):
        if self.sex == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
            
        elif self.sex == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
      
        tee = bmr * self.aktivitas * self.stress
          
        lemak = (0.25 * tee)/9
        
        lemak = 0.30 * lemak
        
        return round(lemak,2)
    
    
    
    def KharbohidratMalam(self):
         if self.sex == 'wanita':
            bmr = 655 + (9.6 * self.bb) + (1.8 * self.tb) - (4.7 * self.usia)
            
         elif self.sex == 'pria':
            bmr = 66 + (13.7 * self.bb) + (5 * self.tb) - (6.8 * self.usia)
      
         tee = bmr * self.aktivitas * self.stress
              
         karbohidrat  = (0.65 * tee)/4 
         
         karbohidat = 0.30 * karbohidrat
         
         return round(karbohidat,2)
