import pandas as pd
import matplotlib.pyplot as plt # Esto es una libreria de visulizavion grafica
import seaborn as sns # Libreria de graficos estadisticos

df = pd.read_csv("archivos_problemas_graficos\\pedos.csv")
sns.lineplot(x="fecha",y="pedos",data=df) # Crea un grafico
plt.plot("01-04",12,"o") #Crea un punto
plt.show()