import math
import matplotlib.pyplot as plt
class Noeud:

    def __init__(self,valeur,enfant):
        self.valeur=valeur
        if enfant is None:
            self.enfant=[]
        else:
            self.enfant=enfant#子节点

    def ajouter_noeud(self,enfant):
        self.enfant.append(enfant)

    def affiche_polonais(self):
        print(self.valeur,end=" ")
        for enfant in self.enfant:
            enfant.affiche_polonais()

    def evaluer(self,variable):#variable是字典
        if isinstance(self.valeur,(int,float)):
            return float(self.valeur)

        if len(self.enfant)==0:
            if self.valeur not in variable:
               raise ValueError("doit etre dans ce variable")
            return float(variable[self.valeur])

        if self.valeur in("+","-","*"):
            a=self.enfant[0].evaluer(variable)
            b=self.enfant[1].evaluer(variable)
            if self.valeur=="+":
                return a+b
            if self.valeur=="-":
                return a-b
            if self.valeur=="*":
                return a*b

        if self.valeur=="exp":
            a=self.enfant[0].evaluer(variable)
            return math.exp(a)

    def tracer(self,valeurs,variable):
        res=[]
        for valeur in valeurs:
            res1=self.evaluer({variable:valeur})
            res.append(res1)

        
        plt.plot(valeurs,res)
        plt.xlabel(variable)
        plt.ylabel("f(" + variable + ")")
        plt.grid()                        # 显示网格
        plt.show()                        # 显示图像窗口

           
    
        