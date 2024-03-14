import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

mpg = pd.read_csv('./input/mpg.csv')
print(mpg.head())
#   manufacturer model  displ  year  cyl       trans drv  cty  hwy fl category
# 0         audi    a4    1.8  1999    4    auto(l5)   f   18   29  p  compact
# 1         audi    a4    1.8  1999    4  manual(m5)   f   21   29  p  compact
# 2         audi    a4    2.0  2008    4  manual(m6)   f   20   31  p  compact
# 3         audi    a4    2.0  2008    4    auto(av)   f   21   30  p  compact
# 4         audi    a4    2.8  1999    6    auto(l5)   f   16   26  p  compact
print(mpg.tail())
#     manufacturer   model  displ  year  cyl  ... drv cty  hwy  fl category
# 229   volkswagen  passat    2.0  2008    4  ...   f  19   28   p  midsize
# 230   volkswagen  passat    2.0  2008    4  ...   f  21   29   p  midsize
# 231   volkswagen  passat    2.8  1999    6  ...   f  16   26   p  midsize
# 232   volkswagen  passat    2.8  1999    6  ...   f  18   26   p  midsize
# 233   volkswagen  passat    3.6  2008    6  ...   f  17   26   p  midsize

# mpg.csv : '구동 방식별 고속도로 연비 평균'
# displ(배기량)
# hwy(고속도로 연비)
# drv(구동방식)

# sns.scatterplot() : 산점도 만들 때 사용
# data : 그래프를 그리는 데 사용할 데이터 프레임을 입력
# x, y : x축과 y축에 사용할 변수(데이터 프레임의 열)를 ''을 이용해 문자 형태로 입력

# x축은 displ, y축은 hwy를 나타낸 산점도 만들기
# mpg 데이터의 displ(배기량) 변수를 x축에, hwy(고속도로 연비) 변수를 y축에 놓음
sns.scatterplot(data=mpg, x='displ', y='hwy')
plt.show()

# 1) 축 범위 설정하기
# 축은 기본적으로 최소값에서 최대값까지 모든 범위의 데이터를 표현하도록 설정
# 데이터 전체가 아니라 일부만 표현하고 싶을 때는 축 범위를 설정

# sns.set() : 범위를 설정하는데 사용
# xlim, ylim을 이용해 설정

# xlim을 이용해 x축 범위 3 ~ 6으로 제한
sns.scatterplot(data=mpg, x='displ', y='hwy').set(xlim=(3,6))
plt.show()

# 2) 종류별로 표시 색깔 바꾸기
# hue를 이용하면 표식 marker의 색깔을 종류별로 다르게 표현할 수 있음

# drv별로 표식 색깔 다르게 표현
sns.scatterplot(data=mpg, x='displ', y='hwy', hue='drv')
plt.show()

# 3) 그래프 활용하기
# 그래프 설정 바꾸기
plt.rcParams.update({'figure.dpi': '150'}) # 해상도, 기본값 72
plt.rcParams.update({'figure.figsize': [8,6]}) # 그림 크기, 기본값 [6,4]
plt.rcParams.update({'font.size': '15'}) # 글자 크기, 기본값 10
plt.rcParams.update({'font.family': 'Malgun Gothic'}) # 폰트, 기본값 sans-serif

# 여러 요소를 한 번에 설정하려면 {}에 설정값을 나열
plt.rcParams.update({'figure.dpi': '150',
                     'figure.figsize': [0, 6],
                     'font.size':'15',
                     'font.family':'Malgun Gothic'})

sns.scatterplot(data=mpg, x='displ', y='hwy')
plt.show()


















