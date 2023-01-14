from random import *

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
  
