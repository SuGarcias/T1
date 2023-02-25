import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd     
from numpy.fft import fft
import tkinter
from tkinter import ttk




audio = 'OASIS_dlb_mono.wav'
x_r, fm = sf.read(audio)
n_mostres = len(x_r)
print(f'''
    Del Fitxer {audio}: 
    - Freqüència de mostratge: {fm} Hz
    - Nombre de mostres: {n_mostres}
    ''')


T1 = 10                 #temps inici audio
L1 = int(fm * T1) 
T2 = 10.025             #25ms més endevant
L2 = int(fm*T2)
Tm=1/fm
t=Tm*np.arange(L1,L2)   #vector de temps des de L1 fins a L2

sd.play(x_r, fm)
plt.figure(0)
plt.plot(t,x_r[L1:L2])
plt.show()


N=fm
X=fft(x_r[L1: L2], N)
k=np.arange(N)

xdb = abs(20*np.log10(np.abs(X)/(max(np.abs(X)))))
fk =(k/N)*fm    

plt.figure(1)
plt.subplot(211)
plt.plot(fk/2, xdb)
plt.title(f'Transformada del senyal de Ls={L2-L1} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()




window = tkinter.Tk()
def close():
    window.quit()


L1 = ttk.Label(window, text = 'Cierra para dejar de escuchar la canción ', font='comic_sans')
L1.grid(column=0, row=1, padx=20, pady=20)

exit = ttk.Button(window, text='Close', command=close)
exit.grid(column=0, row=2, padx=15, pady=15)
window.mainloop()