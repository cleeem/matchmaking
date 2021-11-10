data = {
    ".52 Gal" : 133,
    ".96 Gal" : 180,
    "Aerospray" : 110,
    "Jet Squelcher" : 225,
    "N-Zap" : 125,
    "Splash o matic" : 117,
    "Splattershot" : 125,
    "Splattershot Jr" : 110,
    "Splattershot Pro" : 170,
    "Sploosh o matic" : 80,
    "L-3" : 135,
    "H-3" : 170,
    "Dapple Dualies" : 95,
    "Splat Dualies" : 125,
    "Glooga Dualies" : 160,
    "Dualie Squelchers" : 170,
    "Tetra Dualies" : 140,
    "Squiffer" : 182,
    "Splat Charger" : 260,
    "Splatterscope" : 280,
    "E-litre" : 310,
    "E-Litre Scope" : 330,
    "Baboozler 14" : 210,
    "Goo Tuber" : 210,
    "Mini Splatling" : 150,
    "Heavy Splatling" : 210,
    "Hydra Splatling" : 245,
    "Ballpoint Splatling" : 245,
    "Nautilus" : 180,
    "Luna Blaster" : 110,
    "Blaster" : 133,
    "Range Blaster" : 170,
    "Clash Blaster" : 110,
    "Rapid Blaster" : 169,
    "Rapid Blaster Pro" : 192,
    "Slosher" : 145,
    "Tri-Slosher" : 110,
    "Sloshing Machine" : 147,
    "Bloblober" : 150,
    "Explosher" : 207,
    "Splat Brella" : 125,
    "Tenta Brella" : 150,
    "Undercover Brella" : 118,
    "Carbon Roller" : 95,
    "Splat Roller" : 118,
    "Dynamo Roller" : 185,
    "Flingza Roller" : 140,
    "Inkbrush" : 70,
    "Octobrush" : 105,
}



from itertools import combinations

def combi(liste,tout) :
    temp=combinations(liste,len(liste)//2)
    for combinaisons in list(temp) :
        tout[combinaisons] = power_moyen(combinaisons)

def power_moyen(liste) :
    somme = 0
    for e in liste:
        somme += data[e]
    m=somme/len(liste)
    return m


def find(armes,liste_tri) :
    mid=len(liste_tri)//2
    e1=liste_tri[mid-1]
    e2=liste_tri[mid]
    return e1,e2


def tri(tout,tout_liste) :
    for k, v in sorted(tout.items(), key=lambda x: x[1]):
        tout_liste.append([k,v])
    return tout_liste

def verif(armes,l1,l2) :
    temp=[]
    for i in range(len(armes)) :

        if armes[i] in l1[0] or armes[i] in l2[0] :
            temp.append(armes[i])

    if len(temp)==len(armes) :

        return True
    else :

        return False


def mm(armes : list , dico :dict = data) :
    tout = {}
    tout_liste=[]
    print(armes)
    combi(armes,tout)
    liste_tri=tri(tout,tout_liste)

    equipe1,equipe2=find(armes,liste_tri)

    if verif(armes,equipe1,equipe2) == True :
        print("oui")
        print("")
        return ("l'équipe 1 est composée de : \n"+str(equipe1)+"\nl'équipe 2 est composée de : \n"+str(equipe2))
    else :
        combi(armes,tout)
        liste_tri=tri(tout,tout_liste)

        equipe1,equipe2=find(armes,liste_tri)
        print("peut-être faux")
        print()
        return ("l'équipe 1 est composée de : \n"+str(equipe1)+"\nl'équipe 2 est composée de : \n"+str(equipe2))



from random import *

def random_comp(n=8):
    """Crée une liste d'armes de longueur n."""
    liste = []
    for i in range(n):
        v = randint(1, len(data) - 1)
        liste.append(list(data.keys())[v])
    return liste


print(mm(random_comp()))



