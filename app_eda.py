import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from koreanize_matplotlib import koreanize


def run_eda():
    koreanize()
    st.subheader('데이터 분석')

    # 데이터 로드
    df = pd.read_csv('data/50_Startups.csv')
    
    # 기본 통계량
    st.write('### 1. 데이터 기본 정보')
    st.write('* 데이터 크기:', df.shape)
    st.write('* 기본 통계량')
    st.write(df.describe())

    # 컬럼 선택 기능
    st.write('### 2. 컬럼 별 데이터 분포')
    column = st.selectbox('컬럼을 선택하세요', df.columns)
    
    # 선택된 컬럼의 히스토그램
    fig1 = plt.figure()
    plt.hist(df[column], bins=30)
    plt.title(f'{column} 분포')
    plt.xlabel(column)
    plt.ylabel('빈도')
    st.pyplot(fig1)
    
    # 수치형 데이터 상관관계
    st.write('### 3. 변수 간 상관관계')
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    correlation = df[numeric_columns].corr()
    
    # 히트맵으로 상관관계 시각화
    fig2 = plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
    plt.title('상관관계 히트맵')
    st.pyplot(fig2)
    
    # 주별 분석
    st.write('### 4. 주(State)별 분석')
    state_profit = df.groupby('State')['Profit'].agg(['mean', 'count']).round(2)
    st.write('주별 평균 수익과 기업 수:')
    st.write(state_profit)
    
    # 주별 평균 수익 시각화
    fig3 = px.bar(state_profit, 
                 y='mean',
                 title='주별 평균 수익',
                 labels={'mean': '평균 수익', 'State': '주'})
    st.plotly_chart(fig3)
    
    # 산점도 행렬
    st.write('### 5. 산점도 행렬')
    fig4 = px.scatter_matrix(df, 
                           dimensions=['R&D Spend', 'Administration', 'Marketing Spend', 'Profit'],
                           title='변수 간 산점도 행렬')
    st.plotly_chart(fig4)
    
    # 이상치 분석
    st.write('### 6. 이상치 분석')
    numeric_cols = ['R&D Spend', 'Administration', 'Marketing Spend', 'Profit']
    selected_col = st.selectbox('이상치를 확인할 컬럼 선택', numeric_cols)
    
    fig5 = plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[selected_col])
    plt.title(f'{selected_col} 박스플롯')
    st.pyplot(fig5)