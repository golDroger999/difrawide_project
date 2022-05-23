class wanita_hamil():
    
    def __init__(self, bb=None, tb=None, usia=None, usia_kehamilan=None, trimester=None):
        self.bb = bb 
        self.tb = tb 
        self.usia = usia 
        self.trimester = trimester
        self.usia_kehamilan = usia_kehamilan
        
        
    def lila(self):
        return 0


    def imt(self):
        imt = self.bb / (self.tb/100)**2
        return round(imt,2)



    def bbi(self):
        
        if self.tb >=160:
            bbi = self.tb - 110
            
        elif self.tb <=160: 
            bbi = self.tb - 105
        
        return round(bbi,2)
    
    
    
    def bbih(self):
        if self.tb >=160:
            bbi = self.tb - 110
            
        elif self.tb <=160: 
            bbi = self.tb - 105
        
        bbih = bbi + (self.usia_kehamilan * 0.35)
        return round(bbih,2)
        
        

    def bmr(self):
        if self.tb >=160:
            bbi = self.tb - 110
            
        elif self.tb <=160: 
            bbi = self.tb - 105
        
        bmr = 0.90 * 24 * bbi
        return round(bmr,2)



    def koreksi_tidur(self, tidur=8):
        if self.tb >=160:
            bbi = self.tb - 110
            
        elif self.tb <=160: 
            bbi = self.tb - 105
         
        koreksi_tidur   = 0.1 * tidur * bbi
        return round(koreksi_tidur,2)



    def c_kalori(self, tidur=8):
        if self.tb >=160:
            bbi = self.tb - 110
            
        elif self.tb <=160: 
            bbi = self.tb - 105
        
        bmr = 0.90 * 24 * bbi
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori        = bmr - koreksi_tidur
        return round(c_kalori,2)



    def aktivitas(self, aktivitas=0.50, tidur=8):
        if self.tb >=160:
            bbi = self.tb - 110
            
        elif self.tb <=160: 
            bbi = self.tb - 105
        
        bmr = 0.90 * 24 * bbi
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori   = bmr - koreksi_tidur
        aktivitas  = aktivitas * c_kalori
        return round(aktivitas,2)



    def e_kalori(self, tidur=8, aktivitas=0.50):
        if self.tb >=160:
            bbi = self.tb - 110
            
        elif self.tb <=160: 
            bbi = self.tb - 105
        
        bmr = 0.90 * 24 * bbi        
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori  = bmr - koreksi_tidur
        aktivitas = aktivitas * c_kalori
        e_kalori  = c_kalori + aktivitas
        return round(e_kalori,2)



    def sda(self, tidur=8, aktivitas=0.50):
        if self.tb >=160:
            bbi = self.tb - 110
            
        elif self.tb <=160: 
            bbi = self.tb - 105
        
        bmr = 0.90 * 24 * bbi
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori  = bmr - koreksi_tidur
        aktivitas = aktivitas * c_kalori
        e_kalori  = c_kalori + aktivitas
        sda       = 0.1 * e_kalori
        return round(sda,2)



    def total_energi(self, aktivitas=0.50, tidur=8):
        if self.tb >=160:
            bbi = self.tb - 110
            
        elif self.tb <=160: 
            bbi = self.tb - 105
        
        bmr = 0.90 * 24 * bbi
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda
        
        if self.trimester == 'TRI SEMESTER 1':
            total_energi = total_energi + 180
            
        elif self.trimester == 'TRI SEMESTER 2':
            total_energi = total_energi + 300
        
        elif self.trimester == 'TRI SEMESTER 3':
            total_energi = total_energi + 300
            
        return round(total_energi,2)



    def protein(self, tidur=8, aktivitas=0.50):
        if self.tb >=160:
            bbi = self.tb - 110
            
        elif self.tb <=160: 
            bbi = self.tb - 105
        
        bmr = 0.90 * 24 * bbi
        koreksi_tidur= 0.1 * tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda
        
        if self.trimester == 'TRI SEMESTER 1':
            total_energi = total_energi + 180
            
        elif self.trimester == 'TRI SEMESTER 2':
            total_energi = total_energi + 300
        
        elif self.trimester == 'TRI SEMESTER 3':
            total_energi = total_energi + 300
        
        protein      = (0.15 * total_energi)/4   
        
        if self.trimester == 'TRI SEMESTER 1':
            protein = protein + 1
            
        elif self.trimester == 'TRI SEMESTER 2':
            protein = protein + 10
        
        elif self.trimester == 'TRI SEMESTER 3':
            protein = protein + 30 
        
        return round(protein,2)



    def lemak(self,tidur=8, aktivitas=0.50):
        if self.tb >=160:
            bbi = self.tb - 110
            
        elif self.tb <=160: 
            bbi = self.tb - 105
        
        bmr = 0.90 * 24 * bbi
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda
        
        if self.trimester == 'TRI SEMESTER 1':
            total_energi = total_energi + 180
            
        elif self.trimester == 'TRI SEMESTER 2':
            total_energi = total_energi + 300
        
        elif self.trimester == 'TRI SEMESTER 3':
            total_energi = total_energi + 300
        
        lemak        = (0.25 * total_energi)/9
        
        if self.trimester == 'TRI SEMESTER 1':
            lemak = lemak + 2.3
            
        elif self.trimester == 'TRI SEMESTER 2':
            lemak = lemak + 2.3
        
        elif self.trimester == 'TRI SEMESTER 3':
            lemak = lemak + 2.3
            
        return round(lemak,2)
        


    def karbohidrat(self,tidur=8, aktivitas=0.50):
        if self.tb >=160:
            bbi = self.tb - 110
            
        elif self.tb <=160: 
            bbi = self.tb - 105
        
        bmr = 0.90 * 24 * bbi
        koreksi_tidur= 0.1 * tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda  
        
        if self.trimester == 'TRI SEMESTER 1':
            total_energi = total_energi + 180
            
        elif self.trimester == 'TRI SEMESTER 2':
            total_energi = total_energi + 300
        
        elif self.trimester == 'TRI SEMESTER 3':
            total_energi = total_energi + 300
              
        karbohidrat  = (0.65 * total_energi)/4 
        
        if self.trimester == 'TRI SEMESTER 1':
            karbohidrat = karbohidrat + 25
            
        elif self.trimester == 'TRI SEMESTER 2':
            karbohidrat = karbohidrat + 40
        
        elif self.trimester == 'TRI SEMESTER 3':
            karbohidrat = karbohidrat + 40
        
        return round(karbohidrat,2)



    def cairan(self):
        if self.tb >=160:
            bbi = self.tb - 110
            
        elif self.tb <=160: 
            bbi = self.tb - 105
        
        cairan = (bbi * 50)/1000
        
        return cairan





