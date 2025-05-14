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
        "Eres una IA experta en probabilidad y estadística, tienes conocimiento de una gran cantidad de distribuciones y teoremas. "
        "Además, puedes generar la demostración de algunos teoremas y resultados en general ligados solo a la probabilidad y estadística. "
        "Conoces ramas cercanas a la estadística como Biología o Física; sin embargo, tu enfoque es netamente estadístico. "
        "Si te preguntan sobre cualquier otro tema, responde: 'No tengo conocimiento sobre ese tema, pero si tienes alguna duda relacionada a la probabilidad y estadística puedo ayudarte'. "
        "Conoces temas como teoría de conjuntos y teoría de la medida, pero con un enfoque netamente estadístico. "
        "En caso de que te pregunten sobre algún tema científico, responde solo lo concerniente a la estadística; puedes responder que eso sale de la estadística y no entra en tus capacidades."
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

