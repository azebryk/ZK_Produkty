import pandas as pd
import streamlit as st
import tabula
from tabula import read_pdf

# encoding
import sys

sys.stdout.reconfigure(encoding='latin2')
sys.stdin.reconfigure(encoding='latin2')


@st.cache
def convert_df_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('latin2')


def reapir_encoding(x):
    y = x.encode(encoting='utf-8').decode(encoting='latin-1')

def one_columns_convert(file_name):
    df = read_pdf(file_name, encoding='latin2', pages='all', pandas_options={'header': None})
    df_full = pd.DataFrame(df[0])
    for i in range(1, len(df)):
        df_temp = pd.DataFrame(df[i])
        df_full = df_full.append(df_temp)
    return df_full

def zareba_convert(file_name):
    df = read_pdf(file_name, encoding='latin2', pages='1', pandas_options={'header': None},
                  area=[90, 31, 828, 576], guess=False)
    df_full = pd.DataFrame(df[0])
    df = read_pdf(file_name, encoding='latin2', pages='all', pandas_options={'header': None})
    for i in range(1, len(df)):
        df_temp = pd.DataFrame(df[i])
        df_full = df_full.append(df_temp)
    return df_full

def bemowo_convert(file_name):
    # Lewa kolumna
    df = read_pdf(file_name, encoding='latin2', pages='all', pandas_options={'header': None},
                  area=[30, 0, 828, 300], guess=False)
    pages = len(df)
    df_full = pd.DataFrame(df[0])
    # Prawa kolumna
    df_temp = read_pdf(file_name, encoding='latin2', pages='1', pandas_options={'header': None},
                       area=[30, 310, 828, 593], guess=False)
    df_full = df_full.append(df_temp)

    for page in range(2, pages + 1):
        df_temp_l = read_pdf(file_name, encoding='latin2', pages=page, pandas_options={'header': None},
                             area=[30, 0, 828, 300], guess=False)
        df_temp_p = read_pdf(file_name, encoding='latin2', pages=page, pandas_options={'header': None},
                             area=[30, 310, 828, 593], guess=False)
        df_full = df_full.append(df_temp_l).append(df_temp_p)
    return df_full

def glogow_convert(file_name):
    # Lewa kolumna
    df = read_pdf(file_name, encoding='latin2', pages='all', pandas_options={'header': None},
                  area=[30, 0, 828, 295], guess=False)
    pages = len(df)
    df_full = pd.DataFrame(df[0])
    # Prawa kolumna
    df_temp = read_pdf(file_name, encoding='latin2', pages='1', pandas_options={'header': None},
                       area=[30, 297, 828, 593], guess=False)
    df_full = df_full.append(df_temp)
    for page in range(2, pages + 1):
        df_temp_l = read_pdf(file_name, encoding='latin2', pages=page, pandas_options={'header': None},
                             area=[30, 0, 828, 295], guess=False)
        df_temp_p = read_pdf(file_name, encoding='latin2', pages=page, pandas_options={'header': None},
                             area=[30, 297, 828, 593], guess=False)
        df_full = df_full.append(df_temp_l).append(df_temp_p)
    return df_full


def strzelin_convert(file_name):
    # Lewa kolumna
    df = read_pdf(file_name, encoding='latin2', pages='all', pandas_options={'header': None},
                  area=[30, 0, 828, 295], guess=False)
    pages = len(df)
    df_full = pd.DataFrame(df[0])
    # Prawa kolumna
    df_temp = read_pdf(file_name, encoding='latin2', pages='1', pandas_options={'header': None},
                       area=[30, 300, 828, 593], guess=False)
    df_full = df_full.append(df_temp)
    for page in range(2, pages + 1):
        df_temp_l = read_pdf(file_name, encoding='latin2', pages=page, pandas_options={'header': None},
                             area=[30, 0, 828, 295], guess=False)
        df_temp_p = read_pdf(file_name, encoding='latin2', pages=page, pandas_options={'header': None},
                             area=[30, 300, 828, 593], guess=False)
        df_full = df_full.append(df_temp_l).append(df_temp_p)
    return df_full


def jaslo_convert(file_name):
    df = read_pdf(file_name, encoding='latin2', pages='all', pandas_options={'header': None})
    # df = read_pdf(file_name, encoding='latin2', pages=page, pandas_options={'header': None},
    #                        area=[39, 21, 792, 576], guess=False)
    pages = len(df)
    df_full = pd.DataFrame(df[0])
    for page in range(2, pages + 1):
        df_temp = read_pdf(file_name, encoding='latin2', pages=page, pandas_options={'header': None},
                           area=[39, 21, 792, 576], guess=False)
        df_full = df_full.append(df_temp)
    df_full = df_full.dropna(axis=1, how='all')
    df_final = pd.DataFrame(df_full.to_numpy().reshape(-1, 3))
    return df_final




jedna = ['Jelenia Góra', 'Poznań', 'Inowrocław', 'Włocławek']

### Do Dodanie  1:   'Zaręba'   3:     'Sieradz', 'Jasło', 'Rzeszów', 'Wejherowo'
st.header('ZK Produkty')
zaklad = st.selectbox("Wybierz zakład:", ['Jelenia Góra', 'Poznań', 'Inowrocław', 'Włocławek', 'Zaręba',
                                               'Bemowo', 'Głogów', 'Strzelin',
                                               'Jasło'])

# Upload File
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    if zaklad in jedna:
        df = one_columns_convert(uploaded_file)
        st.write(df)
        output_df = convert_df_to_csv(df)
    elif zaklad == 'Zaręba':
        df = zareba_convert(uploaded_file)
        st.write(df)
        output_df = convert_df_to_csv(df)
    elif zaklad == 'Bemowo':
        df = bemowo_convert(uploaded_file)
        st.write(df)
        output_df = convert_df_to_csv(df)
    elif zaklad == 'Głogów':
        df = glogow_convert(uploaded_file)
        st.write(df)
        output_df = convert_df_to_csv(df)
    elif zaklad == 'Strzelin':
        df = glogow_convert(uploaded_file)
        st.write(df)
        output_df = convert_df_to_csv(df)
    elif zaklad == 'Jasło':
        df = jaslo_convert(uploaded_file)
        st.write(df)
        output_df = convert_df_to_csv(df)

    else:
        st.write('To nie jednokolumnowe')

    st.download_button(
        label="Download data as CSV",
        data=output_df,
        file_name='out.csv',
        mime='text/csv',
    )




# # Stara wersja
# if uploaded_file is not None:
#     st.write(uploaded_file.name)
#     file_name =
# df = read_pdf(uploaded_file, encoding='latin2', pages='all', pandas_options={'header': None})
# st.write(pd.DataFrame(df[0]))
# df_1 = pd.DataFrame(df[0])
# output_df = convert_df_to_csv(df_1)
#
# # Downlaod File
#
# st.download_button(
#     label="Download data as CSV",
#     data=output_df,
#     file_name='out.csv',
#     mime='text/csv',
# )
