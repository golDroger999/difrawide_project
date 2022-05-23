import sys

sys.path.append("")

from rumus_gizi.rumus_gizi_ginjal import gizi_ginjal


class makan_pagi_ginjal():
    
    def energi(bb, tb, usia, sex):
        total_energi = gizi_ginjal(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        te = total_energi.total_energi()
        energi = 0.35 * te
        return round(energi,2)

    def protein(bb, tb, usia, sex, kondisi):
        total_protein = gizi_ginjal(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tp = total_protein.protein(kondisi=kondisi)
        protein = 0.35 * tp
        return round(protein,2) 

    def lemak(bb, tb, usia, sex):
        total_lemak = gizi_ginjal(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tl = total_lemak.lemak()
        lemak = 0.35 * tl
        return round(lemak,2)
    
    def kharbohidrat(bb, tb, usia, sex):
        total_karbohidrat = gizi_ginjal(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tk = total_karbohidrat.karbohidrat()
        karbohidat = 0.35 * tk
        return round(karbohidat,2)




class makan_siang_ginjal():
    
    def energi(bb, tb, usia, sex):
        total_energi = gizi_ginjal(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        te = total_energi.total_energi()
        energi = 0.35 * te
        return round(energi,2)

    def protein(bb, tb, usia, sex, kondisi):
        total_protein = gizi_ginjal(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tp = total_protein.protein(kondisi=kondisi)
        protein = 0.35 * tp
        return round(protein,2) 

    def lemak(bb, tb, usia, sex):
        total_lemak = gizi_ginjal(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tl = total_lemak.lemak()
        lemak = 0.35 * tl
        return round(lemak,2)
    
    def kharbohidrat(bb, tb, usia, sex):
        total_karbohidrat = gizi_ginjal(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tk = total_karbohidrat.karbohidrat()
        karbohidat = 0.35 * tk
        return round(karbohidat,2)


 
class makan_malam_ginjal():
    
    def energi(bb, tb, usia, sex):
        total_energi = gizi_ginjal(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        te = total_energi.total_energi()
        energi = 0.30 * te
        return round(energi,2)

    def protein(bb, tb, usia, sex, kondisi):
        total_protein = gizi_ginjal(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tp = total_protein.protein(kondisi=kondisi)
        protein = 0.30 * tp
        return round(protein,2) 

    def lemak(bb, tb, usia, sex):
        total_lemak = gizi_ginjal(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tl = total_lemak.lemak()
        lemak = 0.30 * tl
        return round(lemak,2)
    
    def kharbohidrat(bb, tb, usia, sex):
        total_karbohidrat = gizi_ginjal(bb=bb, tb=tb, usia=usia, jenis_kelamin=sex)
        tk = total_karbohidrat.karbohidrat()
        karbohidat = 0.30 * tk
        return round(karbohidat,2)

