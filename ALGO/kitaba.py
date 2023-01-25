from ashkal import *

f = open("fichierCoursPrint", "w")

def printInFichier(f,*list):
  for elem in list:
    f.write(str(elem)+ " ")
  f.write("\n")

  

#3
"""Prends en paramètre 2 listes
    Construit une liste de 3 série sur les lettres du cours
    Revoie cette liste"""  
def Cours(lst, lst2,  nomb_mots, harf_awwal, harf_akhir, voy=" ", num = 0):
  nbm = nomb_mots

  A = Serie(lst, nbm, harf_awwal, harf_akhir)
  B = Serie(lst2, nbm, harf_awwal, harf_akhir)
  C = Serie(lst + lst2, nbm, harf_awwal, harf_akhir)
  
  if num >= 8 :
    A = Harakates(A, voy)
    B = Harakates(B, voy)
    C = Harakates(C, voy)

    if num == 13:
      A = Madd(A)
      B = Madd(B)  
      C = Madd(C)

    if num == 14:
      A = Tanwin(A)
      B = Tanwin(B)  
      C = Tanwin(C)


    if num == 15:
      A = Soukoun(A)
      B = Soukoun(B)
      C = Soukoun(C)

    if num == 16:
      A =(Shadda(A))
      B =(Shadda(B))
      C =(Shadda(C))


    #Soukoun + Taarif 
    if num == 17:
      C = Taarif(Soukoun(C))

    #Madd + Shadda + Tanwin
    if num == 18:
      C = Tanwin(Shadda(Madd(C)))
     
     
       

    
      

  L = []
  L.append(A)
  L.append(B)
  L.append(C)

  return L

#AFFICHAGE
"""Prends en parmètre une chaîne contenant toutes les lettres
  Construit une liste
  Renvoie la liste"""
def lettre_temp(txt):
  lst = txt.split(" ")
  return lst

def hark_temp(txt):
  lst = txt.split(" ")
  lst.pop(0)
  return lst


def aff_ligne(lst):
  printInFichier(f, ' '.join(lst))

def aff_colonne(lst, nb_mots):
  
  i = 0
  for mots in lst:
    
    i += 1
    if (i - 1) % nb_mots == 0:
      printInFichier(f, "______")

    mots =  ("إِ").join(mots.split("أِ")) 
    printInFichier(f, i, mots)


"""Prends en paramètres des un cours, qui correspond à une liste de mots 
  Les affiche"""
def print_cours(cours, nb_mots, harf_awwal, harf_akhir):
  

  printInFichier(f, "######################")
  
  #1 à 7
  if cours[0] <= 7 :
    HA, HB = cours[1]
    C = Cours(HA, HB, nb_mots, harf_awwal, harf_akhir)
    printInFichier(f, "       COURS ", cours[0], HA[0], "-" , HB[-1])

  #8
  elif cours[0] <= 19:
    HA, HB = cours[1]
    Har = cours[2]
    C = Cours(HA, HB,nb_mots, harf_awwal, harf_akhir,  Har,cours[0])
    printInFichier(f, "       COURS ", cours[0], C[0][-1])
    

  
  
 

  printInFichier(f, "######################")
  printInFichier(f, "______")  
    
  
  if cours[0] < 8:
    aff_ligne(HA)
    aff_colonne(C[0], nb_mots) #NBM
    

    printInFichier(f, "______")
    printInFichier(f, "______")
    printInFichier(f, "______")
    
    
    aff_ligne(HB) 
    aff_colonne(C[1], nb_mots)

    printInFichier(f, "______")
    printInFichier(f, "______")
    printInFichier(f, "______")
  
  aff_ligne(HA + HB)
  aff_colonne(C[2], nb_mots)
  

