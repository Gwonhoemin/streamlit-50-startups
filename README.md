# 스타트업 수익 예측 애플리케이션 🚀

스타트업의 R&D 지출, 관리 비용, 마케팅 비용 등의 데이터를 기반으로 수익을 예측하는 머신러닝 기반 웹 애플리케이션입니다.

## 📋 주요 기능

1. **데이터 탐색 (EDA)**
   - 기본 통계 분석
   - 변수별 분포 확인
   - 상관관계 분석
   - 지역별 수익 분석
   - 이상치 탐지

2. **수익 예측 (Machine Learning)**
   - 머신러닝 모델 기반 수익 예측
   - 예측 결과 시각화

## 🔧 기술 스택

- **Frontend**: Streamlit
- **Backend**: Python
- **데이터 처리**: Pandas, NumPy
- **시각화**: Matplotlib, Seaborn, Plotly
- **머신러닝**: Scikit-learn

## 💻 설치 방법

1. 저장소 클론
```bash
git clone https://github.com/Gwonhoemin/streamlit-50-startups.git
cd streamlit-50-startups
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate  # Windows
```

3. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

## 🚀 실행 방법

```bash
streamlit run app.py
```

## 📊 데이터셋 구조

- **R&D Spend**: 연구개발 지출 비용
- **Administration**: 관리 비용
- **Marketing Spend**: 마케팅 지출 비용
- **State**: 스타트업 소재 지역
- **Profit**: 수익 (목표 변수)

## 📁 프로젝트 구조

```
streamlit-50-startups/
├── app.py              # 메인 애플리케이션
├── app_home.py         # 홈 화면
├── app_eda.py          # 데이터 분석 페이지
├── app_ml.py           # 머신러닝 예측 페이지
├── requirements.txt    # 필요 라이브러리
└── data/              # 데이터 폴더
    └── 50_Startups.csv
```

## 👥 기여 방법

1. 이 저장소를 Fork 합니다.
2. 새로운 Branch를 생성합니다.
3. 변경사항을 Commit 합니다.
4. Branch에 Push 합니다.
5. Pull Request를 생성합니다.

## 📝 라이센스

이 프로젝트는 MIT 라이센스를 따릅니다. 자세한 내용은 LICENSE 파일을 참조하세요.

## ✨ 참고자료

- [Streamlit 공식 문서](https://docs.streamlit.io)
- [Scikit-learn 공식 문서](https://scikit-learn.org/stable/)
