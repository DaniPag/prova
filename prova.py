import numpy as np

print('Hello world')
g=9.80665
pi=3.1415926
#s1, s2, s3, s4, s5
#Testo1[5],Testo2[5],Testo3[9],Testo4[9],Testo5[2],Testo6[2],Testo7[12]
#N è il numero massimo di righe e colonne delle matrici che si utilizzano
N=9
M=500
#Tmx è il numero massimo di valori del vettore delle portate immesse
#Tout è il numero massimo di valori del vettore calcolo continuità
Tmx=25000000
Tout=60000
Dim=500
print(Dim)
v=np.empty(shape= (N,N))
print(v[0])
i = 0
for i in range (N):
      v[i]=input()

print (v)