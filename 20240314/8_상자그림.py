import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 01. 상자 그림만들기
# sns.boxplot()을 이용하면 상자 그림을 만들 수 있음
# mpg 데이터를 이용해 x축을 drv, y축을 hwy로 지정하고 '구동 방식별 고속도로 연비'를  상자 그림으로 표현

mpg = pd.read_csv('./input/mpg.csv')
print(mpg.head())
#   manufacturer model  displ  year  cyl       trans drv  cty  hwy fl category
# 0         audi    a4    1.8  1999    4    auto(l5)   f   18   29  p  compact
# 1         audi    a4    1.8  1999    4  manual(m5)   f   21   29  p  compact
# 2         audi    a4    2.0  2008    4  manual(m6)   f   20   31  p  compact
# 3         audi    a4    2.0  2008    4    auto(av)   f   21   30  p  compact
# 4         audi    a4    2.8  1999    6    auto(l5)   f   16   26  p  compact

# mpg.csv : '구동 방식별 고속도로 연비 평균'
# displ(배기량)
# hwy(고속도로 연비)
# drv(구동방식)

sns.boxplot(data=mpg, x='drv', y='hwy')
plt.show()

# 상자 그림은 값을 크기순으로 나열해 4등분했을 때 위치하는 값인 '사분위수'를 이용해 만듬.

# 다음은 상자 그림의 요소가 나타내는 값
# 상자 그림             값       설명
# 상자 아래 세로선     아랫수염        하위 0 ~ 25% 내에 해당하는 값
# 상자 밑면           1사분위수(Q1)   하위 25% 위치 값
# 상자 내 굵은 선      2사분위수(Q2)   하위 50% 위치 값 (중앙값)
# 상자 윗면           3사분위수(Q3)   하위 75% 위치 값
# 상자 위 세로선       윗수염          하위 75 ~ 100% 내에 해당하는 값
# 상자 밖 가로선       극단치 경계      Q1, Q3 밖 1.5 IQR 내 최대값
# 상자 밖 점 표식      극단치          Q1, Q3 밖 1.5 IQR을 벗어난 값
# * IQR(사분위 범위)은 1사분위수와 3사분위수의 거리(직사각형의 높이)를 뜻하고,
# '1.5 IQR'은 IQR의 1.5배을 뜻함.

# 출력된 그래프를 보면 각 구동방식의 고속도로 연비 분포를 알수 있음.
# * 전륜구동(f)은 26 ~ 29 사이의 좁은 범위에 자동차가 모여 있는 뾰족한 형태의 분포.
#   수염의 위아래에 점 표식이 있는 것을 보면 연비가 극단적으로 높거나 낮은 자동차들이 있음.
# * 4륜구동(4)은 17 ~ 22 사이에 자동차 대부분이 모여 있음.
#   중앙값이 상자 밑면에 가까운 것을 보면 낮은 값 쪽으로 치우친 형태의 분포
# * 후륜구동(r)은 17 ~ 24 사이의 넓은 범위에 자동차가 분포.
#   수염이 짧고 극단치가 없는 것을 보면 자동차 대부분이 사분위 범위에 해당한다는 것을 알수 있음.
















