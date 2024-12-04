import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression



d = pd.read_csv('Clase_03/data/train.csv')



plt.figure()
plt.title(r"$GHI_{medida} $ vs $ GHI_{cams}$")
plt.plot(d.ghi, d.GHIcams, '.')



plt.figure()
plt.title(r"$GHI_{medida} $ vs $ GHI_{cams}$")
plt.plot(d.ghi, d.GHIcams, '.')
plt.plot([x for x in range(0, 1500)])


#calculo la ecuacion para la linea de tendencia
z = np.polyfit(  d.ghi,d.GHIcams,1)
p = np.poly1d(z)

# zAdap = np.polyfit(df.GHISatAdap,df.GHI, 1)
# pAdap = np.poly1d(zAdap)

#add trendline to plot
plt.figure()
plt.plot(d.ghi, d.GHIcams, '.' ,label=r"$GHI_{medida} $ vs $ GHI_{cams}$")
plt.plot([x for x in range(0, 1500)])
plt.plot([x for x in range(0,1500)], p([x for x in range(0,1500)]),label="linea de tendencia", c="r",)
plt.legend()
plt.grid(True)
plt.show()

"""
Vamos a cómo de desempeña el modelo Heliosat-4, que es modesaw+|
lo de 
toda condición de cielo de CAMS
"""



##Calculo de las métricas de desempeño

MBEcams = ((d.GHIcams- d.ghi).sum() / len(d.ghi))
rMBEcams = MBEcams/ d.ghi.mean() * 100

RMSEcams = (((((d.GHIcams- d.ghi)**2).sum()) / len(d.ghi)) ** 0.5) 
rRMSEcams= RMSEcams/ d.ghi.mean() * 100


#rMAD =  (abs(d.GHIcams - d.ghi).sum() / len(d.ghi)) / d.ghi.mean() * 100



print(f"rMBECams: {rMBEcams}%")
print(f"rRMSECams: {rRMSEcams}%")



varsRegs = ['GHIcamscc', 'GHIcams',
              'tco3', 'tcwv']

X = d[varsRegs]
y = d.ghi.values.reshape(-1,1)

modeloMLR = LinearRegression().fit(X,y)


print('coef: ', modeloMLR.coef_[0]) 
print('inters: ', modeloMLR.intercept_) 




##esto es aquivalente a:
d['ghiAdaptadaMLR'] = modeloMLR.predict(X)


plt.figure()
plt.plot(d.ghi, label=r"$GHI_{medida}$")
plt.plot(d.GHIcams, label=r"$GHI_{cams}$")
plt.plot(d.ghiAdaptadaMLR , label=r"$GHI_{adaptadaMLR}$")
plt.legend()
plt.show()




#calculo la ecuacion para la linea de tendencia para los datos ajustados
zAdaptada = np.polyfit(  d.ghi, d.ghiAdaptadaMLR,1)
pAdaptada = np.poly1d(zAdaptada)


## solo ploteo las lineas de tendencia
plt.figure("Lineas de tendencia")
plt.plot([x for x in range(0, 1500)], label="linea y=x", c="g",)
plt.plot([x for x in range(0,1500)], p([x for x in range(0,1500)]),label="linea de tendencia cams", c="r",)
plt.plot([x for x in range(0,1500)], pAdaptada([x for x in range(0,1500)]),label="linea de tendencia adaptada", c="b",)
plt.legend()
plt.show()





#ploteo en conjunto
plt.figure()
plt.plot(d.ghi, d.GHIcams, '.' ,label=r"$GHI_{medida} $ vs $ GHI_{cams}$")
plt.plot(d.ghi, d.ghiAdaptadaMLR, '.' ,label=r"$GHI_{medida} $ vs $ GHI_{Adaptada}$")
plt.plot([x for x in range(0, 1500)], label="linea y=x", c="g",)
plt.plot([x for x in range(0,1500)], p([x for x in range(0,1500)]),label="linea de tendencia cams", c="r",)
plt.plot([x for x in range(0,1500)], pAdaptada([x for x in range(0,1500)]),label="linea de tendencia adaptada", c="b",)
plt.legend()
plt.grid(True)
plt.show()




##Calculo de las métricas de desempeño

MBEadaptado  = ((d.ghiAdaptadaMLR - d.ghi).sum() / len(d.ghi))
rMBEadaptado = MBEadaptado/ d.ghi.mean() * 100

RMSEadaptado = (((((d.ghiAdaptadaMLR - d.ghi)**2).sum()) / len(d.ghi)) ** 0.5) 
rRMSEadaptado = RMSEadaptado/ d.ghi.mean() * 100


#rMAD =  (abs(d.GHIcams - d.ghi).sum() / len(d.ghi)) / d.ghi.mean() * 100



print(f"rMBECams: {rMBEcams}%")
print(f"rMBEAdaptado: {rMBEadaptado}%")

print(f"rRMSECams: {rRMSEcams}%")
print(f"rRMSEAdaptado: {rRMSEadaptado}%")

import joblib 
joblib.dump(modeloMLR, 'Clase_03/MLR.pkl')





