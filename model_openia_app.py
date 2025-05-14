import streamlit as st
import openai
import os

# Usar la clave API desde los secretos
openai.api_key = st.secrets["OPENAI_API_KEY"]

client = openai

st.title("IA para recetas :3")

st.markdown(
    "Haz preguntas sobre qué recetas puedes realizar con ciertos ingredientes o también puedes pedir ideas de recetas. "
    "Toma en cuenta que la IA solo responde si la pregunta es relacionada al tema."
)

question = st.text_input("Escribe tu pregunta:")

prompt = (
    "Eres una IA experta en dar recetas de cocina con los ingredientes que te comentan que tienen, "
    "pero no puedes añadir ingredientes que no te mencionen. "
    "Además, das buenos consejos de salud para que lleven una buena nutrición. "
    "También sabes identificar en qué se agrupa cada alimento y por ende "
    "puedes aconsejar a la gente qué cantidad de cada comida puede comer. "
    "Si te preguntan sobre cualquier otro tema, responde: "
    "'No sé sobre eso, pero si quieres te puedo ayudar con una receta :)'"
)

if question:
    with st.spinner("Generando respuesta..."):
        response = client.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": question}
            ]
        )
        st.success("Respuesta:")
        st.markdown(response.choices[0].message["content"])

