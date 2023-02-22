import ogv_exercici2 as ex2
print(ex2.fx)

xdb = ex2.np.log10(ex2.np.abs(ex2.X)/(max(ex2.np.abs(ex2.X))))
fk =(ex2.k/ex2.N)*ex2.fm
ex2.plt.figure(0)
ex2.plt.plot(fk, xdb)
ex2.plt.show()