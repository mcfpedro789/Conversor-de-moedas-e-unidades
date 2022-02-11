from graphics import *
import time
import requests
import pandas as pd
from datetime import datetime

############################################################ UNIDADES DE MEDIDA ##########################################################################

#################### MEDIDAS DE COMPRIMENTO ##############

## METRO

def m_cm(m):
    cm = m*100
    return cm

def m_km(m):
    km = m/1000
    return km

def m_mm(m):
    mm = m*1000
    return mm

def m_mi(m):
    mi = m/1609
    return mi

def m_yd(m):
    yd = m*1.094
    return yd

def m_ft(m):
    ft = m*3.281
    return ft

def m_in(m):
    inch = m*39.37
    return inch

def m_nm(m):
    nm = m/1852
    return nm

## QUILOMETRO

def km_m(km):
    m = km*1000
    return m

def km_cm(km):
    cm = km*100000
    return cm

def km_mi(km):
    mi = km/1.609
    return mi

def km_yd(km):
    yd = km*1094
    return yd

def km_ft(km):
    ft = km*3281
    return ft

def km_in(km):
    inch = km*39370
    return inch

def km_nm(km):
    nm = km/1.852
    return nm

## CENTIMETRO

def cm_km(cm):
    km = cm/100000
    return km

def cm_m(cm):
    m = cm/100
    return m

def cm_mm(cm):
    mm = cm*10
    return mm

def cm_yd(cm):
    yd = cm/91.44
    return yd

def cm_ft(cm):
    ft = cm/30.48
    return ft

def cm_in(cm):
    inch = cm/2.54
    return inch

## MILHA

def mi_km(mi):
    km = mi*1.609
    return km

def mi_m(mi):
    m = mi*1609
    return m

def mi_cm(mi):
    cm = mi*160934
    return cm

def mi_yd(mi):
    yd = mi*1760
    return yd

def mi_ft(mi):
    ft = mi*5280
    return ft

def mi_in(mi):
    inch = mi*63360
    return inch

def mi_nm(mi):
    nm = mi/1.151
    return nm

## MILIMETRO

def mm_m(mm):
    m = mm/1000
    return m

def mm_cm(mm):
    cm = mm/10
    return cm

def mm_ft(mm):
    ft = mm/305
    return ft

def mm_in(mm):
    inch = mm/25.4
    return inch

## JARDA

def yd_km(yd):
    km = yd/1094
    return km

def yd_m(yd):
    m = yd/1.094
    return m

def yd_cm(yd):
    cm = yd*91.44
    return cm

def yd_mm(yd):
    mm = yd*914
    return mm

def yd_mi(yd):
    mi = yd/1760
    return mi

def yd_ft(yd):
    ft = yd*3
    return ft

def yd_in(yd):
    inch = yd*36
    return inch

def yd_nm(yd):
    nm = yd/2025
    return nm

## PÉ

def ft_km(ft):
    km = ft/3281
    return km

def ft_m(ft):
    m = ft/3.281
    return m

def ft_cm(ft):
    cm = ft*30.48
    return cm

def ft_mm(ft):
    mm = ft*305
    return mm

def ft_mi(ft):
    mi = ft/5280
    return mi

def ft_yd(ft):
    yd = ft/3
    return yd

def ft_in(ft):
    inch = ft*12
    return inch

def ft_nm(ft):
    nm = ft/6076
    return nm

## POLEGADA

def in_m(inch):
    m = inch/39.37
    return m

def in_cm(inch):
    cm = inch*2.54
    return cm

def in_mm(inch):
    mm = inch*25.4
    return mm

def in_yd(inch):
    yd = inch/36
    return yd

def in_ft(inch):
    ft = inch/12
    return ft

## MILHA NAUTICA

def nm_km(nm):
    km = nm*1.852
    return km

def nm_m(nm):
    m = nm*1852
    return m

def nm_cm(nm):
    cm = nm*185200
    return cm

def nm_mi(nm):
    mi = nm*1.151
    return mi

def nm_yd(nm):
    yd = nm*2025
    return yd

def nm_ft(nm):
    ft = nm*6076
    return ft

def nm_in(nm):
    inch = nm*72913
    return inch

################# MEDIDAS DE VOLUME #################

## LITRO
def l_gal(l):
    gal = l/3.785
    return gal

def l_ml(l):
    ml = l*1000
    return ml

def l_m3(l):
    m3 = l/1000
    return m3

## GALAO AMERICANO
def gal_m3(gal):
    m3 = gal/264
    return m3

def gal_l(gal):
    l = gal*3.785
    return l

def gal_ml(gal):
    ml = gal*3785
    return ml

## MILILITRO
def ml_gal(ml):
    gal = ml/3785
    return gal

def ml_l(ml):
    l = ml*1000
    return l

def ml_m3(ml):
    m3 = ml/1000000
    return m3

## METROS CUBICOS
def m3_gal(m3):
    gal = m3*264
    return gal

def m3_l(m3):
    l = m3*1000
    return l

def m3_ml(m3):
    ml = m3*1000000
    return ml

############## CONVERSÕES DE MASSA ############

## QUILOGRAMA
def kg_t(kg):
    t = kg/1000
    return t

def kg_g(kg):
    g = kg*1000
    return g

def kg_mg(kg):
    mg = kg/1000000
    return mg

def kg_oz(kg):
    oz = kg*35.274
    return oz

def kg_lb(kg):
    lb = kg*2.205
    return lb

## GRAMA
def g_t(g):
    t = g/1000000
    return t

def g_kg(g):
    kg = g/1000
    return kg

def g_mg(g):
    mg = g*1000
    return mg

def g_oz(g):
    oz = g/28.35
    return oz

def g_lb(g):
    lb = g/454
    return lb

## MILIGRAMA
def mg_kg(mg):
    kg = mg/1000000
    return kg

def mg_g(mg):
    g = mg/1000
    return g

def mg_oz(mg):
    oz = mg/28350
    return oz

def mg_lb(mg):
    lb = mg/453592
    return lb

## TONELADA
def t_kg(t):
    kg = t*1000
    return kg

def t_g(t):
    g = t*1000000
    return g

def t_oz(t):
    oz = t*35274
    return oz

def t_lb(t):
    lb = t*2205
    return lb

## ONÇA
def oz_t(oz):
    t = oz/35274
    return t

def oz_kg(oz):
    kg = oz/35.274
    return kg

def oz_g(oz):
    g = oz*28.35
    return g

def oz_mg(oz):
    mg = oz*28350
    return mg

def oz_lb(oz):
    lb = oz/16
    return lb

## LIBRA
def lb_t(lb):
    t = lb/2205
    return t

def lb_kg(lb):
    kg = lb/2.205
    return kg

def lb_g(lb):
    g = lb*454
    return g

def lb_mg(lb):
    mg = lb*453592
    return mg

def lb_oz(lb):
    oz = lb*16
    return oz

############## MEDIDAS DE ÁREA #############

## QUILOMETRO QUADRADO
def km2_m2(km2):
    m2 = km2*1000000
    return m2

def km2_mi2(km2):
    mi2 = km2/2.59
    return mi2

def km2_ha(km2):
    ha = km2*100
    return ha

## METRO QUADRADO
def m2_km2(m2):
    km2 = m2/1000000
    return km2

def m2_ha(m2):
    ha = m2/10000
    return ha

def m2_mi2(m2):
    mi2 = m2/2590000
    return mi2

## HECTARE
def ha_km2(ha):
    km2 = ha/100
    return km2

def ha_m2(ha):
    m2 = ha*10000
    return m2

def ha_mi2(ha):
    mi2 = ha/259
    return mi2

## MILHA QUADRADA
def mi2_km2(mi2):
    km2 = mi2*2.59
    return km2

def mi2_m2(mi2):
    m2 = mi2*2590000
    return m2

def mi2_ha(mi2):
    ha = mi2*259
    return ha

#################### MEDIDAS DE VELOCIDADE #####################

## QUILOMETRO POR HORA
def kmh_ms(kmh):
    ms = kmh/3.6
    return ms

def kmh_mih(kmh):
    mih = kmh/1.609
    return mih

def kmh_kn(kmh):
    kn = kmh/1.852
    return kn

## METROS POR SEGUNDO
def ms_kmh(ms):
    kmh = ms*3.6
    return kmh

def ms_mih(ms):
    mih = ms*2.237
    return mih

def ms_kn(ms):
    kn = ms*1.944
    return kn

## MILHAS POR HORA
def mih_kmh(mih):
    kmh = mih*1.609
    return kmh

def mih_ms(mih):
    ms = mih/2.237
    return ms

def mih_kn(mih):
    kn = mih/1.151
    return kn

############################################################## MOEDAS #################################################
#Dólar Americano = USD
#Euro = EUR
#Libra esterlina = GBP
#Iene = JPY
#Dólar Australiano = AUD
#Franco Suíço = CHF
#Dólar Canadense = CAD
#Renminbi (Yuan) = CNY
#Peso Argentino = ARS

#Ethereum = ETH
#Bitcoin = BTC
#Dogecoin = DOGE


## MOEDAS COM CONVERSÃO COMPLETA (ORIGEM): BRL, EUR, USD
## MOEDAS COM CONVERSÃO PARCIAL (ORIGEM): GBP, JPY, AUD, CHF, CAD, CNY, ARS
## MOEDAS SEM CONVERSÃO (ORIGEM): BTC, ETH, DOGE


###############  MOEDA --> BRL ##############
requisicaobrl = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL,JPY-BRL,AUD-BRL,CHF-BRL,CAD-BRL,CNY-BRL,ARS-BRL,ETH-BRL,DOGE-BRL')
requisicaobrl_dic = requisicaobrl.json()

cotacao_usdbrl = requisicaobrl_dic['USDBRL']['bid']
cotacao_eurbrl = requisicaobrl_dic['EURBRL']['bid']
cotacao_btcbrl = requisicaobrl_dic['BTCBRL']['bid']
cotacao_gbpbrl = requisicaobrl_dic['GBPBRL']['bid']
cotacao_jpybrl = requisicaobrl_dic['JPYBRL']['bid']
cotacao_audbrl = requisicaobrl_dic ['AUDBRL']['bid']
cotacao_chfbrl = requisicaobrl_dic ['CHFBRL']['bid']
cotacao_cadbrl = requisicaobrl_dic ['CADBRL']['bid']
cotacao_cnybrl = requisicaobrl_dic ['CNYBRL']['bid']
cotacao_arsbrl = requisicaobrl_dic ['ARSBRL']['bid']
cotacao_ethbrl = requisicaobrl_dic ['ETHBRL']['bid']
cotacao_dogebrl = requisicaobrl_dic ['DOGEBRL']['bid']

################ MOEDA --> USD #################
requisicaoUSD = requests.get('https://economia.awesomeapi.com.br/last/BRL-USD,EUR-USD,BTC-USD,GBP-USD,JPY-USD,AUD-USD,CHF-USD,CAD-USD,CNY-USD,ARS-USD,ETH-USD,DOGE-USD')
requisicaoUSD_dic = requisicaoUSD.json()

cotacao_brlusd = requisicaoUSD_dic['BRLUSD']['bid']
cotacao_eurusd = requisicaoUSD_dic['EURUSD']['bid']
cotacao_btcusd = requisicaoUSD_dic['BTCUSD']['bid']
cotacao_gbpusd = requisicaoUSD_dic['GBPUSD']['bid']
cotacao_jpyusd = requisicaoUSD_dic['JPYUSD']['bid']
cotacao_audusd = requisicaoUSD_dic ['AUDUSD']['bid']
cotacao_chfusd = requisicaoUSD_dic ['CHFUSD']['bid']
cotacao_cadusd = requisicaoUSD_dic ['CADUSD']['bid']
cotacao_cnyusd = requisicaoUSD_dic ['CNYUSD']['bid']
cotacao_arsusd = requisicaoUSD_dic ['ARSUSD']['bid']
cotacao_ethusd = requisicaoUSD_dic ['ETHUSD']['bid']
cotacao_dogeusd = requisicaoUSD_dic ['DOGEUSD']['bid']

################### MOEDA --> EUR ######################
requisicaoEUR = requests.get('https://economia.awesomeapi.com.br/last/BRL-EUR,USD-EUR,BTC-EUR,GBP-EUR,JPY-EUR,AUD-EUR,CHF-EUR,CAD-EUR,CNY-EUR,ARS-EUR,ETH-EUR,DOGE-EUR')
requisicaoEUR_dic = requisicaoEUR.json()

cotacao_brleur = requisicaoEUR_dic['BRLEUR']['bid']
cotacao_usdeur = requisicaoEUR_dic['USDEUR']['bid']
cotacao_btceur = requisicaoEUR_dic['BTCEUR']['bid']
cotacao_gbpeur = requisicaoEUR_dic['GBPEUR']['bid']
cotacao_jpyeur = requisicaoEUR_dic['JPYEUR']['bid']
cotacao_audeur = requisicaoEUR_dic ['AUDEUR']['bid']
cotacao_chfeur = requisicaoEUR_dic ['CHFEUR']['bid']
cotacao_cadeur = requisicaoEUR_dic ['CADEUR']['bid']
cotacao_cnyeur = requisicaoEUR_dic ['CNYEUR']['bid']
cotacao_arseur = requisicaoEUR_dic ['ARSEUR']['bid']
cotacao_etheur = requisicaoEUR_dic ['ETHEUR']['bid']
cotacao_dogeeur = requisicaoEUR_dic ['DOGEEUR']['bid']

################### MOEDA --> GBP   SÓ BRL, USD E EUR #################
requisicaoGBP = requests.get('https://economia.awesomeapi.com.br/last/BRL-GBP,USD-GBP,EUR-GBP')
requisicaoGBP_dic = requisicaoGBP.json()

cotacao_brlgbp = requisicaoGBP_dic['BRLGBP']['bid']
cotacao_usdgbp = requisicaoGBP_dic['USDGBP']['bid']
cotacao_eurgbp = requisicaoGBP_dic['EURGBP']['bid']


################### MOEDA --> JPY    SÓ BRL, USD E EUR #################
requisicaoJPY = requests.get('https://economia.awesomeapi.com.br/last/BRL-JPY,USD-JPY,EUR-JPY')
requisicaoJPY_dic = requisicaoJPY.json()

cotacao_brljpy = requisicaoJPY_dic['BRLJPY']['bid']
cotacao_usdjpy = requisicaoJPY_dic['USDJPY']['bid']
cotacao_eurjpy = requisicaoJPY_dic['EURJPY']['bid']


################### MOEDA --> AUD    SÓ BRL, USD E EUR #################
requisicaoAUD = requests.get('https://economia.awesomeapi.com.br/last/BRL-AUD,USD-AUD,EUR-AUD')
requisicaoAUD_dic = requisicaoAUD.json()

cotacao_brlaud = requisicaoAUD_dic['BRLAUD']['bid']
cotacao_usdaud = requisicaoAUD_dic['USDAUD']['bid']
cotacao_euraud = requisicaoAUD_dic['EURAUD']['bid']

################### MOEDA --> CHF     SÓ BRL, USD E EUR #################
requisicaoCHF = requests.get('https://economia.awesomeapi.com.br/last/BRL-CHF,USD-CHF,EUR-CHF')
requisicaoCHF_dic = requisicaoCHF.json()

cotacao_brlchf = requisicaoCHF_dic['BRLCHF']['bid']
cotacao_usdchf = requisicaoCHF_dic['USDCHF']['bid']
cotacao_eurchf = requisicaoCHF_dic['EURCHF']['bid']


################### MOEDA --> CAD     SÓ BRL, USD E EUR #################
requisicaoCAD = requests.get('https://economia.awesomeapi.com.br/last/BRL-CAD,USD-CAD,EUR-CAD')
requisicaoCAD_dic = requisicaoCAD.json()

cotacao_brlcad = requisicaoCAD_dic['BRLCAD']['bid']
cotacao_usdcad = requisicaoCAD_dic['USDCAD']['bid']
cotacao_eurcad = requisicaoCAD_dic['EURCAD']['bid']

################### MOEDA --> CNY    SÓ BRL, USD E EUR #################
requisicaoCNY = requests.get('https://economia.awesomeapi.com.br/last/BRL-CNY,USD-CNY,EUR-CNY')
requisicaoCNY_dic = requisicaoCNY.json()

cotacao_brlcny = requisicaoCNY_dic['BRLCNY']['bid']
cotacao_usdcny = requisicaoCNY_dic['USDCNY']['bid']
cotacao_eurcny = requisicaoCNY_dic['EURCNY']['bid']

################### MOEDA --> ARS #    SÓ BRL, USD E EUR #################
requisicaoARS = requests.get('https://economia.awesomeapi.com.br/last/BRL-ARS,USD-ARS,EUR-ARS')
requisicaoARS_dic = requisicaoARS.json()

cotacao_brlars = requisicaoARS_dic['BRLARS']['bid']
cotacao_usdars = requisicaoARS_dic['USDARS']['bid']
cotacao_eurars = requisicaoARS_dic['EURARS']['bid']


# VARIAVEIS (SEPARADAS PELA ORIGEM)

# BRL
#
cotacao_brlars = float(cotacao_brlars)
cotacao_brlcny = float(cotacao_brlcny)
cotacao_brlcad = float(cotacao_brlcad)
cotacao_brlusd = float(cotacao_brlusd)
cotacao_brlchf = float(cotacao_brlchf)
cotacao_brlaud = float(cotacao_brlaud)
cotacao_brljpy = float(cotacao_brljpy)
cotacao_brlgbp = float(cotacao_brlgbp)
cotacao_brleur = float(cotacao_brleur)

# USD
#
cotacao_usdars = float(cotacao_usdars)
cotacao_usdcny = float(cotacao_usdcny)
cotacao_usdcad = float(cotacao_usdcad)
cotacao_usdchf = float(cotacao_usdchf)
cotacao_usdaud = float(cotacao_usdaud)
cotacao_usdjpy = float(cotacao_usdjpy)
cotacao_usdgbp = float(cotacao_usdgbp)
cotacao_usdeur = float(cotacao_usdeur)
cotacao_usdbrl = float(cotacao_usdbrl)

# EUR
#
cotacao_eurars = float(cotacao_eurars)
cotacao_eurcny = float(cotacao_eurcny)
cotacao_eurcad = float(cotacao_eurcad)
cotacao_eurchf = float(cotacao_eurchf)
cotacao_euraud = float(cotacao_euraud)
cotacao_eurjpy = float(cotacao_eurjpy)
cotacao_eurgbp = float(cotacao_eurgbp)
cotacao_eurusd = float(cotacao_eurusd)
cotacao_eurbrl = float(cotacao_eurbrl)

# ARS
#
cotacao_arsusd = float(cotacao_arsusd)
cotacao_arseur = float(cotacao_arseur)
cotacao_arsbrl = float(cotacao_arsbrl)

# CNY
#
cotacao_cnyusd = float(cotacao_cnyusd)
cotacao_cnyeur = float(cotacao_cnyeur)
cotacao_cnybrl = float(cotacao_cnybrl)

#CAD
#
cotacao_cadusd = float(cotacao_cadusd)
cotacao_cadeur = float(cotacao_cadeur)
cotacao_cadbrl = float(cotacao_cadbrl)

# CHF
#
cotacao_chfusd = float(cotacao_chfusd)
cotacao_chfeur = float(cotacao_chfeur)
cotacao_chfbrl = float(cotacao_chfbrl)

# AUD
#
cotacao_audusd = float(cotacao_audusd)
cotacao_audeur = float(cotacao_audeur)
cotacao_audbrl = float(cotacao_audbrl)

# JPY
#
cotacao_jpyusd = float(cotacao_jpyusd)/100
cotacao_jpyeur = float(cotacao_jpyeur)/100
cotacao_jpybrl = float(cotacao_jpybrl)

# GBP
#
cotacao_gbpusd = float(cotacao_gbpusd)
cotacao_gbpeur = float(cotacao_gbpeur)
cotacao_gbpbrl = float(cotacao_gbpbrl)
#------------------------------------------INTERFACE-----------------------------#

