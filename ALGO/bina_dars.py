from dourous import *

#Données
def notNegativ(phrase):
  num = int(input(phrase + ":"))
  while(num < 0):
    print("Pas négatif".upper())
    num = int(input(phrase + ":"))
  return num


def choixDoubleLettres(phrase, a, b):
  choix= input(phrase + " " +  a + " / " +  b + ": ")
  while choix.upper() !=a and choix.upper() != b:
    print("Choix invalide")
    choix= input(phrase + " "  +  a + " / " +  b + ": ")
  return choix.upper()






def controlPersonnifieArguments():

  choix= choixDoubleLettres("Choisir les lettres" , "O", "N")
  choix_lettres=False
  
  if choix == "O": 
    choix2 = choixDoubleLettres("Lettres isolées ou attachées " , "I", "A")
     
    harf_awwal = 1 if choix2 == "I" else 3
    harf_akhir = 1 if choix2 == "I" else 3
    awwal, akhir = 7, 7
    choix_lettres=True


  else:
    awwal= notNegativ("Numéro du premier cours")
    akhir= notNegativ("Numéro du dernier cours")
    harf_awwal= notNegativ("Nombre de lettres de la première série")
    harf_akhir= notNegativ("Nombre de lettres de la dernière série")


  #adad_al_kalimates= int(input("Nombre de mots : "))
  adad_al_kalimates= notNegativ("Nombre de mots")

  
  return (awwal, akhir, adad_al_kalimates, harf_awwal, harf_akhir, choix_lettres)


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
  
  niv1 = (1, 7, 10, 1, 1, False)
  niv2 = (1, 7, 5, 3, 3, False)
  niv3 = (8, 12, 10, 3, 3, False)
  niv4 = (13, 18, 10, 3, 3, False)

  exam_niv1 = (7, 7, 50, 1, 1, False)
  exam_niv2 = (7, 7, 20, 3, 3, False)
  exam_niv3 = (12, 12, 10, 3, 3, False)
  exam_niv4 = (13, 18, 10, 3, 3, False)


  #Variables pour les tests
  niveaux_predefinis = (0, niv1, niv2, niv3, niv4, exam_niv1, exam_niv2, exam_niv3, exam_niv4)
  return niveaux_predefinis[dars]


def ModeBinaDars():
    #Variables des niveau
    
    
    phrase = """Choississez le mode
Personnifié (Tapez p)
Défini (Tapez d)
""" 
    mode = choixDoubleLettres(phrase, "P", "D")

    if(mode == "P"):
        return controlPersonnifieArguments()
    
    if(mode == "D"):    
        return  controlDefinieArguments()
  


def lettresDefinies(houroufs):
  print("Choisissez des lettres")
  houroufs = houroufs[0] + houroufs[1]
  hourouf_moukhtaras=[]
  
  for i in range(len(houroufs)):
    print(i, houroufs[i])

  nb_lettres = int(input("Combien de lettres ? : "))
  while nb_lettres < 0:
    print("Nombre négatifs !")
    nb_lettres = int(input("Combien de lettres ? : "))
  for i in range(nb_lettres):
    n = int(input("Sélectionnez une lettre : "))
    if(n >= len(houroufs) or n < 0):
      print("Chiffre non autorisé !")
      continue
    print("Vous avez choisi : ",houroufs[n]) 
    hourouf_moukhtaras+= houroufs[n]

  return hourouf_moukhtaras   

"""
awwal : Premier Cours
akhir : Dernier Cours
adad_al_kalimates : Nombre de mot dans une série
harf_awwal : nombre de lettre de la première série
harf_akhir : nombre de lettres de la dernière série

"""
def COURS_BUILDER(awwal=1, akhir=12, adad_al_kalimates=5, harf_awwal=1, harf_akhir=3, choix_lettres=False): 
    
    if(awwal > akhir or awwal <= 0 or akhir > 18):
      print("Erreur sur les numéros de Cours") ; return
    if (adad_al_kalimates < 0):
      print("Erreur sur les numéros le nombre de mot") ; return
    if(harf_awwal > harf_akhir or harf_awwal <= 0):
      print("Erreur sur le nombre de lettres") ; return
  
    for numero_du_cours in CC[awwal-1:akhir]:
      #capturer les lettres par "numero_du_cours"
      if choix_lettres:  
        hourouf_mourads = [numero_du_cours[1][0]] + [numero_du_cours[1][1]]
        hourouf_mourads = lettresDefinies(hourouf_mourads)
        n = len(hourouf_mourads)
        hourouf_mourads = [hourouf_mourads[:n//2]] + [hourouf_mourads[n//2:]]
        numero_du_cours[1] = hourouf_mourads

      print_cours(numero_du_cours, adad_al_kalimates, harf_awwal, harf_akhir)
