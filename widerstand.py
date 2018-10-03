import numpy as np
import itertools

data = [1000, 5600, 180, 6800, 8200, 820, 2700, 150, 100, 1800, 220, 1500, 330, 390, 680, 120, 3900, 3300, 4700, 560, 470, 1200, 270, 2200]
data = np.sort(data)

#TODO: rename variables etc, modify output

class WiderstandRechner(object):

    def __init__(self,k,val,data):
        self.data = data
        self.k = k
        self.val = val
        self.combinations = self.getCombinations()

    def getCombinations(self):
        """Tuple Liste mit allen Kombinationsmöglichkeiten von n-Elementen aus den gegebenen Daten"""
        itera = list(itertools.permutations(self.data, self.k))
        itera = np.array(itera)
        return itera

    ###############SCHALTUNGEN FÜR 2 WIDERSTÄNDE##################
    def f2_1(self, itera):
        every_comb_2_1 = {}
        for e1, e2 in itera:
            every_comb_2_1[e1 + e2] = str(e1)+'+'+str(e2)
        return every_comb_2_1

    def f2_2(self, itera):
        every_comb_2_2 = {}
        for e1, e2 in itera:
            every_comb_2_2[1/(1/(e1) + 1/(e2))] = '1/( 1/('+str(e1)+') + 1/('+str(e2)+') )'
        return every_comb_2_2
    ##############################################################

    ###############SCHALTUNGEN FÜR 3 WIDERSTÄNDE##################
    def f3_1(self, itera):
        every_comb_3_1 = {}
        for e1, e2, e3 in itera:
            every_comb_3_1[e1 + e2 + e3] = str(e1)+'+'+str(e2)+'+'+str(e3)
        return every_comb_3_1
    
    def f3_2(self, itera):
        every_comb_3_2 = {}
        for e1, e2, e3 in itera:
            every_comb_3_2[1/(1/(e1) + 1/(e2) + 1/(e3))] = '1/( 1/('+str(e1)+') + 1/('+str(e2)+') + 1/('+str(e3)+') )'
        return every_comb_3_2

    def f3_3(self, itera):
        every_comb_3_3 = {}
        for e1, e2, e3 in itera:
            every_comb_3_3[e1 + (1/1/(e2)+1/(e3))] = str(e1)+' +'+ ' (1/( 1/('+str(e2)+') + 1/('+str(e3)+') ) )'
        return every_comb_3_3
    
    def f3_4(self, itera):
        every_comb_3_4 = {}
        for e1, e2, e3 in itera:
            every_comb_3_4[1/(1/(e1+e2)+1/(e3))] = '1/( 1/('+str(e1)+'+'+str(e2)+') + 1/('+str(e3)+') )'
        return every_comb_3_4
    
    ##############################################################

    ###############SCHALTUNGEN FÜR 4 WIDERSTÄNDE##################
    def f4_1(self, itera):
        every_comb_4_1 = {}
        for e1, e2, e3, e4 in itera:
            every_comb_4_1[e1 + e2 + e3 + e4] = str(e1)+'+'+str(e2)+'+'+str(e3)+'+'+str(e4)
        return every_comb_4_1
    
    def f4_2(self, itera):
        every_comb_4_2 = {}
        for e1, e2, e3, e4 in itera:
            every_comb_4_2[1/(1/(e1) + 1/(e2) + 1/(e3) + 1/(e4))] = '1/( 1/('+str(e1)+') + 1/('+str(e2)+') + 1/('+str(e3)+') + 1/('+str(e4)+') )'
        return every_comb_4_2

    def f4_3(self, itera):
        every_comb_4_3 = {}
        for e1, e2, e3, e4 in itera:
            every_comb_4_3[e1 + e2 + (1/1/(e3)+1/(e4))] = str(e1)+'+'+str(e2)+'+(1/(1/('+str(e3)+')+1/('+str(e4)+')))'
        return every_comb_4_3
    
    def f4_4(self, itera):
        every_comb_4_4 = {}
        for e1, e2, e3, e4 in itera:
            every_comb_4_4[e1 + 1/( 1/(e2) + 1/(e3) + 1/(e4) )] = str(e1)+ ' + 1/( 1/('+str(e2)+') + 1/('+str(e3)+') + 1/('+str(e4)+') )'
        return every_comb_4_4

    def f4_5(self, itera):
        every_comb_4_5 = {}
        for e1, e2, e3, e4 in itera:
            every_comb_4_5[1/( 1/(e1) + 1/(e2) ) + 1/( 1/(e3) + 1/(e4) )] = '1/( 1/('+str(e1)+') + 1/('+str(e2)+') ) + 1/( 1/('+str(e3)+') + 1/('+str(e4)+') )'
        return every_comb_4_5
    
    def f4_6(self, itera):
        every_comb_4_6 = {}
        for e1, e2, e3, e4 in itera:
            every_comb_4_6[1/( 1/(e1+e2+e3) +  1/(e4) )] = '1/( 1/('+str(e1)+'+'+str(e2)+'+'+str(e3)+') + 1/('+str(e4)+') )' 
        return every_comb_4_6

    def f4_7(self, itera):
        every_comb_4_7 = {}
        for e1, e2, e3, e4 in itera:
            every_comb_4_7[1/( 1/(e1+e2) +  1/(1/(1/(e3)+1/(e4))) )] = '1/( 1/('+str(e1)+'+'+str(e2)+') + 1/( 1/( 1/('+str(e3)+') + 1/('+str(e4)+') ) ) )'
        return every_comb_4_7
    
    def f4_8(self, itera):
        every_comb_4_8 = {}
        for e1, e2, e3, e4 in itera:
            every_comb_4_8[1/( 1/(e1 + 1/(1/(e2)+1/(e3)) )+1/(e4))] = '1/( 1/('+str(e1)+' + 1/( 1/('+str(e2)+') + 1/('+str(e3)+') ) ) + 1/('+str(e4)+') )'
        return every_comb_4_8
    
    ##############################################################



    def nearest(self, val, ls):
        """Finde den nächsten Wert in einer Liste zu dem gegebenen Wert"""
        diff = [abs(val - i) for i in ls]
        minimum = np.sort(diff)[0]

        for i in range(len(ls)):
            if ls[i] + minimum == val or ls[i] - minimum == val:
                near_element = ls[i]

        return near_element

    def calc(self):
        """Berechne den nächsten mit k-Widerständen konstruierbaren Widerstandswert und gib die korrespondierende Schaltung aus"""
        if self.k == 1:
            return self.nearest(self.val, self.data)
        
        if self.k == 2:
            it = self.getCombinations()
            
            dic1 = self.f2_1(self.combinations)
            dic2 = self.f2_2(self.combinations)

            values_f1 = list(dic1.keys())            #Alle Widerstandswerte nach Schaltung 1
            values_f2 = list(dic2.keys())            #Alle Widerstandswerte nach Schaltung 2
            
            dic_ges = [dic1, dic2]

            nearest_f1 = self.nearest(self.val, values_f1)                   #Der nächste Widerstandswert nach Schaltung 1
            nearest_f2 = self.nearest(self.val, values_f2)                   #Der nächste Widerstandswert nach Schaltung 2

            nearest_ges = {nearest_f1: 0, nearest_f2: 1}       
            i = self.nearest(self.val, list(nearest_ges.keys()))                #Der insgesamt nächste Widerstandswert
            
            return (i, dic_ges[nearest_ges[i]][i]) 

        if self.k == 3:
            it = self.getCombinations()

            dic1 = self.f3_1(self.combinations)
            dic2 = self.f3_2(self.combinations)
            dic3 = self.f3_3(self.combinations)
            dic4 = self.f3_4(self.combinations)

            values_f1 = list(dic1.keys())
            values_f2 = list(dic2.keys())
            values_f3 = list(dic3.keys())
            values_f4 = list(dic4.keys())
        
            dic_ges = [dic1,dic2,dic3,dic4]

            nearest_f1 = self.nearest(self.val, values_f1)
            nearest_f2 = self.nearest(self.val, values_f2)
            nearest_f3 = self.nearest(self.val, values_f3)
            nearest_f4 = self.nearest(self.val, values_f4)

            nearest_ges = {nearest_f1: 0, nearest_f2: 1, nearest_f3: 2, nearest_f4: 3}
            i = self.nearest(self.val, list(nearest_ges.keys()))
            return (i, dic_ges[nearest_ges[i]][i])

        if self.k == 4:
            it = self.getCombinations()

            dic1 = self.f4_1(self.combinations)
            dic2 = self.f4_2(self.combinations)
            dic3 = self.f4_3(self.combinations)
            dic4 = self.f4_4(self.combinations)
            dic5 = self.f4_5(self.combinations)
            dic6 = self.f4_6(self.combinations)
            dic7 = self.f4_7(self.combinations)
            dic8 = self.f4_8(self.combinations)

            values_f1 = list(dic1.keys())
            values_f2 = list(dic2.keys())
            values_f3 = list(dic3.keys())
            values_f4 = list(dic4.keys())
            values_f5 = list(dic5.keys())
            values_f6 = list(dic6.keys())
            values_f7 = list(dic7.keys())
            values_f8 = list(dic8.keys())
        
            dic_ges = [dic1,dic2,dic3,dic4,dic5,dic6,dic7,dic8]

            nearest_f1 = self.nearest(self.val, values_f1)
            nearest_f2 = self.nearest(self.val, values_f2)
            nearest_f3 = self.nearest(self.val, values_f3)
            nearest_f4 = self.nearest(self.val, values_f4)
            nearest_f5 = self.nearest(self.val, values_f5)
            nearest_f6 = self.nearest(self.val, values_f6)
            nearest_f7 = self.nearest(self.val, values_f7)
            nearest_f8 = self.nearest(self.val, values_f8)

            nearest_ges = {nearest_f1: 0, nearest_f2: 1, nearest_f3: 2, nearest_f4: 3, nearest_f5: 4, nearest_f6: 5, nearest_f7: 6, nearest_f8: 7}
            i = self.nearest(self.val, list(nearest_ges.keys()))
            return (i, dic_ges[nearest_ges[i]][i])
        
        else:
            return "Please select a value for k from 1-4"

op = WiderstandRechner(3, 1337, data)
print(op.calc())

