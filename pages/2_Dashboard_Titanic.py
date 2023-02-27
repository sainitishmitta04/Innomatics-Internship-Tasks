import streamlit as st
import pandas as pd
from matplotlib import image
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.title("Dashboard - Titanic Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)

st.subheader('Displaying Titanic Data Set')
st.dataframe(df)


def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)

st.subheader('Click to Download the Dataset')
st.download_button(
   "Download",
   csv,
   "data.csv",
    key='download-csv'
)




st.subheader('Data Analysis')
option = st.radio('Select an option ', ['Shape', 'Columns','Summary','Head','Tail','Null Values','Duplicates'])

if option == 'Shape':
    st.write('Shape of dataframe:', df.shape)
elif option == 'Columns':
    st.write('Columns of dataframe:', df.columns.tolist())
elif option == 'Head':
    st.write('First 5 rows of dataframe:', df.head())
elif option == 'Tail':
    st.write('Last 5 rows of  dataframe:', df.tail())
elif option == 'Null Values':
    st.write('Number of Null Values in the dataframe',df.isnull().sum())
elif option == 'Duplicates':
    st.write('Number of Duplicated Values in the dataframe = ',df.duplicated().sum())
else:
    st.write('Summary of dataframe:', df.describe())

st.subheader('Data Visualization')
options = list(df.columns)
selected_option = st.selectbox("Select a feature to display Count", options)
st.write(df[selected_option].value_counts())



options2 = list(df.columns)
selected_option2 = st.selectbox("Select a feature to display barchart", options)
filtered_data = df[[selected_option2]]
plot = sns.countplot(x=selected_option2, data=filtered_data)
st.pyplot(plot.figure)

