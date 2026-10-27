import pandas as pd
import json

# 1. Cargar el archivo original
df = pd.read_csv("Conversaciones_chatbot.Salud_mental.csv")
row = df.iloc[0]

intents_limpios = []

# Iterar sobre las 80 intenciones identificadas
for i in range(80):
    tag_col = f"intents[{i}].tag"
    if tag_col in row and pd.notna(row[tag_col]):
        tag = str(row[tag_col])

        # Extraer patrones (mensajes de usuario)
        patterns = [
            str(row[c])
            for c in df.columns
            if f"intents[{i}].patterns" in c and pd.notna(row[c])
        ]

        # Extraer respuestas del bot
        responses = [
            str(row[c])
            for c in df.columns
            if f"intents[{i}].responses" in c and pd.notna(row[c])
        ]

        intents_limpios.append({
            "intent_id": i + 1,
            "categoria": tag,
            "num_patrones": len(patterns),
            "num_respuestas": len(responses),
            "patrones": patterns,
            "respuestas": responses,
        })

# 2. Guardar el archivo JSON formateado
with open("salud_mental_limpio.json", "w", encoding="utf-8") as f:
    json.dump(intents_limpios, f, indent=2, ensure_ascii=False)

print(f"Procesadas {len(intents_limpios)} categorias con exito.")