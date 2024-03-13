import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('./input/fine_dust.xlsx', index_col='area')
data2016 = data[2016]
data2016.head()

# 1) 세로 막대 그래프 그리기

# # 2016년 지역별 미세먼지 세로 막대 그래프
# plt.figure(figsize=(15,4))
# plt.bar(data2016.index, data2016, color='g') # x축에 data2016의 인덱스를, y축 데이터에 data2016을 지정
# plt.title('2016 Fine Dust Bar Graph')
# plt.xlabel('area')
# plt.ylabel('micrometer')
# plt.ylim(35, 55)
# plt.grid()
# plt.show()
#
# # 2) 그룹 세로 막대 그래프 그리기
import numpy as np
index = np.arange(4)
#
# plt.figure(figsize=(15, 4))
# df1 = data.loc['Seoul':'Busan', 2016:2019] # 서울, 경기, 인천, 부산, 지역의 2016-2019년 데이터만 추출
# for year in range(2016, 2020):
#     chart_data = df1[year] # 연도별로 데이터 가지고 옴
#     plt.bar(index, chart_data, width=0.2, label=year) # 두께 0.2의 막대 그래프를 지정
#     index = index + 0.2 # 출력되는 위치를 0.2씩 이동
#
# plt.title('2016 ~ 2019 Fine Dust Group Bar Graph')
# plt.xlabel('area')
# plt.ylabel('micrometer')
# plt.ylim(35,55)
# # x축 눈금을 가운데로 지정하기 위해 막대그래프를 마지막 위치에서 0.5 빼주고, x축 눈금 이름을 지정
# plt.xticks(index-0.5,['Seoul', 'Gyeonggi', 'Incheon', 'Busan'])
# plt.legend()
# plt.show()

# 3) 그룹 누적 가로 막대 그래프 만들기
# 2016 ~ 2019 지역별 미세먼지 그룹 막대 그래프를 누적하여 가로 방향으로 변경하여 표현
# 누적 막대 그래프를 그리는 것은 기존 막대 그래프 위에 막대 그래프를 하나 더 그리는 방식
# 이를 위해서는 index의 위치를 변경해야 함
# 가로 방향으로 바꾸는 것은 bar() 대신 barrg()를 사용하면 됨
# 막대 그래프를 가로 방향으로 변경했으므로 x축 및 y축 이름, x축 및 y축 눈금도 가로 방향에 맞게 변경

# 2016 ~ 2019 지역별 미세먼지 그룹 누적 가로 막대 그래프
index = np.arange(4)

plt.figure(figsize=(15,4))
df1 = data.loc['Seoul':'Busan', 2016:2019] # 서울, 경기, 인천, 부산 지역의 2016 ~ 2019년 데이터만 추출
for year in range(2016, 2020):
    chart_data = df1[year]  # 연도별로 데이터 가지고 옴
    plt.barh(index, chart_data, label=str(year))

plt.title('2016~2019 Fine Dust Group Barh Graph')
plt.ylabel('area')
plt.xlabel('micrometer')
plt.xlim(30,55)
plt.yticks(index, ['Seoul', 'Gyeonggi', 'Incheon','Busan'])
plt.legend()
plt.show()











