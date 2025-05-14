from openai import OpenAI
import streamlit as st

st.title("IA para recetas :3")

st.markdown("""
Haz preguntas sobre qué recetas puedes realizar con ciertos ingredientes,
o también puedes pedir ideas de recetas.

**Nota:** La IA solo responde si la pregunta es relacionada al tema.
""")

api_key = st.text_input("Introduce tu OpenAI API Key:", type="password")

if api_key:
    client = OpenAI(api_key=api_key)  # así se usa desde v1.0+

    question = st.text_input("Escribe tu pregunta:")

    prompt = (
    "Eres una IA experta en dar recetas de cocina con los ingredientes que te mencionan. "
    "No puedes añadir ingredientes que no se mencionen. "
    "Además, das buenos consejos de salud para una buena nutrición. "
    "También sabes agrupar los alimentos y aconsejar sobre cantidades adecuadas. "
    "Si te preguntan sobre otro tema, responde: 'No sé sobre eso, pero si quieres te puedo ayudar con una receta :)'"
    )

    if question:
        with st.spinner("Generando respuesta..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": question}
                ]
            )
            st.success("Respuesta:")
            st.markdown(response.choices[0].message.content)

