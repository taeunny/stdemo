import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import os
import matplotlib.font_manager as fm

@st.cache_data
def fontRegistered():
    fm.fontManager.addfont('./fonts/IBMPlexSansKR-Text.ttf')
    fm._load_fontmanager(try_read_cache=False)
    plt.rc('font', family='IBM Plex Sans KR')

fontRegistered()

# 멀티 페이지용 제목
# st.set_page_config(page_title='Hello, vegan!', page_icon='🌿')
st.sidebar.header('🌿Hello, vegan!🌿')

st.title('🌿비건 화장품 빈도 그래프🌿')

# csv 파일 불러오기
vegan = pd.read_csv('./data/화장품성분전처리투게더_국가추가.csv')


x_var = st.selectbox('보고싶은 항목은?',['브랜드','인증기관','스킨케어','국가'])


optcols = '브랜드명' if x_var == '브랜드' else \
    '비건인증' if x_var =='인증기관' else \
        '스킨케어' if x_var =='스킨케어' else '국가'

# 제품명이 중복되는 경우가 있을 수 있으므로, unique한 제품명만 추출
vegan = vegan.drop_duplicates(subset='제품명', keep='first')

# 인증기관 별로 그룹화하고 제품명의 개수를 계산
grouped = vegan.groupby(optcols)['제품명'].count()
grouped_sorted = grouped.sort_values(ascending=False)

# # 그래프를 그리기 전에, grouped 데이터를 확인 (선택 사항)
# st.write(grouped_sorted)
#
# # 인증기관 별 화장품 갯수 그래프 생성
# st.bar_chart(grouped_sorted)

import matplotlib.colors as mcolors

# 초록색 그라데이션 생성
colors = plt.cm.Greens(np.linspace(1,0.3, len(grouped_sorted)))


# Matplotlib을 사용하여 정렬된 막대 그래프 그리기
fig, ax = plt.subplots(figsize=(7, 5))
grouped_sorted.plot(kind='bar', ax=ax, color=colors)
ax.set_title(f'{x_var} 별 화장품 개수')
ax.set_xlabel(x_var)
ax.set_ylabel('제품수')

# x축 라벨을 45도 각도로 표시
if optcols == '스킨케어' or optcols == '국가':
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha="center")

st.pyplot(fig)


# 데이터 불러오기
vegan = pd.read_csv('./data/화장품정보들(샹테카이없).csv')

# 가격 컬럼의 최솟값과 최댓값
min_price = int(vegan['가격'].min())
max_price = int(vegan['가격'].max())

# Streamlit 슬라이더를 사용하여 원하는 가격 범위 설정
price_range = st.slider(
    "원하는 가격 범위를 선택하세요:",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price)
)

# 설정한 가격 범위에 해당하는 데이터만 필터링
filtered_vegan = vegan[(vegan['가격'] >= price_range[0]) & (vegan['가격'] <= price_range[1])]

# 히스토그램 그리기
st.title(f'💰가격 범위 {price_range[0]:,}원 ~ {price_range[1]:,}원 내의 화장품 가격 분포💰')

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(filtered_vegan['가격'], bins=30, color='yellowgreen', edgecolor='black')
ax.set_title(f'제품별 가격대 분포')
ax.set_xlabel('가격')
ax.set_ylabel('제품 수')
st.pyplot(fig)