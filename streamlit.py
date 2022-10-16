import streamlit as st
import pandas as pd

from gsheetsdb import connect

sheet_id = st.secrets["gsheets"]["sheet_id "]

sheet_name = "Sheet1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

data = pd.read_csv(url)

st.title("hellow")

st.dataframe(data=data, width=None, height=None, use_container_width=False)