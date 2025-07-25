import streamlit as st
from gtts import gTTS
import io

st.title("SensiLoco")

texto = st.text_input("Escribe...")

if st.button("Reproducir"):
    if not texto.strip():
        st.warning("¡Tienes que escribir algo!")
    else:
        try:
            # Crear objeto de audio en memoria
            tts = gTTS(text=texto, lang='es')
            audio_buffer = io.BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)  # Volver al inicio del archivo

            st.audio(audio_buffer, format="audio/mp3")
            st.success("¡Listo!")
        except Exception as e:
            st.error(f"Uy, algo falló\nError: {str(e)}")
