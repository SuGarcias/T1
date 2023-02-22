import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
print("importado correctamente...") 

#CREAR i GUARDAR un fitxer amb un senyal sinusoidal:
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx1=4000
fx2=1500                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x1 = A * np.cos(2 * pi * fx1 * t)      # Senyal sinusoidal
x2 = A * np.cos(2 * pi * fx2 * t)  
sf.write('so_exercici1.wav', x1, fm)   # Escriptura del senyal a un fitxer en format 
sf.write('so_exercici2.wav', x2, fm)

#REPRESENTAR 5 períodes:
Tx1=1/fx1
Tx2=1/fx2                                   # Període del senyal
Ls1=int(fm*5*Tx1)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide
Ls2=int(fm*5*Tx2)

sd.play(x1, fm)                # Reproducció d'àudio
plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls1], x1[0:Ls1])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 

sd.play(x2, fm)
plt.figure(1)                             # Nova figura
plt.plot(t[0:Ls2], x2[0:Ls2])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 





#DOMINI TRANSFROMAT: 
from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X1=fft(x1[0 : Ls1], N)           # Càlcul de la transformada de 5 períodes de la sinusoide
X2=fft(x2[0: Ls2], N)

#REPRESENTAR MÒDUL I FASE:
k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(2)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X1))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls1} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X1)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics

plt.figure(3)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X2))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls2} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X2)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics
