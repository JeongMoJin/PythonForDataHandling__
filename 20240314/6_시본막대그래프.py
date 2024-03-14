import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data6 = pd.read_pickle('./output/data6.pickle')
print(data6.head())
#    gender  height  weight  waist      drinking      smoking
# 0    Male     165      60   72.1  Non-drinking  Non-smoking
# 1  Female     150      65   81.0  Non-drinking  Non-smoking
# 2  Female     155      55   70.0  Non-drinking  Non-smoking
# 3    Male     160      70   90.8  Non-drinking  Non-smoking
# 4  Female     155      50   75.2  Non-drinking  Non-smoking

# 1. 데이터 준비하기
# 음주 여부 및 흡연 상태 데이터 준비하기
# data6에서 성별, 음주 여부의 그룹별 개수(인원)를 구하여 drinking에 저장
drinking = data6.groupby(['gender', 'drinking'])['drinking'].count()
print(drinking)
# gender  drinking
# Female  Drinking        213
#         Non-drinking    305
# Male    Drinking        356
#         Non-drinking    126
# Name: drinking, dtype: int64

# data6에서 성별, 흡연 상태의 그룹별 개수(인원)를 구하여 smoking에 저장
smoking = data6.groupby(['gender', 'smoking'])['smoking'].count()
print(smoking)
# gender  smoking
# Female  Non-smoking    500
#         Smoking         18
# Male    Non-smoking    321
#         Smoking        161
# Name: smoking, dtype: int64


# 음주 여부와 흡연 상태에 대한 그룹별 개수(인원)의 시리즈를 데이터프레임으로 변경
drinking = drinking.to_frame(name='count')
smoking = smoking.to_frame(name='count')
print(drinking)
# gender drinking
# Female Drinking        213
#        Non-drinking    305
# Male   Drinking        356
#        Non-drinking    126

# 데이터프레임의 인덱스를 초기화
drinking = drinking.reset_index()
smoking = smoking.reset_index()
print(drinking)
#    gender      drinking  count
# 0  Female      Drinking    213
# 1  Female  Non-drinking    305
# 2    Male      Drinking    356
# 3    Male  Non-drinking    126

# 2. 기본 막대 그래프 그리기
# 성별 음주 여부 및 흡연 상태 막대 그래프

fig = plt.figure(figsize=(17, 6)) # 그래프 크기 지정 및 그림 객체 생성
fig.suptitle('2022 Health Screenings Drinking & Smoking Type Bar Graph', fontweight='bold')
index = np.arange(4) # x축 눈금 개수를 배열로 생성하고 index에 저장

# 2) 첫 번째 서브플롯 설정
fig.add_subplot(1, 2, 1) # 1행 2열의 서브플롯 중 첫 번째 서브플롯을 생성
# 첫 번째 서브플롯에 그려질 음주 여부 데이터 개수 (인원)을 bar() 함수를 이용하여 지정
plt.bar(index, drinking['count'])
plt.title('Drinking Type')
plt.ylabel('Count')
# x축 눈금 이름을 지정
plt.xticks(index, ['Non-drinking(Female)', 'Drinking(Female)', 'Non-drinking(Male)', 'Drinking(Male)'])
plt.show()

# 3) 두 번째 서브플롯 설정
fig.add_subplot(1, 2, 2) # 1행 2열의 서브플롯 중 두 번째 서브플롯을 생성
# 두 번째 서브플롯에 그려질 흡연 상태 데이터 개수 (인원)을 bar() 함수를 이용하여 지정
plt.bar(index, smoking['count'])
plt.title('Smoking Type')
plt.ylabel('Count')
# x축 눈금 이름을 지정
plt.xticks(index, ['Non-smoking(Female)', 'Drinking(Female)','Non-smoking(Male)','Smoking(Male)'])
plt.show()


# 3) 시본 막대 그래프 그리기
# 성별 음주 여부 및 흡연 상태 시본 막대 그래프

fig = plt.figure(figsize=(17, 6))

# 1행 2열의 서브플롯 생성
area1 = fig.add_subplot(1,2,1)
area2 = fig.add_subplot(1,2,2)

# barplot() 함수를 이용하여 x축에 성별, y축에 음주여부 개수 (인원), hue에 성별 음주 여부를 할당하여 첫 번째 서브플롯에 할당
ax1 = sns.barplot(data=drinking, x='gender', y='count', hue='drinking', ax=area1)
# barplot() 함수를 이용하여 x축에 성별, y축에 흡연상태 개수 (인원), hue에 성별 흡연상태 그룹별 데이터를 할당하여
# 두 번째 서브플롯에 할당
ax2 = sns.barplot(data=smoking, x='gender', y='count', hue='smoking', ax=area2)

fig.suptitle('2022 Health Screenings Drinking & Smoking Type Seaborn Bar Graph', fontweight='bold')
area1.set_title('Drinking Type')
area2.set_title('Smoking Type')

plt.show()





















