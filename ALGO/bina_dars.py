from dourous import *

#Données




def controlPersonnifieArguments():
  awwal= int(input("Numéro du premier cours : "))
  akhir= int(input("Numéro du dernier cours : "))
  adad_al_kalimates= int(input("Nombre de mots : "))
  harf_awwal= int(input("Nombre de lettres de la première série : "))
  harf_akhir= int(input("Nombre de lettres de la dernière série : "))

  return (awwal, akhir, adad_al_kalimates, harf_awwal, harf_akhir)


def controlDefinieArguments():
  print("Niveau 1 -> leçon 1 à 7, lettres non attachées (tapez 1)")
  print("Niveau 2 -> leçon 1 à 7, lettres attachées attachées (tapez 2)")
  print("Niveau 3 -> leçon 1 à 7, voyelles (tapez 3)")
  print("Niveau 4 -> leçon 1 à 7, soukoun, shadda, moudoud, tanwin (tapez 4)")
  print("Examen niveau 1 -> leçon 1 à 7, lettres non attachées (tapez 5)")
  print("Examen niveau 2 -> leçon 1 à 7, lettres non attachées (tapez 6)")
  print("Examen niveau 3 -> leçon 1 à 7, lettres non attachées (tapez 7)")
  print("Examen niveau 4 -> leçon 1 à 7, lettres non attachées (tapez 8)")
  
  dars = int(input("Entrez le numéro : "))
  while(dars < 0 or dars > 8):
    dars = int(input("Entrez le numéro : "))
  
  niv1 = (1, 7, 10, 1, 1)
  niv2 = (1, 7, 5, 3, 3)
  niv3 = (8, 12, 10, 3, 3)
  niv4 = (13, 18, 10, 3, 3)

  exam_niv1 = (7, 7, 50, 1, 1)
  exam_niv2 = (7, 7, 20, 3, 3)
  exam_niv3 = (12, 12, 10, 3, 3)
  exam_niv4 = (13, 18, 10, 3, 3)


  #Variables pour les tests
  niveaux_predefinis = (0, niv1, niv2, niv3, niv4, exam_niv1, exam_niv2, exam_niv3, exam_niv4)
  return niveaux_predefinis[dars]


def ModeBinaDars():
    #Variables des niveau
    print("Choississez le mode  :")
    print("Personnifié  (Tapez p)")
    print("Défini (Tapez d)")
    
    
    mode = input()
    while(mode != "p" and mode!= 'd'):
        mode = input()

    if(mode == "p"):
        return controlPersonnifieArguments()
    
    if(mode == "d"):    
        return  controlDefinieArguments()

"""
awwal : Premier Cours
akhir : Dernier Cours
adad_al_kalimates : Nombre de mot dans une série
harf_awwal : nombre de lettre de la première série
harf_akhir : nombre de lettres de la dernière série

"""
def COURS_BUILDER(awwal=1, akhir=12, adad_al_kalimates=5, harf_awwal=1, harf_akhir=3): 
    if(awwal > akhir or awwal <= 0 or akhir > 18  ):
      print("Erreur sur les numéros de Cours") ; return
    if (adad_al_kalimates < 0  ):
      print("Erreur sur les numéros le nombre de mot") ; return
    if(harf_awwal > harf_akhir or harf_awwal <= 0):
      print("Erreur sur le nombre de lettres") ; return
  

    for numero_du_cours in CC[awwal-1:akhir]:
      print_cours(numero_du_cours, adad_al_kalimates, harf_awwal, harf_akhir)
