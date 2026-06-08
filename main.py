import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer # 텍스트 패킷 처리를 위해 추가

# 1. 데이터 불러오기
print("데이터를 불러오는 중입니다...")
splits = {'train': 'train.csv', 'test': 'test.csv'}
df = pd.read_csv("hf://datasets/rdpahalavan/network-packet-flow-header-payload/" + splits["train"])

print(f"데이터 로드 완료! 데이터 형태: {df.shape}")
print("현재 컬럼 목록:", df.columns.tolist())

# 2. 라벨(Target) 컬럼 지정 (에러 수정 부분!)
# 'label' -> 'attack_cat' 으로 변경
target_column = 'attack_cat'  

# 결측치 제거
df = df.dropna()

# 3. 데이터 전처리 (정답 라벨 인코딩 & 피처 벡터화)
print("\n데이터 전처리를 시작합니다. (시간이 조금 걸릴 수 있습니다...)")

# 3-1. 정답(y) 처리: 'attack_cat' 문자열(예: Normal, DoS 등)을 0, 1, 2 숫자로 변환
le = LabelEncoder()
y = le.fit_transform(df[target_column])
print(f"탐지할 공격 유형들: {le.classes_}")

# 3-2. 특성(X) 처리: 'packet_dat' 안의 긴 문자열을 머신러닝이 이해할 수 있는 수치형 피처로 변환
# TF-IDF를 사용하여 패킷 문자열 내에서 자주 등장하는 중요한 패턴 100개를 추출합니다.
# (컴퓨터 성능이 좋다면 max_features를 500이나 1000으로 늘리면 성능이 더 좋아집니다)
vectorizer = TfidfVectorizer(max_features=100)
X = vectorizer.fit_transform(df['packet_dat'].astype(str)).toarray() # 메모리 에러 시 .toarray() 대신 희소 행렬 그대로 사용 가능

print(f"전처리 완료! 추출된 X 특성 형태: {X.shape}")

# 4. 학습용(Train)과 테스트용(Test) 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\n학습 데이터 크기: {X_train.shape}, 테스트 데이터 크기: {X_test.shape}")

# 5. Random Forest 모델 정의 및 학습
print("\nRandom Forest 모델 학습을 시작합니다...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)

rf_model.fit(X_train, y_train)
print("모델 학습 완료!")

# 6. 모델 예측 및 성능 평가
print("\n모델을 평가하는 중입니다...")
y_pred = rf_model.predict(X_test)

# 정확도(Accuracy) 출력
accuracy = accuracy_score(y_test, y_pred)
print(f"\n[모델 성능 평가]")
print(f"정확도 (Accuracy): {accuracy * 100:.2f}%")

# 상세 분류 결과 리포트
# 원래 문자열 라벨 이름(le.classes_)을 넣어서 보기 쉽게 출력
print("\n[상세 분류 리포트 (Classification Report)]")
print(classification_report(y_test, y_pred, target_names=le.classes_.astype(str)))