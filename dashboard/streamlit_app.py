
import streamlit as st
import requests
from PIL import Image
import io


st.set_page_config(page_title="Toll Validation Demo", layout='wide')
st.title("Tolling Transaction Validation - Demo")


IMG_SERVICE = st.sidebar.text_input('Image ingestion URL', 'http://image_ingestion:80/ingest')
OCR_SERVICE = st.sidebar.text_input('OCR URL (for debug)', 'http://ocr_service:80/ocr')
VALIDATE_URL = st.sidebar.text_input('Validation URL', 'http://validation_service:80/validate')
CLASSIFY_URL = st.sidebar.text_input('Classification URL', 'http://classification_service:80/classify')


st.markdown("### Submit a sample plate or upload an image (demo)")
col1, col2 = st.columns(2)
with col1:
plate_text = st.text_input('Plate text (quick demo, e.g. ABC123)')
if st.button('Process plate'):
# call ingestion with plate_text
resp = requests.post(IMG_SERVICE, data={'plate_text': plate_text})
st.write('Ingest')
