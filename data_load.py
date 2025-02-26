import streamlit as st
import pandas as pd
from datetime import datetime


def data_load():
   if "data" not in st.session_state:
      df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
      df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
      df_data = df_data[df_data["Value(£)"] > 0]
      df_data = df_data.sort_values(by="Overall", ascending=False)
      st.session_state["data"] = df_data