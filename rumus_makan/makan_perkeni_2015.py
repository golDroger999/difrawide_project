import sys
sys.path.append('')

from rumus_gizi.rumus_perkeni_2015 import perkeni


class makan_perkeni_2015():
    
    def energi_pagi(bb, tb, usia, jenis_kelamin, aktivitas, faktor_usia):
        total_energi = perkeni(bb=bb, tb=tb, usia=usia, jenis_kelamin=jenis_kelamin,)
        te = total_energi.total_energi(aktivitas=aktivitas, faktor_usia=faktor_usia)
        energi = 0.35 * te
        return round(energi,2)
    
    def protein_pagi(bb, tb, usia, jenis_kelamin, aktivitas, faktor_usia):
        total_protein = perkeni(bb=bb, tb=tb, usia=usia, jenis_kelamin=jenis_kelamin,)
        tp = total_protein.protein(aktivitas=aktivitas, faktor_usia=faktor_usia)
        protein = 0.35 * tp
        return round(protein,2)
    
    def lemak_pagi(bb, tb, usia, jenis_kelamin, aktivitas, faktor_usia):
        total_lemak = perkeni(bb=bb, tb=tb, usia=usia, jenis_kelamin=jenis_kelamin,)
        tl = total_lemak.lemak(aktivitas=aktivitas, faktor_usia=faktor_usia)
        lemak = 0.35 * tl
        return round(lemak,2)
    
    def karbohidrat_pagi(bb, tb, usia, jenis_kelamin, aktivitas, faktor_usia):
        total_karbohidrat = perkeni(bb=bb, tb=tb, usia=usia, jenis_kelamin=jenis_kelamin,)
        tk = total_karbohidrat.karbohidrat(aktivitas=aktivitas, faktor_usia=faktor_usia)
        karbohidrat = 0.35 * tk
        return round(karbohidrat,2)
    
    
    
    def energi_siang(bb, tb, usia, jenis_kelamin, aktivitas, faktor_usia):
        total_energi = perkeni(bb=bb, tb=tb, usia=usia, jenis_kelamin=jenis_kelamin,)
        te = total_energi.total_energi(aktivitas=aktivitas, faktor_usia=faktor_usia)
        energi = 0.35 * te
        return round(energi,2)
    
    def protein_siang(bb, tb, usia, jenis_kelamin, aktivitas, faktor_usia):
        total_protein = perkeni(bb=bb, tb=tb, usia=usia, jenis_kelamin=jenis_kelamin,)
        tp = total_protein.protein(aktivitas=aktivitas, faktor_usia=faktor_usia)
        protein = 0.35 * tp
        return round(protein,2)
    
    def lemak_siang(bb, tb, usia, jenis_kelamin, aktivitas, faktor_usia):
        total_lemak = perkeni(bb=bb, tb=tb, usia=usia, jenis_kelamin=jenis_kelamin,)
        tl = total_lemak.lemak(aktivitas=aktivitas, faktor_usia=faktor_usia)
        lemak = 0.35 * tl
        return round(lemak,2)
    
    def karbohidrat_siang(bb, tb, usia, jenis_kelamin, aktivitas, faktor_usia):
        total_karbohidrat = perkeni(bb=bb, tb=tb, usia=usia, jenis_kelamin=jenis_kelamin,)
        tk = total_karbohidrat.karbohidrat(aktivitas=aktivitas, faktor_usia=faktor_usia)
        karbohidrat = 0.35 * tk
        return round(karbohidrat,2)
            
        
    
    
    def energi_malam(bb, tb, usia, jenis_kelamin, aktivitas, faktor_usia):
        total_energi = perkeni(bb=bb, tb=tb, usia=usia, jenis_kelamin=jenis_kelamin,)
        te = total_energi.total_energi(aktivitas=aktivitas, faktor_usia=faktor_usia)
        energi = 0.30 * te
        return round(energi,2)
    
    def protein_malam(bb, tb, usia, jenis_kelamin, aktivitas, faktor_usia):
        total_protein = perkeni(bb=bb, tb=tb, usia=usia, jenis_kelamin=jenis_kelamin,)
        tp = total_protein.protein(aktivitas=aktivitas, faktor_usia=faktor_usia)
        protein = 0.30 * tp
        return round(protein,2)
    
    def lemak_malam(bb, tb, usia, jenis_kelamin, aktivitas, faktor_usia):
        total_lemak = perkeni(bb=bb, tb=tb, usia=usia, jenis_kelamin=jenis_kelamin,)
        tl = total_lemak.lemak(aktivitas=aktivitas, faktor_usia=faktor_usia)
        lemak = 0.30 * tl
        return round(lemak,2)
    
    def karbohidrat_malam(bb, tb, usia, jenis_kelamin, aktivitas, faktor_usia):
        total_karbohidrat = perkeni(bb=bb, tb=tb, usia=usia, jenis_kelamin=jenis_kelamin,)
        tk = total_karbohidrat.karbohidrat(aktivitas=aktivitas, faktor_usia=faktor_usia)
        karbohidrat = 0.30 * tk
        return round(karbohidrat,2)
    
    
    