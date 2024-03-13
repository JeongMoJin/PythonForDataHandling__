# # 에어코리아에서 제공하는 2001년 ~ 2019년까지의 미세먼지 데이터 'fine_dust.xlsx'를 이용하여 선 그래프로 표현
#
import pandas as pd
import matplotlib.pyplot as plt

# 1) 2019년 데이터 읽기
data = pd.read_excel('./input/fine_dust.xlsx')
print(data.head())
data2019 = data[2019]

# 2) 2019년 지역별 미세먼지 선 그래프
plt.figure(figsize=(15,4))
plt.plot(data2019, color='b', marker='o') # 원형 마커 지정
plt.title('2019 Fine Dust Line Graph')
plt.xlabel('area')
plt.ylabel('micrometer')
plt.grid() # 격자 표시
plt.show()

# 3) 2016 ~ 2019년 미세먼지 선 그래프
# 2016년 데이터를 가져와 chartdata에 저장하고 마커 및 이름을 저장하는 과정을 2019년까지 반복
plt.figure(figsize=(15,4))
for year in range(2016, 2020):
    plt.plot(data[year], marker='o', label=year)
plt.title('2016 ~ 2019 Fine Dust Line Graph')
plt.xlabel('area')
plt.ylabel('micrometer')
plt.legend()
plt.show()



























