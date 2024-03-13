# 01. 시각화 옵션

# 그래프를 표현하다 보면 그래프 제목, X축 및 Y축 이름 등의 그래프에 대한 추가 옵션을 지정할 때가 많음

# 1) 제목

# 그래프 제목은 title() 메서드를 사용하여 표현
# 제목은 기본적으로 영어를 사용하는데, 한글을 사용하려면 별도의 설정을 해야 함

# 제목 지정
import matplotlib.pyplot as plt
#
# plt.title('Line Graph')
# xdata = [2, 4, 6, 8]
# ydata = [1, 3, 5, 7]
# plt.plot(xdata, ydata)
# plt.show()
#
# # 범례지정
# plt.title('Legend')
# data1 = [2 ,4, 6, 8]
# data2 = [8, 6, 4, 2]
# plt.plot(data1, label='asc')
# plt.plot(data2, label='desc')
# plt.legend()
# plt.show()
#
# # 3) 색상 지정
# xdata = [2, 4, 6, 8]
# ydata = [1, 3, 5, 7]
# plt.plot(xdata, ydata, color = 'red')
# plt.show()
#
# # 4) x축 및 y축 이름 지정
# xdata = [2, 4, 6, 8]
# ydata = [1, 3, 5, 7]
# plt.plot(xdata, ydata)
# plt.xlabel('X value')
# plt.ylabel('Y value')
# plt.show()
#
# # 5) 그래프 선 모양
# # 그래프 선 모양은 plot()의 linestyle 속성을 이용하여 표현.
# # linestyle 속성으로 실선은 '-', 파선은 '--', 점쇄선 '-.', 점선은 ':' 기호로 지정
#
# # 그래프 선 모양 지정
# data1 = [2, 4, 6, 8]
# data2 = [8, 6, 4, 2]
# plt.plot(data1, color='r', label='dashed', linestyle='--')
# plt.plot(data2, color='g', label='dotted', linestyle=':')
# plt.legend()
# plt.show()

# 그림 범위 지정
plt.title('X, Y range')
xdata = [10, 20, 30, 40]
ydata = [1, 3, 5, 7]
plt.plot(xdata, ydata, color='b', linestyle='--', marker='o', markersize='10')
plt.xlim(0, 50)
plt.ylim(-5,15)
plt.show()

# 내장 시각화 옵션

# 그래프 속성 값
# 옵션 : 종류
# line : 선 그래프
# bar : 막대 그래프 - 수직
# barh : 막대 그래프 - 수평
# his : 히스토그램 그래프
# box : 박스 그래프
# kde : 커널 밀도 그래프
# area : 면적 그래프
# pie : 원형 그래프
# scatter : 산점도 그래프
# hexbin : 고밀도 산점도 그래프

import matplotlib.pyplot as plt
import pandas as pd

my_score = [[60, 90, 95], [80, 75, 100], [65, 85, 90], [85, 70, 90], [95, 90, 85], [75, 85, 90], [85, 80, 75]]
subject = ['kor', 'math', 'eng']
df = pd.DataFrame(my_score, columns=subject)

df.plot(kind='line')
plt.show()






































