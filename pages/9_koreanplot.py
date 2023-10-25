import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
import pickle

# pip install scikit-learn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# 멀티 페이지용 제목
st.set_page_config(page_title='한글처리 그래프!',
                   page_icon='🔬')
st.sidebar.header('Hello, machine learning!! 🔬')

st.title('데이터 분석 🔬')

import os
import matplotlib.font_manager as fm

@st.cache_data
def fontRegistered():
    fm.fontManager.addfont('./fonts/IBMPlexSansKR-Regular.ttf')
    fm._load_fontmanager(try_read_cache=False)
    plt.rc('font', family='IBM Plex Sans KR')

fontRegistered()

# iris feature에 따른 품종 분석
st.subheader('iris 품종분석')
iris = pd.read_csv('./data/iris.csv')

# 변수별 분포 그래프
fig, ax = plt.subplots()
ax = sns.displot(x=iris.sepal_length,
                 kind='kde', hue=iris.species).set(title='한글')
st.pyplot(ax)

fig, ax = plt.subplots()
ax = sns.displot(x=iris.sepal_width,
                 kind='kde', hue=iris.species).set(title='한글')
st.pyplot(ax)

fig, ax = plt.subplots()

ax = sns.displot(x=iris.petal_length,
                 kind='kde', hue=iris.species).set(title='한글')
st.pyplot(ax)

fig, ax = plt.subplots()
ax = sns.displot(x=iris.petal_width,
                 kind='kde', hue=iris.species).set(title='한글')
st.pyplot(ax)