__author__ = 'Pierre VIX'

import numpy as np
import time
import matplotlib.pyplot as plt
from random import *
#0==void
#1==block
#2==water

class Percolation(int):
    def __init__(self,value):
        super(Percolation,self).__init__()
        self.taille=15
        self.percentage=value
        self.matrix=self.InitMatrice2()
    def calculate(self):

        for i in range(self.taille):
            self.Ecoulement(0,[i])
        return self.reached2()
    
    def InitMatrice2(self):
        """ initialise la matrice  et l'affiche"""
        MatriceInit=[[0 for i in range(self.taille)]for liste in range(self.taille)]
        for i in range(self.taille):
            MatriceInit[0][i]=2
        Pourcentage = self.percentage/100*((self.taille*self.taille-self.taille))# Calcul le Pourcentage de grain de sable
        while Pourcentage >=0 :
            valeur1=randrange(self.taille)
            valeur2=randrange(1,self.taille)
            if MatriceInit[valeur2][valeur1] ==0 :
                    MatriceInit[valeur2][valeur1]=1
                    Pourcentage-=1
        return MatriceInit

    def InitMatrice(self):
        #initiate matrix with correct percentage and size (supposee carree)
        nums=np.reshape((np.random.rand(self.taille*self.taille) < self.percentage/100).astype(int),(self.taille,self.taille))
        nums[0]=np.full(self.taille,2)
        return nums

    def Ecoulement(self,i,j):
        self.matrix[i][j[-1]]=2
        pos=[-1,0,+1]
        i+=1
        for e in pos:
            j.append(j[-1]+e)
            if self.test(i) and self.test(j[-1]) and self.matrix[i][j[-1]]!=1 and self.matrix[i][j[-1]]!=2:
                self.Ecoulement(i,j)
            j.pop()
    def test(self,e):
        return 0<=e<self.taille
    def reached(self):
        return np.count_nonzero(self.matrix[-1] == 2)
    def reached2(self):
        c=0
        for el in self.matrix[-1]:
            if el==2:
                c+=1
        return c
def main():
    print("We are expecting at least 80 seconds of calculation, pls standby")
    pm=time.time()
    l=[] #contain all the outcome of percolation (between 0 and 50
    final=[]
    iter=100
    for coef in range(10,80):
        g=[]
        for o in range(iter):
            m=Percolation(coef).calculate()
            if m :
                g.append(m)

        l.append(g)
        final.append(len(g))

    print("It took: {} seconds for {} iterations for each coefficient".format(time.time()-pm,iter))
    plt.plot(list(range(10, 80)), final)
    plt.ylabel('Nombre de case atteinte sur les 50 dernieres')
    plt.xlabel("Coefficent")
    plt.show()

main()