class makan_pagi_hamil():
    
    def energi(bb, tb, usia, trimester, usia_kehamilan, aktifitas, tidur):
        total_energi = wanita_hamil(bb=bb, tb=tb, usia=usia, trimester=trimester, usia_kehamilan=usia_kehamilan)
        te = total_energi.total_energi(aktivitas=aktifitas, tidur=tidur)
        energi = 0.35 * te
        return round(energi,2)

    def protein(bb, tb, usia, trimester, usia_kehamilan, aktifitas, tidur):
        total_protein = wanita_hamil(bb=bb, tb=tb, usia=usia, trimester=trimester, usia_kehamilan=usia_kehamilan)
        tp = total_protein.protein(aktivitas=aktifitas, tidur=tidur)
        protein = 0.35 * tp
        return round(protein,2) 

    def lemak(bb, tb, usia, trimester, usia_kehamilan, aktifitas, tidur):
        total_lemak = wanita_hamil(bb=bb, tb=tb, usia=usia, trimester=trimester, usia_kehamilan=usia_kehamilan)
        tl = total_lemak.lemak(aktivitas=aktifitas, tidur=tidur)
        lemak = 0.35 * tl
        return round(lemak,2)
    
    def kharbohidrat(bb, tb, usia, trimester, usia_kehamilan, aktifitas, tidur):
        total_karbohidrat = wanita_hamil(bb=bb, tb=tb, usia=usia, trimester=trimester, usia_kehamilan=usia_kehamilan)
        tk = total_karbohidrat.karbohidrat(aktivitas=aktifitas, tidur=tidur)
        karbohidat = 0.35 * tk
        return round(karbohidat,2)




