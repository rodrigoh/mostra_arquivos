import streamlit as st
from json import loads
import pandas as pd


st.title('Aplicativo para exibir diferentes arquivos')

st.markdown(':smirk:')

arquivo = st.file_uploader(
  'Escolha um arquivo que vou tentar ler',
  type=['png','jpg','csv','mp3','py','json', 'mp4'])
if arquivo:
  match arquivo.type.split('/'):
    case 'application','json':
      st.json(loads(arquivo.read()))
    case 'image',_:
      st.image(arquivo.read(),width=200)
    case 'text','csv':
      df = pd.read_csv(arquivo)
      st.dataframe(df)
    case 'text','x-python':
      st.code(arquivo.read().decode)
    case 'audio', _:
      st.audio(arquivo)
    case 'video', _:
      st.video(arquivo)
else:
  st.error('Ainda não tenho arquivo')
