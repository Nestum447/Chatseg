import streamlit as st

def chatbot_seguros(pregunta):
    seguros_info = {
        "cobertura": "Nuestra póliza cubre daños a terceros, accidentes personales y robo total.",
        "requisitos": "Para obtener un seguro, necesitas licencia de conducir, DUI y tarjeta de circulación.",
        "precio": "El costo varía según el vehículo y la cobertura. Contáctanos para una cotización.",
        "contacto": "Puedes llamarnos al 1234-5678 o escribirnos a contacto@aseguradora.com.",
    }

    return seguros_info.get(pregunta.lower(), "Lo siento, no tengo información sobre eso.")

# Interfaz en Streamlit
st.title("Chatbot de Seguros de Vehículos")
st.write("Escribe tu consulta sobre el seguro y presiona 'Enviar'.")

pregunta = st.text_input("Pregunta:", "")
if st.button("Enviar"):
    if pregunta.strip():
        respuesta = chatbot_seguros(pregunta)
        st.write("**Respuesta:**", respuesta)
    else:
        st.warning("Por favor, escribe una pregunta.")

