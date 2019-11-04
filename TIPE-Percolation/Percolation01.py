__author__ = 'vixpierre'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from ui_fenetre import Ui_MainWindow
from random import *
from pylab import *

nbcellule=70
taillecellule=7
nbIter=100

#MatriceInit=[[0 for i in range(20)]for liste in range(20)]
#MatriceBis=[[0 for i in range(20)]for liste in range(20)]

class fenetreLignes(QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.clock = QTimer()
        self.canvas=ZoneG(self)
        self.canvas.setGeometry(10,10,600,600)
        self.clock.timeout.connect(self.canvas.Ecoulement)
        self.clock.stop()
        self.setGeometry(600,100,1000,800)
        self.PourcentagelSlider.setValue(32)
        self.PourcentagevalueChanged()
        self.VitesseTimerlSlider.setValue(1000)
        self.nbIter=nbIter
        self.Pourcentageldebut=10
        self.Pourcentagelfin=80
        self.ListeResultat=[ 0 for i in range(self.Pourcentagelfin-self.Pourcentageldebut)]

    def PourcentagevalueChanged(self):
        self.valeur=self.PourcentagelSlider.value()
        self.canvas.ValeurInit(self.valeur)
        self.PourcentagelineEdit.setText(str(self.valeur))

    def VitessevalueChanged(self):
        v=self.VitesseTimerlSlider.value()
        self.clock.setInterval(v)

    def StartCalcul(self):
        v=self.VitesseTimerlSlider.value()
        self.clock.start(v)
        self.PourcentagelSlider.setDisabled(True)
        self.clock.timeout.connect(self.canvas.TestEcoulement)

    def ArretCalcul(self):
        self.clock.stop()

    def NouveauDessin(self):
        self.canvas.Percolation=False
        self.canvas.InitMatrice()

    def StartResultat(self):
        self.canvas.EnCalcul=True
        for coef in range(self.Pourcentageldebut,self.Pourcentagelfin+1):
            self.PourcentagelSlider.setValue(coef)
            for Iter in range(self.nbIter):
                self.canvas.Percolation=False
                self.canvas.InitMatrice()
                self.canvas.TestResultat()
                if self.canvas.Percolation :
                    self.ListeResultat[coef]+=1
                else :
                    self.canvas.EnEcoulement=True
                print(Iter,coef)
        plot([i for i in range(self.Pourcentagelfin-self.Pourcentageldebut)],self.ListeResultat)
        show()

class ZoneG(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.canvasZG=QPixmap(600,600)
        self.valeur = 0
        self.EnEcoulement=True
        self.Percolation=False
        self.Matrice=[[0 for i in range(nbcellule)]for liste in range(nbcellule)]
        self.MatriceBis=[[0 for i in range(nbcellule)]for liste in range(nbcellule)]
        self.Listepos=[]
        self.EnCalcul=False

    def ValeurInit(self,nouvellevaleur):
        """ modifie la valeur de PourcentageSlider pour redessiner le dessin """
        self.valeur=nouvellevaleur
        self.InitMatrice()

    def InitMatrice(self):
        """ initialise la matrice  et l'affiche"""
        self.Listepos=[]
        self.Matrice=[[0 for i in range(nbcellule)]for liste in range(nbcellule)]
        for i in range(nbcellule):
            self.Matrice[0][i]=1
            self.Listepos+=[[0,i]]
        Pourcentage = self.valeur/100*((nbcellule*nbcellule-nbcellule))# Calcul le Pourcentage de grain de sable
        while Pourcentage >=0 :
            valeur1=randrange(nbcellule)
            valeur2=randrange(1,nbcellule)
            if self.Matrice[valeur2][valeur1] ==0 :
                    self.Matrice[valeur2][valeur1]=2
                    Pourcentage-=1
        if not self.EnCalcul :
            self.dessin()

    def dessin(self):
        """dessine la matrice"""
        p=QPainter(self.canvasZG)
        p.setPen(Qt.black)
        for i in range(nbcellule):
            for j in range(nbcellule):
                if self.Matrice[j][i]==0 :
                     p.setBrush(Qt.white)
                elif self.Matrice[j][i]==1:
                    p.setBrush(Qt.darkBlue)
                else :
                    p.setBrush(Qt.black)
                p.drawRect(i*taillecellule,j*taillecellule,taillecellule,taillecellule)
        self.repaint()

    def Ecoulement(self):
        """s'occupe uniquement de l'ecoulement de l'eau pour une iteration"""
        iteration =0
        for ligne in range(nbcellule):
            for colonne in range(nbcellule):
                self.MatriceBis[ligne][colonne]=self.Matrice[ligne][colonne]
        while iteration < len(self.Listepos) :
            if self.Listepos[iteration][0]!=nbcellule-1:
                if self.Listepos[iteration][1]==0:
                    if self.Matrice[self.Listepos[iteration][0]+1][self.Listepos[iteration][1]]==0:
                        self.Matrice[self.Listepos[iteration][0]+1][self.Listepos[iteration][1]]=1
                        self.appendsansdoublon(self.Listepos[iteration][0]+1,self.Listepos[iteration][1],iteration+1)
                    if self.Matrice[self.Listepos[iteration][0]][self.Listepos[iteration][1]+1]==0:
                        self.Matrice[self.Listepos[iteration][0]][self.Listepos[iteration][1]+1]=1
                        self.appendsansdoublon(self.Listepos[iteration][0],self.Listepos[iteration][1]+1,iteration+1)
                    iteration+=1
                elif self.Listepos[iteration][1]==nbcellule-1:
                    if self.Matrice[self.Listepos[iteration][0]][self.Listepos[iteration][1]-1]==0:
                        self.Matrice[self.Listepos[iteration][0]][self.Listepos[iteration][1]-1]=1
                        self.appendsansdoublon(self.Listepos[iteration][0],self.Listepos[iteration][1]-1,iteration+1)
                    if self.Matrice[self.Listepos[iteration][0]][self.Listepos[iteration][1]+1]==0:
                        self.Matrice[self.Listepos[iteration][0]][self.Listepos[iteration][1]+1]=1
                        self.appendsansdoublon(self.Listepos[iteration][0],self.Listepos[iteration][1]+1,iteration+1)
                    iteration+=1
                else :
                    if self.Matrice[self.Listepos[iteration][0]+1][self.Listepos[iteration][1]]==0:
                        self.Matrice[self.Listepos[iteration][0]+1][self.Listepos[iteration][1]]=1
                        self.appendsansdoublon(self.Listepos[iteration][0]+1,self.Listepos[iteration][1],iteration+1)
                    if self.Matrice[self.Listepos[iteration][0]][self.Listepos[iteration][1]-1]==0:
                        self.Matrice[self.Listepos[iteration][0]][self.Listepos[iteration][1]-1]=1
                        self.appendsansdoublon(self.Listepos[iteration][0],self.Listepos[iteration][1]-1,iteration+1)
                    if self.Matrice[self.Listepos[iteration][0]][self.Listepos[iteration][1]+1]==0:
                        self.Matrice[self.Listepos[iteration][0]][self.Listepos[iteration][1]+1]=1
                        self.appendsansdoublon(self.Listepos[iteration][0],self.Listepos[iteration][1]+1,iteration+1)
                    iteration+=1
            else :
                self.Percolation=True
                break
        if not self.EnCalcul :
            self.dessin()

    def appendsansdoublon(self,Ligne,Colonne,iteration):
        """verifie si un element est deja present dans ma listeResultat"""
        Trouve=True
        for Liste in self.Listepos :
            if Liste == [Ligne,Colonne] :
                Trouve = False
                break
        if Trouve :
            self.Listepos.insert(iteration,[Ligne,Colonne])

    def TestPeco(self) :
        perco=False
        for i in range(nbcellule):
            if self.Matrice[nbcellule-1][i]==1:
                perco=True
        return perco

    def TestEcoulement(self):
        """Fait le test pour voir s'il y a ecoulement"""
        self.Ecoulement()
        essai.clock.stop()
        essai.lineEdit_Perco.setText("{}".format(self.Percolation))

    def TestResultat(self):
        while (self.EnEcoulement) and (self.Percolation==False):
            self.Ecoulement()
            self.Percolation=self.TestPeco()

    def paintEvent(self, QPaintEvent):
        p=QPainter(self)
        p.drawPixmap(0,0,self.canvasZG)

    def mousePressEvent(self, QMouseEvent):
        """marche pas"""
        xpos=QMouseEvent.x()
        ypos=QMouseEvent.y()
        i=xpos//taillecellule
        j=ypos//taillecellule
        p=QPainter(self.canvasZG)
        if self.Matrice[j-1][i-1]==2:
            self.Matrice[j-1][i-1]=0
            p.setPen(Qt.black)
            p.setBrush(Qt.white)
            p.drawRect(i*taillecellule,j*taillecellule,taillecellule,taillecellule)

        elif self.Matrice[j-1][i-1]==0:
            self.Matrice[j-1][i-1]=2
            p.setPen(Qt.black)
            p.setBrush(Qt.black)
            p.drawRect(i*taillecellule,j*taillecellule,taillecellule,taillecellule)

        self.repaint()

app = QApplication(sys.argv)
essai = fenetreLignes()
essai.show()
app.exec()

