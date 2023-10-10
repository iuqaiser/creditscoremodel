import pandas as pd
import numpy as np
import streamlit as st

data = pd.read_csv("C:/Users/imanq/Documents/Programs/GitHub/creditscoremodel/dataset/Credit Score Classification Dataset.csv")
print(data.head())

st.table(data.head())

