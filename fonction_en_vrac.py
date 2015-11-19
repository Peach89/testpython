import os

def afficher_flottant(nb):
    """Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.

    De plus, on va remplacer le point décimal par la virgule"""
    
    if type(nb) is not float:
        raise TypeError("le paramètre attendu doit être un flottant")
    t = str(nb).split(".")
    t[1] = t[1][0:3]
    t = ','.join(t)
    print(t)

def afficher(*values, sep=' ', end='\n'):
    values = list(values)
    values = [str(value) for value in values]
    chaine = sep.join(values)
    chaine += end
    print(chaine)

def fusion(a,b):
    na,nb = len(a),len(b)
    liste,i,j = [],0,0
    while  i < na and j < nb:
        if a[i][1]<b[j][1]:
            liste.append(a[i])
            i+=1
        else:
            liste.append(b[j])
            j+=1
    if i == na:
        liste += b[j:nb]
    else:
        liste += a[i:na]
    return liste
        
def tri(liste):
    n = len(liste)
    if(n==1):
        return liste
    return fusion(tri(liste[0:n//2]),tri(liste[n//2:n]))