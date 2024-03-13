# import pandas as pd
# import matplotlib.pyplot as plt
#
# data = pd.read_csv('./input/')
# print(data.info())
#
# # 1) 히스토그램 그리기
#
# # data에서 남성(data.gender==1.0)의 성별, 키 데이터만 가져옴
# man_data = data.loc[data.gender == 1.0, ['gender', 'height']]
# print(data['gender'].value_counts())
#
# plt.figure(figsize=(10,6))
# # hist() 메서드로 man_data 데이터의 키를 지정하고 계급 개수 20개 등의 속성을 지정
# plt.hist(man_data['height'], bins=20, label='Man')
# plt.title('2020 Health Screenings Man Height Histogram')
# plt.xlabel('height')
# plt.ylabel('frequency')
# plt.legend()
# plt.grid()
# plt.show()
#
# # 2) 그룹 히스토그램 그리기
#
# # 그룹 히스토그램을 그리는 것은 기존 히스토그램 위에 히스토그램을 하나 더 그리는 형식
# # 남성 및 여성 키 그룹 히스토그램
#
# # data에서 남성(data.gender==1.0)의 성별, 키 데이터만 가져옴
# man_data = data.loc[data.gender == 1.0, ['gender', 'height']]
# # data에서 여성(data.gender==2.0)의 성별, 키 데이터만 가져옴
# woman_data = data.loc[data.gender==2.0, ['gender', 'height']]
#
# plt.figure(figsize=(10,6)) # 그래프의 크기를 지정
# # hist() 메서드로 데이터의 키를 지정하고 계급 개수 20개 등의 속성을 지정
# plt.hist(man_data['height'], bins=20, alpha = 0.5,label='Man')
# plt.hist(woman_data['height'], bins=20, alpha = 0.5,label='Woman')
#
# plt.title('2020 Health Screenings Man & Woman Height Group Histogram')
# plt.xlabel('height')
# plt.ylabel('frequency')
# plt.xlim(120, 200)
# plt.legend()
# plt.grid()
# # plt.show()
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
#
#
#
#
#
#
