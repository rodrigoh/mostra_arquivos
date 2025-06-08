import streamlit as st
import pandas as pd
from json import loads

st.title('Upload de arquivo para leitura')

arquivo = st.file_uploader('Selecione um arquivo', type=['json', 'py', 'csv', 'jpg', ' png', 'mp3', 'mp4'])

if arquivo:
  match arquivo.type.split('/'):
    case 'text','csv':
      df = pd.read_csv(arquivo)
      st.dataframe(df)
    case 'text','x-python':
      st.code(arquivo.read().decode())
    case 'application','json':
      st.json(loads(arquivo.read()))
    case 'image',_:
      st.image(arquivo)
    case 'video','mp4':
      st.video(arquivo)
    case 'audio', _:
      st.audio(arquivo)
else:
  st.error('Ainda não tenho um arquivo para analisar')
