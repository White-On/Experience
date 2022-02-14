import math
from tkinter import Y
import matplotlib.pyplot as plt
import numpy as np

class Point:
    all = []
    def __init__(self, x = 0.0, y = 0.0) -> None:
        self.x = x
        self.y = y
        Point.all.append(self)

    def __repr__(self) -> str:
        return f"Point({self.x}; {self.y})"
    
    def afficher(self,coor_pts = False,color='b'):
        plt.scatter(self.x,self.y,c = color)

        if(coor_pts):
            plt.text(self.x, self.y, f"  {self}")

    @classmethod
    def afficher_all(cls):
        for point in cls.all:
            point.afficher()

class Droite:
    all = []
    def __init__(self, Point1: Point, Point2: Point) -> None:
        self.Point1 = Point1
        self.Point2 = Point2
        Droite.all.append(self)

    def __repr__(self) -> str:
        return f"Droite({self.Point1}; {self.Point2})"

    def calcul_longueur(self):
        return round(math.sqrt((self.Point1.x - self.Point2.x)**2 + (self.Point1.y - self.Point2.y)**2 ),1)

    def afficher(self,c = 'b'):
        self.Point1.afficher()
        self.Point2.afficher()
        plt.plot([self.Point1.x,self.Point2.x],[self.Point1.y,self.Point2.y],c)
    
    @classmethod
    def afficher_all(cls):
        for droite in cls.all:
            droite.afficher()

def learp(p1 : Point, p2 : Point, t : int) -> Point :
    x = (1-t) * p1.x + t*p2.x
    y = (1-t) * p1.y + t*p2.y
    return Point(x,y)

def quadraBezCurv(P0:Point,P1:Point,P2:Point)->None:
    D0 = Droite(P0,P1)
    D1 = Droite(P1,P2)
    D0.afficher();D1.afficher()
    T = [i*0.1 for i in range(10)]
    P = []
    for t in T:
        P.append(learp(learp(P0,P1,t),learp(P1,P2,t),t))
    Point.afficher_all()
    plt.show()

def cubicBezCurv(P0:Point,P1:Point,P2:Point,P3:Point)->None:
    D0 = Droite(P0,P1);D0.afficher('g')
    D2 = Droite(P2,P3);D2.afficher('g')

    T = [i*0.01 for i in range(1,100)]
    P = []
    for t in T:
        P.append(learp(learp(learp(P0,P1,t),learp(P1,P2,t),t),learp(learp(P1,P2,t),learp(P2,P3,t),t),t))
    
    for p in P:
        p.afficher(color = 'g')

    
    

def deriveBezCurv(P0:Point,P1:Point,P2:Point,P3:Point)->None:
    D0 = Droite(P0,P1);D0.afficher('g')
    D2 = Droite(P2,P3);D2.afficher('g')

    T = [i*0.01 for i in range(1,100)]
    P = []
    
    for t in T:
        x = P0.x*( -3*t**2 + 6*t - 3 ) + P1.x*( 9*t**2 - 12*t + 3) + P2.x*( -9*t**2 + 6*t) + P3.x*(3*t**2)
        y = P0.y*( -3*t**2 + 6*t - 3 ) + P1.y*( 9*t**2 - 12*t + 3) + P2.y*( -9*t**2 + 6*t) + P3.y*(3*t**2)
        P.append(Point(x,y))
    
    P_norm = np.array([[P0.x*( -3*t**2 + 6*t - 3 ) + P1.x*( 9*t**2 - 12*t + 3) + P2.x*( -9*t**2 + 6*t) + P3.x*(3*t**2) for t in T ],[P0.y*( -3*t**2 + 6*t - 3 ) + P1.y*( 9*t**2 - 12*t + 3) + P2.y*( -9*t**2 + 6*t) + P3.y*(3*t**2) for t in T ]])

    P_norm = P_norm/np.sqrt(np.sum(P_norm**2))

    Pt = []
    for t in T:
        Pt.append(learp(learp(learp(P0,P1,t),learp(P1,P2,t),t),learp(learp(P1,P2,t),learp(P2,P3,t),t),t))
    

    #Affichage tangeante Vectoriel non normalisée
    """for i in range(P_norm.shape[1]):
        plt.arrow(Pt[i].x,Pt[i].y,P[i].x,P[i].y)"""

    #Affichage tangeante Vectoriel normalisée
    """for i in range(P_norm.shape[1]):
        plt.arrow(Pt[i].x,Pt[i].y,P_norm[0,i]*50,P_norm[1,i]*50)""" #on multiplie par 50 pour voir quelque chose 

    rot90 = - np.pi/2
    P_rot90 = np.array([P_norm[0]*np.cos(rot90) + P_norm[1]*np.sin(rot90),-P_norm[0]*np.sin(rot90) + P_norm[1]*np.cos(rot90)])*50

    #Affichage Norme Vectoriel normalisée
    for i in range(P_norm.shape[1]):
        plt.arrow(Pt[i].x,Pt[i].y,P_rot90[0,i],P_rot90[1,i])
    

    for i in range(P_norm.shape[1]):
        Point(Pt[i].x + P_rot90[0,i],Pt[i].y + P_rot90[1,i]).afficher()
        
    


############# MAIN #############

P0 = Point(5,0)
P1 = Point(0,10)
P2 = Point(20,10)
P3 = Point(15,0)

cubicBezCurv(P0,P1,P2,P3)
deriveBezCurv(P0,P1,P2,P3)

plt.show()


