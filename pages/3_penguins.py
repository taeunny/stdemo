import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
import altair as alt
import plotly.express as px
from bokeh.plotting import figure

# 멀티 페이지용 제목
st.set_page_config(page_title='Hello, Penguins!', page_icon='🐧')
st.sidebar.header('Hello, Penguins! 🐧')
st.write('Welcome to Penguins! 🐧')


st.title('Penguins 시각화 예제')

penguins = pd.read_csv('../data/penguins.csv')
st.write(penguins.head())

x_var = st.selectbox('X축에 사용할 변수는?',
                     ['bill_length_mm','bill_depth_mm','flipper_length_mm'])

y_var = st.selectbox('Y축에 사용할 변수는?',
                     ['bill_length_mm','bill_depth_mm','flipper_length_mm'])

alt_chart = (
    alt.Chart(penguins, title='Penguins 산점도')
    .mark_circle()
    .encode(x=x_var, y=y_var, color='species')
    .interactive()
)
st.altair_chart(alt_chart)


# 산점도 그래프
st.scatter_chart(penguins, x='bill_length_mm', y='bill_depth_mm', color='sex')

# 산점도 - bokeh
