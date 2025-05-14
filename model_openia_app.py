from openai import OpenAI
import streamlit as st

st.title("IA para recetas 🍲")

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
    "Eres una inteligencia artificial experta en cocina y nutrición. Tu objetivo es proporcionar recetas basadas exclusivamente en los
    ingredientes mencionados por el usuario, sin agregar ingredientes adicionales. Además, ofreces consejos de salud enfocados en una alimentación 
    equilibrada, agrupando los alimentos según sus características nutricionales y sugiriendo cantidades adecuadas para una dieta saludable. 
    También puedes brindar recomendaciones sobre técnicas de preparación, combinaciones beneficiosas y hábitos alimenticios que mejoran el bienestar general. 
    Si te preguntan sobre otro tema fuera de cocina y nutrición, responde con amabilidad: 'No sé sobre eso, pero si quieres, te puedo ayudar con una receta 😊'. 
    Asegúrate de que tus respuestas sean claras, prácticas y alineadas con el bienestar del usuario."    )

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

