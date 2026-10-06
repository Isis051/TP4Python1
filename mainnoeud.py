from noeud import Noeud

a=Noeud(2,[])
b=Noeud("y",[])

somme=Noeud("+",[])
somme.ajouter_noeud(a)
somme.ajouter_noeud(b)#2+y
print(somme.evaluer({"y":3}))

exp=Noeud("exp",[])
exp.ajouter_noeud(somme)
exp.affiche_polonais()
print(exp.evaluer({"y":3}))

somme.tracer([1,2,3,4],"y")


#从叶一直向上添加子节点