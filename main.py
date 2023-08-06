import streamlit as st
import pandas as pd
from io import StringIO
import numpy as np


def streamlit_run():
    st.title('DUGAROV HOMEWORK BLOCK 1')
    uploaded_file = st.file_uploader("Choose a CSV file", type='csv')
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        #st.write(dataframe)
        column1 = st.selectbox(
            'Choose column 1',
            dataframe.columns)
        column2 = st.selectbox(
            'Choose column 2',
            dataframe.columns)




if __name__ == '__main__':
    streamlit_run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
