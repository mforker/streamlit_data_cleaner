import streamlit as st
st.set_page_config(page_title="Data Cleaner",layout="wide")
import pandas as pd

st.header("Data Stats")
st.subheader("This app describes data using python.", divider="rainbow")

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
        try:
            df = pd.read_csv(uploaded_file, encoding=encoding)
        
            
            sample = df.head(5)

            st.markdown('''-----''')

            st.write(f'First 5 rows of {uploaded_file.name}')
            st.dataframe(sample)

            col3,col4 = st.columns([0.4,0.6])
            
            with col3:
                st.write(f'Data Summary')
                st.dataframe(df.describe(), height=350)
                
            with col4:
                st.write("NA Values in each Column:")
                na_df = pd.DataFrame(df.isna().sum())
                print(na_df.columns)
                st.dataframe(na_df, height=350)

            a = pd.DataFrame(
                {
                    'columns name' : df.columns.to_list(), 
                    'default data types': df.dtypes,
                    'data types': None
                }
            )
            col5, col6 = st.columns(2)
            with col5:
                st.write('Select Datatypes')
                ed= st.data_editor(a, column_config={
                    'data types': st.column_config.SelectboxColumn(
                        "select Data Type to convert",
                        help="Select the data type of the column",
                        width="medium",
                        options = ['int','str','float','bool','object'],
                        required= False,
                        disabled=False
                    ),
                    'default data types' : st.column_config.Column(disabled=True),
                    'columns name': st.column_config.Column(disabled=True)
                }, hide_index= True)
            with col6:
                st.markdown(f'''\n \n''')
                if st.button('Convert Datatypes', use_container_width=True):
                    for col, def_typ, typ in zip(ed['columns name'],ed['default data types'],ed['data types']):
                        if typ is not None:
                            if typ in ['int','float']:
                                try:
                                    df[col] = df[col].str.replace('$','').str.replace('₹','').str.replace(',','').str.replace(' ','').str.strip().astype(typ)
                                except ValueError:
                                    st.warning(f'can not convert {col} to {typ} try converting to a valid type')
                                # st.dataframe(df[col])                        
                            else:
                                df[col] = df[col].astype(typ)
                    
                    st.write('Updated datatypes:')
                    st.dataframe(df.dtypes)   

        except UnicodeDecodeError:
            st.warning('Unable to read the csv. Try changing the encoding type')            
           





