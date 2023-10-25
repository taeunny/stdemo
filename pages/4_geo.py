import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
import altair as alt
import plotly.express as px
from bokeh.plotting import figure

import json
import plotly.graph_objects as go


# 멀티 페이지용 제목
st.set_page_config(page_title='Hello, geography!', page_icon='🌏')
st.sidebar.header('Hello, geography!🌏')

st.title('지리정보 시각화 🌏')

st.subheader('서울시 인구 데이터 2023')
seoulpop = pd.read_csv('./data/seoulpop_2023.csv')
st.write(seoulpop.head())

# 지도 시각화1 - st.map
seoulpop['pop2'] = seoulpop['pop'].apply(lambda x: x / 10000)
print(seoulpop['pop2'])

st.map(seoulpop, latitude='lat', longitude='lon', color='#ff0000', size='pop2')

# 지도 시각화2 - plotly
fig = px.scatter_mapbox(seoulpop, lat='lat', lon='lon',
                        size='pop2', color='pop2',
                        color_continuous_scale=px.colors.sequential.BuGn,
                        mapbox_style='open-street-map',
                        hover_name='gu',
                        hover_data={'lat':False, 'lon':False, 'pop2':False,
                                    'pop':True},  # 보이고 싶은 부분만 True
                        opacity=0.9)
fig.update_layout(mapbox_zoom=10.5, width=800, height=600,
                  mapbox_center={"lat": 37.532600, "lon": 127.024612})  # 서울 좌표
st.plotly_chart(fig)

# 지도 시각화3 - 동적 시각화
option1 = st.selectbox('보고싶은 인구현황을 선택하세요',
                       ['구별 총인구수', '총 내국인수', '구별 총외국인수'])

optcols = 'pop' if option1 == '구별 총인구수' else \
        'korpop' if option1 == '구별 총내국인수' else 'forepop'

optcolor = px.colors.sequential.RdBu if option1 == '구별 총인구수' else \
            px.colors.sequential.YlGn if option1 == '구별 총내국인수' else \
            px.colors.sequential.Rainbow

seoulpop['pop2'] = seoulpop[optcols].apply(lambda x: x / 10000)

fig = px.scatter_mapbox(seoulpop, lat='lat', lon='lon',
                        size='pop2', color='pop2',
                        color_continuous_scale=optcolor,
                        mapbox_style='open-street-map',
                        hover_name='gu',
                        hover_data={'lat':False, 'lon':False, 'pop2':False,
                                    optcols:True},  # 보이고 싶은 부분만 True
                        opacity=0.9)

fig.update_layout(mapbox_zoom=10.5, width=800, height=600,
                  mapbox_center={"lat": 37.532600, "lon": 127.024612})  # 서울 좌표
st.plotly_chart(fig)

# 지도 시각화4 - 단계구분도
with open('./data/seoul_geo_simple.json', encoding='utf-8') as f:
    geo = json.load(f)

