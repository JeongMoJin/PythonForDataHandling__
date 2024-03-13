# # 1. 공공데이터 '국민건강보험공단_건강검진정보' 다운로드
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 2. 파일을 읽은 후 데이터프레임으로 변환하시오
# data = pd.read_csv('./input/국민건강보험공단_건강검진정보_20221231.csv', encoding='ANSI')
# print(data.head())
# print(data.info())
# # 3. 남성의 키데이터를 가지고 히스토그램을 만들것
# man_data =data.loc[data['성별']==1, ['성별', '신장(5cm단위)']]
# # 4. 남성과 여성이 키 데이터를 하나의 히스토그램으로 만들 것
# plt.hist(man_data['신장(5cm단위)'], bins=10, label='Man')
# plt.title('2022 Health Screenings Man Height Histogram')
# plt.xlabel('height')
# plt.ylabel('frequency')
# plt.legend()
# plt.grid()
# plt.show()
#
# # 4. 남성과 여성이 키 데이터를 하나의 히스토그램으로 만들것
# # data에서 남성(data['성별'] == 1) 성별, 키 데이터만 가져옴
# man_data = data.loc[data['성별']==1, ['성별', '신장(5cm단위)']]
# # data에서 여성(data['성별'] == 2)의 성별, 키 데이터만 가져옴
# woman_data = data.loc[data['성별']==2, ['성별', '신장(5cm단위)']]
#
# plt.figure(figsize=(10,6)) # 그래프의 크기를 지정
# # hist() 메서드로 데이터의 키를 지정하고 계급 개수 20개 등의 속성을 지정
# plt.hist(man_data['신장(5cm단위)'], bins=10, alpha = 0.5,label='Man')
# plt.hist(woman_data['신장(5cm단위)'], bins=10, alpha = 0.5,label='Woman')
#
# plt.title('2022 Health Screenings Man & Woman Height Group Histogram')
# plt.xlabel('height')
# plt.ylabel('frequency')
# plt.xlim(120, 200)
# plt.legend()
# plt.grid()
# plt.show()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
