from random import *

lst = ['ع', 'ل', 'د','أ']
lst2 = ['e','f', 'z']
mot = ""


#A Lettres
"""Prends en paramètres une liste de lettre, la taille du mot, et le nombre de mots
Construit aléatoirement une liste de mots
Renvoie cette liste
"""
def Mot(lst, taille, nb_mots):
  
  Liste = []
  for i in range(nb_mots):
    mot = ""
    for j in range(taille):
      n = randint(0, len(lst) - 1)
      x = lst[n]
      mot = mot + x
    Liste.append(mot)
  
  return Liste





#2
"""Prends en paramètres une liste de lettre et le nombre de mots
    Construit une Série, ce qui correspond à 5 liste de mots, classées par ordre croissant du nombre de lettres
    Renvoie cette Série"""
def Serie(lst, nb_mots, harf_awwal, harf_akhir):
  Ser = []
  
  for i in range(harf_awwal -1, harf_akhir):
    Ser = Ser + Mot(lst, i + 1, nb_mots)
  
  
  
  return Ser
  
#B VOYELLES

def Harakates(serie, voyelles):
  serie_jadid = []
  for mot in serie:
    mot_jadid = []
    

    for lettre in mot :
      n = randint(0, len(voyelles) - 1)
      voy = voyelles[n]
      lettre_jadid = lettre + voy
      
    
      mot_jadid.append(lettre_jadid)
      x = "".join(mot_jadid)
      y = x.split(" ")
      x = "".join(y)
    serie_jadid.append(x)

  return serie_jadid
  #print("serie_jadid :", serie_jadid)

def Madd(serie):
  hrk = " َ ِ ُ"
  x = hrk.split(" ")
  hrk = "".join(x)
  
  mad = "ايو"
  
  serie_jadid = []
  for mot in serie:
    
    x = mot.split(hrk[0])
    y = (hrk[0]+mad[0]).join(x)
    x = y.split(hrk[1])
    y = (hrk[1]+mad[1]).join(x)
    x = y.split(hrk[2])
    y = (hrk[2]+mad[2]).join(x)
    
    serie_jadid.append(y)

  return serie_jadid


def Tanwin(serie):
  hrk = " َ ِ ُ"
  x = hrk.split(" ")
  hrk = "".join(x)
  
  mad = "ً ٍ ٌ"
  x = mad.split(" ")
  mad = "".join(x)
  

  #TODO ne mettre le tanwin qu'à la fin
  serie_jadid = []
  for mot in serie:
    
    x = mot.split(hrk[0])
    y = (mad[0]).join(x)
    x = y.split(hrk[1])
    y = (mad[1]).join(x)
    x = y.split(hrk[2])
    y = (mad[2]).join(x)
    
    serie_jadid.append(y)

  return serie_jadid

def Soukoun(serie):
  hrk = " َ ِ ُ"
  x = hrk.split(" ")
  hrk = "".join(x)
  
  mad = "ً ٍ ٌ"
  x = mad.split(" ")
  mad = "".join(x)
  
  serie_jadid = []
  for mot in serie:  
    mot2 = []
    for i in range(len(mot)):
      mot2.append(mot[i])
      if i == 3 or i == 9:
        mot2[i] = "ْ"
      
    y = "".join(mot2)
    serie_jadid.append(y)
    
  return serie_jadid

def Shadda(serie):
  hrk = " َ ِ ُ"
  x = hrk.split(" ")
  hrk = "".join(x)
  
  mad = "ً ٍ ٌ"
  x = mad.split(" ")
  mad = "".join(x)
  
  serie_jadid = []
  for mot in serie:  
    mot2 = []
    for i in range(len(mot)):
      mot2.append(mot[i])
      if i == 3 or i == 9:
        mot2[i] = "ّ" + mot2[i]
      
    y = "".join(mot2)
    serie_jadid.append(y)
    
  return serie_jadid





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
      A = Shadda(A) 
      B = Shadda(B) 
      C = Shadda(C) 

    if num == 17:
      A = Soukoun(A) 
      B = Shadda(B) 
      C = Soukoun(C)
      C = Tanwin(C)
  
      

  L = []
  L.append(A)
  L.append(B)
  L.append(C)

  return L

