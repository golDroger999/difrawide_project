class wanita_menyusui():
    def __init__(self, bb=None, tb=None, usia=None, lama_menyusui=None):
        self.bb = bb 
        self.tb = tb 
        self.usia = usia 
        self.lama_menyusui = lama_menyusui



    def imt(self):
        imt = self.bb / (self.tb/100)**2
        return round(imt,2)



    def bbi(self):
        bbi = 0.9 * (self.tb - 100) 
        return round(bbi,2)



    def bmr(self):
        bbi = 0.9 * (self.tb - 100) 
        bmr = 0.90 * 24 * bbi
        return round(bmr,2)



    def koreksi_tidur(self, tidur=8):
        bbi = 0.9 * (self.tb - 100)     
        koreksi_tidur   = 0.1 * tidur * bbi
        return round(koreksi_tidur,2)



    def c_kalori(self, tidur=8):
        bbi = 0.9 * (self.tb - 100)    
        bmr = 0.90 * 24 * bbi
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori        = bmr - koreksi_tidur
        return round(c_kalori,2)



    def aktivitas(self, aktivitas=0.50, tidur=8):
        bbi = 0.9 * (self.tb - 100)
        bmr = 0.90 * 24 * bbi
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori   = bmr - koreksi_tidur
        aktivitas  = aktivitas * c_kalori
        return round(aktivitas,2)



    def e_kalori(self, tidur=8, aktivitas=0.50):
        bbi = 0.9 * (self.tb - 100)    
        bmr = 0.90 * 24 * bbi
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori  = bmr - koreksi_tidur
        aktivitas = aktivitas * c_kalori
        e_kalori  = c_kalori + aktivitas
        return round(e_kalori,2)



    def sda(self, tidur=8, aktivitas=0.50):
        bbi = 0.9 * (self.tb - 100)
        bmr = 0.90 * 24 * bbi
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori  = bmr - koreksi_tidur
        aktivitas = aktivitas * c_kalori
        e_kalori  = c_kalori + aktivitas
        sda       = 0.1 * e_kalori        
        return round(sda,2)



    def total_energi(self, aktivitas=0.50, tidur=8):
        bbi = 0.9 * (self.tb - 100)    
        bmr = 0.90 * 24 * bbi
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda
        
        if self.lama_menyusui == '6 BULAN PERTAMA':
            total_energi = total_energi + 330
            
        elif self.lama_menyusui == '6 BULAN KEDUA':
            total_energi = total_energi + 400
        return round(total_energi,2)



    def protein(self, tidur=8, aktivitas=0.50):
        bbi = 0.9 * (self.tb - 100)
        bmr = 0.90 * 24 * bbi
        koreksi_tidur= 0.1 * tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda
        
        if self.lama_menyusui == '6 BULAN PERTAMA':
            total_energi = total_energi + 330
            
        elif self.lama_menyusui == '6 BULAN KEDUA':
            total_energi = total_energi + 400
        
        
        protein      = (0.15 * total_energi)/4
        
        if self.lama_menyusui == '6 BULAN PERTAMA':
            protein = protein + 20
            
        elif self.lama_menyusui == '6 BULAN KEDUA':
            protein = protein + 15
        
        return round(protein,2)



    def lemak(self,tidur=8, aktivitas=0.50):
        bbi = 0.9 * (self.tb - 100)
        bmr = 0.90 * 24 * bbi
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda
        
        if self.lama_menyusui == '6 BULAN PERTAMA':
            total_energi = total_energi + 330
            
        elif self.lama_menyusui == '6 BULAN KEDUA':
            total_energi = total_energi + 400
        
        lemak        = (0.25 * total_energi)/9
        
        if self.lama_menyusui == '6 BULAN PERTAMA':
            lemak = lemak + 2.2
            
        elif self.lama_menyusui == '6 BULAN KEDUA':
            lemak = lemak + 2.2
        
        return round(lemak,2)
        


    def karbohidrat(self,tidur=8, aktivitas=0.50):
        bbi = 0.9 * (self.tb - 100)
        bmr = 0.90 * 24 * bbi
        koreksi_tidur= 0.1 * tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda        
        
        if self.lama_menyusui == '6 BULAN PERTAMA':
            total_energi = total_energi + 330
            
        elif self.lama_menyusui == '6 BULAN KEDUA':
            total_energi = total_energi + 400
        
        karbohidrat  = (0.65 * total_energi)/4 
        
        if self.lama_menyusui == '6 BULAN PERTAMA':
            karbohidrat = karbohidrat + 45
            
        elif self.lama_menyusui == '6 BULAN KEDUA':
            karbohidrat = karbohidrat + 55
        
        return round(karbohidrat,2)



    def cairan(self):
        bbi = 0.9 * (self.tb - 100)
        cairan = (bbi * 50)/1000
        return cairan
    
    

