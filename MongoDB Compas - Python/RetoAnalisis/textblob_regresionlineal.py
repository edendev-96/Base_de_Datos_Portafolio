import matplotlib.pyplot as plt
import pandas as pd
import pymongo
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from textblob import TextBlob

# 1. Conexión a la base de datos NoSQL
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["salud_mental_db"]
collection = db["intenciones"]

# 2. Extracción y Transformación: Cualitativo -> Cuantitativo (PLN)
data = []
for doc in collection.find():
    patrones = doc.get("patrones", [])
    respuestas = doc.get("respuestas", [])

    if patrones and respuestas:
        # Unir los mensajes del usuario para analizar el sentimiento global
        texto_usuario = " ".join(patrones)

        # Extracción de características (Feature Extraction con TextBlob)
        # polaridad: -1.0 (muy negativo) a +1.0 (muy positivo)
        sentimiento = TextBlob(texto_usuario).sentiment.polarity

        # Longitud media de respuesta del bot
        avg_len_respuesta = sum(len(r) for r in respuestas) / len(respuestas)

        data.append({
            "categoria": doc.get("categoria", "N/A"),
            "polaridad_usuario_x": sentimiento,
            "longitud_respuesta_bot_y": avg_len_respuesta,
        })

df = pd.DataFrame(data)

# 3. Entrenamiento del Modelo de Regresión Lineal
X = df[["polaridad_usuario_x"]]
y = df["longitud_respuesta_bot_y"]

modelo = LinearRegression()
modelo.fit(X, y)
y_pred = modelo.predict(X)

# 4. Cálculo de Métricas Evaluativas
m = modelo.coef_[0]
b = modelo.intercept_
r2 = r2_score(y, y_pred)

print(f"Ecuación de la Recta: Y = {m:.3f}X + {b:.3f}")
print(f"Coeficiente de Determinación (R2): {r2:.4f}")

# 5. Visualización de Resultados
plt.figure(figsize=(9, 5))
sns.scatterplot(
    data=df,
    x="polaridad_usuario_x",
    y="longitud_respuesta_bot_y",
    color="purple",
    alpha=0.7,
    s=60,
    label="Intenciones",
)
plt.plot(
    X,
    y_pred,
    color="red",
    linewidth=2,
    label=f"Línea de Tendencia (R2 = {r2:.3f})",
)
plt.title("Reto PLN: Carga Emocional del Usuario vs. Extensión de Respuesta del Bot")
plt.xlabel("Polaridad del Mensaje del Usuario (-1: Negativo/Estrés, +1: Positivo)")
plt.ylabel("Longitud Promedio de Respuesta del Bot (Caracteres)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()