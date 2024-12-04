import pandas as pd
import joblib
import matplotlib.pyplot as plt

dTest = pd.read_csv('Clase_03/data/test.csv')
modeloSLR = joblib.load('Clase_03/slr.pkl')



X = dTest.GHIcams.values.reshape(-1,1)

dTest['ghiAdaptedSLR'] = modeloSLR.predict(X)


##Calculo de las métricas de desempeño

MBEcams = ((dTest.GHIcams- dTest.ghi).sum() / len(dTest.ghi))
rMBEcams = MBEcams/ dTest.ghi.mean() * 100

RMSEcams = (((((dTest.GHIcams- dTest.ghi)**2).sum()) / len(dTest.ghi)) ** 0.5) 
rRMSEcams= RMSEcams/ dTest.ghi.mean() * 100



print(f"rMBECams: {rMBEcams}%")
print(f"rRMSECams: {rRMSEcams}%")


##Calculo de las métricas de desempeño de los adaptados

MBEslr = ((dTest.ghiAdaptedSLR- dTest.ghi).sum() / len(dTest.ghi))
rMBEslr = MBEslr/ dTest.ghi.mean() * 100

RMSEslr = (((((dTest.ghiAdaptedSLR - dTest.ghi)**2).sum()) / len(dTest.ghi)) ** 0.5) 
rRMSEslr= RMSEslr/ dTest.ghi.mean() * 100



print(f"rMBECams: {rMBEslr}%")
print(f"rRMSECams: {rRMSEslr}%")
