#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
from PIL import Image
import matplotlib.pyplot as plt

paths=glob.glob("/userhome/adamn/Documents/Output/17052023/*/*.tiff")
Damagednuclei= [x for x in paths if 'Damaged_nuclei_' in x]
Undamagednuclei= [x for x in paths if "No_damage_nuclei" in x]
DamagedCyto= [x for x in paths if "damage_membrane_" in x]
UndamagedCyto= [x for x in paths if "ok_membrane_" in x]

for z in [DamagedCyto,UndamagedCyto]:
    Damagednuclei_len=range(len(z))
    heights=[]
    widths=[]
    #differences=[]
    for x in Damagednuclei_len:
        img = Image.open(z[x])
        w,h=img.size
        heights.append(h)
        widths.append(w)
        #differences.append(abs(h-w))
    if z==DamagedCyto:
        plt.scatter(widths, heights,s=3, c=['blue'], alpha=0.7)
    else:
        plt.scatter(widths, heights,s=3, c=['red'], alpha=0.1)
    
plt.legend(['Damaged Cytoskeleton', 'Undamaged Cytoskeleton'])
plt.xlabel("Width (Pixels)")
plt.ylabel("Height (Pixels)")
plt.title("Cytoskeleton image size spread")
plt.show()
"""
#ANSWER Damagednuclei max difference in height and width is 48,  and the minimum difference is0 AND 6.280995064961225
Undamaged nuclei max difference in height and width is 93,  and the minimum difference is0 AND 6.188539892571728
Damaged Cyto max difference in height and width is 477,  and the minimum difference is0 AND 35.13979339770941
Undamaged cyto max difference in height and width is 337,  and the minimum difference is0 AND 26.14887335716445
"""
#[Damagednuclei,Undamagednuclei,DamagedCyto,UndamagedCyto]