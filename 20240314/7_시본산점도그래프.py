import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data6 = pd.read_pickle('./output/data6.pickle')
print(data6.head())

# 1. 데이터 준비하기

# data6에서 남성 및 여성의 성별, 몸무게, 허리둘레, 음주 여부, 흡연 상태 데이터를 가져와
# male_data, female_data에 각각 저장
male_data = data6.loc[data6.gender == 'Male', ['gender','weight', 'waist', 'drinking', 'smoking']]
female_data = data6.loc[data6.gender == 'Female', ['gender', 'weight', 'waist', 'drinking', 'smoking']]
print(male_data.head())
#   gender  weight  waist      drinking      smoking
# 0   Male      60   72.1  Non-drinking  Non-smoking
# 3   Male      70   90.8  Non-drinking  Non-smoking
# 5   Male      85   94.0      Drinking      Smoking
# 6   Male      80   93.0      Drinking      Smoking
# 7   Male      65   92.0  Non-drinking      Smoking

print(min(female_data['waist']))
# 53.0
print(max(male_data['waist']))
# 128.0

# 2. 시본 스트림 플롯 그래프 그리기
# 스트립 플롯 그래프는 데이터 분포를 요약하여 간략히 띠 형태로 보여 주는 그래프
# 일반적으로 작은 데이터를 다루는 용도로 사용되는데, 큰 데이터를 다룰 때는 주로 히스토그램 등을 많이 사용

plt.figure(figsize=(10, 5)) # 그래프의 크기를 지정
plt.title('Seaborn Strip Plot Graph') # 그래프의 제목을 지정

# stripplot() 함수로 허리 둘레 데이터를 x축에 지정, 몸무게 데이터를 y축에 각각 지정
sns.stripplot(data=male_data, x='waist', y='weight')
sns.stripplot(data=female_data, x='waist', y='weight')

# x축 눈금 간격(눈금 개수는 총 127개)을 허리둘레의 최솟값(53)과 최댓값(128)을 중심으로 지정
plt.xticks(np.arange(0, 127, 63), labels=[53, 90.5, 120])
plt.show()

plt.figure(figsize=(10, 5)) # 그래프의 크기를 지정
plt.title('Seaborn Strip Plot Graph - Color Palette') # 그래프의 제목을 지정

# stripplot() 함수로 허리 둘레 데이터를 x축에 지정, 몸무게 데이터를 y축에 각각 지정
sns.stripplot(data=male_data, x='waist', y='weight', hue='gender', palette='dark')
sns.stripplot(data=female_data, x='waist', y='weight', hue='gender', palette='Set1')

# x축 눈금 간격(눈금 개수는 총 127개)을 허리둘레의 최솟값(53)과 최댓값(128)을 중심으로 지정
plt.xticks(np.arange(0, 127, 63), labels=[53, 90.5, 120])
plt.show()






















