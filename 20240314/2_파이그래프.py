# plt.pie(x [, labels=label_seq, autopct='비율 표시 형식(ex: %0.1f)', shadow=False(기본) 혹은 True
# , explode=explode_seq, counterClock=True(기본) 혹은 False, startangle=각도 (기본은 0)])

# x는 배열 확인 시퀀스 형태의 데이터.
# pie()는 x를 입력하면 x의 각 요소가 전체에서 차지하는 비율을 계산하고 그 비율에 맞게 부채꼴 크기를 결정해서 파이 그래프를 그림.

# labels : x 데이터 항목의 수와 같은 문자열 시퀀스(리스트, 튜플)을 지정해 파이 그래프의 각 부채꼴 부분에 문자열을 표시.

# autopct : 각 부채꼴 부분의 항목의 비율이 표시되는 숫자의 형식을 지정.
# 예를 들어 '%0.1f'가 입력되면 소수점 첫째 자리까지 표시되며, '%0.0f'가 입력되면 정수만 표시.
# %를 추가하고 싶으면 '%0.1f%%'와 같이 입력.

# shadow : 그림자 효과를 지정. 기본 값은 False.

# explode : 부채꼴 부분이 원에서 돌출되는 효과를 주어 특정 부채꼴 부분을 강조할 때 이용.
# x 데이터 항목의 수와 같은 문자열 시퀀스(리스트, 튜플)을 지정. 기본 값은 강조 효과가 없음.

# counterClock : x 데이터에서 부채꼴 부분이 그려지는 순서가 반시계방향(True)인지 시계방향(False)인지를 지정.
# 기본값은 True로 반시계 방향.

# startangle : 제일 처음 부채꼴 부분이 그려지는 각도로 x축을 중심으로 반시계 방향으로 증가. 기본값은 0.

# 파이 그래프는 가로, 세로 비율이 1 대 1로 같아야 그래프가 제대로 보임.
# plt.figure(figsize = (w, h)
# w와 h는 그래프의 너비 width와 높이 height 를 의미. 단위는 인치 inch.
# 값을 지정하지 않으면 (w, h)의 기본값은 (6, 4).
# w와 h를 같은 값으로 지정하면 생성되는 그래프는 가로와 세로의 비율은 1 대 1이 됨.

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'Malgun Gothic' # '맑은 고딕'으로 지정
matplotlib.rcParams['axes.unicode_minus'] = False

fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
result = [7, 6, 3, 2, 2]
plt.pie(result)
plt.show()

# 각 부채꼴 부분에 속하느 데이터의 라벨과 비율을 추가
plt.figure(figsize=(7,7))
plt.pie(result, labels=fruit, autopct='%.1f%%')
plt.show()

# 각 부채꼴 부분은 x축 기준 각도 0도를 시작으로 반시계방향으로 그려짐
# x축 기준 각도 90도에서 시작해서 시계방향으로 그려는 예

plt.figure(figsize=(7,7))
plt.pie(result, labels=fruit, autopct='%.1f&&', startangle= 90, counterclock=False)
plt.show()

# 그림자를 추가하고, 특정 요소(사과)를 표시한 부채꼴 부분만 강조한 예
explode_value =(0.1, 0, 0, 0, 0)
# 0.1 : 반지름의 10% 만큼 벗어나도록 설정

plt.figure(figsize=(7,7))
plt.pie(result, labels=fruit, autopct='%.1f%%', startangle=90, explode=explode_value, shadow=True, counterclock=False)
plt.show()


























