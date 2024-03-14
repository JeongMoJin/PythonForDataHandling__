# 공공 데이터 포탈에서 다운받은 '소상공인시장진흥공단_상가(상권)정보_대구_202312.csv'을 사용.
# 1. [상권업종중분류명]이 '부동산 서비스'인 데이터만 따로 데이터프레임으로 생성. -> df1
# 2. df1에서
# 상가업소번호, 상호명, 상권업종대분류명, 상권업종중분류명, 상권업종소분류명, 시도명, 시군구명, 법정동명만 남기고 나머지 컬럼은 삭제 -> df2
#
# 3. seaborn의 countplot()을 이용해서 각 구별 상점수를 그래프 출력.
#
# 4. seaborn의 barplot()을 이용해서 수성구의 상점수를 각 동별로  그래프 출력 (상점수가 많은 동 순서로 정렬).
#
# 5. matplotlib의 pie()를 이용해서 수성구의 상점수를 각 동별로  그래프 출력. (몇 퍼센트인지 나오도록)
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#
# df1 = pd.read_csv('./input/소상공인시장진흥공단_상가(상권)정보_대구_202312.csv')
# df1 = df1['상권업종중분류명' == '부동산 서비스']
# df2 = df1[['상가업소번호', '상호명', '상권업종대분류명', '상권업종중분류명', '상권업종소분류명', '시도명', '시군구명','법정동명']]
# # df2_bin = df2.groupby('상호명', as_index=False).agg(n=('상호명','시군구명'))
# # sns.countplot(data=df2, x='시군구명')
# # plt.show()
# # print(df2_bin)
#
# # 5) matplotlib의 pie()를 이용해서 수성구의 상점수를 각 동별로 그래프 출력. (몇 퍼센트인지 나오도록)
# plt.figure(figsize=(10,10))
# plt.pie(df1['n'], labels=df2['법정동명'], autopct='%1.1f%')
# plt.show()






# 공공 데이터 포탈에서 다운받은 '한국도로공사_대구경북권 톨게이트 진출입 일교통량'을 검색.
# 상세 정보에서 한국도로 공사링크를 제공.
# 링크를 따라간 후  집계주기 1일, 분기 : 2023년 4분기 파일을 다운로드
#
#
# 1. 집계일자, 영업소명, 입출구명, TCS하이패스명, 총교통량을 제외한 나머지 컬럼 삭제
#
# 2. 2023년 10월 1일의 각 영업소별 총 교통량을 막대 그래프로 출력

df = pd.read_csv('./input/TCS_B3_04_03_238959.csv', encoding='ANSI')
print(df.head())

# 한글이라서 코드 입력
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

df1 = df[['집계일자','영업소명', '입출구명','TCS하이패스명','총교통량']]
# print(df1.head())
# print(df1.tail())
print(df1.info())
want_month = df1['집계일자'] == '2023-10-01'
df2 = df1[want_month]
print(df2.tail())

df3 = df2.groupby('영업소명', as_index=False).agg(n=('총교통량', 'sum'))
print(df3.tail())

plt.figure(figsize=(20,6))
plt.xticks(rotation=45)
sns.barplot(data=df3, x='영업소명', y='n')
plt.show()