class makan_pagi_menyusui():
    
    def energi(bb, tb, usia, lama_menyusui, aktifitas, tidur):
        total_energi = wanita_menyusui(bb=bb, tb=tb, usia=usia, lama_menyusui=lama_menyusui)
        te = total_energi.total_energi(aktivitas=aktifitas, tidur=tidur)
        energi = 0.35 * te
        return round(energi,2)

    def protein(bb, tb, usia, lama_menyusui, aktifitas, tidur):
        total_protein = wanita_menyusui(bb=bb, tb=tb, usia=usia, lama_menyusui=lama_menyusui)
        tp = total_protein.protein(aktivitas=aktifitas, tidur=tidur)
        protein = 0.35 * tp
        return round(protein,2) 

    def lemak(bb, tb, usia, lama_menyusui, aktifitas, tidur):
        total_lemak = wanita_menyusui(bb=bb, tb=tb, usia=usia, lama_menyusui=lama_menyusui)
        tl = total_lemak.lemak(aktivitas=aktifitas, tidur=tidur)
        lemak = 0.35 * tl
        return round(lemak,2)
    
    def kharbohidrat(bb, tb, usia, lama_menyusui, aktifitas, tidur):
        total_karbohidrat = wanita_menyusui(bb=bb, tb=tb, usia=usia, lama_menyusui=lama_menyusui)
        tk = total_karbohidrat.karbohidrat(aktivitas=aktifitas, tidur=tidur)
        karbohidat = 0.35 * tk
        return round(karbohidat,2)




class makan_siang_menyusui():
    
    def energi(bb, tb, usia, lama_menyusui, aktifitas, tidur):
        total_energi = wanita_menyusui(bb=bb, tb=tb, usia=usia, lama_menyusui=lama_menyusui)
        te = total_energi.total_energi(aktivitas=aktifitas, tidur=tidur)
        energi = 0.35 * te
        return round(energi,2)

    def protein(bb, tb, usia, lama_menyusui, aktifitas, tidur):
        total_protein = wanita_menyusui(bb=bb, tb=tb, usia=usia, lama_menyusui=lama_menyusui)
        tp = total_protein.protein(aktivitas=aktifitas, tidur=tidur)
        protein = 0.35 * tp
        return round(protein,2) 

    def lemak(bb, tb, usia, lama_menyusui, aktifitas, tidur):
        total_lemak = wanita_menyusui(bb=bb, tb=tb, usia=usia, lama_menyusui=lama_menyusui)
        tl = total_lemak.lemak(aktivitas=aktifitas, tidur=tidur)
        lemak = 0.35 * tl
        return round(lemak,2)
    
    def kharbohidrat(bb, tb, usia, lama_menyusui, aktifitas, tidur):
        total_karbohidrat = wanita_menyusui(bb=bb, tb=tb, usia=usia, lama_menyusui=lama_menyusui)
        tk = total_karbohidrat.karbohidrat(aktivitas=aktifitas, tidur=tidur)
        karbohidat = 0.35 * tk
        return round(karbohidat,2)


 
class makan_malam_menyusui():
    
    def energi(bb, tb, usia, lama_menyusui, aktifitas, tidur):
        total_energi = wanita_menyusui(bb=bb, tb=tb, usia=usia, lama_menyusui=lama_menyusui)
        te = total_energi.total_energi(aktivitas=aktifitas, tidur=tidur)
        energi = 0.30 * te
        return round(energi,2)

    def protein(bb, tb, usia, lama_menyusui, aktifitas, tidur):
        total_protein = wanita_menyusui(bb=bb, tb=tb, usia=usia, lama_menyusui=lama_menyusui)
        tp = total_protein.protein(aktivitas=aktifitas, tidur=tidur)
        protein = 0.30 * tp
        return round(protein,2) 

    def lemak(bb, tb, usia, lama_menyusui, aktifitas, tidur):
        total_lemak = wanita_menyusui(bb=bb, tb=tb, usia=usia, lama_menyusui=lama_menyusui)
        tl = total_lemak.lemak(aktivitas=aktifitas, tidur=tidur)
        lemak = 0.30 * tl
        return round(lemak,2)
    
    def kharbohidrat(bb, tb, usia, lama_menyusui, aktifitas, tidur):
        total_karbohidrat = wanita_menyusui(bb=bb, tb=tb, usia=usia, lama_menyusui=lama_menyusui)
        tk = total_karbohidrat.karbohidrat(aktivitas=aktifitas, tidur=tidur)
        karbohidat = 0.30 * tk
        return round(karbohidat,2)
