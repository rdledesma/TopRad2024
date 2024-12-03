#importamos las librerias necesarias

import pandas as pd
import matplotlib.pyplot as plt

#cargamos en memoria el archivo que contiene nuestras series
df  = pd.read_csv('Datos/gwn_2020_1min_TST.csv')
df['timestamp'] = pd.to_datetime(df.timestamp)

plt.figure()
plt.plot(df.timestamp, df.GHI)
plt.show()


plt.figure()
plt.plot(df.CZ, df.GHI, '.', ms=0.2)
plt.grid(True)
plt.show()


extremeLimitGHI = 1361 * 1.2 * df.CZ**1.2 + 50

plt.figure()
plt.plot(df.CZ, df.GHI, '.', ms=0.2)
plt.plot(df.CZ, extremeLimitGHI)
plt.grid(True)
plt.show()




#df['f1_GHI'] = (df.GHI > -4) & (df.GHI< 1361 * 1.5 * df.CZ**1.2 + 100)



#extremeLimitGHI = 1361 * 1.2 * df.CTZ**1.2 + 50



#df['f1_DHI'] = (df.DHI > -4) & (df.DHI< 1361 * 0.95 * df.CTZ**1.2 + 50)
#df['f1_DNI'] = (df.DNI > -4) & (df.DNI < 1361 )

#df['f2_GHI'] = (df.GHI > -2) & (df.GHI< 1361 * 1.2 * df.CTZ**1.2 + 50)
#df['f2_GHI_adap'] = (df.GHI > -2) & (df.GHI< 1361* 0.91 * df.CTZ **1.2 + 10)

#df['f2_DHI'] = (df.DHI > -2) & (df.DHI< 1361 * 0.75 * df.CTZ**1.2 + 30)
#df['f2_DHI_adap'] = (df.DHI > -2) & (df.DHI< 1361* 0.5 * df.CTZ **1.2 + 30)


#df['f2_DNI'] = (df.DNI > -2) & (df.DNI< 1361 * 0.95 * df.CTZ**0.2 + 10)



#extremeLimitDHI = 1361* 0.75 * df.CTZ **1.2 + 30
#adaptedLimitDHI = 1361* 0.5 * df.CTZ **1.2 + 30
#extremeLimitDNI = 1361 * 0.95 * df.CTZ**0.2 + 10

