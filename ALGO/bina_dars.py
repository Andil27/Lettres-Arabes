from dourous import *

#Données



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
