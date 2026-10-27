import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

try:
    # 1. Conexión a MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["salud_mental_db"]
    collection = db["intenciones"]
    print("Conexión exitosa")
except:
    print("Conexión fallida")

# 2. Cargar datos en Pandas
documentos = list(
    collection.find(
        {},
        {"_id": 0, "categoria": 1, "num_patrones": 1, "num_respuestas": 1},
    )
)
df = pd.DataFrame(documentos)

# 3. Regresión Lineal Simple
X = df[["num_patrones"]]
y = df["num_respuestas"]

modelo = LinearRegression()
modelo.fit(X, y)
y_pred = modelo.predict(X)

# 4. Métricas
m = modelo.coef_[0]
b = modelo.intercept_
r2 = r2_score(y, y_pred)
mse = mean_squared_error(X,y)

print(f"Ecuación: Y = {m:.3f}X + {b:.3f}")
print(f"Coeficiente R2: {r2:.3f}")
print(f"El Error Cuadrático Medio (MSE) es: {mse}")

# 5. Visualización
plt.figure(figsize=(8, 4))
sns.scatterplot(
    data=df,
    x="num_patrones",
    y="num_respuestas",
    color="blue",
    label="Datos",
)
plt.plot(
    X,
    y_pred,
    color="red",
    label=f"Línea de Regresión (R2 = {r2:.2f})",
)
plt.title("Regresión Lineal: Patrones vs Respuestas")
plt.xlabel("Número de Patrones (Mensajes de Usuario)")
plt.ylabel("Número de Respuestas Configuradas")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()