# # 공공데이터포털에서 다운로드한 2020년 건강검진 일부 데이터를
# # 이용하여 산점도 그래프를 표현
#
# import pandas as pd
# import matplotlib.pyplot as plt
#
# data = pd.read_csv('./input/')
# # print(data.head())
#
# df1 = data.iloc[:100000]
# # print(df1.info())
#
# height_data = df1['height'] # 키 데이터만 가져와 heightdata에 저장
# weight_data = df1['weight'] # 몸무게 데이터만 가져와 weight_data에 저장
# print(height_data.head())
# # 0    175
# # 1    150
# # 2    155
# # 3    165
# # 4    160
# # Name: height, dtype: int64
#
# plt.figure(figsize=(10,4)) # 그래프 크기를 지정
# plt.scatter(height_data, weight_data) # x축 데이터에 height_data, y축 데이터 weight_data 지정
# plt.title('2020 Health screenings Scatter Graph')
# plt.xlabel('height')
# plt.ylabel('weight')
# plt.show()
#
# # 2) 그룹 산점도 그래프 그리기
# # 누적 산점도 그래프를 그리는 것은 기존 산점도 그래프위에 산점도 그래프를 하나 더 그리는 형식
#
# # HDL, LDL, cholesterol 데이터를 가져와 각각의 변수에 저장
# HDL_date = df1['HDL']
# LDL_date = df1['LDL']
# cholesterol_date = df1['cholesterol']
#
# plt.figure(figsize=(10,6)) # 그래프의 크기를 지정
#
# # scatter()에 x축 데이터와 y축 데이터를 지정하고 점 색상과 점 테두리 색상을 지정
# plt.scatter(cholesterol_date, LDL_date, color='r', edgecolors='w', label='Cholesterol*LDL')
# plt.scatter(HDL_date, cholesterol_date, color='g', edgecolors='w', label='HDL*Cholesterol')
# plt.scatter(HDL_date, LDL_date, color='b', edgecolors='w', label='HDL*LDL')
#
# plt.title('2020 Health screenings Group Scatter Graph')
# plt.xlim(-50, 500)
# plt.ylim(-50, 500)
# plt.legend()
# plt.show()