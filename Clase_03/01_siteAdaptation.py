import pandas as pd
import matplotlib.pyplot as plt

d = pd.read_csv('Clase_03/data/measured.csv')
d['date'] = pd.to_datetime(d.date)


plt.figure()
plt.title("Set de datos original")
plt.plot(d.date, d.ghi)

dTrain = d[d.date.dt.year == 2016]
dTest = d[d.date.dt.year > 2016]


plt.figure()
plt.title("Set de datos de entrenamiento y testeo")
plt.plot(dTrain.date, dTrain.ghi, label="Train")
plt.plot(dTest.date, dTest.ghi, label="Test")
plt.legend(True)
plt.show()



dTrain.to_csv('Clase_03/data/train.csv', index=False)
dTest.to_csv('Clase_03/data/test.csv', index=False)




