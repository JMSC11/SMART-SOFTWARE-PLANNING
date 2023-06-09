import numpy as np
import pandas as pd
import pickle
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import matplotlib as mpl
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

mpl.use("Qt5Cairo")


"""# Cargar el archivo xlsx en un DataFrame
data = pd.read_excel('Tabla_PrimerOrdenJones_Planeac_Esf_20230518.xlsx', sheet_name='Hoja1')  

# Extraer los datos del DataFrame como un arreglo NumPy
datos = data.to_numpy()"""

datos = np.loadtxt("./planeacion_jones")

# Seleccionar columnas específicas del arreglo
#idx = np.r_[0:2, :]
X = datos[:, 0:2]

y = datos[:, -2:]
#y = y[:, :]
# Divide nuestros puntos totales, de manera que el 20% serán
# puntos de prueba, y el 80% puntos de entrenamiento.
#datasets = train_test_split(X, y, test_size=0.2)
datasets = train_test_split(X, y, test_size=0.2, random_state=42)
train_X, test_X, train_y, test_y = datasets

train_y = np.array(train_y)
test_y = np.array(test_y)



mlp = MLPRegressor(hidden_layer_sizes=(2,2),
                   solver='adam', tol=1e-15,
                   learning_rate='adaptive',
                   max_iter=200000,
                   activation='logistic')

mlp.fit(train_X, train_y)

y_pred = mlp.predict(test_X)

nombreArchivo = 'mlp_driver.drv'
pickle.dump(mlp, open(nombreArchivo, 'wb'))

test_y = mlp.predict(X)

if test_y.shape != y_pred.shape:
    print("Algo anda mal")
    test_y = test_y.reshape(y_pred.shape)
mse = mean_squared_error(test_y, y_pred)

print("Error cuadrático medio:", mse)


"""inicio = 350
fin = 750
diff = fin-inicio + 1

tiempo = np.linspace(inicio, fin, diff)

fig, ax = plt.subplots()
ax.plot(tiempo, test_y[inicio:fin+1], 'ro',  tiempo, y[inicio:fin+1], 'bo')
plt.show()"""