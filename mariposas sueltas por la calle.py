import streamlit as st
from gtts import gTTS
import tempfile

st.title("SensiLoco")

texto = st.text_input("Escribe...")

if st.button("Reproducir"):
    if not texto.strip():
        st.warning("¡Tienes que escribir algo!")
    else:
        try:
            # Crear archivo temporal
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tf:
                tts = gTTS(text=texto, lang='es')
                tts.save(tf.name)

                # Leer el audio generado
                audio_bytes = tf.read()

            st.audio(audio_bytes, format="audio/mp3")
            st.success("¡Listo!")
        except Exception as e:
            st.error(f"Uy, algo falló\nError: {str(e)}")
