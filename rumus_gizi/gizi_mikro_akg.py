class vitamin():
    
    def __init__(self, usia, jenis_kelamin):
        self.usia = usia 
        self.jenis_kelamin = jenis_kelamin
        
        
    def vitamin_a(self):
        if self.jenis_kelamin == 'pria':
            
            if self.usia <=10 and self.usia >=12:
                vitamin_a = f'{600} RE'
            
            elif self.usia <=13 and self.usia >=15:
                vitamin_a = f'{600} RE'
                
            elif self.usia <=16 and self.usia >=18:
                vitamin_a = f'{700} RE'
                
            elif self.usia <=16 and self.usia >=18:
                vitamin_a = f'{700} RE'
                
            elif self.usia > 29:
                vitamin_a = f'{650} RE'
                
        elif self.jenis_kelamin =='wanita':
            
            if self.usia <=10 and self.usia > 10:
              vitamin_a = f'{600} RE'
              
        return vitamin_a
    
    
    def vitamin_d(self):
        return 0