def main():
    ## Visual da Tela
    win=GraphWin("ConverTHIS",1280,720)
    win.setBackground(color_rgb(126, 139, 236))
    tela_interna=Rectangle(Point(25,25),Point(1255,695))
    tela_interna.setFill(color_rgb(126, 179, 250))
    tela_interna.draw(win)
    

    moeda = Rectangle(Point(390,95), Point(890,295))
    moeda.setFill(color_rgb(224, 178, 89))
    moeda.setOutline(color_rgb(224, 132, 75))
    moeda.setWidth(6)
    moeda.draw(win)
    text_moeda = Text(Point(640,195), 'CONVERSÃO MONETÁRIA')
    text_moeda.setFace('helvetica')
    text_moeda.setStyle('bold')
    text_moeda.setOutline(color_rgb(247, 106, 69))
    text_moeda.setSize(25)
    text_moeda.draw(win)

    unidade = Rectangle(Point(390,430), Point(890,630))
    unidade.setFill(color_rgb(224, 178, 89))
    unidade.setOutline(color_rgb(224, 132, 75))
    unidade.setWidth(6)
    unidade.draw(win)
    text_unidade = Text(Point(640,530),'CONVERSÃO UNIDADES')
    text_unidade.setFace('helvetica')
    text_unidade.setStyle('bold')
    text_unidade.setOutline(color_rgb(247, 106, 69))
    text_unidade.setSize(25)
    text_unidade.draw(win)

    converthis = Text(Point(640,362.5),'CONVERTHIS')
    converthis.setFace('helvetica')
    converthis.setStyle('bold')
    converthis.setOutline(color_rgb(75, 75, 75))
    converthis.setSize(36)
    converthis.draw(win)

    close = Rectangle(Point(1000,50),Point(1200,200))
    close.setFill(color_rgb(223, 42, 67))
    close.setOutline(color_rgb(191, 68, 75))
    close.setWidth(6)
    close.draw(win)
    text_close = Text(Point(1100,125),'SAIR')
    text_close.setFace('helvetica')
    text_close.setStyle('bold')
    text_close.setSize(25)
    text_close.draw(win)

    def moeda():
        moedaa = GraphWin("CONVERSOR DE MOEDAS",1280,720)
        moedaa.setBackground(color_rgb(229, 175, 104))
        tela_interna=Rectangle(Point(25,25),Point(1255,695))
        tela_interna.setFill(color_rgb(241, 182, 71))
        tela_interna.draw(moedaa)
        text_moeda = Text(Point(640,60),'ESCOLHA A SUA MOEDA ORIGEM')
        text_moeda.setSize(36)
        text_moeda.setFace('helvetica')
        text_moeda.setStyle('bold')
        text_moeda.draw(moedaa)
        
        usd = Rectangle(Point(70,130),Point(420,280))
        usd.setFill(color_rgb(107, 236, 0))
        usd.setOutline(color_rgb(52, 115, 0))
        usd.setWidth(6)
        usd.draw(moedaa)
        text_usd = Text(Point(245,205),'DÓLAR AMERICANO')
        text_usd.setFace('helvetica')
        text_usd.setStyle('bold')
        text_usd.setSize(25)
        text_usd.draw(moedaa)

        gbp = Rectangle(Point(465,130),Point(815,280))
        gbp.setFill(color_rgb(107, 236, 0))
        gbp.setOutline(color_rgb(52, 115, 0))
        gbp.setWidth(6)
        gbp.draw(moedaa)
        text_gbp = Text(Point(640,205),'LIBRA ESTERLINA')
        text_gbp.setFace('helvetica')
        text_gbp.setStyle('bold')
        text_gbp.setSize(25)
        text_gbp.draw(moedaa)

        jpy = Rectangle(Point(860,130),Point(1210,280))
        jpy.setFill(color_rgb(107, 236, 0))
        jpy.setOutline(color_rgb(52, 115, 0))
        jpy.setWidth(6)
        jpy.draw(moedaa)
        text_jpy = Text(Point(1035,205),'IENE')
        text_jpy.setFace('helvetica')
        text_jpy.setStyle('bold')
        text_jpy.setSize(25)
        text_jpy.draw(moedaa)

        eur = Rectangle(Point(70,320),Point(420,470))
        eur.setFill(color_rgb(107, 236, 0))
        eur.setOutline(color_rgb(52, 115, 0))
        eur.setWidth(6)
        eur.draw(moedaa)
        text_eur = Text(Point(245,395),'EURO')
        text_eur.setFace('helvetica')
        text_eur.setStyle('bold')
        text_eur.setSize(25)
        text_eur.draw(moedaa)

        aud = Rectangle(Point(465,320),Point(815,470))
        aud.setFill(color_rgb(107, 236, 0))
        aud.setOutline(color_rgb(52, 115, 0))
        aud.setWidth(6)
        aud.draw(moedaa)
        text_aud = Text(Point(640,395),'DOLAR AUSTRALIANO')
        text_aud.setFace('helvetica')
        text_aud.setStyle('bold')
        text_aud.setSize(25)
        text_aud.draw(moedaa)

        cad = Rectangle(Point(860,320),Point(1210,470))
        cad.setFill(color_rgb(107, 236, 0))
        cad.setOutline(color_rgb(52, 115, 0))
        cad.setWidth(6)
        cad.draw(moedaa)
        text_cad = Text(Point(1035,395),'DOLAR CANADENSE')
        text_cad.setFace('helvetica')
        text_cad.setStyle('bold')
        text_cad.setSize(25)
        text_cad.draw(moedaa)

        brl = Rectangle(Point(70,510),Point(420,660))
        brl.setFill(color_rgb(107, 236, 0))
        brl.setOutline(color_rgb(52, 115, 0))
        brl.setWidth(6)
        brl.draw(moedaa)
        text_brl = Text(Point(245,585),'REAL')
        text_brl.setFace('helvetica')
        text_brl.setStyle('bold')
        text_brl.setSize(25)
        text_brl.draw(moedaa)

        cny = Rectangle(Point(465,510),Point(815,660))
        cny.setFill(color_rgb(107, 236, 0))
        cny.setOutline(color_rgb(52, 115, 0))
        cny.setWidth(6)
        cny.draw(moedaa)
        text_cny = Text(Point(640,585),'YUAN')
        text_cny.setFace('helvetica')
        text_cny.setStyle('bold')
        text_cny.setSize(25)
        text_cny.draw(moedaa)

        ars = Rectangle(Point(860,510),Point(1210,660))
        ars.setFill(color_rgb(107, 236, 0))
        ars.setOutline(color_rgb(52, 115, 0))
        ars.setWidth(6)
        ars.draw(moedaa)
        text_ars = Text(Point(1035,585),'PESO ARGENTINO')
        text_ars.setFace('helvetica')
        text_ars.setStyle('bold')
        text_ars.setSize(25)
        text_ars.draw(moedaa)

        close = Rectangle(Point(1100,30),Point(1200,120))
        close.setFill(color_rgb(223, 42, 67))
        close.setOutline(color_rgb(191, 68, 75))
        close.setWidth(6)
        close.draw(moedaa)
        text_close = Text(Point(1150,75),'SAIR')
        text_close.setFace('helvetica')
        text_close.setStyle('bold')
        text_close.setSize(25)
        text_close.draw(moedaa)

        voltar = Rectangle(Point(50,40),Point(200,80))
        voltar.setFill('blue')
        voltar.setOutline('blue4')
        voltar.setWidth(6)
        voltar.draw(moedaa)
        text_voltar = Text(Point(125,60),'VOLTAR')
        text_voltar.setFace('helvetica')
        text_voltar.setStyle('bold')
        text_voltar.setSize(25)
        text_voltar.draw(moedaa)




        def usd():
            usdd = GraphWin("CONVERSOR MONETARIO - DOLAR",1280,720)
            usdd.setBackground(color_rgb(126, 182, 157))
            tela_internausd=Rectangle(Point(25,25),Point(1255,695))
            tela_internausd.setFill(color_rgb(126, 206, 184))
            tela_internausd.draw(usdd)
            text_usd = Text(Point(640,60),'VALOR INICIAL EM DÓLAR')
            text_usd.setSize(36)
            text_usd.setFace('helvetica')
            text_usd.setStyle('bold')
            text_usd.draw(usdd)

            confirmar = Rectangle(Point(545,120),Point(745,150))
            confirmar.setFill('green')
            confirmar.draw(usdd)
            text_confirmar = Text(Point(640,135),'CONFIRMAR')
            text_confirmar.setSize(10)
            text_confirmar.setFace('helvetica')
            text_confirmar.setStyle('bold')
            text_confirmar.draw(usdd)
            
            textEntry = Entry(Point(640,100),25)
            textEntry.setFill('white')
            textEntry.draw(usdd)

            usdARS = Rectangle(Point(430,180),Point(630,230))
            usdARS.setFill('white')
            usdARS.draw(usdd)

            usdCNY = Rectangle(Point(430,250),Point(630,300))
            usdCNY.setFill('white')
            usdCNY.draw(usdd)

            usdCAD = Rectangle(Point(430,320),Point(630,370))
            usdCAD.setFill('white')
            usdCAD.draw(usdd)

            usdCHF = Rectangle(Point(430,390),Point(630,440))
            usdCHF.setFill('white')
            usdCHF.draw(usdd)

            usdAUD = Rectangle(Point(650,180),Point(850,230))
            usdAUD.setFill('white')
            usdAUD.draw(usdd)

            usdJPY = Rectangle(Point(650,250),Point(850,300))
            usdJPY.setFill('white')
            usdJPY.draw(usdd)

            usdGBP = Rectangle(Point(650,320),Point(850,370))
            usdGBP.setFill('white')
            usdGBP.draw(usdd)

            usdEUR = Rectangle(Point(650,390),Point(850,440))
            usdEUR.setFill('white')
            usdEUR.draw(usdd)

            usdBRL = Rectangle(Point(540,460),Point(740,510))
            usdBRL.setFill('white')
            usdBRL.draw(usdd)

            voltar = Rectangle(Point(50,40),Point(200,80))
            voltar.setFill('blue')
            voltar.setOutline('blue4')
            voltar.setWidth(6)
            voltar.draw(usdd)
            text_voltar = Text(Point(125,60),'VOLTAR')
            text_voltar.setFace('helvetica')
            text_voltar.setStyle('bold')
            text_voltar.setSize(25)
            text_voltar.draw(usdd)

            text_novaconsulta = Text(Point(640,660),'PARA NOVA CONSULTA, CLIQUE EM VOLTAR E RETORNE')
            text_novaconsulta.setFace('helvetica')
            text_novaconsulta.setStyle('bold')
            text_novaconsulta.setSize(25)
            text_novaconsulta.draw(usdd)    
            def check_click_usd():

                mouse = usdd.getMouse()
                X = mouse.getX()
                Y = mouse.getY()

                if X > 545 and X < 745 and Y > 120 and Y < 150:
                    text = textEntry.getText()
                    text_usdARS = Text(Point(530,205),'{} ARS'.format(round(cotacao_usdars*float(text), 2)))
                    text_usdARS.setSize(20)
                    text_usdARS.setFace('helvetica')
                    text_usdARS.setStyle('bold')
                    text_usdARS.draw(usdd)

                    text = textEntry.getText()
                    text_usdCNY = Text(Point(530,275),'{} CNY'.format(round(cotacao_usdcny*float(text), 2)))
                    text_usdCNY.setSize(20)
                    text_usdCNY.setFace('helvetica')
                    text_usdCNY.setStyle('bold')
                    text_usdCNY.draw(usdd)

                    text = textEntry.getText()
                    text_usdCAD = Text(Point(530,345),'{} CAD'.format(round(cotacao_usdcad*float(text), 2)))
                    text_usdCAD.setSize(20)
                    text_usdCAD.setFace('helvetica')
                    text_usdCAD.setStyle('bold')
                    text_usdCAD.draw(usdd)

                    text = textEntry.getText()
                    text_usdCHF = Text(Point(530,415),'{} CHF'.format(round(cotacao_usdchf*float(text), 2)))
                    text_usdCHF.setSize(20)
                    text_usdCHF.setFace('helvetica')
                    text_usdCHF.setStyle('bold')
                    text_usdCHF.draw(usdd)

                    text = textEntry.getText()
                    text_usdAUD = Text(Point(750,205),'{} AUD'.format(round(cotacao_usdaud*float(text), 2)))
                    text_usdAUD.setSize(20)
                    text_usdAUD.setFace('helvetica')
                    text_usdAUD.setStyle('bold')
                    text_usdAUD.draw(usdd)

                    text = textEntry.getText()
                    text_usdJPY = Text(Point(750,275),'{} JPY'.format(round(cotacao_usdjpy*float(text), 2)))
                    text_usdJPY.setSize(20)
                    text_usdJPY.setFace('helvetica')
                    text_usdJPY.setStyle('bold')
                    text_usdJPY.draw(usdd)

                    text = textEntry.getText()
                    text_usdGBP = Text(Point(750,345),'{} GBP'.format(round(cotacao_usdgbp*float(text), 2)))
                    text_usdGBP.setSize(20)
                    text_usdGBP.setFace('helvetica')
                    text_usdGBP.setStyle('bold')
                    text_usdGBP.draw(usdd)

                    text = textEntry.getText()
                    text_usdEUR = Text(Point(750,415),'{} EUR'.format(round(cotacao_usdeur*float(text), 2)))
                    text_usdEUR.setSize(20)
                    text_usdEUR.setFace('helvetica')
                    text_usdEUR.setStyle('bold')
                    text_usdEUR.draw(usdd)

                    text = textEntry.getText()
                    text_usdBRL = Text(Point(640,485),'{} BRL'.format(round(cotacao_usdbrl*float(text), 2)))
                    text_usdBRL.setSize(20)
                    text_usdBRL.setFace('helvetica')
                    text_usdBRL.setStyle('bold')
                    text_usdBRL.draw(usdd)

                    arquivo = open('conversao_monetaria-DOLAR AMERICANO.txt','w')
                    arquivo.writelines('Valor inicial: {} USD'.format(text)+'\n')
                    arquivo.writelines('{} BRL'.format(cotacao_usdbrl*float(text))+'\n')
                    arquivo.writelines('{} EUR'.format(cotacao_usdeur*float(text))+'\n')
                    arquivo.writelines('{} GBP'.format(cotacao_usdgbp*float(text))+'\n')
                    arquivo.writelines('{} ARS'.format(cotacao_usdars*float(text))+'\n')
                    arquivo.writelines('{} CNY'.format(cotacao_usdcny*float(text))+'\n')
                    arquivo.writelines('{} CAD'.format(cotacao_usdcad*float(text))+'\n')
                    arquivo.writelines('{} CHF'.format(cotacao_usdchf*float(text))+'\n')
                    arquivo.writelines('{} AUD'.format(cotacao_usdaud*float(text))+'\n')
                    arquivo.writelines('{} JPY'.format(cotacao_usdjpy*float(text))+'\n')
                    arquivo.close   
                    check_click_usd()
                if X > 50 and X < 200 and Y > 40 and Y < 80:
                    time.sleep(1)
                    usdd.close()
                    moeda()
                    check_click_usd()  
                else:
                    check_click_usd()
            check_click_usd()
            
            
            usdd.getKey()
            usdd.close()






        def eur():
            eurr = GraphWin("CONVERSOR MONETARIO - EURO",1280,720)
            eurr.setBackground(color_rgb(126, 182, 157))
            tela_internaeur=Rectangle(Point(25,25),Point(1255,695))
            tela_internaeur.setFill(color_rgb(126, 206, 184))
            tela_internaeur.draw(eurr)
            text_eur = Text(Point(640,60),'INSIRA O VALOR INICIAL EM EURO')
            text_eur.setSize(36)
            text_eur.setFace('helvetica')
            text_eur.setStyle('bold')
            text_eur.draw(eurr)

            confirmar = Rectangle(Point(545,120),Point(745,150))
            confirmar.setFill('green')
            confirmar.draw(eurr)
            text_confirmar = Text(Point(640,135),'CONFIRMAR')
            text_confirmar.setSize(10)
            text_confirmar.setFace('helvetica')
            text_confirmar.setStyle('bold')
            text_confirmar.draw(eurr)
            
            textEntry = Entry(Point(640,100),25)
            textEntry.setFill('white')
            textEntry.draw(eurr)

            eurARS = Rectangle(Point(430,180),Point(630,230))
            eurARS.setFill('white')
            eurARS.draw(eurr)

            eurCNY = Rectangle(Point(430,250),Point(630,300))
            eurCNY.setFill('white')
            eurCNY.draw(eurr)

            eurCAD = Rectangle(Point(430,320),Point(630,370))
            eurCAD.setFill('white')
            eurCAD.draw(eurr)

            eurCHF = Rectangle(Point(430,390),Point(630,440))
            eurCHF.setFill('white')
            eurCHF.draw(eurr)

            eurAUD = Rectangle(Point(650,180),Point(850,230))
            eurAUD.setFill('white')
            eurAUD.draw(eurr)

            eurJPY = Rectangle(Point(650,250),Point(850,300))
            eurJPY.setFill('white')
            eurJPY.draw(eurr)

            eurGBP = Rectangle(Point(650,320),Point(850,370))
            eurGBP.setFill('white')
            eurGBP.draw(eurr)

            eurUSD = Rectangle(Point(650,390),Point(850,440))
            eurUSD.setFill('white')
            eurUSD.draw(eurr)

            eurBRL = Rectangle(Point(540,460),Point(740,510))
            eurBRL.setFill('white')
            eurBRL.draw(eurr)

            voltar = Rectangle(Point(50,40),Point(200,80))
            voltar.setFill('blue')
            voltar.setOutline('blue4')
            voltar.setWidth(6)
            voltar.draw(eurr)
            text_voltar = Text(Point(125,60),'VOLTAR')
            text_voltar.setFace('helvetica')
            text_voltar.setStyle('bold')
            text_voltar.setSize(25)
            text_voltar.draw(eurr)

            text_novaconsulta = Text(Point(640,660),'PARA NOVA CONSULTA, CLIQUE EM VOLTAR E RETORNE')
            text_novaconsulta.setFace('helvetica')
            text_novaconsulta.setStyle('bold')
            text_novaconsulta.setSize(25)
            text_novaconsulta.draw(eurr)               
            def check_click_usd():

                mouse = eurr.getMouse()
                X = mouse.getX()
                Y = mouse.getY()

                if X > 545 and X < 745 and Y > 120 and Y < 150:
                    text = textEntry.getText()
                    text_eurARS = Text(Point(530,205),'{} ARS'.format(round(cotacao_eurars*float(text), 2)))
                    text_eurARS.setSize(20)
                    text_eurARS.setFace('helvetica')
                    text_eurARS.setStyle('bold')
                    text_eurARS.draw(eurr)

                    text = textEntry.getText()
                    text_eurCNY = Text(Point(530,275),'{} CNY'.format(round(cotacao_eurcny*float(text), 2)))
                    text_eurCNY.setSize(20)
                    text_eurCNY.setFace('helvetica')
                    text_eurCNY.setStyle('bold')
                    text_eurCNY.draw(eurr)

                    text = textEntry.getText()
                    text_eurCAD = Text(Point(530,345),'{} CAD'.format(round(cotacao_eurcad*float(text), 2)))
                    text_eurCAD.setSize(20)
                    text_eurCAD.setFace('helvetica')
                    text_eurCAD.setStyle('bold')
                    text_eurCAD.draw(eurr)

                    text = textEntry.getText()
                    text_eurCHF = Text(Point(530,415),'{} CHF'.format(round(cotacao_eurchf*float(text), 2)))
                    text_eurCHF.setSize(20)
                    text_eurCHF.setFace('helvetica')
                    text_eurCHF.setStyle('bold')
                    text_eurCHF.draw(eurr)

                    text = textEntry.getText()
                    text_eurAUD = Text(Point(750,205),'{} AUD'.format(round(cotacao_euraud*float(text), 2)))
                    text_eurAUD.setSize(20)
                    text_eurAUD.setFace('helvetica')
                    text_eurAUD.setStyle('bold')
                    text_eurAUD.draw(eurr)

                    text = textEntry.getText()
                    text_eurJPY = Text(Point(750,275),'{} JPY'.format(round(cotacao_eurjpy*float(text), 2)))
                    text_eurJPY.setSize(20)
                    text_eurJPY.setFace('helvetica')
                    text_eurJPY.setStyle('bold')
                    text_eurJPY.draw(eurr)

                    text = textEntry.getText()
                    text_eurGBP = Text(Point(750,345),'{} GBP'.format(round(cotacao_eurgbp*float(text), 2)))
                    text_eurGBP.setSize(20)
                    text_eurGBP.setFace('helvetica')
                    text_eurGBP.setStyle('bold')
                    text_eurGBP.draw(eurr)

                    text = textEntry.getText()
                    text_eurUSD = Text(Point(750,415),'{} USD'.format(round(cotacao_eurusd*float(text), 2)))
                    text_eurUSD.setSize(20)
                    text_eurUSD.setFace('helvetica')
                    text_eurUSD.setStyle('bold')
                    text_eurUSD.draw(eurr)

                    text = textEntry.getText()
                    text_eurBRL = Text(Point(640,485),'{} BRL'.format(round(cotacao_eurbrl*float(text), 2)))
                    text_eurBRL.setSize(20)
                    text_eurBRL.setFace('helvetica')
                    text_eurBRL.setStyle('bold')
                    text_eurBRL.draw(eurr)

                    arquivo = open('conversao_monetaria-EURO.txt','w')
                    arquivo.writelines('Valor inicial: {} EUR'.format(text)+'\n')
                    arquivo.writelines('{} USD'.format(cotacao_eurusd*float(text))+'\n')
                    arquivo.writelines('{} BRL'.format(cotacao_eurbrl*float(text))+'\n')
                    arquivo.writelines('{} GBP'.format(cotacao_eurgbp*float(text))+'\n')
                    arquivo.writelines('{} ARS'.format(cotacao_eurars*float(text))+'\n')
                    arquivo.writelines('{} CNY'.format(cotacao_eurcny*float(text))+'\n')
                    arquivo.writelines('{} CAD'.format(cotacao_eurcad*float(text))+'\n')
                    arquivo.writelines('{} CHF'.format(cotacao_eurchf*float(text))+'\n')
                    arquivo.writelines('{} AUD'.format(cotacao_euraud*float(text))+'\n')
                    arquivo.writelines('{} JPY'.format(cotacao_eurjpy*float(text))+'\n')
                    arquivo.close   

                    check_click_usd()
                if X > 50 and X < 200 and Y > 40 and Y < 80:
                    time.sleep(1)
                    eurr.close()
                    moeda()
                    check_click_usd()  
                else:
                    check_click_usd()
            check_click_usd()
            
            
            eurr.getKey()
            eurr.close()

        def brl():
            brll = GraphWin("CONVERSOR MONETARIO - REAL",1280,720)
            brll.setBackground(color_rgb(126, 182, 157))
            tela_internabrl=Rectangle(Point(25,25),Point(1255,695))
            tela_internabrl.setFill(color_rgb(126, 206, 184))
            tela_internabrl.draw(brll)
            text_brl = Text(Point(640,60),'VALOR INICIAL EM REAL')
            text_brl.setSize(36)
            text_brl.setFace('helvetica')
            text_brl.setStyle('bold')
            text_brl.draw(brll)

            confirmar = Rectangle(Point(545,120),Point(745,150))
            confirmar.setFill('green')
            confirmar.draw(brll)
            text_confirmar = Text(Point(640,135),'CONFIRMAR')
            text_confirmar.setSize(10)
            text_confirmar.setFace('helvetica')
            text_confirmar.setStyle('bold')
            text_confirmar.draw(brll)
            
            textEntry = Entry(Point(640,100),25)
            textEntry.setFill('white')
            textEntry.draw(brll)

            brlARS = Rectangle(Point(430,180),Point(630,230))
            brlARS.setFill('white')
            brlARS.draw(brll)

            brlCNY = Rectangle(Point(430,250),Point(630,300))
            brlCNY.setFill('white')
            brlCNY.draw(brll)

            brlCAD = Rectangle(Point(430,320),Point(630,370))
            brlCAD.setFill('white')
            brlCAD.draw(brll)

            brlCHF = Rectangle(Point(430,390),Point(630,440))
            brlCHF.setFill('white')
            brlCHF.draw(brll)

            brlAUD = Rectangle(Point(650,180),Point(850,230))
            brlAUD.setFill('white')
            brlAUD.draw(brll)

            brlJPY = Rectangle(Point(650,250),Point(850,300))
            brlJPY.setFill('white')
            brlJPY.draw(brll)

            brlGBP = Rectangle(Point(650,320),Point(850,370))
            brlGBP.setFill('white')
            brlGBP.draw(brll)

            brlEUR = Rectangle(Point(650,390),Point(850,440))
            brlEUR.setFill('white')
            brlEUR.draw(brll)

            brlUSD = Rectangle(Point(540,460),Point(740,510))
            brlUSD.setFill('white')
            brlUSD.draw(brll)

            voltar = Rectangle(Point(50,40),Point(200,80))
            voltar.setFill('blue')
            voltar.setOutline('blue4')
            voltar.setWidth(6)
            voltar.draw(brll)
            text_voltar = Text(Point(125,60),'VOLTAR')
            text_voltar.setFace('helvetica')
            text_voltar.setStyle('bold')
            text_voltar.setSize(25)
            text_voltar.draw(brll)

            text_novaconsulta = Text(Point(640,660),'PARA NOVA CONSULTA, CLIQUE EM VOLTAR E RETORNE')
            text_novaconsulta.setFace('helvetica')
            text_novaconsulta.setStyle('bold')
            text_novaconsulta.setSize(25)
            text_novaconsulta.draw(brll)                
            def check_click_usd():

                mouse = brll.getMouse()
                X = mouse.getX()
                Y = mouse.getY()

                if X > 545 and X < 745 and Y > 120 and Y < 150:
                    text = textEntry.getText()
                    text_usdARS = Text(Point(530,205),'{} ARS'.format(round(cotacao_brlars*float(text), 2)))
                    text_usdARS.setSize(20)
                    text_usdARS.setFace('helvetica')
                    text_usdARS.setStyle('bold')
                    text_usdARS.draw(brll)

                    text = textEntry.getText()
                    text_usdCNY = Text(Point(530,275),'{} CNY'.format(round(cotacao_brlcny*float(text), 2)))
                    text_usdCNY.setSize(20)
                    text_usdCNY.setFace('helvetica')
                    text_usdCNY.setStyle('bold')
                    text_usdCNY.draw(brll)

                    text = textEntry.getText()
                    text_usdCAD = Text(Point(530,345),'{} CAD'.format(round(cotacao_brlcad*float(text), 2)))
                    text_usdCAD.setSize(20)
                    text_usdCAD.setFace('helvetica')
                    text_usdCAD.setStyle('bold')
                    text_usdCAD.draw(brll)

                    text = textEntry.getText()
                    text_usdCHF = Text(Point(530,415),'{} CHF'.format(round(cotacao_brlchf*float(text), 2)))
                    text_usdCHF.setSize(20)
                    text_usdCHF.setFace('helvetica')
                    text_usdCHF.setStyle('bold')
                    text_usdCHF.draw(brll)

                    text = textEntry.getText()
                    text_usdAUD = Text(Point(750,205),'{} AUD'.format(round(cotacao_brlaud*float(text), 2)))
                    text_usdAUD.setSize(20)
                    text_usdAUD.setFace('helvetica')
                    text_usdAUD.setStyle('bold')
                    text_usdAUD.draw(brll)

                    text = textEntry.getText()
                    text_usdJPY = Text(Point(750,275),'{} JPY'.format(round(cotacao_brljpy*float(text), 2)))
                    text_usdJPY.setSize(20)
                    text_usdJPY.setFace('helvetica')
                    text_usdJPY.setStyle('bold')
                    text_usdJPY.draw(brll)

                    text = textEntry.getText()
                    text_usdGBP = Text(Point(750,345),'{} GBP'.format(round(cotacao_brlgbp*float(text), 2)))
                    text_usdGBP.setSize(20)
                    text_usdGBP.setFace('helvetica')
                    text_usdGBP.setStyle('bold')
                    text_usdGBP.draw(brll)

                    text = textEntry.getText()
                    text_usdEUR = Text(Point(750,415),'{} EUR'.format(round(cotacao_brleur*float(text), 2)))
                    text_usdEUR.setSize(20)
                    text_usdEUR.setFace('helvetica')
                    text_usdEUR.setStyle('bold')
                    text_usdEUR.draw(brll)

                    text = textEntry.getText()
                    text_usdBRL = Text(Point(640,485),'{} USD'.format(round(cotacao_brlusd*float(text), 2)))
                    text_usdBRL.setSize(20)
                    text_usdBRL.setFace('helvetica')
                    text_usdBRL.setStyle('bold')
                    text_usdBRL.draw(brll)

                    arquivo = open('conversao_monetaria-REAL.txt','w')
                    arquivo.writelines('Valor inicial: {} BRL'.format(text)+'\n')
                    arquivo.writelines('{} USD'.format(cotacao_brlusd*float(text))+'\n')
                    arquivo.writelines('{} EUR'.format(cotacao_brleur*float(text))+'\n')
                    arquivo.writelines('{} GBP'.format(cotacao_brlgbp*float(text))+'\n')
                    arquivo.writelines('{} ARS'.format(cotacao_brlars*float(text))+'\n')
                    arquivo.writelines('{} CNY'.format(cotacao_brlcny*float(text))+'\n')
                    arquivo.writelines('{} CAD'.format(cotacao_brlcad*float(text))+'\n')
                    arquivo.writelines('{} CHF'.format(cotacao_brlchf*float(text))+'\n')
                    arquivo.writelines('{} AUD'.format(cotacao_brlaud*float(text))+'\n')
                    arquivo.writelines('{} JPY'.format(cotacao_brljpy*float(text))+'\n')
                    arquivo.close   
                    check_click_usd()
                if X > 50 and X < 200 and Y > 40 and Y < 80:
                    time.sleep(1)
                    brll.close()
                    moeda()
                    check_click_usd()  
                else:
                    check_click_usd()
            check_click_usd()
            
            
            usd.getKey()
            usd.close()


        def gbp():
            gbpp = GraphWin("CONVERSOR MONETARIO - LIBRA EST.",1280,720)
            gbpp.setBackground(color_rgb(126, 182, 157))
            tela_interna=Rectangle(Point(25,25),Point(1255,695))
            tela_interna.setFill(color_rgb(126, 206, 184))
            tela_interna.draw(gbpp)
            text_ = Text(Point(640,60),'VALOR INICIAL EM LIBRA EST.')
            text_.setSize(36)
            text_.setFace('helvetica')
            text_.setStyle('bold')
            text_.draw(gbpp)

            confirmar = Rectangle(Point(545,120),Point(745,150))
            confirmar.setFill('green')
            confirmar.draw(gbpp)
            text_confirmar = Text(Point(640,135),'CONFIRMAR')
            text_confirmar.setSize(10)
            text_confirmar.setFace('helvetica')
            text_confirmar.setStyle('bold')
            text_confirmar.draw(gbpp)
            
            textEntry = Entry(Point(640,100),25)
            textEntry.setFill('white')
            textEntry.draw(gbpp)

            gbpUSD = Rectangle(Point(430,180),Point(630,230))
            gbpUSD.setFill('white')
            gbpUSD.draw(gbpp)

            gbpEUR = Rectangle(Point(650,180),Point(850,230))
            gbpEUR.setFill('white')
            gbpEUR.draw(gbpp)

            gbpBRL = Rectangle(Point(540,250),Point(740,300))
            gbpBRL.setFill('white')
            gbpBRL.draw(gbpp)

            voltar = Rectangle(Point(50,40),Point(200,80))
            voltar.setFill('blue')
            voltar.setOutline('blue4')
            voltar.setWidth(6)
            voltar.draw(gbpp)
            text_voltar = Text(Point(125,60),'VOLTAR')
            text_voltar.setFace('helvetica')
            text_voltar.setStyle('bold')
            text_voltar.setSize(25)
            text_voltar.draw(gbpp)

            text_novaconsulta = Text(Point(640,660),'PARA NOVA CONSULTA, CLIQUE EM VOLTAR E RETORNE')
            text_novaconsulta.setFace('helvetica')
            text_novaconsulta.setStyle('bold')
            text_novaconsulta.setSize(25)
            text_novaconsulta.draw(gbpp)    
            def check_click_usd():

                mouse = gbpp.getMouse()
                X = mouse.getX()
                Y = mouse.getY()

                if X > 545 and X < 745 and Y > 120 and Y < 150:
                    text = textEntry.getText()
                    text_gbpUSD = Text(Point(530,205),'{} USD'.format(round(cotacao_gbpusd*float(text), 2)))
                    text_gbpUSD.setSize(20)
                    text_gbpUSD.setFace('helvetica')
                    text_gbpUSD.setStyle('bold')
                    text_gbpUSD.draw(gbpp)

                    text = textEntry.getText()
                    text_gbpEUR = Text(Point(750,205),'{} EUR'.format(round(cotacao_gbpeur*float(text), 2)))
                    text_gbpEUR.setSize(20)
                    text_gbpEUR.setFace('helvetica')
                    text_gbpEUR.setStyle('bold')
                    text_gbpEUR.draw(gbpp)

                    text = textEntry.getText()
                    text_gbpBRL = Text(Point(640,275),'{} BRL'.format(round(cotacao_gbpbrl*float(text), 2)))
                    text_gbpBRL.setSize(20)
                    text_gbpBRL.setFace('helvetica')
                    text_gbpBRL.setStyle('bold')
                    text_gbpBRL.draw(gbpp)

                    arquivo = open('conversao_monetaria-LIBRA ESTERLINA.txt','w')
                    arquivo.writelines('Valor inicial: {} GBP'.format(text)+'\n')
                    arquivo.writelines('{} USD'.format(cotacao_gbpusd*float(text))+'\n')
                    arquivo.writelines('{} EUR'.format(cotacao_gbpeur*float(text))+'\n')
                    arquivo.writelines('{} BRL'.format(cotacao_gbpbrl*float(text))+'\n')
                    arquivo.close   
                    check_click_usd()
                if X > 50 and X < 200 and Y > 40 and Y < 80:
                    time.sleep(1)
                    gbpp.close()
                    moeda()
                    check_click_usd()  
                else:
                    check_click_usd()
            check_click_usd()
            
            
            gbpp.getKey()
            gbpp.close()

        def aud():
            audd = GraphWin("CONVERSOR MONETARIO - DÓLAR AUST.",1280,720)
            audd.setBackground(color_rgb(126, 182, 157))
            tela_interna=Rectangle(Point(25,25),Point(1255,695))
            tela_interna.setFill(color_rgb(126, 206, 184))
            tela_interna.draw(audd)
            text_ = Text(Point(640,60),'VALOR INICIAL EM DÓLAR AUST.')
            text_.setSize(36)
            text_.setFace('helvetica')
            text_.setStyle('bold')
            text_.draw(audd)

            confirmar = Rectangle(Point(545,120),Point(745,150))
            confirmar.setFill('green')
            confirmar.draw(audd)
            text_confirmar = Text(Point(640,135),'CONFIRMAR')
            text_confirmar.setSize(10)
            text_confirmar.setFace('helvetica')
            text_confirmar.setStyle('bold')
            text_confirmar.draw(audd)
            
            textEntry = Entry(Point(640,100),25)
            textEntry.setFill('white')
            textEntry.draw(audd)

            audUSD = Rectangle(Point(430,180),Point(630,230))
            audUSD.setFill('white')
            audUSD.draw(audd)

            audEUR = Rectangle(Point(650,180),Point(850,230))
            audEUR.setFill('white')
            audEUR.draw(audd)

            audBRL = Rectangle(Point(540,250),Point(740,300))
            audBRL.setFill('white')
            audBRL.draw(audd)

            voltar = Rectangle(Point(50,40),Point(200,80))
            voltar.setFill('blue')
            voltar.setOutline('blue4')
            voltar.setWidth(6)
            voltar.draw(audd)
            text_voltar = Text(Point(125,60),'VOLTAR')
            text_voltar.setFace('helvetica')
            text_voltar.setStyle('bold')
            text_voltar.setSize(25)
            text_voltar.draw(audd)

            text_novaconsulta = Text(Point(640,660),'PARA NOVA CONSULTA, CLIQUE EM VOLTAR E RETORNE')
            text_novaconsulta.setFace('helvetica')
            text_novaconsulta.setStyle('bold')
            text_novaconsulta.setSize(25)
            text_novaconsulta.draw(audd)  
            def check_click_usd():

                mouse = audd.getMouse()
                X = mouse.getX()
                Y = mouse.getY()

                if X > 545 and X < 745 and Y > 120 and Y < 150:
                    text = textEntry.getText()
                    text_audUSD = Text(Point(530,205),'{} USD'.format(round(cotacao_audusd*float(text), 2)))
                    text_audUSD.setSize(20)
                    text_audUSD.setFace('helvetica')
                    text_audUSD.setStyle('bold')
                    text_audUSD.draw(audd)

                    text = textEntry.getText()
                    text_audEUR = Text(Point(750,205),'{} EUR'.format(round(cotacao_audeur*float(text), 2)))
                    text_audEUR.setSize(20)
                    text_audEUR.setFace('helvetica')
                    text_audEUR.setStyle('bold')
                    text_audEUR.draw(audd)

                    text = textEntry.getText()
                    text_audBRL = Text(Point(640,275),'{} BRL'.format(round(cotacao_audbrl*float(text), 2)))
                    text_audBRL.setSize(20)
                    text_audBRL.setFace('helvetica')
                    text_audBRL.setStyle('bold')
                    text_audBRL.draw(audd)

                    arquivo = open('conversao_monetaria-DOLAR AUSTRALIANO.txt','w')
                    arquivo.writelines('Valor inicial: {} AUD'.format(text)+'\n')
                    arquivo.writelines('{} USD'.format(cotacao_audusd*float(text))+'\n')
                    arquivo.writelines('{} EUR'.format(cotacao_audeur*float(text))+'\n')
                    arquivo.writelines('{} BRL'.format(cotacao_audbrl*float(text))+'\n')
                    arquivo.close   
                    check_click_usd()
                if X > 50 and X < 200 and Y > 40 and Y < 80:
                    time.sleep(1)
                    audd.close()
                    moeda()
                    check_click_usd()  
                else:
                    check_click_usd()
            check_click_usd()
            
            
            audd.getKey()
            audd.close()

        def cny():
            cnyy = GraphWin("CONVERSOR MONETARIO - YUAN.",1280,720)
            cnyy.setBackground(color_rgb(126, 182, 157))
            tela_interna=Rectangle(Point(25,25),Point(1255,695))
            tela_interna.setFill(color_rgb(126, 206, 184))
            tela_interna.draw(cnyy)
            text_ = Text(Point(640,60),'VALOR INICIAL EM YUAN.')
            text_.setSize(36)
            text_.setFace('helvetica')
            text_.setStyle('bold')
            text_.draw(cnyy)

            confirmar = Rectangle(Point(545,120),Point(745,150))
            confirmar.setFill('green')
            confirmar.draw(cnyy)
            text_confirmar = Text(Point(640,135),'CONFIRMAR')
            text_confirmar.setSize(10)
            text_confirmar.setFace('helvetica')
            text_confirmar.setStyle('bold')
            text_confirmar.draw(cnyy)
            
            textEntry = Entry(Point(640,100),25)
            textEntry.setFill('white')
            textEntry.draw(cnyy)

            cnyUSD = Rectangle(Point(430,180),Point(630,230))
            cnyUSD.setFill('white')
            cnyUSD.draw(cnyy)

            cnyEUR = Rectangle(Point(650,180),Point(850,230))
            cnyEUR.setFill('white')
            cnyEUR.draw(cnyy)

            cnyBRL = Rectangle(Point(540,250),Point(740,300))
            cnyBRL.setFill('white')
            cnyBRL.draw(cnyy)

            voltar = Rectangle(Point(50,40),Point(200,80))
            voltar.setFill('blue')
            voltar.setOutline('blue4')
            voltar.setWidth(6)
            voltar.draw(cnyy)
            text_voltar = Text(Point(125,60),'VOLTAR')
            text_voltar.setFace('helvetica')
            text_voltar.setStyle('bold')
            text_voltar.setSize(25)
            text_voltar.draw(cnyy)

            text_novaconsulta = Text(Point(640,660),'PARA NOVA CONSULTA, CLIQUE EM VOLTAR E RETORNE')
            text_novaconsulta.setFace('helvetica')
            text_novaconsulta.setStyle('bold')
            text_novaconsulta.setSize(25)
            text_novaconsulta.draw(cnyy)  
            def check_click_usd():

                mouse = cnyy.getMouse()
                X = mouse.getX()
                Y = mouse.getY()

                if X > 545 and X < 745 and Y > 120 and Y < 150:
                    text = textEntry.getText()
                    text_cnyUSD = Text(Point(530,205),'{} USD'.format(round(cotacao_cnyusd*float(text), 2)))
                    text_cnyUSD.setSize(20)
                    text_cnyUSD.setFace('helvetica')
                    text_cnyUSD.setStyle('bold')
                    text_cnyUSD.draw(cnyy)

                    text = textEntry.getText()
                    text_cnyEUR = Text(Point(750,205),'{} EUR'.format(round(cotacao_cnyeur*float(text), 2)))
                    text_cnyEUR.setSize(20)
                    text_cnyEUR.setFace('helvetica')
                    text_cnyEUR.setStyle('bold')
                    text_cnyEUR.draw(cnyy)

                    text = textEntry.getText()
                    text_cnyBRL = Text(Point(640,275),'{} BRL'.format(round(cotacao_cnybrl*float(text), 2)))
                    text_cnyBRL.setSize(20)
                    text_cnyBRL.setFace('helvetica')
                    text_cnyBRL.setStyle('bold')
                    text_cnyBRL.draw(cnyy)
                    arquivo = open('conversao_monetaria-YUAN.txt','w')
                    arquivo.writelines('Valor inicial: {} CNY'.format(text)+'\n')
                    arquivo.writelines('{} USD'.format(cotacao_cnyusd*float(text))+'\n')
                    arquivo.writelines('{} EUR'.format(cotacao_cnyeur*float(text))+'\n')
                    arquivo.writelines('{} BRL'.format(cotacao_cnybrl*float(text))+'\n')
                    arquivo.close   
                    check_click_usd()
                if X > 50 and X < 200 and Y > 40 and Y < 80:
                    time.sleep(1)
                    cnyy.close()
                    moeda()
                    check_click_usd()  
                else:
                    check_click_usd()
            check_click_usd()
            
            
            cnyy.getKey()
            cnyy.close()

        def jpy():
            jpyy = GraphWin("CONVERSOR MONETARIO - IENE",1280,720)
            jpyy.setBackground(color_rgb(126, 182, 157))
            tela_interna=Rectangle(Point(25,25),Point(1255,695))
            tela_interna.setFill(color_rgb(126, 206, 184))
            tela_interna.draw(jpyy)
            text_ = Text(Point(640,60),'VALOR INICIAL EM IENE')
            text_.setSize(36)
            text_.setFace('helvetica')
            text_.setStyle('bold')
            text_.draw(jpyy)

            confirmar = Rectangle(Point(545,120),Point(745,150))
            confirmar.setFill('green')
            confirmar.draw(jpyy)
            text_confirmar = Text(Point(640,135),'CONFIRMAR')
            text_confirmar.setSize(10)
            text_confirmar.setFace('helvetica')
            text_confirmar.setStyle('bold')
            text_confirmar.draw(jpyy)
            
            textEntry = Entry(Point(640,100),25)
            textEntry.setFill('white')
            textEntry.draw(jpyy)

            jpyUSD = Rectangle(Point(430,180),Point(630,230))
            jpyUSD.setFill('white')
            jpyUSD.draw(jpyy)

            jpyEUR = Rectangle(Point(650,180),Point(850,230))
            jpyEUR.setFill('white')
            jpyEUR.draw(jpyy)

            jpyBRL = Rectangle(Point(540,250),Point(740,300))
            jpyBRL.setFill('white')
            jpyBRL.draw(jpyy)

            voltar = Rectangle(Point(50,40),Point(200,80))
            voltar.setFill('blue')
            voltar.setOutline('blue4')
            voltar.setWidth(6)
            voltar.draw(jpyy)
            text_voltar = Text(Point(125,60),'VOLTAR')
            text_voltar.setFace('helvetica')
            text_voltar.setStyle('bold')
            text_voltar.setSize(25)
            text_voltar.draw(jpyy)

            text_novaconsulta = Text(Point(640,660),'PARA NOVA CONSULTA, CLIQUE EM VOLTAR E RETORNE')
            text_novaconsulta.setFace('helvetica')
            text_novaconsulta.setStyle('bold')
            text_novaconsulta.setSize(25)
            text_novaconsulta.draw(jpyy)  
            def check_click_usd():

                mouse = jpyy.getMouse()
                X = mouse.getX()
                Y = mouse.getY()

                if X > 545 and X < 745 and Y > 120 and Y < 150:
                    text = textEntry.getText()
                    text_jpyUSD = Text(Point(530,205),'{} USD'.format(round(cotacao_jpyusd*float(text), 2)))
                    text_jpyUSD.setSize(20)
                    text_jpyUSD.setFace('helvetica')
                    text_jpyUSD.setStyle('bold')
                    text_jpyUSD.draw(jpyy)

                    text = textEntry.getText()
                    text_jpyEUR = Text(Point(750,205),'{} EUR'.format(round(cotacao_jpyeur*float(text), 2)))
                    text_jpyEUR.setSize(20)
                    text_jpyEUR.setFace('helvetica')
                    text_jpyEUR.setStyle('bold')
                    text_jpyEUR.draw(jpyy)

                    text = textEntry.getText()
                    text_jpyBRL = Text(Point(640,275),'{} BRL'.format(round(cotacao_jpybrl*float(text), 2)))
                    text_jpyBRL.setSize(20)
                    text_jpyBRL.setFace('helvetica')
                    text_jpyBRL.setStyle('bold')
                    text_jpyBRL.draw(jpyy)

                    arquivo = open('conversao_monetaria-IENE.txt','w')
                    arquivo.writelines('Valor inicial: {} JPY'.format(text)+'\n')
                    arquivo.writelines('{} USD'.format(cotacao_jpyusd*float(text))+'\n')
                    arquivo.writelines('{} EUR'.format(cotacao_jpyeur*float(text))+'\n')
                    arquivo.writelines('{} BRL'.format(cotacao_jpybrl*float(text))+'\n')
                    arquivo.close   
                    check_click_usd()
                if X > 50 and X < 200 and Y > 40 and Y < 80:
                    time.sleep(1)
                    jpyy.close()
                    moeda()
                    check_click_usd()  
                else:
                    check_click_usd()
            check_click_usd()
            
            
            jpyy.getKey()
            jpyy.close()

        def cad():
            cadd = GraphWin("CONVERSOR MONETARIO - DOLAR CAN.",1280,720)
            cadd.setBackground(color_rgb(126, 182, 157))
            tela_interna=Rectangle(Point(25,25),Point(1255,695))
            tela_interna.setFill(color_rgb(126, 206, 184))
            tela_interna.draw(cadd)
            text_ = Text(Point(640,60),'VALOR INICIAL EM DOLAR CAN.')
            text_.setSize(36)
            text_.setFace('helvetica')
            text_.setStyle('bold')
            text_.draw(cadd)

            confirmar = Rectangle(Point(545,120),Point(745,150))
            confirmar.setFill('green')
            confirmar.draw(cadd)
            text_confirmar = Text(Point(640,135),'CONFIRMAR')
            text_confirmar.setSize(10)
            text_confirmar.setFace('helvetica')
            text_confirmar.setStyle('bold')
            text_confirmar.draw(cadd)
            
            textEntry = Entry(Point(640,100),25)
            textEntry.setFill('white')
            textEntry.draw(cadd)

            cadUSD = Rectangle(Point(430,180),Point(630,230))
            cadUSD.setFill('white')
            cadUSD.draw(cadd)

            cadEUR = Rectangle(Point(650,180),Point(850,230))
            cadEUR.setFill('white')
            cadEUR.draw(cadd)

            cadBRL = Rectangle(Point(540,250),Point(740,300))
            cadBRL.setFill('white')
            cadBRL.draw(cadd)

            voltar = Rectangle(Point(50,40),Point(200,80))
            voltar.setFill('blue')
            voltar.setOutline('blue4')
            voltar.setWidth(6)
            voltar.draw(cadd)
            text_voltar = Text(Point(125,60),'VOLTAR')
            text_voltar.setFace('helvetica')
            text_voltar.setStyle('bold')
            text_voltar.setSize(25)
            text_voltar.draw(cadd)

            text_novaconsulta = Text(Point(640,660),'PARA NOVA CONSULTA, CLIQUE EM VOLTAR E RETORNE')
            text_novaconsulta.setFace('helvetica')
            text_novaconsulta.setStyle('bold')
            text_novaconsulta.setSize(25)
            text_novaconsulta.draw(cadd)  

            def check_click_usd():

                mouse = cadd.getMouse()
                X = mouse.getX()
                Y = mouse.getY()

                if X > 545 and X < 745 and Y > 120 and Y < 150:
                    text = textEntry.getText()
                    text_cadUSD = Text(Point(530,205),'{} USD'.format(round(cotacao_cadusd*float(text), 2)))
                    text_cadUSD.setSize(20)
                    text_cadUSD.setFace('helvetica')
                    text_cadUSD.setStyle('bold')
                    text_cadUSD.draw(cadd)

                    text = textEntry.getText()
                    text_cadEUR = Text(Point(750,205),'{} EUR'.format(round(cotacao_cadeur*float(text), 2)))
                    text_cadEUR.setSize(20)
                    text_cadEUR.setFace('helvetica')
                    text_cadEUR.setStyle('bold')
                    text_cadEUR.draw(cadd)

                    text = textEntry.getText()
                    text_cadBRL = Text(Point(640,275),'{} BRL'.format(round(cotacao_cadbrl*float(text), 2)))
                    text_cadBRL.setSize(20)
                    text_cadBRL.setFace('helvetica')
                    text_cadBRL.setStyle('bold')
                    text_cadBRL.draw(cadd)

                    arquivo = open('conversao_monetaria-DOLAR CANADENSE.txt','w')
                    arquivo.writelines('Valor inicial: {} CAD'.format(text)+'\n')
                    arquivo.writelines('{} USD'.format(cotacao_cadusd*float(text))+'\n')
                    arquivo.writelines('{} EUR'.format(cotacao_cadeur*float(text))+'\n')
                    arquivo.writelines('{} BRL'.format(cotacao_cadbrl*float(text))+'\n')
                    arquivo.close   
                    check_click_usd()
                if X > 50 and X < 200 and Y > 40 and Y < 80:
                    time.sleep(1)
                    cadd.close()
                    moeda()
                    check_click_usd()  
                else:
                    check_click_usd()
            check_click_usd()
            
            
            cadd.getKey()
            cadd.close()

        def ars():
            arss = GraphWin("CONVERSOR MONETARIO - LIBRA EST.",1280,720)
            arss.setBackground(color_rgb(126, 182, 157))
            tela_interna=Rectangle(Point(25,25),Point(1255,695))
            tela_interna.setFill(color_rgb(126, 206, 184))
            tela_interna.draw(arss)
            text_ = Text(Point(640,60),'VALOR INICIAL EM PESO ARG')
            text_.setSize(36)
            text_.setFace('helvetica')
            text_.setStyle('bold')
            text_.draw(arss)

            confirmar = Rectangle(Point(545,120),Point(745,150))
            confirmar.setFill('green')
            confirmar.draw(arss)
            text_confirmar = Text(Point(640,135),'CONFIRMAR')
            text_confirmar.setSize(10)
            text_confirmar.setFace('helvetica')
            text_confirmar.setStyle('bold')
            text_confirmar.draw(arss)
            
            textEntry = Entry(Point(640,100),25)
            textEntry.setFill('white')
            textEntry.draw(arss)

            arsUSD = Rectangle(Point(430,180),Point(630,230))
            arsUSD.setFill('white')
            arsUSD.draw(arss)

            arsEUR = Rectangle(Point(650,180),Point(850,230))
            arsEUR.setFill('white')
            arsEUR.draw(arss)

            arsBRL = Rectangle(Point(540,250),Point(740,300))
            arsBRL.setFill('white')
            arsBRL.draw(arss)

            voltar = Rectangle(Point(50,40),Point(200,80))
            voltar.setFill('blue')
            voltar.setOutline('blue4')
            voltar.setWidth(6)
            voltar.draw(arss)
            text_voltar = Text(Point(125,60),'VOLTAR')
            text_voltar.setFace('helvetica')
            text_voltar.setStyle('bold')
            text_voltar.setSize(25)
            text_voltar.draw(arss)

            text_novaconsulta = Text(Point(640,660),'PARA NOVA CONSULTA, CLIQUE EM VOLTAR E RETORNE')
            text_novaconsulta.setFace('helvetica')
            text_novaconsulta.setStyle('bold')
            text_novaconsulta.setSize(25)
            text_novaconsulta.draw(arss)  
            def check_click_usd():

                mouse = arss.getMouse()
                X = mouse.getX()
                Y = mouse.getY()

                if X > 545 and X < 745 and Y > 120 and Y < 150:
                    text = textEntry.getText()
                    text_arsUSD = Text(Point(530,205),'{} USD'.format(round(cotacao_arsusd*float(text), 2)))
                    text_arsUSD.setSize(20)
                    text_arsUSD.setFace('helvetica')
                    text_arsUSD.setStyle('bold')
                    text_arsUSD.draw(arss)

                    text = textEntry.getText()
                    text_arsEUR = Text(Point(750,205),'{} EUR'.format(round(cotacao_arseur*float(text), 2)))
                    text_arsEUR.setSize(20)
                    text_arsEUR.setFace('helvetica')
                    text_arsEUR.setStyle('bold')
                    text_arsEUR.draw(arss)

                    text = textEntry.getText()
                    text_arsBRL = Text(Point(640,275),'{} BRL'.format(round(cotacao_arsbrl*float(text), 2)))
                    text_arsBRL.setSize(20)
                    text_arsBRL.setFace('helvetica')
                    text_arsBRL.setStyle('bold')
                    text_arsBRL.draw(arss)
                    arquivo = open('conversao_monetaria-PESO ARGENTINO.txt','w')
                    arquivo.writelines('Valor inicial: {} ARS'.format(text)+'\n')
                    arquivo.writelines('{} USD'.format(cotacao_arsusd*float(text))+'\n')
                    arquivo.writelines('{} EUR'.format(cotacao_arseur*float(text))+'\n')
                    arquivo.writelines('{} BRL'.format(cotacao_arsbrl*float(text))+'\n')
                    arquivo.close
                if X > 50 and X < 200 and Y > 40 and Y < 80:
                    time.sleep(1)
                    arss.close()
                    moeda()
                    check_click_usd()                      
                else:
                    check_click_usd()

            check_click_usd()
            
            
            arss.getMouse()
            arss.close()


        def check_click_moeda():

            mouse = moedaa.getMouse()
            X = mouse.getX()
            Y = mouse.getY()

            if X > 70 and X < 420 and Y > 130 and Y < 280:
                time.sleep(1)
                moedaa.close()
                usd()
                check_click_moeda()
            if X > 465 and X < 815 and Y > 130 and Y < 280:
                time.sleep(1)
                moedaa.close()                
                gbp()
                check_click_moeda()
            if X > 860 and X < 1210 and Y > 130 and Y < 280:
                time.sleep(1)
                moedaa.close()                
                jpy()
                check_click_moeda()
            
            if X > 70 and X < 420 and Y > 320 and Y < 470:
                time.sleep(1)
                moedaa.close()                
                eur()
                check_click_moeda()
            if X > 465 and X < 815 and Y > 320 and Y < 470:
                time.sleep(1)
                moedaa.close()                
                aud()
                check_click_moeda()
            if X > 860 and X < 1210 and Y > 320 and Y < 470:
                time.sleep(1)
                moedaa.close()                
                cad()
                check_click_moeda()
            
            if X > 70 and X < 420 and Y > 510 and Y < 660:
                time.sleep(1)
                moedaa.close()                
                brl()
                check_click_moeda()
            if X > 465 and X < 815 and Y > 510 and Y < 660:
                time.sleep(1)
                moedaa.close()                
                cny()
                check_click_moeda()
            if X > 860 and X < 1210 and Y > 510 and Y < 660:
                time.sleep(1)
                moedaa.close()                
                ars()
                check_click_moeda()
            
            if X > 1100 and X < 1200 and Y > 30 and Y < 120:         
                win.close()
                moedaa.close()
            if X > 50 and X < 200 and Y > 40 and Y < 80:
                time.sleep(1)
                moedaa.close()
                main()
                check_click_moeda()
            else:
                check_click_moeda()
        check_click_moeda()


        moedaa.checkKey()
        moedaa.close()
                                             


    def unidades():
        ##### COMPRIMENTO
        ##### VOLUME
        ##### ÁREA
        ##### MASSA
        ##### VELOCIDADE

        unidadess = GraphWin("CONVERSOR DE UNIDADES",1280,720)
        unidadess.setBackground(color_rgb(13, 12, 222))
        tela_interna=Rectangle(Point(25,25),Point(1255,695))
        tela_interna.setFill(color_rgb(91, 89, 222))
        tela_interna.draw(unidadess)
        text_unidades = Text(Point(640,60),'ESCOLHA O TIPO DE CONVERSÃO')
        text_unidades.setSize(36)
        text_unidades.setFace('helvetica')
        text_unidades.setStyle('bold')
        text_unidades.draw(unidadess)

        comprimento = Rectangle(Point(330,200),Point(630,300))
        comprimento.setFill(color_rgb(71, 119, 252))
        comprimento.setOutline(color_rgb(21, 31, 162))
        comprimento.draw(unidadess)
        text_comprimento = Text(Point(480,250),'COMPRIMENTO')
        text_comprimento.setSize(25)
        text_comprimento.setFace('helvetica')
        text_comprimento.setStyle('bold')
        text_comprimento.draw(unidadess)

        volume = Rectangle(Point(650,200),Point(950,300))
        volume.setFill(color_rgb(71, 119, 252))
        volume.setOutline(color_rgb(21, 31, 162))
        volume.draw(unidadess)
        text_volume = Text(Point(800,250),'VOLUME')
        text_volume.setSize(25)
        text_volume.setFace('helvetica')
        text_volume.setStyle('bold')
        text_volume.draw(unidadess)

        area = Rectangle(Point(330,350),Point(630,450))
        area.setFill(color_rgb(71, 119, 252))
        area.setOutline(color_rgb(21, 31, 162))
        area.draw(unidadess)
        text_area = Text(Point(480,400),'ÁREA')
        text_area.setSize(25)
        text_area.setFace('helvetica')
        text_area.setStyle('bold')
        text_area.draw(unidadess)

        massa = Rectangle(Point(650,350),Point(950,450))
        massa.setFill(color_rgb(71, 119, 252))
        massa.setOutline(color_rgb(21, 31, 162))
        massa.draw(unidadess)
        text_massa = Text(Point(800,400),'MASSA')
        text_massa.setSize(25)
        text_massa.setFace('helvetica')
        text_massa.setStyle('bold')
        text_massa.draw(unidadess)

        velocidade = Rectangle(Point(490,500),Point(790,600))
        velocidade.setFill(color_rgb(71, 119, 252))
        velocidade.setOutline(color_rgb(21, 31, 162))
        velocidade.draw(unidadess)
        text_velocidade = Text(Point(640,550),'VELOCIDADE')
        text_velocidade.setSize(25)
        text_velocidade.setFace('helvetica')
        text_velocidade.setStyle('bold')
        text_velocidade.draw(unidadess)

        close = Rectangle(Point(1100,30),Point(1200,120))
        close.setFill(color_rgb(223, 42, 67))
        close.setOutline(color_rgb(191, 68, 75))
        close.setWidth(6)
        close.draw(unidadess)
        text_close = Text(Point(1150,75),'SAIR')
        text_close.setFace('helvetica')
        text_close.setStyle('bold')
        text_close.setSize(25)
        text_close.draw(unidadess)

        voltar = Rectangle(Point(50,640),Point(200,680))
        voltar.setFill('yellow')
        voltar.setOutline('orange')
        voltar.setWidth(6)
        voltar.draw(unidadess)
        text_voltar = Text(Point(125,660),'VOLTAR')
        text_voltar.setFace('helvetica')
        text_voltar.setStyle('bold')
        text_voltar.setSize(25)
        text_voltar.draw(unidadess)


        def comprimento():
            comprimentoo = GraphWin("CONVERSOR DE COMPRIMENTO",1280,720)
            comprimentoo.setBackground(color_rgb(13, 12, 222))
            tela_interna=Rectangle(Point(25,25),Point(1255,695))
            tela_interna.setFill(color_rgb(91, 89, 222))
            tela_interna.draw(comprimentoo)
            text_comprimento = Text(Point(640,60),'ESCOLHA A UNIDADE INICIAL')
            text_comprimento.setSize(36)
            text_comprimento.setFace('helvetica')
            text_comprimento.setStyle('bold')
            text_comprimento.draw(comprimentoo)

            metro = Rectangle(Point(330,100),Point(630,200))
            metro.setFill(color_rgb(71, 119, 252))
            metro.setOutline(color_rgb(21, 31, 162))
            metro.draw(comprimentoo)
            text_metro = Text(Point(480,150),'METRO')
            text_metro.setSize(25)
            text_metro.setFace('helvetica')
            text_metro.setStyle('bold')
            text_metro.draw(comprimentoo)

            quilometro = Rectangle(Point(650,100),Point(950,200))
            quilometro.setFill(color_rgb(71, 119, 252))
            quilometro.setOutline(color_rgb(21, 31, 162))
            quilometro.draw(comprimentoo)
            text_quilometro = Text(Point(800,150),'QUILOMETRO')
            text_quilometro.setSize(25)
            text_quilometro.setFace('helvetica')
            text_quilometro.setStyle('bold')
            text_quilometro.draw(comprimentoo)

            centimetro = Rectangle(Point(330,220),Point(630,320))
            centimetro.setFill(color_rgb(71, 119, 252))
            centimetro.setOutline(color_rgb(21, 31, 162))
            centimetro.draw(comprimentoo)
            text_centimetro = Text(Point(480,270),'CENTIMETRO')
            text_centimetro.setSize(25)
            text_centimetro.setFace('helvetica')
            text_centimetro.setStyle('bold')
            text_centimetro.draw(comprimentoo)

            milha = Rectangle(Point(650,220),Point(950,320))
            milha.setFill(color_rgb(71, 119, 252))
            milha.setOutline(color_rgb(21, 31, 162))
            milha.draw(comprimentoo)
            text_milha = Text(Point(800,270),'MILHA')
            text_milha.setSize(25)
            text_milha.setFace('helvetica')
            text_milha.setStyle('bold')
            text_milha.draw(comprimentoo)

            milimetro = Rectangle(Point(330,340),Point(630,440))
            milimetro.setFill(color_rgb(71, 119, 252))
            milimetro.setOutline(color_rgb(21, 31, 162))
            milimetro.draw(comprimentoo)
            text_milimetro = Text(Point(480,390),'MILIMETRO')
            text_milimetro.setSize(25)
            text_milimetro.setFace('helvetica')
            text_milimetro.setStyle('bold')
            text_milimetro.draw(comprimentoo)

            jarda = Rectangle(Point(650,340),Point(950,440))
            jarda.setFill(color_rgb(71, 119, 252))
            jarda.setOutline(color_rgb(21, 31, 162))
            jarda.draw(comprimentoo)
            text_jarda = Text(Point(800,390),'JARDA')
            text_jarda.setSize(25)
            text_jarda.setFace('helvetica')
            text_jarda.setStyle('bold')
            text_jarda.draw(comprimentoo)

            pe = Rectangle(Point(330,460),Point(630,560))
            pe.setFill(color_rgb(71, 119, 252))
            pe.setOutline(color_rgb(21, 31, 162))
            pe.draw(comprimentoo)
            text_pe = Text(Point(480,510),'PÉ')
            text_pe.setSize(25)
            text_pe.setFace('helvetica')
            text_pe.setStyle('bold')
            text_pe.draw(comprimentoo)

            polegada = Rectangle(Point(650,460),Point(950,560))
            polegada.setFill(color_rgb(71, 119, 252))
            polegada.setOutline(color_rgb(21, 31, 162))
            polegada.draw(comprimentoo)
            text_polegada = Text(Point(800,510),'POLEGADA')
            text_polegada.setSize(25)
            text_polegada.setFace('helvetica')
            text_polegada.setStyle('bold')
            text_polegada.draw(comprimentoo)

            milha_nautica = Rectangle(Point(490,580),Point(790,680))
            milha_nautica.setFill(color_rgb(71, 119, 252))
            milha_nautica.setOutline(color_rgb(21, 31, 162))
            milha_nautica.draw(comprimentoo)
            text_milha_nautica = Text(Point(640,630),'MILHA NÁUTICA')
            text_milha_nautica.setSize(25)
            text_milha_nautica.setFace('helvetica')
            text_milha_nautica.setStyle('bold')
            text_milha_nautica.draw(comprimentoo)

            voltar = Rectangle(Point(50,640),Point(200,680))
            voltar.setFill('yellow')
            voltar.setOutline('orange')
            voltar.setWidth(6)
            voltar.draw(comprimentoo)
            text_voltar = Text(Point(125,660),'VOLTAR')
            text_voltar.setFace('helvetica')
            text_voltar.setStyle('bold')
            text_voltar.setSize(25)
            text_voltar.draw(comprimentoo)


            def metro():
                metroo = GraphWin("CONVERSOR DE COMPRIMENTO - METRO",1280,720)
                metroo.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(metroo)
                text_metro = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_metro.setSize(36)
                text_metro.setFace('helvetica')
                text_metro.setStyle('bold')
                text_metro.draw(metroo)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(metroo)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(metroo)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(metroo)

                mKM = Rectangle(Point(430,180),Point(630,230))
                mKM.setFill('white')
                mKM.draw(metroo)

                mCM = Rectangle(Point(430,250),Point(630,300))
                mCM.setFill('white')
                mCM.draw(metroo)

                mMI = Rectangle(Point(430,320),Point(630,370))
                mMI.setFill('white')
                mMI.draw(metroo)

                mMM = Rectangle(Point(430,390),Point(630,440))
                mMM.setFill('white')
                mMM.draw(metroo)

                mYD = Rectangle(Point(650,180),Point(850,230))
                mYD.setFill('white')
                mYD.draw(metroo)

                mFT = Rectangle(Point(650,250),Point(850,300))
                mFT.setFill('white')
                mFT.draw(metroo)

                mIN = Rectangle(Point(650,320),Point(850,370))
                mIN.setFill('white')
                mIN.draw(metroo)

                mNM = Rectangle(Point(650,390),Point(850,440))
                mNM.setFill('white')
                mNM.draw(metroo)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(metroo)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(metroo)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(metroo)  
                def check_click_usd():

                    mouse = metroo.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_mKM = Text(Point(530,205),'{}km'.format(round(m_km(float(text)), 4)))
                        text_mKM.setSize(20)
                        text_mKM.setFace('helvetica')
                        text_mKM.setStyle('bold')
                        text_mKM.draw(metroo)

                        text = textEntry.getText()
                        text_mCM = Text(Point(530,275),'{}cm'.format(round(m_cm(float(text)), 4)))
                        text_mCM.setSize(20)
                        text_mCM.setFace('helvetica')
                        text_mCM.setStyle('bold')
                        text_mCM.draw(metroo)

                        text = textEntry.getText()
                        text_mMI = Text(Point(530,345),'{}mi'.format(round(m_mi(float(text)), 4)))
                        text_mMI.setSize(20)
                        text_mMI.setFace('helvetica')
                        text_mMI.setStyle('bold')
                        text_mMI.draw(metroo)

                        text = textEntry.getText()
                        text_mMM = Text(Point(530,415),'{}mm'.format(round(m_mm(float(text)), 4)))
                        text_mMM.setSize(20)
                        text_mMM.setFace('helvetica')
                        text_mMM.setStyle('bold')
                        text_mMM.draw(metroo)

                        text = textEntry.getText()
                        text_mYD = Text(Point(750,205),'{}yd'.format(round(m_yd(float(text)), 4)))
                        text_mYD.setSize(20)
                        text_mYD.setFace('helvetica')
                        text_mYD.setStyle('bold')
                        text_mYD.draw(metroo)

                        text = textEntry.getText()
                        text_mFT = Text(Point(750,275),'{}ft'.format(round(m_ft(float(text)), 4)))
                        text_mFT.setSize(20)
                        text_mFT.setFace('helvetica')
                        text_mFT.setStyle('bold')
                        text_mFT.draw(metroo)

                        text = textEntry.getText()
                        text_mIN = Text(Point(750,345),'{}in'.format(round(m_in(float(text)), 4)))
                        text_mIN.setSize(20)
                        text_mIN.setFace('helvetica')
                        text_mIN.setStyle('bold')
                        text_mIN.draw(metroo)

                        text = textEntry.getText()
                        text_mNM = Text(Point(750,415),'{}nm'.format(round(m_nm(float(text)), 4)))
                        text_mNM.setSize(20)
                        text_mNM.setFace('helvetica')
                        text_mNM.setStyle('bold')
                        text_mNM.draw(metroo)

                        arquivo = open('conversao_de_comprimento-METRO.txt','w')
                        arquivo.writelines('Valor inicial: {}m'.format(text)+'\n')
                        arquivo.writelines('{}km'.format(m_km(float(text)))+'\n')
                        arquivo.writelines('{}cm'.format(m_cm(float(text)))+'\n')
                        arquivo.writelines('{}mi'.format(m_mi(float(text)))+'\n')
                        arquivo.writelines('{}yd'.format(m_yd(float(text)))+'\n')
                        arquivo.writelines('{}nm'.format(m_nm(float(text)))+'\n')
                        arquivo.writelines('{}in'.format(m_in(float(text)))+'\n')
                        arquivo.writelines('{}ft'.format(m_ft(float(text)))+'\n')
                        arquivo.writelines('{}mm'.format(m_mm(float(text)))+'\n')
                        arquivo.close
                        check_click_usd()

                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                            time.sleep(1)
                            metroo.close()
                            comprimento()
                            check_click_unidades()

                    else:
                        check_click_usd()
                check_click_usd()
            
            def quilometro():
                quilometroo = GraphWin("CONVERSOR DE COMPRIMENTO - QUILOMETRO",1280,720)
                quilometroo.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(quilometroo)
                text_metro = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_metro.setSize(36)
                text_metro.setFace('helvetica')
                text_metro.setStyle('bold')
                text_metro.draw(quilometroo)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(quilometroo)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(quilometroo)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(quilometroo)

                kmM = Rectangle(Point(430,180),Point(630,230))
                kmM.setFill('white')
                kmM.draw(quilometroo)

                kmCM = Rectangle(Point(430,250),Point(630,300))
                kmCM.setFill('white')
                kmCM.draw(quilometroo)

                kmMI = Rectangle(Point(430,320),Point(630,370))
                kmMI.setFill('white')
                kmMI.draw(quilometroo)

                #kmMM = Rectangle(Point(430,390),Point(630,440))
                #kmMM.setFill('white')
                #kmMM.draw(quilometro)

                kmYD = Rectangle(Point(650,180),Point(850,230))
                kmYD.setFill('white')
                kmYD.draw(quilometroo)

                kmFT = Rectangle(Point(650,250),Point(850,300))
                kmFT.setFill('white')
                kmFT.draw(quilometroo)

                kmIN = Rectangle(Point(650,320),Point(850,370))
                kmIN.setFill('white')
                kmIN.draw(quilometroo)

                kmNM = Rectangle(Point(540,390),Point(740,440))
                kmNM.setFill('white')
                kmNM.draw(quilometroo)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(quilometroo)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(quilometroo)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(quilometroo)  
                def check_click_usd():

                    mouse = quilometroo.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_mKM = Text(Point(530,205),'{}m'.format(round(km_m(float(text)), 4)))
                        text_mKM.setSize(20)
                        text_mKM.setFace('helvetica')
                        text_mKM.setStyle('bold')
                        text_mKM.draw(quilometroo)

                        text = textEntry.getText()
                        text_mCM = Text(Point(530,275),'{}cm'.format(round(km_cm(float(text)), 4)))
                        text_mCM.setSize(20)
                        text_mCM.setFace('helvetica')
                        text_mCM.setStyle('bold')
                        text_mCM.draw(quilometroo)

                        text = textEntry.getText()
                        text_mMI = Text(Point(530,345),'{}mi'.format(round(km_mi(float(text)), 4)))
                        text_mMI.setSize(20)
                        text_mMI.setFace('helvetica')
                        text_mMI.setStyle('bold')
                        text_mMI.draw(quilometroo)

                        text = textEntry.getText()
                        text_mYD = Text(Point(750,205),'{}yd'.format(round(km_yd(float(text)), 4)))
                        text_mYD.setSize(20)
                        text_mYD.setFace('helvetica')
                        text_mYD.setStyle('bold')
                        text_mYD.draw(quilometroo)

                        text = textEntry.getText()
                        text_mFT = Text(Point(750,275),'{}ft'.format(round(km_ft(float(text)), 4)))
                        text_mFT.setSize(20)
                        text_mFT.setFace('helvetica')
                        text_mFT.setStyle('bold')
                        text_mFT.draw(quilometroo)

                        text = textEntry.getText()
                        text_mIN = Text(Point(750,345),'{}in'.format(round(km_in(float(text)), 4)))
                        text_mIN.setSize(20)
                        text_mIN.setFace('helvetica')
                        text_mIN.setStyle('bold')
                        text_mIN.draw(quilometroo)

                        text = textEntry.getText()
                        text_mNM = Text(Point(640,415),'{}nm'.format(round(km_nm(float(text)), 4)))
                        text_mNM.setSize(20)
                        text_mNM.setFace('helvetica')
                        text_mNM.setStyle('bold')
                        text_mNM.draw(quilometroo)

                        arquivo = open('conversao_de_comprimento-QUILOMETRO.txt','w')
                        arquivo.writelines('Valor inicial: {}km'.format(text)+'\n')
                        arquivo.writelines('{}km'.format(km_ft(float(text)))+'\n')
                        arquivo.writelines('{}cm'.format(km_cm(float(text)))+'\n')
                        arquivo.writelines('{}mi'.format(km_mi(float(text)))+'\n')
                        arquivo.writelines('{}yd'.format(km_yd(float(text)))+'\n')
                        arquivo.writelines('{}nm'.format(km_nm(float(text)))+'\n')
                        arquivo.writelines('{}in'.format(km_in(float(text)))+'\n')
                        arquivo.writelines('{}m'.format(km_m(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()

                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                            time.sleep(1)
                            quilometroo.close()
                            comprimento()
                            check_click_unidades()                       
                    else:
                        check_click_usd()
                check_click_usd()

            def centimetro():
                centimetroo = GraphWin("CONVERSOR DE COMPRIMENTO - CENTIMETRO",1280,720)
                centimetroo.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(centimetroo)
                text_centimetro = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_centimetro.setSize(36)
                text_centimetro.setFace('helvetica')
                text_centimetro.setStyle('bold')
                text_centimetro.draw(centimetroo)


                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(centimetroo)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(centimetroo)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(centimetroo)

                mKM = Rectangle(Point(430,180),Point(630,230))
                mKM.setFill('white')
                mKM.draw(centimetroo)

                mCM = Rectangle(Point(430,250),Point(630,300))
                mCM.setFill('white')
                mCM.draw(centimetroo)

                mMM = Rectangle(Point(430,320),Point(630,370))
                mMM.setFill('white')
                mMM.draw(centimetroo)

                mYD = Rectangle(Point(650,180),Point(850,230))
                mYD.setFill('white')
                mYD.draw(centimetroo)

                mFT = Rectangle(Point(650,250),Point(850,300))
                mFT.setFill('white')
                mFT.draw(centimetroo)

                mIN = Rectangle(Point(650,320),Point(850,370))
                mIN.setFill('white')
                mIN.draw(centimetroo)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(centimetroo)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(centimetroo)                

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(centimetroo)  
                def check_click_usd():

                    mouse = centimetroo.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_mKM = Text(Point(530,205),'{}km'.format(round(cm_km(float(text)), 4)))
                        text_mKM.setSize(20)
                        text_mKM.setFace('helvetica')
                        text_mKM.setStyle('bold')
                        text_mKM.draw(centimetroo)

                        text = textEntry.getText()
                        text_mCM = Text(Point(530,275),'{}m'.format(round(cm_m(float(text)), 4)))
                        text_mCM.setSize(20)
                        text_mCM.setFace('helvetica')
                        text_mCM.setStyle('bold')
                        text_mCM.draw(centimetroo)

                        text = textEntry.getText()
                        text_mMM = Text(Point(530,345),'{}mm'.format(round(cm_mm(float(text)), 4)))
                        text_mMM.setSize(20)
                        text_mMM.setFace('helvetica')
                        text_mMM.setStyle('bold')
                        text_mMM.draw(centimetroo)

                        text = textEntry.getText()
                        text_mYD = Text(Point(750,205),'{}yd'.format(round(cm_yd(float(text)), 4)))
                        text_mYD.setSize(20)
                        text_mYD.setFace('helvetica')
                        text_mYD.setStyle('bold')
                        text_mYD.draw(centimetroo)

                        text = textEntry.getText()
                        text_mFT = Text(Point(750,275),'{}ft'.format(round(cm_ft(float(text)), 4)))
                        text_mFT.setSize(20)
                        text_mFT.setFace('helvetica')
                        text_mFT.setStyle('bold')
                        text_mFT.draw(centimetroo)

                        text = textEntry.getText()
                        text_mIN = Text(Point(750,345),'{}in'.format(round(cm_in(float(text)), 4)))
                        text_mIN.setSize(20)
                        text_mIN.setFace('helvetica')
                        text_mIN.setStyle('bold')
                        text_mIN.draw(centimetroo)

                        arquivo = open('conversao_de_comprimento-CENTIMETRO.txt','w')
                        arquivo.writelines('Valor inicial: {}cm'.format(text)+'\n')
                        arquivo.writelines('{}km'.format(cm_km(float(text)))+'\n')
                        arquivo.writelines('{}ft'.format(cm_ft(float(text)))+'\n')
                        arquivo.writelines('{}yd'.format(cm_yd(float(text)))+'\n')
                        arquivo.writelines('{}in'.format(cm_in(float(text)))+'\n')
                        arquivo.writelines('{}m'.format(cm_m(float(text)))+'\n')
                        arquivo.writelines('{}mm'.format(cm_mm(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()
                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                            time.sleep(1)
                            centimetroo.close()
                            comprimento()
                            check_click_unidades()  

                    else:
                        check_click_usd()
                check_click_usd()



            def milha():
                milhaa = GraphWin("CONVERSOR DE COMPRIMENTO - MILHA",1280,720)
                milhaa.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(milhaa)
                text_milha = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_milha.setSize(36)
                text_milha.setFace('helvetica')
                text_milha.setStyle('bold')
                text_milha.draw(milhaa)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(milhaa)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(milhaa)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(milhaa)

                mKM = Rectangle(Point(430,180),Point(630,230))
                mKM.setFill('white')
                mKM.draw(milhaa)

                mCM = Rectangle(Point(430,250),Point(630,300))
                mCM.setFill('white')
                mCM.draw(milhaa)

                mMI = Rectangle(Point(430,320),Point(630,370))
                mMI.setFill('white')
                mMI.draw(milhaa)

                #mMM = Rectangle(Point(430,390),Point(630,440))
                #mMM.setFill('white')
                #mMM.draw(milha)

                mYD = Rectangle(Point(650,180),Point(850,230))
                mYD.setFill('white')
                mYD.draw(milhaa)

                mFT = Rectangle(Point(650,250),Point(850,300))
                mFT.setFill('white')
                mFT.draw(milhaa)

                mIN = Rectangle(Point(650,320),Point(850,370))
                mIN.setFill('white')
                mIN.draw(milhaa)

                mNM = Rectangle(Point(540,390),Point(740,440))
                mNM.setFill('white')
                mNM.draw(milhaa)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(milhaa)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(milhaa)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(milhaa)  
                def check_click_usd():

                    mouse = milhaa.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_mKM = Text(Point(530,205),'{}km'.format(round(mi_km(float(text)), 4)))
                        text_mKM.setSize(20)
                        text_mKM.setFace('helvetica')
                        text_mKM.setStyle('bold')
                        text_mKM.draw(milhaa)

                        text = textEntry.getText()
                        text_mCM = Text(Point(530,275),'{}cm'.format(round(mi_cm(float(text)), 4)))
                        text_mCM.setSize(20)
                        text_mCM.setFace('helvetica')
                        text_mCM.setStyle('bold')
                        text_mCM.draw(milhaa)

                        text = textEntry.getText()
                        text_mMI = Text(Point(530,345),'{}m'.format(round(mi_m(float(text)), 4)))
                        text_mMI.setSize(20)
                        text_mMI.setFace('helvetica')
                        text_mMI.setStyle('bold')
                        text_mMI.draw(milhaa)

                        text = textEntry.getText()
                        text_mYD = Text(Point(750,205),'{}yd'.format(round(mi_yd(float(text)), 4)))
                        text_mYD.setSize(20)
                        text_mYD.setFace('helvetica')
                        text_mYD.setStyle('bold')
                        text_mYD.draw(milhaa)

                        text = textEntry.getText()
                        text_mFT = Text(Point(750,275),'{}ft'.format(round(mi_ft(float(text)), 4)))
                        text_mFT.setSize(20)
                        text_mFT.setFace('helvetica')
                        text_mFT.setStyle('bold')
                        text_mFT.draw(milhaa)

                        text = textEntry.getText()
                        text_mIN = Text(Point(750,345),'{}in'.format(round(mi_in(float(text)), 4)))
                        text_mIN.setSize(20)
                        text_mIN.setFace('helvetica')
                        text_mIN.setStyle('bold')
                        text_mIN.draw(milhaa)

                        text = textEntry.getText()
                        text_mNM = Text(Point(640,415),'{}nm'.format(round(mi_nm(float(text)), 4)))
                        text_mNM.setSize(20)
                        text_mNM.setFace('helvetica')
                        text_mNM.setStyle('bold')
                        text_mNM.draw(milhaa)

                        arquivo = open('conversao_de_comprimento-MILHA.txt','w')
                        arquivo.writelines('Valor inicial: {}mi'.format(text)+'\n')
                        arquivo.writelines('{}km'.format(mi_km(float(text)))+'\n')
                        arquivo.writelines('{}cm'.format(mi_cm(float(text)))+'\n')
                        arquivo.writelines('{}ft'.format(mi_ft(float(text)))+'\n')
                        arquivo.writelines('{}yd'.format(mi_yd(float(text)))+'\n')
                        arquivo.writelines('{}nm'.format(mi_nm(float(text)))+'\n')
                        arquivo.writelines('{}in'.format(mi_in(float(text)))+'\n')
                        arquivo.writelines('{}m'.format(mi_m(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()

                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                            time.sleep(1)
                            milhaa.close()
                            comprimento()
                            check_click_unidades()
                    else:
                        check_click_usd()
                check_click_usd()

            def milimetro():
                milimetroo = GraphWin("CONVERSOR DE COMPRIMENTO - METRO",1280,720)
                milimetroo.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(milimetroo)
                text_milimetro = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_milimetro.setSize(36)
                text_milimetro.setFace('helvetica')
                text_milimetro.setStyle('bold')
                text_milimetro.draw(milimetroo)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(milimetroo)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(milimetroo)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(milimetroo)

                mCM = Rectangle(Point(430,180),Point(630,230))
                mCM.setFill('white')
                mCM.draw(milimetroo)

                mMM = Rectangle(Point(430,250),Point(630,300))
                mMM.setFill('white')
                mMM.draw(milimetroo)

                mFT = Rectangle(Point(650,180),Point(850,230))
                mFT.setFill('white')
                mFT.draw(milimetroo)

                mIN = Rectangle(Point(650,250),Point(850,300))
                mIN.setFill('white')
                mIN.draw(milimetroo)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(milimetroo)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(milimetroo)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(milimetroo)  
                def check_click_usd():

                    mouse = milimetroo.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_mCM = Text(Point(530,205),'{}cm'.format(round(mm_cm(float(text)), 4)))
                        text_mCM.setSize(20)
                        text_mCM.setFace('helvetica')
                        text_mCM.setStyle('bold')
                        text_mCM.draw(milimetroo)

                        text = textEntry.getText()
                        text_mMM = Text(Point(530,275),'{}m'.format(round(mm_m(float(text)), 4)))
                        text_mMM.setSize(20)
                        text_mMM.setFace('helvetica')
                        text_mMM.setStyle('bold')
                        text_mMM.draw(milimetroo)

                        text = textEntry.getText()
                        text_mFT = Text(Point(750,205),'{}ft'.format(round(mm_ft(float(text)), 4)))
                        text_mFT.setSize(20)
                        text_mFT.setFace('helvetica')
                        text_mFT.setStyle('bold')
                        text_mFT.draw(milimetroo)

                        text = textEntry.getText()
                        text_mIN = Text(Point(750,275),'{}in'.format(round(mm_in(float(text)), 4)))
                        text_mIN.setSize(20)
                        text_mIN.setFace('helvetica')
                        text_mIN.setStyle('bold')
                        text_mIN.draw(milimetroo)

                        arquivo = open('conversao_de_comprimento-MILIMETRO.txt','w')
                        arquivo.writelines('Valor inicial: {}mm'.format(text)+'\n')
                        arquivo.writelines('{}cm'.format(mm_cm(float(text)))+'\n')
                        arquivo.writelines('{}in'.format(mm_in(float(text)))+'\n')
                        arquivo.writelines('{}m'.format(mm_m(float(text)))+'\n')
                        arquivo.writelines('{}ft'.format(mm_ft(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()

                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                            time.sleep(1)
                            milimetroo.close()
                            comprimento()
                            check_click_unidades()
                    else:
                        check_click_usd()
                check_click_usd()

            def jarda():
                jardaa = GraphWin("CONVERSOR DE COMPRIMENTO - JARDA",1280,720)
                jardaa.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(jardaa)
                text_jarda = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_jarda.setSize(36)
                text_jarda.setFace('helvetica')
                text_jarda.setStyle('bold')
                text_jarda.draw(jardaa)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(jardaa)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(jardaa)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(jardaa)

                mKM = Rectangle(Point(430,180),Point(630,230))
                mKM.setFill('white')
                mKM.draw(jardaa)

                mCM = Rectangle(Point(430,250),Point(630,300))
                mCM.setFill('white')
                mCM.draw(jardaa)

                mMI = Rectangle(Point(430,320),Point(630,370))
                mMI.setFill('white')
                mMI.draw(jardaa)

                mMM = Rectangle(Point(430,390),Point(630,440))
                mMM.setFill('white')
                mMM.draw(jardaa)

                mYD = Rectangle(Point(650,180),Point(850,230))
                mYD.setFill('white')
                mYD.draw(jardaa)

                mFT = Rectangle(Point(650,250),Point(850,300))
                mFT.setFill('white')
                mFT.draw(jardaa)

                mIN = Rectangle(Point(650,320),Point(850,370))
                mIN.setFill('white')
                mIN.draw(jardaa)

                mNM = Rectangle(Point(650,390),Point(850,440))
                mNM.setFill('white')
                mNM.draw(jardaa)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(jardaa)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(jardaa)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(jardaa)  
                def check_click_usd():

                    mouse = jardaa.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_mKM = Text(Point(530,205),'{}km'.format(round(yd_km(float(text)), 4)))
                        text_mKM.setSize(20)
                        text_mKM.setFace('helvetica')
                        text_mKM.setStyle('bold')
                        text_mKM.draw(jardaa)

                        text = textEntry.getText()
                        text_mCM = Text(Point(530,275),'{}cm'.format(round(yd_cm(float(text)), 4)))
                        text_mCM.setSize(20)
                        text_mCM.setFace('helvetica')
                        text_mCM.setStyle('bold')
                        text_mCM.draw(jardaa)

                        text = textEntry.getText()
                        text_mMI = Text(Point(530,345),'{}mi'.format(round(yd_mi(float(text)), 4)))
                        text_mMI.setSize(20)
                        text_mMI.setFace('helvetica')
                        text_mMI.setStyle('bold')
                        text_mMI.draw(jardaa)

                        text = textEntry.getText()
                        text_mMM = Text(Point(530,415),'{}mm'.format(round(yd_mm(float(text)), 4)))
                        text_mMM.setSize(20)
                        text_mMM.setFace('helvetica')
                        text_mMM.setStyle('bold')
                        text_mMM.draw(jardaa)

                        text = textEntry.getText()
                        text_mYD = Text(Point(750,205),'{}m'.format(round(yd_m(float(text)), 4)))
                        text_mYD.setSize(20)
                        text_mYD.setFace('helvetica')
                        text_mYD.setStyle('bold')
                        text_mYD.draw(jardaa)

                        text = textEntry.getText()
                        text_mFT = Text(Point(750,275),'{}ft'.format(round(yd_ft(float(text)), 4)))
                        text_mFT.setSize(20)
                        text_mFT.setFace('helvetica')
                        text_mFT.setStyle('bold')
                        text_mFT.draw(jardaa)

                        text = textEntry.getText()
                        text_mIN = Text(Point(750,345),'{}in'.format(round(yd_in(float(text)), 4)))
                        text_mIN.setSize(20)
                        text_mIN.setFace('helvetica')
                        text_mIN.setStyle('bold')
                        text_mIN.draw(jardaa)

                        text = textEntry.getText()
                        text_mNM = Text(Point(750,415),'{}nm'.format(round(yd_nm(float(text)), 4)))
                        text_mNM.setSize(20)
                        text_mNM.setFace('helvetica')
                        text_mNM.setStyle('bold')
                        text_mNM.draw(jardaa)

                        arquivo = open('conversao_de_comprimento-JARDA.txt','w')
                        arquivo.writelines('Valor inicial: {}yd'.format(text)+'\n')
                        arquivo.writelines('{}km'.format(yd_km(float(text)))+'\n')
                        arquivo.writelines('{}cm'.format(yd_cm(float(text)))+'\n')
                        arquivo.writelines('{}mi'.format(yd_mi(float(text)))+'\n')
                        arquivo.writelines('{}ft'.format(yd_ft(float(text)))+'\n')
                        arquivo.writelines('{}nm'.format(yd_nm(float(text)))+'\n')
                        arquivo.writelines('{}in'.format(yd_in(float(text)))+'\n')
                        arquivo.writelines('{}m'.format(yd_m(float(text)))+'\n')
                        arquivo.writelines('{}mm'.format(yd_mm(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()

                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                            time.sleep(1)
                            jardaa.close()
                            comprimento()
                            check_click_unidades()
                    else:
                        check_click_usd()
                check_click_usd()

            def pe():
                pee = GraphWin("CONVERSOR DE COMPRIMENTO - PÉS",1280,720)
                pee.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(pee)
                text_pe = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_pe.setSize(36)
                text_pe.setFace('helvetica')
                text_pe.setStyle('bold')
                text_pe.draw(pee)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(pee)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(pee)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(pee)

                mKM = Rectangle(Point(430,180),Point(630,230))
                mKM.setFill('white')
                mKM.draw(pee)

                mCM = Rectangle(Point(430,250),Point(630,300))
                mCM.setFill('white')
                mCM.draw(pee)

                mMI = Rectangle(Point(430,320),Point(630,370))
                mMI.setFill('white')
                mMI.draw(pee)

                mMM = Rectangle(Point(430,390),Point(630,440))
                mMM.setFill('white')
                mMM.draw(pee)

                mYD = Rectangle(Point(650,180),Point(850,230))
                mYD.setFill('white')
                mYD.draw(pee)

                mFT = Rectangle(Point(650,250),Point(850,300))
                mFT.setFill('white')
                mFT.draw(pee)

                mIN = Rectangle(Point(650,320),Point(850,370))
                mIN.setFill('white')
                mIN.draw(pee)

                mNM = Rectangle(Point(650,390),Point(850,440))
                mNM.setFill('white')
                mNM.draw(pee)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(pee)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(pee)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(pee)  
                def check_click_usd():

                    mouse = pee.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_mKM = Text(Point(530,205),'{}km'.format(round(ft_km(float(text)), 4)))
                        text_mKM.setSize(20)
                        text_mKM.setFace('helvetica')
                        text_mKM.setStyle('bold')
                        text_mKM.draw(pee)

                        text = textEntry.getText()
                        text_mCM = Text(Point(530,275),'{}cm'.format(round(ft_cm(float(text)), 4)))
                        text_mCM.setSize(20)
                        text_mCM.setFace('helvetica')
                        text_mCM.setStyle('bold')
                        text_mCM.draw(pee)

                        text = textEntry.getText()
                        text_mMI = Text(Point(530,345),'{}mi'.format(round(ft_mi(float(text)), 4)))
                        text_mMI.setSize(20)
                        text_mMI.setFace('helvetica')
                        text_mMI.setStyle('bold')
                        text_mMI.draw(pee)

                        text = textEntry.getText()
                        text_mMM = Text(Point(530,415),'{}mm'.format(round(ft_mm(float(text)), 4)))
                        text_mMM.setSize(20)
                        text_mMM.setFace('helvetica')
                        text_mMM.setStyle('bold')
                        text_mMM.draw(pee)

                        text = textEntry.getText()
                        text_mYD = Text(Point(750,205),'{}yd'.format(round(ft_yd(float(text)), 4)))
                        text_mYD.setSize(20)
                        text_mYD.setFace('helvetica')
                        text_mYD.setStyle('bold')
                        text_mYD.draw(pee)

                        text = textEntry.getText()
                        text_mFT = Text(Point(750,275),'{}m'.format(round(ft_m(float(text)), 4)))
                        text_mFT.setSize(20)
                        text_mFT.setFace('helvetica')
                        text_mFT.setStyle('bold')
                        text_mFT.draw(pee)

                        text = textEntry.getText()
                        text_mIN = Text(Point(750,345),'{}in'.format(round(ft_in(float(text)), 4)))
                        text_mIN.setSize(20)
                        text_mIN.setFace('helvetica')
                        text_mIN.setStyle('bold')
                        text_mIN.draw(pee)

                        text = textEntry.getText()
                        text_mNM = Text(Point(750,415),'{}nm'.format(round(ft_nm(float(text)), 4)))
                        text_mNM.setSize(20)
                        text_mNM.setFace('helvetica')
                        text_mNM.setStyle('bold')
                        text_mNM.draw(pee)

                        arquivo = open('conversao_de_comprimento-PE.txt','w')
                        arquivo.writelines('Valor inicial: {}ft'.format(text)+'\n')
                        arquivo.writelines('{}km'.format(ft_km(float(text)))+'\n')
                        arquivo.writelines('{}cm'.format(ft_cm(float(text)))+'\n')
                        arquivo.writelines('{}mi'.format(ft_mi(float(text)))+'\n')
                        arquivo.writelines('{}yd'.format(ft_yd(float(text)))+'\n')
                        arquivo.writelines('{}nm'.format(ft_nm(float(text)))+'\n')
                        arquivo.writelines('{}in'.format(ft_in(float(text)))+'\n')
                        arquivo.writelines('{}m'.format(ft_m(float(text)))+'\n')
                        arquivo.writelines('{}mm'.format(ft_mm(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()

                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                            time.sleep(1)
                            pee.close()
                            comprimento()
                            check_click_unidades()
                    else:
                        check_click_usd()
                check_click_usd()

            def polegada():
                polegadaa = GraphWin("CONVERSOR DE COMPRIMENTO - POLEGADA",1280,720)
                polegadaa.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(polegadaa)
                text_polegada = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_polegada.setSize(36)
                text_polegada.setFace('helvetica')
                text_polegada.setStyle('bold')
                text_polegada.draw(polegadaa)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(polegadaa)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(polegadaa)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(polegadaa)

                mKM = Rectangle(Point(430,180),Point(630,230))
                mKM.setFill('white')
                mKM.draw(polegadaa)

                mCM = Rectangle(Point(430,250),Point(630,300))
                mCM.setFill('white')
                mCM.draw(polegadaa)

                mYD = Rectangle(Point(650,180),Point(850,230))
                mYD.setFill('white')
                mYD.draw(polegadaa)

                mFT = Rectangle(Point(650,250),Point(850,300))
                mFT.setFill('white')
                mFT.draw(polegadaa)

                mIN = Rectangle(Point(540,320),Point(740,370))
                mIN.setFill('white')
                mIN.draw(polegadaa)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(polegadaa)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(polegadaa)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(polegadaa)  
                def check_click_usd():

                    mouse = polegadaa.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:

                        text = textEntry.getText()
                        text_mCM = Text(Point(530,275),'{}cm'.format(round(in_cm(float(text)), 4)))
                        text_mCM.setSize(20)
                        text_mCM.setFace('helvetica')
                        text_mCM.setStyle('bold')
                        text_mCM.draw(polegadaa)

                        text = textEntry.getText()
                        text_mMM = Text(Point(530,205),'{}mm'.format(round(in_mm(float(text)), 4)))
                        text_mMM.setSize(20)
                        text_mMM.setFace('helvetica')
                        text_mMM.setStyle('bold')
                        text_mMM.draw(polegadaa)

                        text = textEntry.getText()
                        text_mYD = Text(Point(750,205),'{}yd'.format(round(in_yd(float(text)), 4)))
                        text_mYD.setSize(20)
                        text_mYD.setFace('helvetica')
                        text_mYD.setStyle('bold')
                        text_mYD.draw(polegadaa)

                        text = textEntry.getText()
                        text_mFT = Text(Point(750,275),'{}ft'.format(round(in_ft(float(text)), 4)))
                        text_mFT.setSize(20)
                        text_mFT.setFace('helvetica')
                        text_mFT.setStyle('bold')
                        text_mFT.draw(polegadaa)

                        text = textEntry.getText()
                        text_mIN = Text(Point(640,345),'{}m'.format(round(in_m(float(text)), 4)))
                        text_mIN.setSize(20)
                        text_mIN.setFace('helvetica')
                        text_mIN.setStyle('bold')
                        text_mIN.draw(polegadaa)

                        arquivo = open('conversao_de_comprimento-POLEGADA.txt','w')
                        arquivo.writelines('Valor inicial: {}in'.format(text)+'\n')
                        arquivo.writelines('{}cm'.format(in_cm(float(text)))+'\n')
                        arquivo.writelines('{}yd'.format(in_yd(float(text)))+'\n')
                        arquivo.writelines('{}ft'.format(in_ft(float(text)))+'\n')
                        arquivo.writelines('{}in'.format(in_mm(float(text)))+'\n')
                        arquivo.writelines('{}m'.format(in_m(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()

                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                            time.sleep(1)
                            polegadaa.close()
                            comprimento()
                            check_click_unidades()
                    else:
                        check_click_usd()
                check_click_usd()

            def milhanautica():
                milhanauticaa = GraphWin("CONVERSOR DE COMPRIMENTO - MILHA NAUTICA",1280,720)
                milhanauticaa.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(milhanauticaa)
                text_milhanautica = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_milhanautica.setSize(36)
                text_milhanautica.setFace('helvetica')
                text_milhanautica.setStyle('bold')
                text_milhanautica.draw(milhanauticaa)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(milhanauticaa)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(milhanauticaa)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(milhanauticaa)

                mKM = Rectangle(Point(430,180),Point(630,230))
                mKM.setFill('white')
                mKM.draw(milhanauticaa)

                mCM = Rectangle(Point(430,250),Point(630,300))
                mCM.setFill('white')
                mCM.draw(milhanauticaa)

                mMI = Rectangle(Point(430,320),Point(630,370))
                mMI.setFill('white')
                mMI.draw(milhanauticaa)

                mYD = Rectangle(Point(650,180),Point(850,230))
                mYD.setFill('white')
                mYD.draw(milhanauticaa)

                mFT = Rectangle(Point(650,250),Point(850,300))
                mFT.setFill('white')
                mFT.draw(milhanauticaa)

                mIN = Rectangle(Point(650,320),Point(850,370))
                mIN.setFill('white')
                mIN.draw(milhanauticaa)

                mNM = Rectangle(Point(540,390),Point(740,440))
                mNM.setFill('white')
                mNM.draw(milhanauticaa)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(milhanauticaa)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(milhanauticaa)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(milhanauticaa)  
                def check_click_usd():

                    mouse = milhanauticaa.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_mKM = Text(Point(530,205),'{}km'.format(round(nm_km(float(text)), 4)))
                        text_mKM.setSize(20)
                        text_mKM.setFace('helvetica')
                        text_mKM.setStyle('bold')
                        text_mKM.draw(milhanauticaa)

                        text = textEntry.getText()
                        text_mCM = Text(Point(530,275),'{}cm'.format(round(nm_cm(float(text)), 4)))
                        text_mCM.setSize(20)
                        text_mCM.setFace('helvetica')
                        text_mCM.setStyle('bold')
                        text_mCM.draw(milhanauticaa)

                        text = textEntry.getText()
                        text_mMI = Text(Point(530,345),'{}mi'.format(round(nm_mi(float(text)), 4)))
                        text_mMI.setSize(20)
                        text_mMI.setFace('helvetica')
                        text_mMI.setStyle('bold')
                        text_mMI.draw(milhanauticaa)

                        text = textEntry.getText()
                        text_mYD = Text(Point(750,205),'{}yd'.format(round(nm_yd(float(text)), 4)))
                        text_mYD.setSize(20)
                        text_mYD.setFace('helvetica')
                        text_mYD.setStyle('bold')
                        text_mYD.draw(milhanauticaa)

                        text = textEntry.getText()
                        text_mFT = Text(Point(750,275),'{}ft'.format(round(nm_ft(float(text)), 4)))
                        text_mFT.setSize(20)
                        text_mFT.setFace('helvetica')
                        text_mFT.setStyle('bold')
                        text_mFT.draw(milhanauticaa)

                        text = textEntry.getText()
                        text_mIN = Text(Point(750,345),'{}in'.format(round(nm_in(float(text)), 4)))
                        text_mIN.setSize(20)
                        text_mIN.setFace('helvetica')
                        text_mIN.setStyle('bold')
                        text_mIN.draw(milhanauticaa)

                        text = textEntry.getText()
                        text_mNM = Text(Point(640,415),'{}m'.format(round(nm_m(float(text)), 4)))
                        text_mNM.setSize(20)
                        text_mNM.setFace('helvetica')
                        text_mNM.setStyle('bold')
                        text_mNM.draw(milhanauticaa)

                        arquivo = open('conversao_de_comprimento-MILHA NAUTICA.txt','w')
                        arquivo.writelines('Valor inicial: {}nm'.format(text)+'\n')
                        arquivo.writelines('{}km'.format(nm_km(float(text)))+'\n')
                        arquivo.writelines('{}cm'.format(nm_cm(float(text)))+'\n')
                        arquivo.writelines('{}mi'.format(nm_mi(float(text)))+'\n')
                        arquivo.writelines('{}yd'.format(nm_yd(float(text)))+'\n')
                        arquivo.writelines('{}ft'.format(nm_ft(float(text)))+'\n')
                        arquivo.writelines('{}in'.format(nm_in(float(text)))+'\n')
                        arquivo.writelines('{}m'.format(nm_m(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()

                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        milhanauticaa.close()
                        comprimento()
                    else:
                        check_click_usd()
                check_click_usd()
                
            def check_click_unidades():

                mouse = comprimentoo.getMouse()
                X = mouse.getX()
                Y = mouse.getY()

                if X > 330 and X < 630 and Y > 100 and Y < 200:
                    time.sleep(1)
                    comprimentoo.close()
                    metro()
                    check_click_unidades()
                if X > 650 and X < 950 and Y > 100 and Y < 200:
                    time.sleep(1)
                    comprimentoo.close()
                    quilometro()
                    check_click_unidades()
    
                if X > 330 and X < 630 and Y > 220 and Y < 320:
                    time.sleep(1)
                    comprimentoo.close()
                    centimetro()
                    check_click_unidades()           
                if X > 650 and X < 950 and Y > 220 and Y < 320:
                    time.sleep(1)
                    comprimentoo.close()
                    milha()
                    check_click_unidades()

                if X > 330 and X < 630 and Y > 340 and Y < 440:
                    time.sleep(1)
                    comprimentoo.close()
                    milimetro()
                    check_click_unidades()
                if X > 650 and X < 950 and Y > 340 and Y < 440:
                    time.sleep(1)
                    comprimentoo.close()
                    jarda()
                    check_click_unidades()
                
                if X > 330 and X < 630 and Y > 460 and Y < 560:
                    time.sleep(1)
                    comprimentoo.close()
                    pe()
                    check_click_unidades()
                if X > 650 and X < 950 and Y > 460 and Y < 560:
                    time.sleep(1)
                    comprimentoo.close()
                    polegada()
                    check_click_unidades()

                if X > 490 and X < 790 and Y > 580 and Y < 680:
                    time.sleep(1)
                    comprimentoo.close()
                    milhanautica()
                    check_click_unidades()
                if X > 50 and X < 200 and Y > 640 and Y < 680:
                    time.sleep(1)
                    comprimentoo.close()
                    unidades()
                    check_click_unidades()
                else:
                    check_click_unidades()
            check_click_unidades()
        
        def volume():
            volumee = GraphWin("CONVERSOR DE VOLUME",1280,720)
            volumee.setBackground(color_rgb(13, 12, 222))
            tela_interna=Rectangle(Point(25,25),Point(1255,695))
            tela_interna.setFill(color_rgb(91, 89, 222))
            tela_interna.draw(volumee)
            text_volume = Text(Point(640,60),'ESCOLHA A UNIDADE INICIAL')
            text_volume.setSize(36)
            text_volume.setFace('helvetica')
            text_volume.setStyle('bold')
            text_volume.draw(volumee)

            litro = Rectangle(Point(330,200),Point(630,300))
            litro.setFill(color_rgb(71, 119, 252))
            litro.setOutline(color_rgb(21, 31, 162))
            litro.draw(volumee)
            text_litro = Text(Point(480,250),'LITRO')
            text_litro.setSize(25)
            text_litro.setFace('helvetica')
            text_litro.setStyle('bold')
            text_litro.draw(volumee)

            galao = Rectangle(Point(650,200),Point(950,300))
            galao.setFill(color_rgb(71, 119, 252))
            galao.setOutline(color_rgb(21, 31, 162))
            galao.draw(volumee)
            text_galao = Text(Point(800,250),'GALÃO')
            text_galao.setSize(25)
            text_galao.setFace('helvetica')
            text_galao.setStyle('bold')
            text_galao.draw(volumee)

            mililitro = Rectangle(Point(330,350),Point(630,450))
            mililitro.setFill(color_rgb(71, 119, 252))
            mililitro.setOutline(color_rgb(21, 31, 162))
            mililitro.draw(volumee)
            text_mililitro = Text(Point(480,400),'MILILITRO')
            text_mililitro.setSize(25)
            text_mililitro.setFace('helvetica')
            text_mililitro.setStyle('bold')
            text_mililitro.draw(volumee)

            mcubico = Rectangle(Point(650,350),Point(950,450))
            mcubico.setFill(color_rgb(71, 119, 252))
            mcubico.setOutline(color_rgb(21, 31, 162))
            mcubico.draw(volumee)
            text_mcubico = Text(Point(800,400),'METRO CUBICO')
            text_mcubico.setSize(25)
            text_mcubico.setFace('helvetica')
            text_mcubico.setStyle('bold')
            text_mcubico.draw(volumee)

            voltar = Rectangle(Point(50,640),Point(200,680))
            voltar.setFill('yellow')
            voltar.setOutline('orange')
            voltar.setWidth(6)
            voltar.draw(volumee)
            text_voltar = Text(Point(125,660),'VOLTAR')
            text_voltar.setFace('helvetica')
            text_voltar.setStyle('bold')
            text_voltar.setSize(25)
            text_voltar.draw(volumee)

            def litro():
                litroo = GraphWin("CONVERSOR DE VOLUME - LITRO",1280,720)
                litroo.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(litroo)
                text_litro = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_litro.setSize(36)
                text_litro.setFace('helvetica')
                text_litro.setStyle('bold')
                text_litro.draw(litroo)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(litroo)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(litroo)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(litroo)

                lGAL = Rectangle(Point(430,180),Point(630,230))
                lGAL.setFill('white')
                lGAL.draw(litroo)

                lM3 = Rectangle(Point(650,180),Point(850,230))
                lM3.setFill('white')
                lM3.draw(litroo)

                lML = Rectangle(Point(540,250),Point(740,300))
                lML.setFill('white')
                lML.draw(litroo)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(litroo)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(litroo)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(litroo)  
                def check_click_usd():

                    mouse = litroo.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_lGAL = Text(Point(530,205),'{}gal'.format(round(l_gal(float(text)), 4)))
                        text_lGAL.setSize(20)
                        text_lGAL.setFace('helvetica')
                        text_lGAL.setStyle('bold')
                        text_lGAL.draw(litroo)

                        text = textEntry.getText()
                        text_mM3 = Text(Point(750,205),'{}m³'.format(round(l_m3(float(text)), 4)))
                        text_mM3.setSize(20)
                        text_mM3.setFace('helvetica')
                        text_mM3.setStyle('bold')
                        text_mM3.draw(litroo)

                        text = textEntry.getText()
                        text_lML = Text(Point(640,275),'{}ml'.format(round(l_ml(float(text)), 4)))
                        text_lML.setSize(20)
                        text_lML.setFace('helvetica')
                        text_lML.setStyle('bold')
                        text_lML.draw(litroo)

                        arquivo = open('conversao_de_volume-LITRO.txt','w')
                        arquivo.writelines('Valor inicial: {}l'.format(text)+'\n')
                        arquivo.writelines('{}gal'.format(l_gal(float(text)))+'\n')
                        arquivo.writelines('{}m³'.format(l_m3(float(text)))+'\n')
                        arquivo.writelines('{}ml'.format(l_ml(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()
                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        litroo.close()
                        volume()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()

            def galao():
                litroo = GraphWin("CONVERSOR DE VOLUME - GALAO",1280,720)
                litroo.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(litroo)
                text_litro = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_litro.setSize(36)
                text_litro.setFace('helvetica')
                text_litro.setStyle('bold')
                text_litro.draw(litroo)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(litroo)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(litroo)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(litroo)

                lGAL = Rectangle(Point(430,180),Point(630,230))
                lGAL.setFill('white')
                lGAL.draw(litroo)

                lM3 = Rectangle(Point(650,180),Point(850,230))
                lM3.setFill('white')
                lM3.draw(litroo)

                lML = Rectangle(Point(540,250),Point(740,300))
                lML.setFill('white')
                lML.draw(litroo)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(litroo)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(litroo)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(litroo)  
                def check_click_usd():

                    mouse = litroo.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_lGAL = Text(Point(530,205),'{}l'.format(round(gal_l(float(text)), 4)))
                        text_lGAL.setSize(20)
                        text_lGAL.setFace('helvetica')
                        text_lGAL.setStyle('bold')
                        text_lGAL.draw(litroo)

                        text = textEntry.getText()
                        text_mM3 = Text(Point(750,205),'{}m³'.format(round(gal_m3(float(text)), 4)))
                        text_mM3.setSize(20)
                        text_mM3.setFace('helvetica')
                        text_mM3.setStyle('bold')
                        text_mM3.draw(litroo)

                        text = textEntry.getText()
                        text_lML = Text(Point(640,275),'{}ml'.format(round(gal_ml(float(text)), 4)))
                        text_lML.setSize(20)
                        text_lML.setFace('helvetica')
                        text_lML.setStyle('bold')
                        text_lML.draw(litroo)

                        arquivo = open('conversao_de_volume-GALAO.txt','w')
                        arquivo.writelines('Valor inicial: {}gal'.format(text)+'\n')
                        arquivo.writelines('{}m³'.format(gal_m3(float(text)))+'\n')
                        arquivo.writelines('{}l'.format(gal_l(float(text)))+'\n')
                        arquivo.writelines('{}ml'.format(gal_ml(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()
                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        litroo.close()
                        volume()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()
            def mililitro():
                litroo = GraphWin("CONVERSOR DE VOLUME - MILILITRO",1280,720)
                litroo.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(litroo)
                text_litro = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_litro.setSize(36)
                text_litro.setFace('helvetica')
                text_litro.setStyle('bold')
                text_litro.draw(litroo)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(litroo)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(litroo)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(litroo)

                lGAL = Rectangle(Point(430,180),Point(630,230))
                lGAL.setFill('white')
                lGAL.draw(litroo)

                lM3 = Rectangle(Point(650,180),Point(850,230))
                lM3.setFill('white')
                lM3.draw(litroo)

                lML = Rectangle(Point(540,250),Point(740,300))
                lML.setFill('white')
                lML.draw(litroo)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(litroo)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(litroo)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(litroo)  
                def check_click_usd():

                    mouse = litroo.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_lGAL = Text(Point(530,205),'{}gal'.format(round(ml_gal(float(text)), 4)))
                        text_lGAL.setSize(20)
                        text_lGAL.setFace('helvetica')
                        text_lGAL.setStyle('bold')
                        text_lGAL.draw(litroo)

                        text = textEntry.getText()
                        text_mM3 = Text(Point(750,205),'{}m³'.format(round(ml_m3(float(text)), 4)))
                        text_mM3.setSize(20)
                        text_mM3.setFace('helvetica')
                        text_mM3.setStyle('bold')
                        text_mM3.draw(litroo)

                        text = textEntry.getText()
                        text_lML = Text(Point(640,275),'{}l'.format(round(ml_l(float(text)), 4)))
                        text_lML.setSize(20)
                        text_lML.setFace('helvetica')
                        text_lML.setStyle('bold')
                        text_lML.draw(litroo)

                        arquivo = open('conversao_de_volume-MILILITRO.txt','w')
                        arquivo.writelines('Valor inicial: {}ml'.format(text)+'\n')
                        arquivo.writelines('{}gal'.format(ml_gal(float(text)))+'\n')
                        arquivo.writelines('{}m³'.format(ml_m3(float(text)))+'\n')
                        arquivo.writelines('{}l'.format(ml_l(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()
                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        litroo.close()
                        volume()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()
            def mcubico(): 
                litroo = GraphWin("CONVERSOR DE VOLUME - METRO CUBICO",1280,720)
                litroo.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(litroo)
                text_litro = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_litro.setSize(36)
                text_litro.setFace('helvetica')
                text_litro.setStyle('bold')
                text_litro.draw(litroo)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(litroo)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(litroo)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(litroo)

                lGAL = Rectangle(Point(430,180),Point(630,230))
                lGAL.setFill('white')
                lGAL.draw(litroo)

                lM3 = Rectangle(Point(650,180),Point(850,230))
                lM3.setFill('white')
                lM3.draw(litroo)

                lML = Rectangle(Point(540,250),Point(740,300))
                lML.setFill('white')
                lML.draw(litroo)
                
                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(litroo)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(litroo)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(litroo)  
                def check_click_usd():

                    mouse = litroo.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_lGAL = Text(Point(530,205),'{}gal'.format(round(m3_gal(float(text)), 4)))
                        text_lGAL.setSize(20)
                        text_lGAL.setFace('helvetica')
                        text_lGAL.setStyle('bold')
                        text_lGAL.draw(litroo)

                        text = textEntry.getText()
                        text_mM3 = Text(Point(750,205),'{}l'.format(round(m3_l(float(text)), 4)))
                        text_mM3.setSize(20)
                        text_mM3.setFace('helvetica')
                        text_mM3.setStyle('bold')
                        text_mM3.draw(litroo)

                        text = textEntry.getText()
                        text_lML = Text(Point(640,275),'{}ml'.format(round(m3_ml(float(text)), 4)))
                        text_lML.setSize(20)
                        text_lML.setFace('helvetica')
                        text_lML.setStyle('bold')
                        text_lML.draw(litroo)
                        
                        arquivo = open('conversao_de_volume-METRO CUBICO.txt','w')
                        arquivo.writelines('Valor inicial: {}m³'.format(text)+'\n')
                        arquivo.writelines('{}gal'.format(m3_gal(float(text)))+'\n')
                        arquivo.writelines('{}l'.format(m3_l(float(text)))+'\n')
                        arquivo.writelines('{}ml'.format(m3_ml(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()
                    
                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        litroo.close()
                        volume()
                        check_click_usd()
                
                    else:
                        check_click_usd()
                check_click_usd()
            
            def check_click_unidades():

                mouse = volumee.getMouse()
                X = mouse.getX()
                Y = mouse.getY()

                if X > 330 and X < 630 and Y > 200 and Y < 300:
                    time.sleep(1)
                    volumee.close()                    
                    litro()
                    check_click_unidades()
                if X > 650 and X < 950 and Y > 200 and Y < 300:
                    time.sleep(1)
                    volumee.close()                       
                    galao()
                    check_click_unidades()
    
                if X > 330 and X < 630 and Y > 350 and Y < 450:
                    time.sleep(1)
                    volumee.close()                       
                    mililitro()
                    check_click_unidades()           
                if X > 650 and X < 950 and Y > 350 and Y < 450:
                    time.sleep(1)
                    volumee.close()                       
                    mcubico()
                    check_click_unidades()
                if X > 50 and X < 200 and Y > 640 and Y < 680:
                    time.sleep(1)
                    volumee.close()
                    unidades()
                    check_click_unidades()
                else:
                    check_click_unidades()
            check_click_unidades()                            

        def area():
            areaa = GraphWin("CONVERSOR DE UNIDADES",1280,720)
            areaa.setBackground(color_rgb(13, 12, 222))
            tela_interna=Rectangle(Point(25,25),Point(1255,695))
            tela_interna.setFill(color_rgb(91, 89, 222))
            tela_interna.draw(areaa)
            text_area = Text(Point(640,60),'ESCOLHA A UNIDADE INICIAL')
            text_area.setSize(36)
            text_area.setFace('helvetica')
            text_area.setStyle('bold')
            text_area.draw(areaa)

            qquadrado = Rectangle(Point(330,200),Point(630,300))
            qquadrado.setFill(color_rgb(71, 119, 252))
            qquadrado.setOutline(color_rgb(21, 31, 162))
            qquadrado.draw(areaa)
            text_qquadrado = Text(Point(480,250),'QUILOMETRO²')
            text_qquadrado.setSize(25)
            text_qquadrado.setFace('helvetica')
            text_qquadrado.setStyle('bold')
            text_qquadrado.draw(areaa)

            mquadrado = Rectangle(Point(650,200),Point(950,300))
            mquadrado.setFill(color_rgb(71, 119, 252))
            mquadrado.setOutline(color_rgb(21, 31, 162))
            mquadrado.draw(areaa)
            text_mquadrado = Text(Point(800,250),'METRO²')
            text_mquadrado.setSize(25)
            text_mquadrado.setFace('helvetica')
            text_mquadrado.setStyle('bold')
            text_mquadrado.draw(areaa)

            hectare = Rectangle(Point(330,350),Point(630,450))
            hectare.setFill(color_rgb(71, 119, 252))
            hectare.setOutline(color_rgb(21, 31, 162))
            hectare.draw(areaa)
            text_hectare = Text(Point(480,400),'HECTARE')
            text_hectare.setSize(25)
            text_hectare.setFace('helvetica')
            text_hectare.setStyle('bold')
            text_hectare.draw(areaa)

            miquadrada = Rectangle(Point(650,350),Point(950,450))
            miquadrada.setFill(color_rgb(71, 119, 252))
            miquadrada.setOutline(color_rgb(21, 31, 162))
            miquadrada.draw(areaa)
            text_miquadrada = Text(Point(800,400),'MILHA²')
            text_miquadrada.setSize(25)
            text_miquadrada.setFace('helvetica')
            text_miquadrada.setStyle('bold')
            text_miquadrada.draw(areaa)

            voltar = Rectangle(Point(50,640),Point(200,680))
            voltar.setFill('yellow')
            voltar.setOutline('orange')
            voltar.setWidth(6)
            voltar.draw(areaa)
            text_voltar = Text(Point(125,660),'VOLTAR')
            text_voltar.setFace('helvetica')
            text_voltar.setStyle('bold')
            text_voltar.setSize(25)
            text_voltar.draw(areaa)

            def qquadrado():
                qquadradoo = GraphWin("CONVERSOR DE ÁREA - QUILOMETRO QUADRADO",1280,720)
                qquadradoo.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(qquadradoo)
                text_qquadrado = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_qquadrado.setSize(36)
                text_qquadrado.setFace('helvetica')
                text_qquadrado.setStyle('bold')
                text_qquadrado.draw(qquadradoo)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(qquadradoo)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(qquadradoo)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(qquadradoo)

                km2M2 = Rectangle(Point(430,180),Point(630,230))
                km2M2.setFill('white')
                km2M2.draw(qquadradoo)

                km2HA = Rectangle(Point(650,180),Point(850,230))
                km2HA.setFill('white')
                km2HA.draw(qquadradoo)

                km2MI2 = Rectangle(Point(540,250),Point(740,300))
                km2MI2.setFill('white')
                km2MI2.draw(qquadradoo)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(qquadradoo)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(qquadradoo)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(qquadradoo)  
                def check_click_usd():

                    mouse = qquadradoo.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_km2M2 = Text(Point(530,205),'{}m²'.format(round(km2_m2(float(text)), 4)))
                        text_km2M2.setSize(20)
                        text_km2M2.setFace('helvetica')
                        text_km2M2.setStyle('bold')
                        text_km2M2.draw(qquadradoo)

                        text = textEntry.getText()
                        text_km2HA = Text(Point(750,205),'{}ha'.format(round(km2_ha(float(text)), 4)))
                        text_km2HA.setSize(20)
                        text_km2HA.setFace('helvetica')
                        text_km2HA.setStyle('bold')
                        text_km2HA.draw(qquadradoo)

                        text = textEntry.getText()
                        text_km2MI2 = Text(Point(640,275),'{}mi²'.format(round(km2_mi2(float(text)), 4)))
                        text_km2MI2.setSize(20)
                        text_km2MI2.setFace('helvetica')
                        text_km2MI2.setStyle('bold')
                        text_km2MI2.draw(qquadradoo)
                        
                        arquivo = open('conversao_de_area-QUILOMETRO QUADRADO.txt','w')
                        arquivo.writelines('Valor inicial: {}km²'.format(text)+'\n')
                        arquivo.writelines('{}m²'.format(km2_m2(float(text)))+'\n')
                        arquivo.writelines('{}ha'.format(km2_ha(float(text)))+'\n')
                        arquivo.writelines('{}mi²'.format(km2_mi2(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()
                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        qquadradoo.close()
                        area()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()
            def mquadrado():
                mquadradoo = GraphWin("CONVERSOR DE ÁREA - METRO QUADRADO",1280,720)
                mquadradoo.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(mquadradoo)
                text_mquadrado = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_mquadrado.setSize(36)
                text_mquadrado.setFace('helvetica')
                text_mquadrado.setStyle('bold')
                text_mquadrado.draw(mquadradoo)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(mquadradoo)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(mquadradoo)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(mquadradoo)

                km2M2 = Rectangle(Point(430,180),Point(630,230))
                km2M2.setFill('white')
                km2M2.draw(mquadradoo)

                km2HA = Rectangle(Point(650,180),Point(850,230))
                km2HA.setFill('white')
                km2HA.draw(mquadradoo)

                km2MI2 = Rectangle(Point(540,250),Point(740,300))
                km2MI2.setFill('white')
                km2MI2.draw(mquadradoo)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(mquadradoo)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(mquadradoo)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(mquadradoo)  

                def check_click_usd():

                    mouse = mquadradoo.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_km2M2 = Text(Point(530,205),'{}km²'.format(round(m2_km2(float(text)), 4)))
                        text_km2M2.setSize(20)
                        text_km2M2.setFace('helvetica')
                        text_km2M2.setStyle('bold')
                        text_km2M2.draw(mquadradoo)

                        text = textEntry.getText()
                        text_km2HA = Text(Point(750,205),'{}ha'.format(round(m2_ha(float(text)), 4)))
                        text_km2HA.setSize(20)
                        text_km2HA.setFace('helvetica')
                        text_km2HA.setStyle('bold')
                        text_km2HA.draw(mquadradoo)

                        text = textEntry.getText()
                        text_km2MI2 = Text(Point(640,275),'{}mi²'.format(round(m2_mi2(float(text)), 4)))
                        text_km2MI2.setSize(20)
                        text_km2MI2.setFace('helvetica')
                        text_km2MI2.setStyle('bold')
                        text_km2MI2.draw(mquadradoo)

                        arquivo = open('conversao_de_area-METRO QUADRADO.txt','w')
                        arquivo.writelines('Valor inicial: {}m²'.format(text)+'\n')
                        arquivo.writelines('{}m²'.format(m2_mi2(float(text)))+'\n')
                        arquivo.writelines('{}ha'.format(m2_ha(float(text)))+'\n')
                        arquivo.writelines('{}km²'.format(m2_km2(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()

                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        mquadradoo.close()
                        area()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()
            def hectare():
                hectaree = GraphWin("CONVERSOR DE ÁREA - HECTARE",1280,720)
                hectaree.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(hectaree)
                text_qquadrado = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_qquadrado.setSize(36)
                text_qquadrado.setFace('helvetica')
                text_qquadrado.setStyle('bold')
                text_qquadrado.draw(hectaree)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(hectaree)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(hectaree)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(hectaree)

                km2M2 = Rectangle(Point(430,180),Point(630,230))
                km2M2.setFill('white')
                km2M2.draw(hectaree)

                km2HA = Rectangle(Point(650,180),Point(850,230))
                km2HA.setFill('white')
                km2HA.draw(hectaree)

                km2MI2 = Rectangle(Point(540,250),Point(740,300))
                km2MI2.setFill('white')
                km2MI2.draw(hectaree)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(hectaree)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(hectaree)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(hectaree)  
                def check_click_usd():

                    mouse = hectaree.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_km2M2 = Text(Point(530,205),'{}m²'.format(round(ha_m2(float(text)), 4)))
                        text_km2M2.setSize(20)
                        text_km2M2.setFace('helvetica')
                        text_km2M2.setStyle('bold')
                        text_km2M2.draw(hectaree)

                        text = textEntry.getText()
                        text_km2HA = Text(Point(750,205),'{}km²'.format(round(ha_km2(float(text)), 4)))
                        text_km2HA.setSize(20)
                        text_km2HA.setFace('helvetica')
                        text_km2HA.setStyle('bold')
                        text_km2HA.draw(hectaree)

                        text = textEntry.getText()
                        text_km2MI2 = Text(Point(640,275),'{}mi²'.format(round(ha_mi2(float(text)), 4)))
                        text_km2MI2.setSize(20)
                        text_km2MI2.setFace('helvetica')
                        text_km2MI2.setStyle('bold')
                        text_km2MI2.draw(hectaree)
                        
                        arquivo = open('conversao_de_area-HECTARE.txt','w')
                        arquivo.writelines('Valor inicial: {}ha'.format(text)+'\n')
                        arquivo.writelines('{}m²'.format(ha_m2(float(text)))+'\n')
                        arquivo.writelines('{}mi²'.format(ha_mi2(float(text)))+'\n')
                        arquivo.writelines('{}km²'.format(ha_km2(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()

                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        hectaree.close()
                        area()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()
            def miquadrada():
                miquadradaa = GraphWin("CONVERSOR DE ÁREA - MILHA QUADRADA",1280,720)
                miquadradaa.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(miquadradaa)
                text_qquadrado = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_qquadrado.setSize(36)
                text_qquadrado.setFace('helvetica')
                text_qquadrado.setStyle('bold')
                text_qquadrado.draw(miquadradaa)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(miquadradaa)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(miquadradaa)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(miquadradaa)

                km2M2 = Rectangle(Point(430,180),Point(630,230))
                km2M2.setFill('white')
                km2M2.draw(miquadradaa)

                km2HA = Rectangle(Point(650,180),Point(850,230))
                km2HA.setFill('white')
                km2HA.draw(miquadradaa)

                km2MI2 = Rectangle(Point(540,250),Point(740,300))
                km2MI2.setFill('white')
                km2MI2.draw(miquadradaa)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(miquadradaa)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(miquadradaa)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(miquadradaa)  

                def check_click_usd():

                    mouse = miquadradaa.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_km2M2 = Text(Point(530,205),'{}m²'.format(round(mi2_m2(float(text)), 4)))
                        text_km2M2.setSize(20)
                        text_km2M2.setFace('helvetica')
                        text_km2M2.setStyle('bold')
                        text_km2M2.draw(miquadradaa)

                        text = textEntry.getText()
                        text_km2HA = Text(Point(750,205),'{}ha'.format(round(mi2_ha(float(text)), 4)))
                        text_km2HA.setSize(20)
                        text_km2HA.setFace('helvetica')
                        text_km2HA.setStyle('bold')
                        text_km2HA.draw(miquadradaa)

                        text = textEntry.getText()
                        text_km2MI2 = Text(Point(640,275),'{}km²'.format(round(mi2_km2(float(text)), 4)))
                        text_km2MI2.setSize(20)
                        text_km2MI2.setFace('helvetica')
                        text_km2MI2.setStyle('bold')
                        text_km2MI2.draw(miquadradaa)
                        
                        arquivo = open('conversao_de_area-MILHA QUADRADA.txt','w')
                        arquivo.writelines('Valor inicial: {}mi²'.format(text)+'\n')
                        arquivo.writelines('{}m²'.format(mi2_m2(float(text)))+'\n')
                        arquivo.writelines('{}ha'.format(mi2_ha(float(text)))+'\n')
                        arquivo.writelines('{}km²'.format(mi2_km2(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()


                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        miquadradaa.close()
                        area()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()

            def check_click_unidades():

                mouse = areaa.getMouse()
                X = mouse.getX()
                Y = mouse.getY()

                if X > 330 and X < 630 and Y > 200 and Y < 300:
                    time.sleep(1)
                    areaa.close()                       
                    qquadrado()
                    check_click_unidades()
                if X > 650 and X < 950 and Y > 200 and Y < 300:
                    time.sleep(1)
                    areaa.close()                      
                    mquadrado()
                    check_click_unidades()
    
                if X > 330 and X < 630 and Y > 350 and Y < 450:
                    time.sleep(1)
                    areaa.close()                      
                    hectare()
                    check_click_unidades()           
                if X > 650 and X < 950 and Y > 350 and Y < 450:
                    time.sleep(1)
                    areaa.close()                      
                    miquadrada()
                    check_click_unidades()
                if X > 50 and X < 200 and Y > 640 and Y < 680:
                    time.sleep(1)
                    areaa.close()
                    unidades()
                    check_click_unidades()
                else:
                    check_click_unidades()
            check_click_unidades()                   



        def velocidade():
            velocidadee = GraphWin("CONVERSOR DE VELOCIDADE",1280,720)
            velocidadee.setBackground(color_rgb(13, 12, 222))
            tela_interna=Rectangle(Point(25,25),Point(1255,695))
            tela_interna.setFill(color_rgb(91, 89, 222))
            tela_interna.draw(velocidadee)
            text_velocidade = Text(Point(640,60),'ESCOLHA A UNIDADE INICIAL')
            text_velocidade.setSize(36)
            text_velocidade.setFace('helvetica')
            text_velocidade.setStyle('bold')
            text_velocidade.draw(velocidadee)

            kmh = Rectangle(Point(330,200),Point(630,300))
            kmh.setFill(color_rgb(71, 119, 252))
            kmh.setOutline(color_rgb(21, 31, 162))
            kmh.draw(velocidadee)
            text_kmh = Text(Point(480,250),'KM/H')
            text_kmh.setSize(25)
            text_kmh.setFace('helvetica')
            text_kmh.setStyle('bold')
            text_kmh.draw(velocidadee)

            ms = Rectangle(Point(650,200),Point(950,300))
            ms.setFill(color_rgb(71, 119, 252))
            ms.setOutline(color_rgb(21, 31, 162))
            ms.draw(velocidadee)
            text_ms = Text(Point(800,250),'M/S')
            text_ms.setSize(25)
            text_ms.setFace('helvetica')
            text_ms.setStyle('bold')
            text_ms.draw(velocidadee)

            mih = Rectangle(Point(490,350),Point(790,450))
            mih.setFill(color_rgb(71, 119, 252))
            mih.setOutline(color_rgb(21, 31, 162))
            mih.draw(velocidadee)
            text_mih = Text(Point(640,400),'MI/H')
            text_mih.setSize(25)
            text_mih.setFace('helvetica')
            text_mih.setStyle('bold')
            text_mih.draw(velocidadee)

            voltar = Rectangle(Point(50,640),Point(200,680))
            voltar.setFill('yellow')
            voltar.setOutline('orange')
            voltar.setWidth(6)
            voltar.draw(velocidadee)
            text_voltar = Text(Point(125,660),'VOLTAR')
            text_voltar.setFace('helvetica')
            text_voltar.setStyle('bold')
            text_voltar.setSize(25)
            text_voltar.draw(velocidadee)
            def kmh():
                kmhh = GraphWin("CONVERSOR DE VELOCIDADE - QUILOMETRO POR HORA",1280,720)
                kmhh.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(kmhh)
                text_kmh = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_kmh.setSize(36)
                text_kmh.setFace('helvetica')
                text_kmh.setStyle('bold')
                text_kmh.draw(kmhh)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(kmhh)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(kmhh)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(kmhh)

                kmhMS = Rectangle(Point(430,180),Point(630,230))
                kmhMS.setFill('white')
                kmhMS.draw(kmhh)

                kmhMIH = Rectangle(Point(650,180),Point(850,230))
                kmhMIH.setFill('white')
                kmhMIH.draw(kmhh)

                kmhKN = Rectangle(Point(540,250),Point(740,300))
                kmhKN.setFill('white')
                kmhKN.draw(kmhh)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(kmhh)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(kmhh)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(kmhh)  
                def check_click_usd():

                    mouse = kmhh.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_kmhMS = Text(Point(530,205),'{}m/s'.format(round(kmh_ms(float(text)), 4)))
                        text_kmhMS.setSize(20)
                        text_kmhMS.setFace('helvetica')
                        text_kmhMS.setStyle('bold')
                        text_kmhMS.draw(kmhh)

                        text = textEntry.getText()
                        text_kmhMIH = Text(Point(750,205),'{}mi/h'.format(round(kmh_mih(float(text)), 4)))
                        text_kmhMIH.setSize(20)
                        text_kmhMIH.setFace('helvetica')
                        text_kmhMIH.setStyle('bold')
                        text_kmhMIH.draw(kmhh)

                        text = textEntry.getText()
                        text_kmhKN = Text(Point(640,275),'{}kn'.format(round(kmh_kn(float(text)), 4)))
                        text_kmhKN.setSize(20)
                        text_kmhKN.setFace('helvetica')
                        text_kmhKN.setStyle('bold')
                        text_kmhKN.draw(kmhh)

                        arquivo = open('conversao_de_velocidade-QUILOMETRO POR HORA.txt','w')
                        arquivo.writelines('Valor inicial: {}km/s'.format(text)+'\n')
                        arquivo.writelines('{}m/s'.format(kmh_ms(float(text)))+'\n')
                        arquivo.writelines('{}mi/h'.format(kmh_mih(float(text)))+'\n')
                        arquivo.writelines('{}kn'.format(kmh_kn(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()

                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        kmhh.close()
                        velocidade()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()
            def ms():
                mss = GraphWin("CONVERSOR DE VELOCIDADE - METRO POR SEGUNDO",1280,720)
                mss.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(mss)
                text_kmh = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_kmh.setSize(36)
                text_kmh.setFace('helvetica')
                text_kmh.setStyle('bold')
                text_kmh.draw(mss)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(mss)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(mss)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(mss)

                kmhMS = Rectangle(Point(430,180),Point(630,230))
                kmhMS.setFill('white')
                kmhMS.draw(mss)

                kmhMIH = Rectangle(Point(650,180),Point(850,230))
                kmhMIH.setFill('white')
                kmhMIH.draw(mss)

                kmhKN = Rectangle(Point(540,250),Point(740,300))
                kmhKN.setFill('white')
                kmhKN.draw(mss)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(mss)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(mss)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(mss)  
                def check_click_usd():

                    mouse = mss.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_kmhMS = Text(Point(530,205),'{}km/h'.format(round(ms_kmh(float(text)), 4)))
                        text_kmhMS.setSize(20)
                        text_kmhMS.setFace('helvetica')
                        text_kmhMS.setStyle('bold')
                        text_kmhMS.draw(mss)

                        text = textEntry.getText()
                        text_kmhMIH = Text(Point(750,205),'{}mi/h'.format(round(ms_mih(float(text)), 4)))
                        text_kmhMIH.setSize(20)
                        text_kmhMIH.setFace('helvetica')
                        text_kmhMIH.setStyle('bold')
                        text_kmhMIH.draw(mss)

                        text = textEntry.getText()
                        text_kmhKN = Text(Point(640,275),'{}kn'.format(round(ms_kn(float(text)), 4)))
                        text_kmhKN.setSize(20)
                        text_kmhKN.setFace('helvetica')
                        text_kmhKN.setStyle('bold')
                        text_kmhKN.draw(mss)

                        arquivo = open('conversao_de_velocidade-METRO POR SEGUNDO.txt','w')
                        arquivo.writelines('Valor inicial: {}m/s'.format(text)+'\n')
                        arquivo.writelines('{}mi/h'.format(ms_mih(float(text)))+'\n')
                        arquivo.writelines('{}km/h'.format(ms_kmh(float(text)))+'\n')
                        arquivo.writelines('{}kn'.format(ms_kn(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()
                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        mss.close()
                        velocidade()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()
            def mih():
                mihh = GraphWin("CONVERSOR DE VELOCIDADE - MILHA POR HORA",1280,720)
                mihh.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(mihh)
                text_kmh = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_kmh.setSize(36)
                text_kmh.setFace('helvetica')
                text_kmh.setStyle('bold')
                text_kmh.draw(mihh)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(mihh)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(mihh)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(mihh)

                kmhMS = Rectangle(Point(430,180),Point(630,230))
                kmhMS.setFill('white')
                kmhMS.draw(mihh)

                kmhMIH = Rectangle(Point(650,180),Point(850,230))
                kmhMIH.setFill('white')
                kmhMIH.draw(mihh)

                kmhKN = Rectangle(Point(540,250),Point(740,300))
                kmhKN.setFill('white')
                kmhKN.draw(mihh)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(mihh)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(mihh)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(mihh)  
                def check_click_usd():

                    mouse = mihh.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_kmhMS = Text(Point(530,205),'{}m/s'.format(round(mih_ms(float(text)), 4)))
                        text_kmhMS.setSize(20)
                        text_kmhMS.setFace('helvetica')
                        text_kmhMS.setStyle('bold')
                        text_kmhMS.draw(mihh)

                        text = textEntry.getText()
                        text_kmhMIH = Text(Point(750,205),'{}km/h'.format(round(mih_kmh(float(text)), 4)))
                        text_kmhMIH.setSize(20)
                        text_kmhMIH.setFace('helvetica')
                        text_kmhMIH.setStyle('bold')
                        text_kmhMIH.draw(mihh)

                        text = textEntry.getText()
                        text_kmhKN = Text(Point(640,275),'{}kn'.format(round(mih_kn(float(text)), 4)))
                        text_kmhKN.setSize(20)
                        text_kmhKN.setFace('helvetica')
                        text_kmhKN.setStyle('bold')
                        text_kmhKN.draw(mihh)
                        
                        arquivo = open('conversao_de_velocidade-MILHA POR HORA.txt','w')
                        arquivo.writelines('Valor inicial: {}mi/h'.format(text)+'\n')
                        arquivo.writelines('{}m/s'.format(mih_ms(float(text)))+'\n')
                        arquivo.writelines('{}km/h'.format(mih_kmh(float(text)))+'\n')
                        arquivo.writelines('{}kn'.format(mih_kn(float(text)))+'\n')
                        arquivo.close  
                        check_click_usd()
                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        mihh.close()
                        velocidade()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()

            def check_click_unidades():

                mouse = velocidadee.getMouse()
                X = mouse.getX()
                Y = mouse.getY()

                if X > 330 and X < 630 and Y > 200 and Y < 300:
                    time.sleep(1)
                    velocidadee.close() 
                    kmh()
                    check_click_unidades()
                if X > 650 and X < 950 and Y > 200 and Y < 300:
                    time.sleep(1)
                    velocidadee.close() 
                    ms()
                    check_click_unidades()
    
                if X > 490 and X < 790 and Y > 350 and Y < 450:
                    time.sleep(1)
                    velocidadee.close() 
                    mih()
                    check_click_unidades()
                if X > 50 and X < 200 and Y > 640 and Y < 680:
                    time.sleep(1)
                    velocidadee.close()
                    unidades()
                    check_click_unidades()           
                else:
                    check_click_unidades()
            check_click_unidades()





        def massa():
            massaa = GraphWin("CONVERSOR DE MASSA",1280,720)
            massaa.setBackground(color_rgb(13, 12, 222))
            tela_interna=Rectangle(Point(25,25),Point(1255,695))
            tela_interna.setFill(color_rgb(91, 89, 222))
            tela_interna.draw(massaa)
            text_massa = Text(Point(640,60),'ESCOLHA A UNIDADE INICIAL')
            text_massa.setSize(36)
            text_massa.setFace('helvetica')
            text_massa.setStyle('bold')
            text_massa.draw(massaa)

            kg = Rectangle(Point(330,100),Point(630,200))
            kg.setFill(color_rgb(71, 119, 252))
            kg.setOutline(color_rgb(21, 31, 162))
            kg.draw(massaa)
            text_kg = Text(Point(480,150),'QUILOGRAMA')
            text_kg.setSize(25)
            text_kg.setFace('helvetica')
            text_kg.setStyle('bold')
            text_kg.draw(massaa)

            g = Rectangle(Point(650,100),Point(950,200))
            g.setFill(color_rgb(71, 119, 252))
            g.setOutline(color_rgb(21, 31, 162))
            g.draw(massaa)
            text_g = Text(Point(800,150),'GRAMA')
            text_g.setSize(25)
            text_g.setFace('helvetica')
            text_g.setStyle('bold')
            text_g.draw(massaa)

            mg = Rectangle(Point(330,220),Point(630,320))
            mg.setFill(color_rgb(71, 119, 252))
            mg.setOutline(color_rgb(21, 31, 162))
            mg.draw(massaa)
            text_mg = Text(Point(480,270),'MILIGRAMA')
            text_mg.setSize(25)
            text_mg.setFace('helvetica')
            text_mg.setStyle('bold')
            text_mg.draw(massaa)

            t = Rectangle(Point(650,220),Point(950,320))
            t.setFill(color_rgb(71, 119, 252))
            t.setOutline(color_rgb(21, 31, 162))
            t.draw(massaa)
            text_t = Text(Point(800,270),'TONELADA')
            text_t.setSize(25)
            text_t.setFace('helvetica')
            text_t.setStyle('bold')
            text_t.draw(massaa)

            oz = Rectangle(Point(330,340),Point(630,440))
            oz.setFill(color_rgb(71, 119, 252))
            oz.setOutline(color_rgb(21, 31, 162))
            oz.draw(massaa)
            text_oz = Text(Point(480,390),'ONÇA')
            text_oz.setSize(25)
            text_oz.setFace('helvetica')
            text_oz.setStyle('bold')
            text_oz.draw(massaa)

            lb = Rectangle(Point(650,340),Point(950,440))
            lb.setFill(color_rgb(71, 119, 252))
            lb.setOutline(color_rgb(21, 31, 162))
            lb.draw(massaa)
            text_lb = Text(Point(800,390),'LIBRA')
            text_lb.setSize(25)
            text_lb.setFace('helvetica')
            text_lb.setStyle('bold')
            text_lb.draw(massaa)

            voltar = Rectangle(Point(50,640),Point(200,680))
            voltar.setFill('yellow')
            voltar.setOutline('orange')
            voltar.setWidth(6)
            voltar.draw(massaa)
            text_voltar = Text(Point(125,660),'VOLTAR')
            text_voltar.setFace('helvetica')
            text_voltar.setStyle('bold')
            text_voltar.setSize(25)
            text_voltar.draw(massaa)
            def kg():
                kgg = GraphWin("CONVERSOR DE MASSA - QUILOGRAMA",1280,720)
                kgg.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(kgg)
                text_kg = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_kg.setSize(36)
                text_kg.setFace('helvetica')
                text_kg.setStyle('bold')
                text_kg.draw(kgg)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(kgg)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(kgg)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(kgg)

                kgG = Rectangle(Point(430,180),Point(630,230))
                kgG.setFill('white')
                kgG.draw(kgg)

                kgMG = Rectangle(Point(430,250),Point(630,300))
                kgMG.setFill('white')
                kgMG.draw(kgg)

                kgT = Rectangle(Point(540,320),Point(740,370))
                kgT.setFill('white')
                kgT.draw(kgg)

                kgOZ = Rectangle(Point(650,180),Point(850,230))
                kgOZ.setFill('white')
                kgOZ.draw(kgg)

                kgLB = Rectangle(Point(650,250),Point(850,300))
                kgLB.setFill('white')
                kgLB.draw(kgg)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(kgg)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(kgg)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(kgg)  
                def check_click_usd():

                    mouse = kgg.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_kgG = Text(Point(530,205),'{}g'.format(round(kg_g(float(text)), 4)))
                        text_kgG.setSize(20)
                        text_kgG.setFace('helvetica')
                        text_kgG.setStyle('bold')
                        text_kgG.draw(kgg)

                        text = textEntry.getText()
                        text_kgMG = Text(Point(530,275),'{}mg'.format(round(kg_mg(float(text)), 4)))
                        text_kgMG.setSize(20)
                        text_kgMG.setFace('helvetica')
                        text_kgMG.setStyle('bold')
                        text_kgMG.draw(kgg)

                        text = textEntry.getText()
                        text_kgT = Text(Point(640,345),'{}t'.format(round(kg_t(float(text)), 4)))
                        text_kgT.setSize(20)
                        text_kgT.setFace('helvetica')
                        text_kgT.setStyle('bold')
                        text_kgT.draw(kgg)

                        text = textEntry.getText()
                        text_kgOZ = Text(Point(750,205),'{}oz'.format(round(kg_oz(float(text)), 4)))
                        text_kgOZ.setSize(20)
                        text_kgOZ.setFace('helvetica')
                        text_kgOZ.setStyle('bold')
                        text_kgOZ.draw(kgg)

                        text = textEntry.getText()
                        text_kgLB = Text(Point(750,275),'{}lb'.format(round(kg_lb(float(text)), 4)))
                        text_kgLB.setSize(20)
                        text_kgLB.setFace('helvetica')
                        text_kgLB.setStyle('bold')
                        text_kgLB.draw(kgg)

                        arquivo = open('conversao_de_massa-QUILOGRAMA.txt','w')
                        arquivo.writelines('Valor inicial: {}kg'.format(text)+'\n')
                        arquivo.writelines('{}oz'.format(kg_oz(float(text)))+'\n')
                        arquivo.writelines('{}mg'.format(kg_mg(float(text)))+'\n')
                        arquivo.writelines('{}t'.format(kg_t(float(text)))+'\n')
                        arquivo.writelines('{}g'.format(kg_g(float(text)))+'\n')
                        arquivo.writelines('{}lb'.format(kg_lb(float(text))))
                        arquivo.close  
                        check_click_usd()
                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        kgg.close()
                        massa()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()

            def g():
                gg = GraphWin("CONVERSOR DE MASSA - GRAMA",1280,720)
                gg.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(gg)
                text_kg = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_kg.setSize(36)
                text_kg.setFace('helvetica')
                text_kg.setStyle('bold')
                text_kg.draw(gg)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(gg)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(gg)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(gg)

                kgG = Rectangle(Point(430,180),Point(630,230))
                kgG.setFill('white')
                kgG.draw(gg)

                kgMG = Rectangle(Point(430,250),Point(630,300))
                kgMG.setFill('white')
                kgMG.draw(gg)

                kgT = Rectangle(Point(540,320),Point(740,370))
                kgT.setFill('white')
                kgT.draw(gg)

                kgOZ = Rectangle(Point(650,180),Point(850,230))
                kgOZ.setFill('white')
                kgOZ.draw(gg)

                kgLB = Rectangle(Point(650,250),Point(850,300))
                kgLB.setFill('white')
                kgLB.draw(gg)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(gg)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(gg)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(gg)  
                def check_click_usd():

                    mouse = gg.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_kgG = Text(Point(530,205),'{}kg'.format(round(g_kg(float(text)), 4)))
                        text_kgG.setSize(20)
                        text_kgG.setFace('helvetica')
                        text_kgG.setStyle('bold')
                        text_kgG.draw(gg)

                        text = textEntry.getText()
                        text_kgMG = Text(Point(530,275),'{}mg'.format(round(g_mg(float(text)), 4)))
                        text_kgMG.setSize(20)
                        text_kgMG.setFace('helvetica')
                        text_kgMG.setStyle('bold')
                        text_kgMG.draw(gg)

                        text = textEntry.getText()
                        text_kgT = Text(Point(640,345),'{}t'.format(round(g_t(float(text)), 4)))
                        text_kgT.setSize(20)
                        text_kgT.setFace('helvetica')
                        text_kgT.setStyle('bold')
                        text_kgT.draw(gg)

                        text = textEntry.getText()
                        text_kgOZ = Text(Point(750,205),'{}oz'.format(round(g_oz(float(text)), 4)))
                        text_kgOZ.setSize(20)
                        text_kgOZ.setFace('helvetica')
                        text_kgOZ.setStyle('bold')
                        text_kgOZ.draw(gg)

                        text = textEntry.getText()
                        text_kgLB = Text(Point(750,275),'{}lb'.format(round(g_lb(float(text)), 4)))
                        text_kgLB.setSize(20)
                        text_kgLB.setFace('helvetica')
                        text_kgLB.setStyle('bold')
                        text_kgLB.draw(gg)
                        
                        arquivo = open('conversao_de_massa-GRAMA.txt','w')
                        arquivo.writelines('Valor inicial: {}g'.format(text)+'\n')
                        arquivo.writelines('{}kg'.format(g_kg(float(text)))+'\n')
                        arquivo.writelines('{}mg'.format(g_mg(float(text)))+'\n')
                        arquivo.writelines('{}t'.format(g_t(float(text)))+'\n')
                        arquivo.writelines('{}oz'.format(g_oz(float(text)))+'\n')
                        arquivo.writelines('{}lb'.format(g_lb(float(text))))
                        arquivo.close  
                        check_click_usd()
                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        gg.close()
                        massa()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()                

            def mg():
                mgg = GraphWin("CONVERSOR DE MASSA - MILIGRAMA",1280,720)
                mgg.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(mgg)
                text_kg = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_kg.setSize(36)
                text_kg.setFace('helvetica')
                text_kg.setStyle('bold')
                text_kg.draw(mgg)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(mgg)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(mgg)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(mgg)

                kgG = Rectangle(Point(430,180),Point(630,230))
                kgG.setFill('white')
                kgG.draw(mgg)

                kgMG = Rectangle(Point(430,250),Point(630,300))
                kgMG.setFill('white')
                kgMG.draw(mgg)

                kgOZ = Rectangle(Point(650,180),Point(850,230))
                kgOZ.setFill('white')
                kgOZ.draw(mgg)

                kgLB = Rectangle(Point(650,250),Point(850,300))
                kgLB.setFill('white')
                kgLB.draw(mgg)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(mgg)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(mgg)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(mgg)  
                def check_click_usd():

                    mouse = mgg.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_kgG = Text(Point(530,205),'{}g'.format(round(mg_g(float(text)), 4)))
                        text_kgG.setSize(20)
                        text_kgG.setFace('helvetica')
                        text_kgG.setStyle('bold')
                        text_kgG.draw(mgg)

                        text = textEntry.getText()
                        text_kgMG = Text(Point(530,275),'{}kg'.format(round(mg_kg(float(text)), 4)))
                        text_kgMG.setSize(20)
                        text_kgMG.setFace('helvetica')
                        text_kgMG.setStyle('bold')
                        text_kgMG.draw(mgg)

                        text = textEntry.getText()
                        text_kgOZ = Text(Point(750,205),'{}oz'.format(round(mg_oz(float(text)), 4)))
                        text_kgOZ.setSize(20)
                        text_kgOZ.setFace('helvetica')
                        text_kgOZ.setStyle('bold')
                        text_kgOZ.draw(mgg)

                        text = textEntry.getText()
                        text_kgLB = Text(Point(750,275),'{}lb'.format(round(mg_lb(float(text)), 4)))
                        text_kgLB.setSize(20)
                        text_kgLB.setFace('helvetica')
                        text_kgLB.setStyle('bold')
                        text_kgLB.draw(mgg)
                        
                        arquivo = open('conversao_de_massa-MILIGRAMA.txt','w')
                        arquivo.writelines('Valor inicial: {}mg'.format(text)+'\n')
                        arquivo.writelines('{}kg'.format(mg_kg(float(text)))+'\n')
                        arquivo.writelines('{}oz'.format(mg_oz(float(text)))+'\n')
                        arquivo.writelines('{}g'.format(mg_g(float(text)))+'\n')
                        arquivo.writelines('{}lb'.format(mg_lb(float(text))))
                        arquivo.close  
                        check_click_usd()
                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        mgg.close()
                        massa()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()     
            def t():
                tt = GraphWin("CONVERSOR DE MASSA - MILIGRAMA",1280,720)
                tt.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(tt)
                text_kg = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_kg.setSize(36)
                text_kg.setFace('helvetica')
                text_kg.setStyle('bold')
                text_kg.draw(tt)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(tt)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(tt)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(tt)

                kgG = Rectangle(Point(430,180),Point(630,230))
                kgG.setFill('white')
                kgG.draw(tt)

                kgMG = Rectangle(Point(430,250),Point(630,300))
                kgMG.setFill('white')
                kgMG.draw(tt)

                kgOZ = Rectangle(Point(650,180),Point(850,230))
                kgOZ.setFill('white')
                kgOZ.draw(tt)

                kgLB = Rectangle(Point(650,250),Point(850,300))
                kgLB.setFill('white')
                kgLB.draw(tt)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(tt)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(tt)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(tt)  
                def check_click_usd():

                    mouse = tt.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_kgG = Text(Point(530,205),'{}g'.format(round(t_g(float(text)), 4)))
                        text_kgG.setSize(20)
                        text_kgG.setFace('helvetica')
                        text_kgG.setStyle('bold')
                        text_kgG.draw(tt)

                        text = textEntry.getText()
                        text_kgMG = Text(Point(530,275),'{}kg'.format(round(t_kg(float(text)), 4)))
                        text_kgMG.setSize(20)
                        text_kgMG.setFace('helvetica')
                        text_kgMG.setStyle('bold')
                        text_kgMG.draw(tt)

                        text = textEntry.getText()
                        text_kgOZ = Text(Point(750,205),'{}oz'.format(round(t_oz(float(text)), 4)))
                        text_kgOZ.setSize(20)
                        text_kgOZ.setFace('helvetica')
                        text_kgOZ.setStyle('bold')
                        text_kgOZ.draw(tt)

                        text = textEntry.getText()
                        text_kgLB = Text(Point(750,275),'{}lb'.format(round(t_lb(float(text)), 4)))
                        text_kgLB.setSize(20)
                        text_kgLB.setFace('helvetica')
                        text_kgLB.setStyle('bold')
                        text_kgLB.draw(tt)
                        
                        arquivo = open('conversao_de_massa-TONELADA.txt','w')
                        arquivo.writelines('Valor inicial: {}t'.format(text)+'\n')
                        arquivo.writelines('{}kg'.format(t_kg(float(text)))+'\n')
                        arquivo.writelines('{}oz'.format(t_oz(float(text)))+'\n')
                        arquivo.writelines('{}g'.format(t_g(float(text)))+'\n')
                        arquivo.writelines('{}lb'.format(t_lb(float(text))))
                        arquivo.close  
                        check_click_usd()
                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        tt.close()
                        massa()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()     
            def oz():
                ozz = GraphWin("CONVERSOR DE MASSA - ONÇA",1280,720)
                ozz.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(ozz)
                text_kg = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_kg.setSize(36)
                text_kg.setFace('helvetica')
                text_kg.setStyle('bold')
                text_kg.draw(ozz)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(ozz)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(ozz)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(ozz)

                kgG = Rectangle(Point(430,180),Point(630,230))
                kgG.setFill('white')
                kgG.draw(ozz)

                kgMG = Rectangle(Point(430,250),Point(630,300))
                kgMG.setFill('white')
                kgMG.draw(ozz)

                kgT = Rectangle(Point(540,320),Point(740,370))
                kgT.setFill('white')
                kgT.draw(ozz)

                kgOZ = Rectangle(Point(650,180),Point(850,230))
                kgOZ.setFill('white')
                kgOZ.draw(ozz)

                kgLB = Rectangle(Point(650,250),Point(850,300))
                kgLB.setFill('white')
                kgLB.draw(ozz)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(ozz)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(ozz)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(ozz)  
                def check_click_usd():

                    mouse = ozz.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_kgG = Text(Point(530,205),'{}kg'.format(round(oz_kg(float(text)), 4)))
                        text_kgG.setSize(20)
                        text_kgG.setFace('helvetica')
                        text_kgG.setStyle('bold')
                        text_kgG.draw(ozz)

                        text = textEntry.getText()
                        text_kgMG = Text(Point(530,275),'{}mg'.format(round(oz_mg(float(text)), 4)))
                        text_kgMG.setSize(20)
                        text_kgMG.setFace('helvetica')
                        text_kgMG.setStyle('bold')
                        text_kgMG.draw(ozz)

                        text = textEntry.getText()
                        text_kgT = Text(Point(640,345),'{}t'.format(round(oz_t(float(text)), 4)))
                        text_kgT.setSize(20)
                        text_kgT.setFace('helvetica')
                        text_kgT.setStyle('bold')
                        text_kgT.draw(ozz)

                        text = textEntry.getText()
                        text_kgOZ = Text(Point(750,205),'{}g'.format(round(oz_g(float(text)), 4)))
                        text_kgOZ.setSize(20)
                        text_kgOZ.setFace('helvetica')
                        text_kgOZ.setStyle('bold')
                        text_kgOZ.draw(ozz)

                        text = textEntry.getText()
                        text_kgLB = Text(Point(750,275),'{}lb'.format(round(oz_lb(float(text)), 4)))
                        text_kgLB.setSize(20)
                        text_kgLB.setFace('helvetica')
                        text_kgLB.setStyle('bold')
                        text_kgLB.draw(ozz)
                        
                        arquivo = open('conversao_de_massa-ONCA.txt','w')
                        arquivo.writelines('Valor inicial: {}oz'.format(text)+'\n')
                        arquivo.writelines('{}kg'.format(oz_kg(float(text)))+'\n')
                        arquivo.writelines('{}mg'.format(oz_mg(float(text)))+'\n')
                        arquivo.writelines('{}t'.format(oz_t(float(text)))+'\n')
                        arquivo.writelines('{}g'.format(oz_g(float(text)))+'\n')
                        arquivo.writelines('{}lb'.format(oz_lb(float(text))))
                        arquivo.close  

                        check_click_usd()
                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        ozz.close()
                        massa()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()      
            def lb():
                lbb = GraphWin("CONVERSOR DE MASSA - LIBRA",1280,720)
                lbb.setBackground(color_rgb(13, 12, 222))
                tela_interna=Rectangle(Point(25,25),Point(1255,695))
                tela_interna.setFill(color_rgb(91, 89, 222))
                tela_interna.draw(lbb)
                text_kg = Text(Point(640,60),'INSIRA A QUANTIA INICIAL')
                text_kg.setSize(36)
                text_kg.setFace('helvetica')
                text_kg.setStyle('bold')
                text_kg.draw(lbb)

                confirmar = Rectangle(Point(545,120),Point(745,150))
                confirmar.setFill('green')
                confirmar.draw(lbb)
                text_confirmar = Text(Point(640,135),'CONFIRMAR')
                text_confirmar.setSize(10)
                text_confirmar.setFace('helvetica')
                text_confirmar.setStyle('bold')
                text_confirmar.draw(lbb)
                
                textEntry = Entry(Point(640,100),25)
                textEntry.setFill('white')
                textEntry.draw(lbb)

                kgG = Rectangle(Point(430,180),Point(630,230))
                kgG.setFill('white')
                kgG.draw(lbb)

                kgMG = Rectangle(Point(430,250),Point(630,300))
                kgMG.setFill('white')
                kgMG.draw(lbb)

                kgT = Rectangle(Point(540,320),Point(740,370))
                kgT.setFill('white')
                kgT.draw(lbb)

                kgOZ = Rectangle(Point(650,180),Point(850,230))
                kgOZ.setFill('white')
                kgOZ.draw(lbb)

                kgLB = Rectangle(Point(650,250),Point(850,300))
                kgLB.setFill('white')
                kgLB.draw(lbb)

                voltar = Rectangle(Point(50,640),Point(200,680))
                voltar.setFill('yellow')
                voltar.setOutline('orange')
                voltar.setWidth(6)
                voltar.draw(lbb)
                text_voltar = Text(Point(125,660),'VOLTAR')
                text_voltar.setFace('helvetica')
                text_voltar.setStyle('bold')
                text_voltar.setSize(25)
                text_voltar.draw(lbb)

                text_novaconsulta = Text(Point(230,560),'PARA NOVA CONSULTA,\nCLIQUE EM VOLTAR       \nE RETORNE                      ')
                text_novaconsulta.setFace('helvetica')
                text_novaconsulta.setStyle('bold')
                text_novaconsulta.setSize(25)
                text_novaconsulta.draw(lbb)  
                def check_click_usd():

                    mouse = lbb.getMouse()
                    X = mouse.getX()
                    Y = mouse.getY()

                    if X > 545 and X < 745 and Y > 120 and Y < 150:
                        text = textEntry.getText()
                        text_kgG = Text(Point(530,205),'{}kg'.format(round(lb_kg(float(text)), 4)))
                        text_kgG.setSize(20)
                        text_kgG.setFace('helvetica')
                        text_kgG.setStyle('bold')
                        text_kgG.draw(lbb)

                        text = textEntry.getText()
                        text_kgMG = Text(Point(530,275),'{}mg'.format(round(lb_mg(float(text)), 4)))
                        text_kgMG.setSize(20)
                        text_kgMG.setFace('helvetica')
                        text_kgMG.setStyle('bold')
                        text_kgMG.draw(lbb)

                        text = textEntry.getText()
                        text_kgT = Text(Point(640,345),'{}t'.format(round(lb_t(float(text)), 4)))
                        text_kgT.setSize(20)
                        text_kgT.setFace('helvetica')
                        text_kgT.setStyle('bold')
                        text_kgT.draw(lbb)

                        text = textEntry.getText()
                        text_kgOZ = Text(Point(750,205),'{}g'.format(round(lb_g(float(text)), 4)))
                        text_kgOZ.setSize(20)
                        text_kgOZ.setFace('helvetica')
                        text_kgOZ.setStyle('bold')
                        text_kgOZ.draw(lbb)

                        text = textEntry.getText()
                        text_kgLB = Text(Point(750,275),'{}oz'.format(round(lb_oz(float(text)), 4)))
                        text_kgLB.setSize(20)
                        text_kgLB.setFace('helvetica')
                        text_kgLB.setStyle('bold')
                        text_kgLB.draw(lbb)
                        
                        arquivo = open('conversao_de_massa-LIBRA.txt','w')
                        arquivo.writelines('Valor inicial: {}lb'.format(text)+'\n')
                        arquivo.writelines('{}kg'.format(lb_kg(float(text)))+'\n')
                        arquivo.writelines('{}mg'.format(lb_mg(float(text)))+'\n')
                        arquivo.writelines('{}t'.format(lb_t(float(text)))+'\n')
                        arquivo.writelines('{}g'.format(lb_g(float(text)))+'\n')
                        arquivo.writelines('{}oz'.format(lb_oz(float(text))))
                        arquivo.close  
                        check_click_usd()
                    if X > 50 and X < 200 and Y > 640 and Y < 680:
                        time.sleep(1)
                        lbb.close()
                        massa()
                        check_click_usd()
                    else:
                        check_click_usd()
                check_click_usd()                    
            
            def check_click_unidades():

                mouse = massaa.getMouse()
                X = mouse.getX()
                Y = mouse.getY()

                if X > 330 and X < 630 and Y > 100 and Y < 200:
                    time.sleep(1)
                    massaa.close()
                    kg()
                    check_click_unidades()
                if X > 650 and X < 950 and Y > 100 and Y < 200:
                    time.sleep(1)
                    massaa.close()
                    g()
                    check_click_unidades()
    
                if X > 330 and X < 630 and Y > 220 and Y < 320:
                    time.sleep(1)
                    massaa.close()
                    mg()
                    check_click_unidades()           
                if X > 650 and X < 950 and Y > 220 and Y < 320:
                    time.sleep(1)
                    massaa.close()
                    t()
                    check_click_unidades()

                if X > 330 and X < 630 and Y > 340 and Y < 440:
                    time.sleep(1)
                    massaa.close()
                    oz()
                    check_click_unidades()
                if X > 650 and X < 950 and Y > 340 and Y < 440:
                    lb()
                    check_click_unidades()
                if X > 50 and X < 200 and Y > 640 and Y < 680:
                    time.sleep(1)
                    massaa.close()
                    unidades()
                    check_click_unidades()
                else:
                    check_click_unidades()
            check_click_unidades()



        def check_click_unidades():

            mouse = unidadess.getMouse()
            X = mouse.getX()
            Y = mouse.getY()

            if X > 330 and X < 630 and Y > 200 and Y < 300:
                time.sleep(1)
                unidadess.close()
                comprimento()
                check_click_unidades()
            if X > 650 and X < 950 and Y > 200 and Y < 300:
                time.sleep(1)
                unidadess.close()
                volume()
                check_click_unidades()
  
            if X > 330 and X < 630 and Y > 350 and Y < 450:
                time.sleep(1)
                unidadess.close()
                area()
                check_click_unidades()           
            if X > 650 and X < 950 and Y > 350 and Y < 450:
                time.sleep(1)
                unidadess.close()
                massa()
                check_click_unidades()

            if X > 490 and X < 790 and Y > 500 and Y < 600:
                time.sleep(1)
                unidadess.close()
                velocidade()
                check_click_unidades()

            if X > 50 and X < 200 and Y > 640 and Y < 680:
                time.sleep(1)
                unidadess.close()
                main()
                check_click_unidades()
            if X > 1100 and X < 1200 and Y > 30 and Y < 120:
                win.close()
                unidadess.close()
            else:
                check_click_unidades()
        check_click_unidades()




        unidadess.getKey()
        unidadess.close()
    
## CHECA ONDE ESTÁ O CLIQUE
    def check_click():
        mouse = win.getMouse()
        X = mouse.getX()
        Y = mouse.getY()
        if X > 390 and X < 890 and Y > 95 and Y < 295:
            time.sleep(1)
            win.close()
            moeda()
            check_click()
        if X > 390 and X < 890 and Y > 430 and Y < 630:
            time.sleep(1)
            win.close()
            unidades()
            check_click()
        if X > 1000 and X < 1200 and Y > 50 and Y < 200:
            win.close()
        else:
            check_click()
    check_click()

## ENCERRA A EXECUÇÃO
main()
