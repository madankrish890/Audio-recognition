import whisper
import streamlit as st
import subprocess

# def download_audio(video_url, output_path):
#     command = f"yt-dlp {video_url} --extract-audio --audio-format mp3 --output {output_path}"
#     try:
#         subprocess.call(command, shell=True)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# video_url = 'https://youtu.be/fgdIkPXMNyA'
# output_path = r"eng1.mp3"
# download_audio(video_url, output_path)

# input_file=r"C:\Users\lenovo\PycharmProjects\whisper\eng1.wav"
# whisper_model='medium'
# model = whisper.load_model(whisper_model)
#
# transcript = model.transcribe(input_file)
#
# text = transcript["text"]
#
# print(text)

# Output
# Good morning. I'm Christine Romans. It's Tuesday, November 1st. Here are this morning's headlines.
# Republican presidential candidate Herman Cain now changing his story, saying he was aware of an agreement with one woman.
# He says he's trying to think back on the sexual harassment claims from the early 1990s.
# The Northeast power outage could last for days. More than one million homes are still without power.
# The freak October storm blamed for at least 13 deaths. The government wants answers.
# An investigation now underway after JetBlue left travelers stranded on the tarmac at the wrong airport for more than seven hours.
# Libya's transitional government names a new acting prime minister. U.S. educated engineer Abdurahm al-
# Kaib is promising to improve human rights and respect international law. Will Conrad Murray take the stand in his own defense?
# We're waiting on a bombshell decision in the trial of Michael Jackson's doctor. A rough day on Wall Street,
# the Dow plunging more than 200 points, but that shouldn't take away from a stellar month as the Dow ended up 10%. Goodbye debit card fees,
# SunTrust and Regions Bank, the latest to reverse the controversial $5 monthly charge. That leaves Bank of America as the only major bank to still keep the fees.
# In just 72 days after their made-for-TV dream wedding, Kim Kardashian and Chris Humphries calling it quits, the reality star announced the split, citing irreconcilable differences.
# Those are the headlines. Be sure to watch American Morning every weekday starting at 6 a.m. Eastern. Have a great day.

from pydub import AudioSegment

st.title('Audio Recognition')

audio_file = st.file_uploader("Upload audio")

model = whisper.load_model("base")

if st.sidebar.button('Transcribe Audio'):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")

        audio = AudioSegment.from_file(audio_file)
        audio = audio.set_frame_rate(16000)
        audio = audio.set_channels(1)
        audio_file_path = "./temp.wav"
        audio.export(audio_file_path, format="wav")

        transcription = model.transcribe(audio_file_path)
        st.sidebar.success("Transcription complete")
        st.write(transcription['text'])
    else:
        st.sidebar.error('Please upload an audio file')

st.sidebar.header("Play audio file")
st.sidebar.audio(audio_file)