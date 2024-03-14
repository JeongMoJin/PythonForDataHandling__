# mpg 데이터에서 drv(구동방식)별 hwy(고속도록 연비) 평균을 나타낸 막대 그래프를 만듬
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

mpg = pd.read_csv('./input/mpg.csv')
# print(mpg.head())
# 1) 집단별 평균표 만들기
# 평균 막대 그래프를 만들려면 집단별 평균값을 담은 데이터 프레임이 필요
# '구동 박식별 고속도로 연비 평균'을 담은 데이터 프레임을 만듬
# drv별로 분리하고 hwy 평균 구하기

# agg(mean_hwy=('hwy', 'mean') -> mean_hwy열을 생성하면서 'hwy'열의 평균(mean)값을 입력

df_mpg = mpg.groupby('drv').agg(mean_hwy=('hwy', 'mean'))
print(df_mpg)
#       mean_hwy
# drv
# 4    19.174757
# f    28.160377
# r    21.000000

# 출력 결과를 보관 집단을 나타낸 변수 drv가 인덱스로 바뀌어 mean_hwy 아래에 표시
# seaborn으로 그래프를 만들려면 값이 변수에 담겨 있어야 함
# -> 인덱스가 아니라 열로 만들어져야 함
# 변수를 인덱스로 바꾸지 않고 원래대로 유지하려면 df.groupby()에 as_index = False를 입력

df_mpg = mpg.groupby('drv', as_index=False).agg(mean_hwy=('hwy', 'mean'))
print(df_mpg)
#   drv   mean_hwy
# 0   4  19.174757
# 1   f  28.160377
# 2   r  21.000000

# 2) 그래프 만들기
# 생성된 데이터 프레임을 이용해 막대 그래프를 만듬
# sns.barplot() : 막대 그래프 만들 때 사용
# data : 데이터 프레임을 지정
# x : x축에 범주를 나타낸 변수
# y : y축에 평균값을 나타낸 변수

sns.barplot(data=df_mpg, x='drv', y='mean_hwy')
plt.show()

# 3) 크기순으로 정렬하기
# 막대 정렬 순서는 그래프를 만드는데 사용한 데이터 프레임의 행 순서에 따라 정해짐
# 앞에서 출력한 그래프를 보면 drv 막대가 4, f, r 순으로 정렬
# 크기 순으로 정렬하려면 그래프를 만들기 전에 df.sort_values()를 이용해 데이터 프레임을 내림차순으로 정렬

# 데이터 프레임 정렬하기
df_mpg = df_mpg.sort_values('mean_hwy', ascending=False)
# 막대 그래프 만들기
sns.barplot(data=df_mpg, x='drv', y='mean_hwy')
plt.show()

# 02 빈도 막대 그래프
# 1) 집단별 빈도표 만들기
# 빈도 막대 그래프를 만들려면 집단별 빈도를 담은 데이터 프레임이 필요
# df.agg()에 빈도를 구하는 함수 count를 적용해 '구동 방식 별 빈도'를 담은 데이터 프레임을 만듬

# 집단별 빈도표 만들기
df_mpg = mpg.groupby('drv', as_index=False).agg(n=('drv', 'count'))
print(df_mpg)
#   drv    n
# 0   4  103
# 1   f  106
# 2   r   25

# 2) 그래프 만들기
# sns.barplot()을 적용해 막대 그래프 만듬
# 막대 그래프 만들기
sns.barplot(data=df_mpg, x='drv', y='n')
plt.show()

# sns.barplot() 사용할 때 df.groupby()와 df.agg()를 이용해 집단별 빈도표를 만드는 작업했음
# 대신 sns.countplot()을 이용하면 원데이터를 바로 이용해 빈도 막대 그래프를 만들 수 있음

# 빈도 막대 그래프 만들기
sns.countplot(data=mpg, x='drv')
plt.show()


# 두 그래프는 x축의 순서가 다름
# sns.barplot()으로 만든 그래프는 x축 순서가 4, f, r인 반면
# sbs.countplot()로 만든 그래프는 f, 4, r
# 이는 sns.barplot()에 사용한 df_mpg와 sns.countplot()에 사용한 mpg의 drv 값 순서가 다르기 때문

# 데이터 프레임에서 변수의 값 순서는 데이터 프레임에 입력된 행의 순서에 따름
# mpg의 drv는 0~6행이 f, 7~17행이 4, 18~27이 r로 되어 있으므로 값의 순서는 f, 4, r
# 변수의 고유값을 출력하는 unique()를 이용하면 값의 순서를 알 수 있음
print(mpg['drv'].unique()) # ['f', '4','r']

# df_mpg의 drv는 값의 순서가 알파벳 순으로 되어 있음
# groupby()를 이용해 데이터 프레임을 요약하면 값의 순서가 알파벳순으로 바뀌기 때문
print(df_mpg['drv'].unique()) # ['4' 'f' 'r']


# 3) 막대 정렬하기
# sns.countplot()으로 만든 그래프의 막대를 정렬하려면 order에 원하는 순서로 값을 입력하면 됨

# 4, f, r 순으로 막대 정렬
sns.countplot(data=mpg, x='drv', order=['4', 'f', 'r'])
plt.show()

# sns.countplot()의 order에 mpg['drv'].value_counts().index를 입력하면
# drv의 빈도가 높은 수능로 막대를 정렬
# mpg['drv'].value_counts().index는 빈도가 높은 순으로 변수의 값을 출력

# drv의 값을 빈도가 높은 순으로 출력
mpg['drv'].value_counts().index

# drv 빈도 높은 순으로 막대 정렬
sns.countplot(data=mpg, x='drv', order=mpg['drv'].value_counts().index)
plt.show()






























