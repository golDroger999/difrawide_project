import pandas as pd
import numpy as np  


class dubois():

    def __init__(self, bb=None, tb=None, usia=None, jenis_kelamin=None):
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
            bmr = 1 * 24 * bbi
        
        elif self.jenis_kelamin == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        return round(bmr,2)



    def koreksi_tidur(self, tidur=8):
        if self.jenis_kelamin == 'pria': 
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita': 
            bbi = 0.9 * (self.tb - 100) 
        
        koreksi_tidur   = 0.1 * tidur * bbi
        
        return round(koreksi_tidur,2)



    def c_kalori(self, tidur=8):
        if self.jenis_kelamin == 'pria': 
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        
        if self.jenis_kelamin == 'pria': 
            bmr = 1 * 24 * bbi
        
        elif self.jenis_kelamin == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori        = bmr - koreksi_tidur
        
        return round(c_kalori,2)



    def aktivitas(self, aktivitas=0.50, tidur=8):
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        if self.jenis_kelamin == 'pria':
            bmr = 1 * 24 * bbi
        
        elif self.jenis_kelamin == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori   = bmr - koreksi_tidur
        aktivitas  = aktivitas * c_kalori
        
        return round(aktivitas,2)



    def e_kalori(self, tidur=8, aktivitas=0.50):
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        
        if self.jenis_kelamin == 'pria':
            bmr = 1 * 24 * bbi
        
        elif self.jenis_kelamin == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori  = bmr - koreksi_tidur
        aktivitas = aktivitas * c_kalori
        e_kalori  = c_kalori + aktivitas
        
        return round(e_kalori,2)



    def sda(self, tidur=8, aktivitas=0.50):
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita': 
            bbi = 0.9 * (self.tb - 100)
        
        
        if self.jenis_kelamin == 'pria':
            bmr = 1 * 24 * bbi
        
        elif self.jenis_kelamin == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori  = bmr - koreksi_tidur
        aktivitas = aktivitas * c_kalori
        e_kalori  = c_kalori + aktivitas
        sda       = 0.1 * e_kalori
        
        return round(sda,2)



    def total_energi(self, aktivitas=0.50, tidur=8):
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        
        if self.jenis_kelamin == 'pria':
            bmr = 1 * 24 * bbi
        
        elif self.jenis_kelamin == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda
        
        return round(total_energi,2)



    def protein(self, tidur=8, aktivitas=0.50):
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        
        if self.jenis_kelamin == 'pria':
            bmr = 1 * 24 * bbi
        
        elif self.jenis_kelamin == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        koreksi_tidur= 0.1 * tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda
        protein      = (0.15 * total_energi)/4
        
        return round(protein,2)



    def lemak(self,tidur=8, aktivitas=0.50):
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
       
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100)
       
       
        if self.jenis_kelamin == 'pria':
            bmr = 1 * 24 * bbi
       
        elif self.jenis_kelamin == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        koreksi_tidur   = 0.1 * tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda
        lemak        = (0.25 * total_energi)/9
        
        return round(lemak,2)
        


    def karbohidrat(self,tidur=8, aktivitas=0.50):
        if self.jenis_kelamin == 'pria'    :
            bbi = 0.9 * (self.tb - 100)
        
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        
        if self.jenis_kelamin == 'pria'    : 
            bmr = 1 * 24 * bbi
        
        elif self.jenis_kelamin == 'wanita':
            bmr = 0.90 * 24 * bbi
        
        koreksi_tidur= 0.1 * tidur * bbi
        c_kalori     = bmr - koreksi_tidur
        aktivitas    = aktivitas * c_kalori
        e_kalori     = c_kalori + aktivitas
        sda          = 0.1 * e_kalori
        total_energi = e_kalori + sda        
        karbohidrat  = (0.65 * total_energi)/4 
        
        return round(karbohidrat,2)



    def cairan(self):
        if self.jenis_kelamin == 'pria':
            bbi = 0.9 * (self.tb - 100)
        elif self.jenis_kelamin == 'wanita':
            bbi = 0.9 * (self.tb - 100)
        
        cairan = (bbi * 50)/1000
        
        return cairan
        




    def imt_group(self): 
        imt_group = self.bb / (self.tb/100)**2
        return imt_group



    def bbi_group(self):    
        bbi_pria    = 0.9 * (self.tb - 100)
        bbi_wanita  = 0.9 * (self.tb - 100)
        
        bbi_coice   = [
            (self.jenis_kelamin == 'pria'), 
            (self.jenis_kelamin == 'wanita')
            ]
        
        bbi_formula = [bbi_pria, bbi_wanita]
        result_bbi  = np.select(bbi_coice, bbi_formula)
        
        return result_bbi



    def bmr_group(self):
        bbi_pria    = 0.9 * (self.tb - 100)
        bbi_wanita  = 0.9 * (self.tb - 100)
        
        bbi_coice   = [
            (self.jenis_kelamin == 'pria'), 
            (self.jenis_kelamin == 'wanita')
            ]
        
        bbi_formula = [bbi_pria, bbi_wanita]
        result_bbi  = np.select(bbi_coice, bbi_formula)
        
        bmr_pria    = 1 * 24 * result_bbi
        bmr_wanita  = 0.90 * 24 * result_bbi
        
        bmr_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bmr_formula = [bmr_pria, bmr_wanita]
        result_bmr  = np.select(bmr_coice, bmr_formula)
        
        return result_bmr
        


    def koreksi_tidur_group(self, tidur=8):
        bbi_pria    = 0.9 * (self.tb - 100)
        bbi_wanita  = 0.9 * (self.tb - 100)
        
        bbi_coice   = [
            (self.jenis_kelamin == 'pria'), 
            (self.jenis_kelamin == 'wanita')
            ]
        
        bbi_formula = [bbi_pria, bbi_wanita]
        result_bbi  = np.select(bbi_coice, bbi_formula)
        koreksi_tidur_group   = 0.1 * tidur * result_bbi
        
        return koreksi_tidur_group



    def c_kalori_group(self, tidur=8):
        bbi_pria    = 0.9 * (self.tb - 100)
        bbi_wanita  = 0.9 * (self.tb - 100)
        
        bbi_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bbi_formula = [bbi_pria, bbi_wanita]
        result_bbi  = np.select(bbi_coice, bbi_formula)
        
        bmr_pria    = 1 * 24 * result_bbi
        bmr_wanita  = 0.90 * 24 * result_bbi
        
        bmr_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bmr_formula = [bmr_pria, bmr_wanita]
        result_bmr  = np.select(bmr_coice, bmr_formula)
        koreksi_tidur_group   = 0.1 * tidur * result_bbi
        c_kalori_group  = result_bmr - koreksi_tidur_group
        
        return c_kalori



    def aktivitas_group(self, tidur=8 ,aktivitas=0.50):
        bbi_pria    = 0.9 * (self.tb - 100)
        bbi_wanita  = 0.9 * (self.tb - 100)
        
        bbi_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bbi_formula = [bbi_pria, bbi_wanita]
        result_bbi  = np.select(bbi_coice, bbi_formula)
        
        bmr_pria    = 1 * 24 * result_bbi
        bmr_wanita  = 0.90 * 24 * result_bbi
        
        bmr_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bmr_formula = [bmr_pria, bmr_wanita]
        result_bmr  = np.select(bmr_coice, bmr_formula)
        koreksi_tidur_group   = 0.1 * tidur * result_bbi
        c_kalori_group        = result_bmr - koreksi_tidur_group
        aktivitas_group       = aktivitas * c_kalori_group
        
        return aktivitas_group



    def e_kalori_group(self, tidur=8, aktivitas=0.50):
        bbi_pria    = 0.9 * (self.tb - 100)
        bbi_wanita  = 0.9 * (self.tb - 100)
        
        bbi_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bbi_formula = [bbi_pria, bbi_wanita]
        result_bbi  = np.select(bbi_coice, bbi_formula)
        
        bmr_pria    = 1 * 24 * result_bbi
        bmr_wanita  = 0.90 * 24 * result_bbi
        
        bmr_coice   = [(self.jenis_kelamin == 'pria'), 
                       (self.jenis_kelamin == 'wanita')
                       ]
        
        bmr_formula = [bmr_pria, bmr_wanita]
        result_bmr  = np.select(bmr_coice, bmr_formula)
        koreksi_tidur_group   = 0.1 * tidur * result_bbi
        c_kalori_group = result_bmr - koreksi_tidur_group
        aktivitas_group  = aktivitas * c_kalori_group
        e_kalori_group = c_kalori_group + aktivitas_group
        
        return e_kalori_group



    def sda_group(self, tidur=8, aktivitas=0.50):
        bbi_pria    = 0.9 * (self.tb - 100)
        bbi_wanita  = 0.9 * (self.tb - 100)
        
        bbi_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bbi_formula = [bbi_pria, bbi_wanita]
        result_bbi  = np.select(bbi_coice, bbi_formula)
        
        bmr_pria    = 1 * 24 * result_bbi
        bmr_wanita  = 0.90 * 24 * result_bbi
        
        bmr_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bmr_formula = [bmr_pria, bmr_wanita]
        result_bmr  = np.select(bmr_coice, bmr_formula)
        koreksi_tidur_group   = 0.1 * tidur * result_bbi
        c_kalori_group = result_bmr - koreksi_tidur_group
        aktivitas_group  = aktivitas * c_kalori_group
        e_kalori_group = c_kalori_group + aktivitas_group
        sda_group             = 0.1 * e_kalori_group
       
        return sda_group



    def total_energi_group(self, tidur =8, aktivitas=0.50):
        bbi_pria    = 0.9 * (self.tb - 100)
        bbi_wanita  = 0.9 * (self.tb - 100)
        
        bbi_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bbi_formula = [bbi_pria, bbi_wanita]
        result_bbi  = np.select(bbi_coice, bbi_formula)
        
        bmr_pria    = 1 * 24 * result_bbi
        bmr_wanita  = 0.90 * 24 * result_bbi
        
        bmr_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bmr_formula = [bmr_pria, bmr_wanita]
        result_bmr  = np.select(bmr_coice, bmr_formula)
        koreksi_tidur_group   = 0.1 * tidur * result_bbi
        c_kalori_group = result_bmr - koreksi_tidur_group
        aktivitas_group  = aktivitas * c_kalori_group
        e_kalori_group = c_kalori_group + aktivitas_group
        sda_group = 0.1 * e_kalori_group
        total_energi_group  = e_kalori_group + sda_group
        
        return total_energi_group



    def protein_group(self, tidur=8, aktivitas=0.50):
        bbi_pria    = 0.9 * (self.tb - 100)
        bbi_wanita  = 0.9 * (self.tb - 100)
        
        bbi_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bbi_formula = [bbi_pria, bbi_wanita]
        result_bbi  = np.select(bbi_coice, bbi_formula)
        bmr_pria    = 1 * 24 * result_bbi
        bmr_wanita  = 0.90 * 24 * result_bbi
        
        bmr_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bmr_formula = [bmr_pria, bmr_wanita]
        result_bmr  = np.select(bmr_coice, bmr_formula)
        koreksi_tidur_group   = 0.1 * tidur * result_bbi
        c_kalori_group = result_bmr - koreksi_tidur_group
        aktivitas_group  = aktivitas * c_kalori_group
        e_kalori_group = c_kalori_group + aktivitas_group
        sda_group = 0.1 * e_kalori_group
        total_energi_group    = e_kalori_group + sda_group
        protein_group     = (0.15 * total_energi_group)/4
        
        return protein_group



    def lemak_group(self, tidur=8, aktivitas=0.50):
        bbi_pria    = 0.9 * (self.tb - 100)
        bbi_wanita  = 0.9 * (self.tb - 100)
        
        bbi_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bbi_formula = [bbi_pria, bbi_wanita]
        result_bbi  = np.select(bbi_coice, bbi_formula)
        
        bmr_pria    = 1 * 24 * result_bbi
        bmr_wanita  = 0.90 * 24 * result_bbi
        
        bmr_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bmr_formula = [bmr_pria, bmr_wanita]
        result_bmr  = np.select(bmr_coice, bmr_formula)
        koreksi_tidur_group   = 0.1 * tidur * result_bbi
        c_kalori_group = result_bmr - koreksi_tidur_group
        aktivitas_group  = aktivitas * c_kalori_group
        e_kalori_group = c_kalori_group + aktivitas_group
        sda_group = 0.1 * e_kalori_group
        total_energi_group  = e_kalori_group + sda_group
        lemak_group       = (0.25 * total_energi_group)/9
        
        return lemak_group



    def karbohidrat_group(self, tidur = 8, aktivitas=0.50):
        bbi_pria    = 0.9 * (self.tb - 100)
        bbi_wanita  = 0.9 * (self.tb - 100)
        
        bbi_coice   = [
            (self.jenis_kelamin == 'pria'), 
            (self.jenis_kelamin == 'wanita')
            ]
        
        bbi_formula = [bbi_pria, bbi_wanita]
        result_bbi  = np.select(bbi_coice, bbi_formula)
        
        bmr_pria    = 1 * 24 * result_bbi
        bmr_wanita  = 0.90 * 24 * result_bbi
        
        bmr_coice   = [
            (self.jenis_kelamin == 'pria'),
            (self.jenis_kelamin == 'wanita')
            ]
        
        bmr_formula = [bmr_pria, bmr_wanita]
        result_bmr  = np.select(bmr_coice, bmr_formula)
        koreksi_tidur_group   = 0.1 * tidur * result_bbi
        c_kalori_group = result_bmr - koreksi_tidur_group
        aktivitas_group  = aktivitas * c_kalori_group
        e_kalori_group = c_kalori_group + aktivitas_group
        sda_group = 0.1 * e_kalori_group
        total_energi_group  = e_kalori_group + sda_group
        karbohidrat_group = (0.65 * total_energi_group)/4 
        
        return karbohidrat_group
    
