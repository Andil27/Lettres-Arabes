from kalimates import *

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
    
    x = mot[2:4].split(hrk[0])
    y = (hrk[0]+mad[0]).join(x)
    x = y.split(hrk[1])
    y = (hrk[1]+mad[1]).join(x)
    x = y.split(hrk[2])
    y = (hrk[2]+mad[2]).join(x)
    y = mot[:2] + y + mot[4:]
    
    serie_jadid.append(y)

  return serie_jadid


def Tanwin(serie):
  hrk = " َ ِ ُ"
  x = hrk.split(" ")
  hrk = "".join(x)
  
  mad = "ً ٍ ٌ"
  x = mad.split(" ")
  mad = "".join(x)
  
  serie_jadid = []
  for mot in serie:
    
    x = mot[4:].split(hrk[0])
    y = (mad[0]+'ا').join(x)
    x = y.split(hrk[1])
    y = (mad[1]).join(x)
    x = y.split(hrk[2])
    y = (mad[2]).join(x)
    y = mot[:4] + y
    
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
      if i == 3:
        mot2[i] = "ّ" + mot2[i]
      
    y = "".join(mot2)
    serie_jadid.append(y)
    
  return serie_jadid

#DONE Rajouer Al
#DONE Distinguer lunaire et solaire
def Taarif(serie):
  
  hourouf_shamsia = " ت ث د ذ ر ز س ش ص ض ط ظ ل ن"

  serie_jadid = []
  for mot in serie:  
    mot = 'ال'+ mot
    al_harf_al_awwal = mot[2]
    mot2 = []
    for i in range(len(mot)):
      mot2.append(mot[i])
      if (i == 3) and (al_harf_al_awwal in hourouf_shamsia):
        mot2[i] = "ّ" + mot2[i]
    

    y = "".join(mot2) 
    serie_jadid.append(y)
    
  return serie_jadid
