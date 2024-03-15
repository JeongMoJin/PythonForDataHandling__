import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# economic 데이터 불러오기
# economics = pd.read_csv('./input/economics.csv')
# print(economics.head())
#
# # sns.lineplot()을 이용하면 선 그래프를 만들 수 있음
# # x축에는 시간을 나타낸 date, y축에는 실업자 수를 나타낸 unemploy를 지정
# sns.lineplot(data=economics, x='date', y='unemploy')
# plt.show()
#
# # 출력된 그래프를 보면 x축에 굵은 선이 표시되어 있음
# # date 변수에는 '1967-07-01'처럼 '연월일'을 나타낸 문자가 있는데,
# # 이 값이 x축에 가로로 여러 번 겹쳐 표시되어서 굵은 선으로 보임
#
# # 1) x축에 연도 표시하기
# # x축에 연도가 표시되도록 설정
# # x축에 연도를 표시하려면 먼저 변수 타입을 날짜 시간 타입 datetime64으로 바꿔야 함,
# # economics 데이터의 date가 문자 object 타입으로 되어 있음
#
# # a) 날짜 시간 타입 변수 만들기
# # 날짜 시간 타입 변수 만들기
# # pd.to_datetime()을 이용하면 변수의 타입을 날짜 시간 타입으로 바꿀 수 있음
# # date 타입을 날짜 시간 타입으로 변경해서 date2 변수 추가
# economics['date2'] = pd.to_datetime(economics['date'])
#
# # 변수 타입 확인
# print(economics.info())
# #  #   Column    Non-Null Count  Dtype
# # ---  ------    --------------  -----
# #  0   date      574 non-null    object
# #  1   pce       574 non-null    float64
# #  2   pop       574 non-null    float64
# #  3   psavert   574 non-null    float64
# #  4   uempmed   574 non-null    float64
# #  5   unemploy  574 non-null    int64
# #  6   date2     574 non-null    datetime64[ns]
# # dtypes: datetime64[ns](1), float64(4), int64(1), object(1)
# # memory usage: 31.5+ KB
#
# # date 열은 object 타입이고 datetime64 타입인 date2 열 추가 확인
#
# # 변수의 타입을 날짜 시간 타입으로 바꾸더라도 값이 달라지지 않음
# print(economics[['date', 'date2']].head())
# #          date      date2
# # 0  1967-07-01 1967-07-01
# # 1  1967-08-01 1967-08-01
# # 2  1967-09-01 1967-09-01
# # 3  1967-10-01 1967-10-01
# # 4  1967-11-01 1967-11-01
#
# # 출력 결과를 보면 두 변수의 값이 같음
# # date2 변수는 날짜 시간 타입으로 되어 있어서 df.dt를 이용해 연,월,일을 추출할 수 있음
# # 연 추출
# print(economics['date2'].dt.year.head())
# #          date      date2
# # 0  1967-07-01 1967-07-01
# # 1  1967-08-01 1967-08-01
# # 2  1967-09-01 1967-09-01
# # 3  1967-10-01 1967-10-01
# # 4  1967-11-01 1967-11-01
# # 0    1967
# # 1    1967
# # 2    1967
# # 3    1967
# # 4    1967
# # Name: date2, dtype: int32
#
# # 월 추출
# print(economics['date2'].dt.month.head())
# # Name: date2, dtype: int32
# # 0     7
# # 1     8
# # 2     9
# # 3    10
# # 4    11
# # Name: date2, dtype: int32
#
# # 일 추출
# print(economics['date2'].dt.day.head())
# # Name: date2, dtype: int32
# # 0    1
# # 1    1
# # 2    1
# # 3    1
# # 4    1
# # Name: date2, dtype: int32
#
# # b) 연도 변수 만들기
# # economics에 년도를 나타낸 변수 year를 추가
#
# # 연도 변수 추가
# economics['year'] = economics['date2'].dt.year
# print(economics.head())
# #          date    pce       pop  psavert  uempmed  unemploy      date2  year
# # 0  1967-07-01  506.7  198712.0     12.6      4.5      2944 1967-07-01  1967
# # 1  1967-08-01  509.8  198911.0     12.6      4.7      2945 1967-08-01  1967
# # 2  1967-09-01  515.6  199113.0     11.9      4.6      2958 1967-09-01  1967
# # 3  1967-10-01  512.2  199311.0     12.9      4.9      3143 1967-10-01  1967
# # 4  1967-11-01  517.4  199498.0     12.8      4.7      3066 1967-11-01  1967
#
# print(economics.info())
# #  #   Column    Non-Null Count  Dtype
# # ---  ------    --------------  -----
# #  0   date      574 non-null    object
# #  1   pce       574 non-null    float64
# #  2   pop       574 non-null    float64
# #  3   psavert   574 non-null    float64
# #  4   uempmed   574 non-null    float64
# #  5   unemploy  574 non-null    int64
# #  6   date2     574 non-null    datetime64[ns]
# #  7   year      574 non-null    int32
# # dtypes: datetime64[ns](1), float64(4), int32(1), int64(1), object(1)
# # memory usage: 33.8+ KB
# # None
#
# # c) x축에 연도 표시하기
# # 연도를 나타낸 변수를 sns.lineplot()의 x에 입력하면 x축에 연도가 표시
#
# # x축에 연도 표시
# sns.lineplot(data=economics, x='year', y='unemploy')
# plt.show()
#
# # 선의 위아래에 표시된 면적은 신뢰구간 confidence interval
# # 신뢰 구간을 표시하지 않을려면 errorbar=None을 입력하면 됨
#
# # 신뢰구간 제거
# sns.lineplot(data=economics, x='year', y='unemploy', errorbar=None)
# plt.show()
#
# sns.lineplot(data=economics, x='date2', y='unemploy')
# plt.show()


# 연습문제
# 북대구 영업소의 2023년 12월 일자별 총 교통량의 변화를 선그래프로
#
# df1 = pd.read_csv('./input/TCS_B3_04_03_238959.csv', encoding='ANSI')
# df4 = df1[df1['영업소명'] == '북대구']
# print(df4.tail())
#
# df5 = df4[df4['집계일자'].astype(str).str.contains('2023-12')]
# print(df5.head()) # 북대구 12월 데이터
#
# df6 = df5.groupby('집계일자', as_index=False).agg(n=('총교통량', 'sum'))
# df6['집계일자'] = pd.to_datetime(df6['집계일자'])
# plt.figure(figsize=(20, 6))
# sns.lineplot(data=df6, x='집계일자', y='n')
# plt.show()


















