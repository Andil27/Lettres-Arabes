from kitaba import *

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
C18 = [18, alph, H9]




CC = [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18]