class makan_siang_hamil():
    
    def energi(bb, tb, usia, trimester, usia_kehamilan, aktifitas, tidur):
        total_energi = wanita_hamil(bb=bb, tb=tb, usia=usia, trimester=trimester, usia_kehamilan=usia_kehamilan)
        te = total_energi.total_energi(aktivitas=aktifitas, tidur=tidur)
        energi = 0.35 * te
        return round(energi,2)

    def protein(bb, tb, usia, trimester, usia_kehamilan, aktifitas, tidur):
        total_protein = wanita_hamil(bb=bb, tb=tb, usia=usia, trimester=trimester, usia_kehamilan=usia_kehamilan)
        tp = total_protein.protein(aktivitas=aktifitas, tidur=tidur)
        protein = 0.35 * tp
        return round(protein,2) 

    def lemak(bb, tb, usia, trimester, usia_kehamilan, aktifitas, tidur):
        total_lemak = wanita_hamil(bb=bb, tb=tb, usia=usia, trimester=trimester, usia_kehamilan=usia_kehamilan)
        tl = total_lemak.lemak(aktivitas=aktifitas, tidur=tidur)
        lemak = 0.35 * tl
        return round(lemak,2)
    
    def kharbohidrat(bb, tb, usia, trimester, usia_kehamilan, aktifitas, tidur):
        total_karbohidrat = wanita_hamil(bb=bb, tb=tb, usia=usia, trimester=trimester, usia_kehamilan=usia_kehamilan)
        tk = total_karbohidrat.karbohidrat(aktivitas=aktifitas, tidur=tidur)
        karbohidat = 0.35 * tk
        return round(karbohidat,2)


 
class makan_malam_hamil():
    
    def energi(bb, tb, usia, trimester, usia_kehamilan, aktifitas, tidur):
        total_energi = wanita_hamil(bb=bb, tb=tb, usia=usia, trimester=trimester, usia_kehamilan=usia_kehamilan)
        te = total_energi.total_energi(aktivitas=aktifitas, tidur=tidur)
        energi = 0.30 * te
        return round(energi,2)

    def protein(bb, tb, usia, trimester, usia_kehamilan, aktifitas, tidur):
        total_protein = wanita_hamil(bb=bb, tb=tb, usia=usia, trimester=trimester, usia_kehamilan=usia_kehamilan)
        tp = total_protein.protein(aktivitas=aktifitas, tidur=tidur)
        protein = 0.30 * tp
        return round(protein,2) 

    def lemak(bb, tb, usia, trimester, usia_kehamilan, aktifitas, tidur):
        total_lemak = wanita_hamil(bb=bb, tb=tb, usia=usia, trimester=trimester, usia_kehamilan=usia_kehamilan)
        tl = total_lemak.lemak(aktivitas=aktifitas, tidur=tidur)
        lemak = 0.30 * tl
        return round(lemak,2)
    
    def kharbohidrat(bb, tb, usia, trimester, usia_kehamilan, aktifitas, tidur):
        total_karbohidrat = wanita_hamil(bb=bb, tb=tb, usia=usia, trimester=trimester, usia_kehamilan=usia_kehamilan)
        tk = total_karbohidrat.karbohidrat(aktivitas=aktifitas, tidur=tidur)
        karbohidat = 0.30 * tk
        return round(karbohidat,2)
