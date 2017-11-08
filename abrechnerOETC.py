import math
import numpy as np
import itertools

co, oc, eo, oe, to, ot, ce, ec, ct, tc, et, te = 0,0,0,0,0,0,0,0,0,0,0,0


def dividor(payer):
    number = 0
    for char in payer:
        number += 1
        #if char != ",":
            #number += 1
    return number

def relations(buyer, payer):
    relation = []
    for char in payer:
        #if char != "," and char != buyer:
        if char != buyer:
            relation.append(char+buyer)
    #print(relation)
    return relation



with open('input.txt','r') as f:
    lines = f.read().splitlines()
    c = 0
    for char in lines:
        buyer, price, payer = char.split()
        #print("buyer: " + buyer + ", price: " + price)
        #print("countPayer: " + str(dividor(payer)))
        partPrice = float(price)/ dividor(payer)
        #print("partPrice: " + str(partPrice))

        relationArray = relations(buyer, payer)

        for i in relationArray:
            if i == 'co':
                co += partPrice
            elif i == 'oc':
                oc += partPrice
            elif i == 'eo':
                eo += partPrice
            elif i == 'oe':
                oe += partPrice
            elif i == 'to':
                to += partPrice
            elif i == 'ot':
                ot += partPrice
            elif i == 'ce':
                ce += partPrice
            elif i == 'ec':
                ec += partPrice
            elif i == 'ct':
                ct += partPrice
            elif i == 'tc':
                tc += partPrice
            elif i == 'et':
                et += partPrice
            elif i == 'te':
                te += partPrice
            else:
                print("Probably a wrong letter! Please check!")

        #end of for loop


#counting against
if(eo > oe):
    eo -= oe
    oe = 0
else:
    oe -= eo
    eo = 0

if(co > oc):
    co -= oc
    oc = 0
else:
    oc -= co
    co = 0

if(to > ot):
    to -= ot
    ot = 0
else:
    ot -= to
    to = 0

if(te > et):
    te -= et
    et = 0
else:
    et -= te
    te = 0

if(ce > ec):
    ce -= ec
    ec = 0
else:
    ec -= ce
    ce = 0

if(ct > tc):
    ct -= tc
    tc = 0
else:
    tc -= ct
    ct = 0


#print results
if(oe > 0):
    print("O -> E: %.2f" % round(oe, 2))
if(te > 0):
    print("T -> E: %.2f" % round(te, 2))
if(ce > 0):
    print("C -> E: %.2f" % round(ce, 2))
    
if(oc > 0):
    print("O -> C: %.2f" % round(oc, 2))
if(ec > 0):
    print("E -> C: %.2f" % round(ec, 2))
if(tc > 0):
    print("T -> C: %.2f" % round(tc, 2))
    
if(ot > 0):
    print("O -> T: %.2f" % round(ot, 2))
if(et > 0):
    print("E -> T: %.2f" % round(et, 2))
if(ct > 0):
    print("C -> T: %.2f" % round(ct, 2))
    
if(eo > 0):
    print("E -> O: %.2f" % round(eo, 2))
if(to > 0):
    print("T -> O: %.2f" % round(to, 2))
if(co > 0):
    print("C -> O: %.2f" % round(co, 2))