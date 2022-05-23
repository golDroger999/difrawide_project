import sys

sys.path.append("")

from rumus_gizi.rumus_gizi_dubois import dubois


############## RUMUS KEBUTUHAN GIZI SEKALI MAKAN DUBOIS ######################## 
class makan_pagi_dubois():
    
    def energi(bb, tb, usia, sex, aktivitas, tidur):
        total_energi = dubois(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        te = total_energi.total_energi(aktivitas=aktivitas, tidur=tidur)
        energi = 0.35 * te
        return round(energi,2)

    def protein(bb, tb, usia, sex, aktivitas, tidur):
        total_protein = dubois(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tp = total_protein.protein(aktivitas=aktivitas, tidur=tidur)
        protein = 0.35 * tp
        return round(protein,2) 

    def lemak(bb, tb, usia, sex, aktivitas, tidur):
        total_lemak = dubois(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tl = total_lemak.lemak(aktivitas=aktivitas, tidur=tidur)
        lemak = 0.35 * tl
        return round(lemak,2)
    
    def kharbohidrat(bb, tb, usia, sex, aktifitas, tidur):
        total_karbohidrat = dubois(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tk = total_karbohidrat.karbohidrat(aktivitas=aktifitas, tidur=tidur)
        karbohidat = 0.35 * tk
        return round(karbohidat,2)




class makan_siang_dubois():
    
    def energi(bb, tb, usia, sex, aktivitas, tidur):
        total_energi = dubois(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        te = total_energi.total_energi(aktivitas=aktivitas, tidur=tidur)
        energi = 0.35 * te
        return round(energi,2)

    def protein(bb, tb, usia, sex, aktivitas, tidur):
        total_protein = dubois(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tp = total_protein.protein(aktivitas=aktivitas, tidur=tidur)
        protein = 0.35 * tp
        return round(protein,2) 

    def lemak(bb, tb, usia, sex, aktivitas, tidur):
        total_lemak = dubois(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tl = total_lemak.lemak(aktivitas=aktivitas, tidur=tidur)
        lemak = 0.35 * tl
        return round(lemak,2)
    
    def kharbohidrat(bb, tb, usia, sex, aktivitas, tidur):
        total_karbohidrat = dubois(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tk = total_karbohidrat.karbohidrat(aktivitas=aktivitas, tidur=tidur)
        karbohidat = 0.35 * tk
        return round(karbohidat,2)


 
class makan_malam_dubois():
    
    def energi(bb, tb, usia, sex, aktivitas, tidur):
        total_energi = dubois(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        te = total_energi.total_energi(aktivitas=aktivitas, tidur=tidur)
        energi = 0.30 * te
        return round(energi,2)

    def protein(bb, tb, usia, sex, aktivitas, tidur):
        total_protein = dubois(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tp = total_protein.protein(aktivitas=aktivitas, tidur=tidur)
        protein = 0.30 * tp
        return round(protein,2) 

    def lemak(bb, tb, usia, sex, aktivitas, tidur):
        total_lemak = dubois(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tl = total_lemak.lemak(aktivitas=aktivitas, tidur=tidur)
        lemak = 0.30 * tl
        return round(lemak,2)
    
    def kharbohidrat(bb, tb, usia, sex, aktifitas, tidur):
        total_karbohidrat = dubois(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tk = total_karbohidrat.karbohidrat(aktivitas=aktifitas, tidur=tidur)
        karbohidat = 0.30 * tk
        return round(karbohidat,2)

