import streamlit as st
import pandas as pd

def run_home():
    st.image('https://img.freepik.com/free-vector/startup-life-concept-illustration_114360-1068.jpg', width=400)
    
    st.write('''
    # 스타트업 수익 예측 서비스 🚀
    
    이 앱은 스타트업의 다양한 지출 데이터를 기반으로 수익을 예측하는 서비스를 제공합니다.
    
    ## 📊 데이터셋 소개
    
    사용된 데이터셋은 다음과 같은 정보를 포함하고 있습니다:
    
    - R&D 지출 (R&D Spend)
    - 관리 비용 (Administration)
    - 마케팅 지출 (Marketing Spend)
    - 주/지역 (State)
    - 수익 (Profit)
    ''')
    
    # 데이터 샘플 보여주기
    df = pd.read_csv('data/50_Startups.csv')
    st.write('### 📈 데이터 샘플')
    st.write(df.head())
    
    st.write('''
    ## 🛠 주요 기능
    
    1. **데이터 분석 (EDA)**
        - 각 변수들의 통계적 특성 확인
        - 변수 간의 상관관계 분석
        - 지역별 수익 분포 확인
    
    2. **머신러닝 예측**
        - 지출 데이터 기반 수익 예측
        - 예측 결과 시각화
        
    왼쪽 사이드바의 메뉴에서 원하는 기능을 선택하여 사용해보세요!
    ''')