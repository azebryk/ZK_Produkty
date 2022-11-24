import pandas as pd
import streamlit as st
import tabula
from tabula import read_pdf

#encoding
import sys
sys.stdout.reconfigure(encoding='latin2')
sys.stdin.reconfigure(encoding='latin2')

@st.cache
def convert_df_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('latin2')


st.header('Menu ZK sprawdzam polskie znaki śćśłż')


# Upload File
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = read_pdf(uploaded_file, encoding='latin2', pages='all', pandas_options={'header': None})
    st.write(pd.DataFrame(df[0]))
    df_1 = pd.DataFrame(df[0])
    output_df = convert_df_to_csv(df_1)


    # Downlaod File

    st.download_button(
    label="Download data as CSV",
    data=output_df,
    file_name='out.csv',
    mime='text/csv',
    )