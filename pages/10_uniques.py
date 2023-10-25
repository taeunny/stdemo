import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
import altair as alt
import plotly.express as px
from bokeh.plotting import figure

st.title('시각화 🌏')

vegans = pd.read_csv('./data/uniques.csv', encoding='utf-8')
st.write(vegans.head())

types = st.selectbox('화장품 종류는?',
         ['모두','로션/크림','스킨/토너','에센스/세럼/앰플'], index=0)

x_var = st.selectbox('X축에 사용할 변수는?',
         ['브랜드명','스킨케어','제품명','가격','피부타입','비건인증','고유성분'], index=3)

y_var = st.selectbox('Y축에 사용할 변수는?',
         ['브랜드명','스킨케어','제품명','가격','피부타입','비건인증','고유성분'], index=6)

hue_var = st.selectbox('다변량 분석 사용할 변수는?',
         ['브랜드명','스킨케어','제품명','피부타입','비건인증'], index=3)

fdvegans = vegans
if types != '모두':
    find = vegans.loc[:, '스킨케어'] == types
    fdvegans = vegans.loc[find,]

alt_chart = (
    alt.Chart(fdvegans, title='비건 데이터셋 산점도')
    .mark_circle()
    .encode(x=x_var, y=y_var, color=hue_var)
    .interactive()
).properties(
    width=800,
    height=600
)
st.altair_chart(alt_chart, use_container_width=True)
