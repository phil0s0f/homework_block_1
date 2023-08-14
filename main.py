import streamlit as st
import pandas as pd
import plotly.express as px
from scipy import stats


def load_data(file):
    try:
        dataframe = pd.read_csv(file)
        return dataframe
    except Exception as e:
        st.error(f"Error: {e}")
        return None


def plotting(dataframe, column):
    distribution_df = dataframe.dropna(subset=column)
    if (distribution_df[column].dtypes != 'object') and (distribution_df[column].dtypes != 'string'):
        st.bar_chart(distribution_df[column].value_counts().nlargest(15), use_container_width=True)
    else:
        subdataframe = distribution_df[column].value_counts().nlargest(15).rename_axis('unique_values').reset_index(
            name='counts')
        fig = px.pie(subdataframe, values='counts', names='unique_values', title='Pie ' + column)
        st.plotly_chart(fig, use_container_width=True)


def hypothesis_test(dataframe, column1, column2, test):
    st.subheader("Hypothesis test")
    if test == "t-test":
        if (dataframe[column1].dtypes != 'object') and (
                dataframe[column1].dtypes != 'string') and (dataframe[column2].dtypes != 'object') and (
                dataframe[column2].dtypes != 'string'):
            stat, p_value = stats.ttest_ind(dataframe[column1], dataframe[column2])
            st.write(f"t-test: statistic={stat:.6f}, p-value={p_value:.6f}")
        else:
            st.write(f"Wrong data types")
    else:
        if (dataframe[column1].dtypes != 'object') and (
                dataframe[column1].dtypes != 'string') and (dataframe[column2].dtypes != 'object') and (
                dataframe[column2].dtypes != 'string'):
            # results = stats.mannwhitneyu(dataframe[column1], dataframe[column2])
            # st.write(f"Mann-Whitney U Test: {results}")
            stat, p_value = stats.mannwhitneyu(dataframe[column1], dataframe[column2])
            st.write(f"Mann-Whitney U Test: statistic={stat:.6f}, p-value={p_value:.6f}")
        else:
            st.write(f"Wrong data types")


def streamlit_run():
    st.title('DUGAROV HOMEWORK BLOCK 1')
    uploaded_file = st.file_uploader("Choose a CSV file", type='csv')
    if uploaded_file is not None:
        dataframe = load_data(uploaded_file)
        # st.write(dataframe)
        if dataframe is not None:
            cols = st.columns([1, 1])
            with cols[0]:
                column1 = st.selectbox(
                    'Choose column 1',
                    dataframe.columns)
            with cols[1]:
                column2 = st.selectbox(
                    'Choose column 2',
                    dataframe.columns)
            plotting(dataframe, column1)
            plotting(dataframe, column2)
            selected_test = st.selectbox("Choose a hypothesis test algorithm",
                                         ["Mann-Whitney U-test", "t-test"])
            if st.button("Start test"):
                hypothesis_test(dataframe, column1, column2, selected_test)


if __name__ == '__main__':
    streamlit_run()
