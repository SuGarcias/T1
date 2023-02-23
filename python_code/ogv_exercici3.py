import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd     
from numpy.fft import fft

x_r, fm = sf.read('so_exercici2.wav')

plt.figure(0)
plt.xlabel('Hz')
magspec = plt.magnitude_spectrum(x_r, fm) 
fx = magspec[1][np.argmax(magspec[0])] 
print(f'Freqüència fonamental del senyal: {fx} Hz')
plt.show()

T= 2.5
L = int(fm * T) 
Tm=1/fm
t=Tm*np.arange(L)  
Tx=1/fx
Ls=int(fm*5*Tx)
N=fm
X=fft(x_r[0: Ls], N)
k=np.arange(N)

xdb = 20*np.log10(np.abs(X)/(max(np.abs(X))))
fk =(k/N)*fm    

plt.figure(1)
plt.plot(fk/2, xdb)
plt.show()