#AFFICHAGE
"""Prends en parmètre une chaînes contenant toutes les lettres
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
  print(' '.join(lst))

def aff_colonne(lst, nb_mots):
  i = 0
  for mots in lst:
    i += 1
    if (i - 1) % nb_mots == 0:
      print("______")
    print(i, mots)


"""Prends en paramètres des un cours, qui correspond à une liste de mots 
  Les affiche"""
def print_cours(cours, nb_mots, harf_awwal, harf_akhir):
  

  print("######################")
  
  #1 à 7
  if cours[0] <= 7 :
    HA, HB = cours[1]
    C = Cours(HA, HB, nb_mots, harf_awwal, harf_akhir)
    print("       COURS ", cours[0], HA[0], "-" , HB[-1])

  #8
  elif cours[0] <= 17:
    HA, HB = cours[1]
    Har = cours[2]
    C = Cours(HA, HB,nb_mots, harf_awwal, harf_akhir,  Har,cours[0])
    print("       COURS ", cours[0], C[0][-1])


  
  
 

  print("######################")
  print("______")  
  
  if cours[0] < 8:
    aff_ligne(HA)
    aff_colonne(C[0], nb_mots) #NBM

    print("______")
    print("______")
    print("______")
    
    
    aff_ligne(HB) 
    aff_colonne(C[1], nb_mots)

    print("______")
    print("______")
    print("______")
  
  aff_ligne(HA + HB)
  aff_colonne(C[2], nb_mots)



#Données


HRF = lettre_temp("أ ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي")
HRK = hark_temp(" َ ِ ُ")

H1 = HRF[0:4]
H2 = HRF[4:7]
H3 = HRF[7:11]
H4 = HRF[11:15]
H5 = HRF[15:19]
H6 = HRF[19:22]
H7 = HRF[22:25]
H8 = HRF[25:28]
H9 = HRK

H1, H2, H3, H4, H5, H6, H7, H8


C1 = [1, [H1, H2]]
C2 = [2, [H3, H4]]
C3 = [3, [H5, H6]]
C4 = [4, [H7, H8]]
C5 = [5, [H1 + H2, H3 + H4]]
C6 = [6, [H5 + H6, H7 + H8]]
C7 = [7, [H1 + H2 + H3 + H4, H5 + H6 + H7 + H8]]
alph = C7[1]

C8 = [8, alph, H9[0]]
C9 = [9, alph, H9[1]]
C10 = [10, alph, H9[0:2]]
C11 = [11, alph, H9[2]]
C12 = [12, alph, H9[0:3]]
C13 = [13, alph, H9]
C14 = [14, alph, H9]
C15 = [15, alph, H9]
C16 = [16, alph, H9]
C17 = [17, alph, H9]




CC = [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17]

"""
awwal : Premier Cours
akhir : Dernier Cours
adad_al_kalaimtes : Nombre de mot dans une série
harf_awwal : nombre de lettre de la première série
harf_akhir : nombre de lettres de la dernière série

"""
def COURS_BUILDER(awwal=1, akhir=12, adad_al_kalimates=5, harf_awwal=1, harf_akhir=3): 
    if(awwal > akhir or awwal <= 0 or akhir > 17  ):
      print("Erreur sur les numéros de Cours") ; return
    if (adad_al_kalimates < 0  ):
      print("Erreur sur les numéros le nombre de mot") ; return
    if(harf_awwal > harf_akhir or harf_awwal <= 0):
      print("Erreur sur le nombre de lettres") ; return
  

    for numero_du_cours in CC[awwal-1:akhir]:
      print_cours(numero_du_cours, adad_al_kalimates, harf_awwal, harf_akhir)


premier_cours=1
dernier_cours=7
nombre_mot=10
nombre_de_lettres_premiere_serie=1
nombre_de_lettres_derniere_serie=1


niv1 = (1, 7, 10, 1, 1)
niv2 = (1, 7, 5, 3,3)
niv3 = (8, 12, 10, 3,3)
nivX = (8, 16, 10, 3,3)
nivTest = (17, 17, 30, 3,3)

premier_cours,dernier_cours, nombre_mot, nombre_de_lettres_premiere_serie, nombre_de_lettres_derniere_serie = nivTest



COURS_BUILDER(premier_cours,
              dernier_cours, 
              nombre_mot, 
              nombre_de_lettres_premiere_serie, 
              nombre_de_lettres_derniere_serie 
)

#Faire une nouvelle fonction OK
#ajouter le paramètre des lettres OK
#Régler le problème pour la leçon 8 à 12 (nombre de lettres)

