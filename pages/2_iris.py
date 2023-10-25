import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
import altair as alt
import plotly.express as px
from bokeh.plotting import figure

# 멀티 페이지용 제목
st.set_page_config(page_title='Hello, Iris!', page_icon='🌻')
st.sidebar.header('Hello, Iris!🌻')
st.write('Welcome to Iris! 🌻')


st.title('Iris 데이터셋을 이용한 시각화 예제')

iris = pd.read_csv('./data/iris.csv')
st.write(iris.head())

x_var = st.selectbox('X축에 사용할 변수는?',
                     ['sepal_length','sepal_width','petal_length','petal_width'])

y_var = st.selectbox('Y축에 사용할 변수는?',
                     ['sepal_length','sepal_width','petal_length','petal_width'])

alt_chart = (
    alt.Chart(iris, title='Iris 데이터셋 산점도')
    .mark_circle()
    .encode(x=x_var, y=y_var, color='species')
    .interactive()
)
st.altair_chart(alt_chart)

# 막대 그래프
st.bar_chart(iris.iloc[:, :4])

# 산점도 그래프
st.scatter_chart(iris.iloc[:, :4])


# 히스토그램 - plotly 차트 이용
fig = px.histogram(iris.iloc[:, :4])
st.plotly_chart(fig)

# pip install seaborn bokeh==2.4.3

# 카운트플롯 - seaborn
fig_sns, ax_sns = plt.subplots()
ax_sns = sns.countplot(x='species', data=iris)
st.pyplot(fig_sns)

# 산점도 - bokeh
colormaps = {'setosa':'red','versicolor':'blue','virginica':'green'}
colors = [ colormaps[s] for s in iris['species'] ]

scplot = figure()
scplot.scatter(iris['petal_length'], iris['petal_width'], size=5, fill_alpha=0.2, color=colors)
st.bokeh_chart(scplot)

