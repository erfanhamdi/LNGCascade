# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 21:07:45 2019

@author: Erfan
https://github.com/JayJoeAy
"""
import CoolProp.CoolProp as cp
import matplotlib.pyplot as plt
import numpy as np
Ch_ch4={}
Q_lng,h_lng={},{}
T,P,Cp,dT ={},{},{},{}
T_ch4,h_ch4,s_ch4={},{},{}
T_eth,h_eth,s_eth={},{},{}
T_prp,h_prp,s_prp={},{},{}
coeff={}
LNG='CH4'
ch4='CH4'
eth='R1150'
prp='R290'

"===================================== Stage 3 (Methane) ========================================"
dT[3]=78
T[4]=-162+273.15
T[3]=T[4]+dT[3]
P[4]=101325
Cp[3]=cp.PropsSI('C','T',T[4],'P',P[4],LNG)


T_ch4[1]=T[4]-6
T_ch4[2]=T_ch4[1]
T_ch4[4]=T_ch4[1]+dT[3]
T_ch4[3]=T_ch4[4]

s_ch4[2]=cp.PropsSI('S','T',T_ch4[2],'Q',1,ch4)
s_ch4[3]=s_ch4[2]

h_ch4[2]=cp.PropsSI('H','T',T_ch4[1],'Q',1,ch4)
h_ch4[4]=cp.PropsSI('H','T',T_ch4[4],'Q',0,ch4)
dh=h_ch4[2]-h_ch4[4]
h_ch4[1]=h_ch4[4]
h_ch4[3]=cp.PropsSI('H','T',T_ch4[3],'S',s_ch4[3],ch4)

M_lng=1

h_lng[4]=cp.PropsSI('H','T',T[4],'P',P[4],LNG)
h_lng[3]=cp.PropsSI('H','T',T[3],'P',P[4],LNG)
dh=h_lng[3]-h_lng[4]

Q_lng[3]=M_lng*(h_lng[3]-h_lng[4])
M_ch4=Q_lng[3]/(h_ch4[2]-h_ch4[1])

Qe_ch4=M_ch4*(h_ch4[2]-h_ch4[1])
Qc_ch4=M_ch4*(h_ch4[3]-h_ch4[4])
W_ch4=M_ch4*(h_ch4[3]-h_ch4[2])

coeff[3]=Qe_ch4/W_ch4

"===================================== Stage 2 (Ethylene) ======================================="
T[3]=T[4]+dT[3]
P[3]=101325
dT[2]=88
T[2]=T[3]+dT[2]

T_eth[1]=T[3]-6
T_eth[2]=T_eth[1]
T_eth[4]=T_eth[1]+dT[2]
T_eth[3]=T_eth[4]

s_eth[2]=cp.PropsSI('S','T',T_eth[2],'Q',1,eth)
s_eth[3]=s_eth[2]

h_eth[2]=cp.PropsSI('H','T',T_eth[2],'Q',1,eth)
h_eth[4]=cp.PropsSI('H','T',T_eth[4],'Q',0,eth)
h_eth[1]=h_eth[4]
h_eth[3]=cp.PropsSI('H','T',T_eth[3],'S',s_eth[3],eth)

h_lng[2]=cp.PropsSI('H','T',T[2],'P',P[4],LNG)
Q_lng[2]=M_lng*(h_lng[2]-h_lng[3])
M_eth=(Q_lng[2]+Qc_ch4)/(h_eth[2]-h_eth[1])

Qe_eth=M_eth*(h_eth[2]-h_eth[1])
Qc_eth=M_eth*(h_eth[3]-h_eth[4])
W_eth=M_eth*(h_eth[3]-h_eth[2])

coeff[2]=Qe_eth/W_eth

"===================================== Stage 1 (Propane) ========================================"
T[2]=T[3]+dT[2]
P[2]=101325
dT[1]=29
T[1]=T[2]+dT[1]

T_prp[1]=T[2]-6
T_prp[2]=T_prp[1]
T_prp[4]=T_prp[1]+dT[1]
T_prp[3]=T_prp[4]

s_prp[2]=cp.PropsSI('S','T',T_prp[2],'Q',1,prp)
s_prp[3]=s_prp[2]

h_prp[2]=cp.PropsSI('H','T',T_prp[2],'Q',1,prp)
h_prp[4]=cp.PropsSI('H','T',T_prp[4],'Q',0,prp)
h_prp[1]=h_prp[4]
h_prp[3]=cp.PropsSI('H','T',T_prp[3],'S',s_prp[3],prp)


h_lng[1]=cp.PropsSI('H','T',T[1],'P',P[4],LNG)
Q_lng[1]=M_lng*(h_lng[1]-h_lng[1])
M_prp=(Q_lng[1]+Qc_eth)/(h_prp[2]-h_prp[1])

Qe_prp=M_prp*(h_prp[2]-h_prp[1])
Qc_prp=M_prp*(h_prp[3]-h_prp[4])
W_prp=M_prp*(h_prp[3]-h_prp[2])

coeff[1]=Qe_prp/W_prp

"=========================================Cycle COP==================================================="
coeff[4]=(Q_lng[1]+Q_lng[2]+Q_lng[3])/(W_ch4+W_eth+W_prp)




