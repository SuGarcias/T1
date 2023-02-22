import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd     
from numpy.fft import fft

print("importado correctamente...") 

#LLEGIR :
x_r, fm = sf.read('so_exercici2.wav')

#Trobar freqüència del senyal:
plt.figure(0)
plt.xlabel('Hz')
magspec = plt.magnitude_spectrum(x_r, fm) 
fx = magspec[1][np.argmax(magspec[0])] 
print(f'Freqüència fonamental del senyal: {fx} Hz')
plt.show()

###
T= 2.5
L = int(fm * T) 
Tm=1/fm
t=Tm*np.arange(L)  
Tx=1/fx
Ls=int(fm*5*Tx)
sd.play(x_r, fm)

#5 primers períodes:
plt.figure(1)
plt.plot(t[0:Ls], x_r[0:Ls])
plt.xlabel('t en segons')
plt.title('5 periodes de la sinusoide')
plt.show()

#Transformada:
N=fm
X=fft(x_r[0: Ls], N)
k=np.arange(N)

plt.figure(2)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics



