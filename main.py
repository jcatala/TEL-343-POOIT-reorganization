#!/usr/bin/env python3
import pprint
import math
import geopy.distance
import numpy as np
import random
import matplotlib.pyplot as plt
import time

def calculateDistance(x1,x2,y1,y2):
    xVal = pow(x1-x2, 2)
    yVal = pow(y1-y2, 2)
    return math.sqrt(xVal + yVal)




def newPoints(data):
    xdenom = 0
    xnumer = 0
    ydenom = 0
    ynumer = 0
    for x,y,w,d2 in data:
        xnumer += (w*x)/d2
        xdenom += (w)/d2
        ynumer += (w*y)/d2
        ydenom += (w)/d2
    x = xnumer / xdenom
    y = ynumer / ydenom
    return (x,y)


def initialPoint(data):
    xdenom = 0
    xnumer = 0
    ydenom = 0
    ynumer = 0
    for x,y,w in data:
        xnumer += (w*x)
        xdenom += (w)
        ynumer += (w*y)
        ydenom += (w)
    x = xnumer / xdenom
    y = ynumer / ydenom
    return (x,y)

def calculate_distance_meters(x1,y1,x2,y2):
    coords_1 = (x1, y1)
    coords_2 = (x2, y2)
    return geopy.distance.distance(coords_1, coords_2).m

pooits = {12:(-33.54849627271406, -71.60218512265082,1),  
14:(-33.45559509581717, -71.66711299516905,1),  
13:(-33.36898813956519, -71.69042322634887,1),  
11:(-33.37056427315103, -71.66751079198616,1),  
15:(-32.752827073542846, -70.72734271538006,1),  
10:(-32.84341122102814, -71.22627269602326,1),  
18:(-32.992422307121274, -71.18965841090773,1),  
4 :(-32.800253356400646, -70.58063511617193,1),  
17 :(-32.744769307616856, -70.6544455948493,1),        
16:(-32.630825852956676, -70.71763738801766,1),  
8:(-32.25036206126296, -70.94388316715583,1),  
5:(-32.424438530731756, -71.06556136870246,1),  
6:(-32.44836260358062, -71.22852229374578,1),  
7:(-32.50554505551637, -71.44788931496512,1),  
9:(-32.552670330646365, -71.4594766591706,1),  
0:(-32.72269081362008, -71.41456000911093,1),  
1:(-32.77473658097262, -71.53313275519938,1),  
3:(-32.85356752296912, -70.6243858146913,1),  
2:(-32.83097574632666, -70.68867876076227,1),  
19:(-33.04726679144815, -71.61277415340342,1)}

pooits_v2 = {12:(-33.54849627271406, -71.60218512265082,1),  
14:(-33.45559509581717, -71.66711299516905,1),  
13:(-33.36898813956519, -71.69042322634887,1),  
11:(-33.37056427315103, -71.66751079198616,1),  
15:(-32.752827073542846, -70.72734271538006,1),  
10:(-32.84341122102814, -71.22627269602326,1),  
18:(-32.992422307121274, -71.18965841090773,1),  
4 :(-32.800253356400646, -70.58063511617193,1),  
17 :(-32.744769307616856, -70.6544455948493,1),        
16:(-32.630825852956676, -70.71763738801766,1),  
8:(-32.25036206126296, -70.94388316715583,1),  
5:(-32.424438530731756, -71.06556136870246,1),  
6:(-32.44836260358062, -71.22852229374578,1),  
7:(-32.50554505551637, -71.44788931496512,1),  
9:(-32.552670330646365, -71.4594766591706,1),  
0:(-32.72269081362008, -71.41456000911093,1),  
1:(-32.77473658097262, -71.53313275519938,1),  
3:(-32.85356752296912, -70.6243858146913,1),  
2:(-32.83097574632666, -70.68867876076227,1),  
19:(-33.04726679144815, -71.61277415340342,1)}

conn_matrix = [[0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
            [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
            [1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0]]

"""
Puchuncavi,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1
Quintero,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1
Rinconada,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0
Calle Larga,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0
San Esteban,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0
Cabildo,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0
La Ligua,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0
Papudo,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0
Petorca,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0
Zapallar,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0
Hijuelas,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1
Algarrobo,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1
Cartagena,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0
Guallelemu,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0
Totoral,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0
Catemu,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0
Putaendo,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0
Santa Maria,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0
Olmue,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1
Valparaiso,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0
"""

names = {0:"Puchuncavi", 
1:"Quintero", 
2:"Rinconada", 
3:"Calle Larga", 
4:"San Esteban", 
5:"Cabildo", 
6:"La Ligua", 
7:"Papudo", 
8:"Petorca", 
9:"Zapallar", 
10:"Hijuelas", 
11:"Algarrobo", 
12:"Cartagena", 
13:"Guallelemu", 
14:"Totoral", 
15:"Catemu", 
16:"Putaendo", 
17:"Santa Maria", 
18:"Olmue", 
19:"Valparaiso"
}
radius = {13:10000,
15:10000,
14:10000,
12:10000,
16:10000,
11:10000,
19:10000,
5 :10000,
18 :10000,
17:10000,
9:10000,
6:10000,
7:10000,
8:10000,
10:10000,
1:10000,
2:10000,
4:10000,
3:10000,
0:10000}

centroids ={12:(-33.54849627271406, -71.60218512265082,1),  
14:(-33.45559509581717, -71.66711299516905,1),  
13:(-33.36898813956519, -71.69042322634887,1),  
11:(-33.37056427315103, -71.66751079198616,1),  
15:(-32.752827073542846, -70.72734271538006,1),  
10:(-32.84341122102814, -71.22627269602326,1),  
18:(-32.992422307121274, -71.18965841090773,1),  
4 :(-32.800253356400646, -70.58063511617193,1),  
17 :(-32.744769307616856, -70.6544455948493,1),        
16:(-32.630825852956676, -70.71763738801766,1),  
8:(-32.25036206126296, -70.94388316715583,1),  
5:(-32.424438530731756, -71.06556136870246,1),  
6:(-32.44836260358062, -71.22852229374578,1),  
7:(-32.50554505551637, -71.44788931496512,1),  
9:(-32.552670330646365, -71.4594766591706,1),  
0:(-32.72269081362008, -71.41456000911093,1),  
1:(-32.77473658097262, -71.53313275519938,1),  
3:(-32.85356752296912, -70.6243858146913,1),  
2:(-32.83097574632666, -70.68867876076227,1),  
19:(-33.04726679144815, -71.61277415340342,1)}

verbose = True
def solve(rad = 0):
    ERR = 0.001
    for key_1,val_1 in pooits.items():
        #curr_x, curr_y,w = val_1
        curr_x, curr_y,w = pooits_v2[key_1]
        if verbose:
            print(f"[!] Starting to iterate on pooit: {key_1}, with current coordinates: {curr_x}, {curr_y}")
        # Se crea la primera iteración
        data = []
        datai = []
        neighbours = 0
        for key_2, val_2 in pooits.items():
            if conn_matrix[key_1][key_2] == 1:
                neighbours += 1
                if verbose:
                    print(f"[?] key_1, key_2: {key_1}, {key_2}")
                #xn, yn, w = val_2
                xn, yn, w = pooits_v2[key_2]
                # Calculate first 
                d2p0 = calculate_distance_meters(curr_x, curr_y, xn, yn)
                datai.append( (xn, yn, w, d2p0) )
        # Cannot calculate centroid on one neigh
        if neighbours <= 1:
            continue
        data.append(datai)
        k = 0
        zlist = []
        zlist.append(0)
        for r in data[0]:
            zlist[0] += r[-1] * r[-2]
        xn, yn = curr_x, curr_y
        while k <= 10000:
            old_x, old_y = (xn, yn)
            newPoint = newPoints(data[k])
            if verbose:
                print(f"[*] The new generated point for the pooit is: {newPoint}")
            xn,yn = newPoint
            zn = 0
            datai = []
            for pointVal in data[k]:
                #if conn_matrix[key_1][key_2] == 1:
                if verbose:
                    print(f"[*] Calculating distance between: ({pointVal[0]},{pointVal[1]}), ({newPoint[0]},{newPoint[1]})")
                d2p0 = calculate_distance_meters(pointVal[0], pointVal[1], newPoint[0], newPoint[1])
                weight = pointVal[2]
                # Se prueba la nueva iteración
                datai.append( (pointVal[0], pointVal[1], weight, d2p0))
                zn += (weight * d2p0)
            data.append(datai)
            zlist.append(zn)
            zdif = abs(zlist[-1] - zlist[-2])
            if zdif < ERR:
                if verbose:
                    print("[!] Converge. stopping")
                break
            if rad == 0:
                rad = radius[key_1]
            if calculate_distance_meters(xn, yn, centroids[key_1][0], centroids[key_1][1]) >= rad:
                xn = old_x
                yn = old_y
                if verbose:
                    print("[!] Excede radio, saliendo")
                break
            k = k + 1
        if verbose:
            print(f"[*] Got the following coordinates for pooit {key_1}: {xn}, {yn}")
        pooits_v2[key_1] = (xn, yn,1)
    pprint.pprint(pooits_v2)
    for j,k in pooits_v2.items():
        print(f"{names[j]}:\t\t({k[0]},{k[1]})")
    return None


def calculate_cost(p):
    s = 0
    for k1,v1 in p.items():
        for k2,v2 in p.items():
            if conn_matrix[k1][k2]:
                s += calculate_distance_meters(v1[0], v1[1], v2[0], v2[1])
    return s




if __name__ == "__main__":
    solve(rad = 10000)
    distance_1 = calculate_cost(pooits)
    distance_2 = calculate_cost(pooits_v2)

    print(f"Total distance of fiber cable initial: {distance_1/1000} meters")
    print(f"Total distance of fiber cable initial: {distance_2/1000} meters")