import streamlit as st
st.set_page_config(page_title="Data Cleaner",layout="wide")
import pandas as pd

st.header("Data Cleaner")
st.subheader("This app cleans data using python.", divider="rainbow")

col1,col2 = st.columns([0.3,0.7])

with col1:
    encoding = st.selectbox("Choose File Encoding",[
    "utf-8",
    "latin-1",
    "cp1252",
    "windows-1252",
    "iso-8859-1",
    "macroman",
    "ascii",
    "gbk",
    "big5",
    "cp936"
])
with col2:
    uploaded_file = st.file_uploader("Upload your file", accept_multiple_files=False, type=["csv"])

with st.container():
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, encoding=encoding)
        sample = df.head(5)

        st.markdown('''-----''')

        col3,col4 = st.columns([0.4,0.6])
        
        with col3:
            st.write(f'First 5 rows of {uploaded_file.name}')
            st.dataframe(sample)
        with col4:
            st.write(f'Data Summary')
            st.write(df.describe())
        st.write("NA Values in each Column:")
        st.write(df.isna().sum())
                    
           


    elif uploaded_file is None:
        st.error("Upload a valid file")





