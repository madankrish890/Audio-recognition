import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
import os


def process_audio(filename, language='en-US'):
    transcriptions = []
    audio = AudioSegment.from_file(filename)
    chunks_length_ms = 8000
    chunks = make_chunks(audio, chunks_length_ms)

    # Create the 'chunked' directory if it doesn't exist
    os.makedirs("chunked", exist_ok=True)

    for i, chunk in enumerate(chunks):
        chunk_name = f"./chunked/{os.path.basename(filename)}_{i}.wav"
        chunk.export(chunk_name, format="wav")
        file = chunk_name
        r = sr.Recognizer()
        with sr.AudioFile(file) as source:
            audio_listened = r.listen(source)
            try:
                rec = r.recognize_google(audio_listened, language=language)
                transcriptions.append(rec)
            except sr.UnknownValueError:
                print("I don't recognize your audio")
            except sr.RequestError as e:
                print("Could not get the result. Check your internet connection.")

    return ' '.join(transcriptions)


def main():
    st.title("Audio Recognition")

    uploaded_file = st.file_uploader("Upload audio")
    language = st.selectbox("Select Language",
                            options=["en-US", "ta-IN", "te-IN", "hi-IN","fr-FR","kn-IN"])  # Add more languages if needed

    if uploaded_file is not None:
        audio_path = "./audio"
        with open(audio_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.audio(uploaded_file)

        if st.button("Transcribe Audio"):
            st.text("Transcribing Audio...")
            transcription = process_audio(audio_path, language)
            st.text("Transcription:")
            st.write(transcription)

    st.text("Note: Supported audio formats include WAV, MP3, OGG, FLAC, and more.")


if __name__ == "__main__":
    main()
