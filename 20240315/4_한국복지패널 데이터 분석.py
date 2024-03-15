# 1. '한국복지패널 데이터' 분석 준비하기

# https://www.koweps.re.kr:442/data/data/list.do

# 1) 데이터 준비하기
# Koweps_hpwc14_2019_beta2.sav : 2020년에 발간된 복지패널 데이터로 6,331가구, 14,418명의 정보를 담고 있음.

# 2) 패키지 설치 및 로드하기
# 데이터 파일은 통계 분석 소프트웨어인 SPSS 전용파일.
# pyreadstat 패키지를 설치하면 pandas 패키지의 함수를 이용해 SPSS, SAS, STATA 등 다양한 통계 분석
# 소프트웨어의 데이터 파일을 불러올 수 있음.
# pip install pyreadstat

import pyreadstat
import pandas as pd
import seaborn as sns
import numpy as np

# 3) 데이터 불러오기
# 데이터 원본은 복구할 상황을 대비해 그대로 두고 복사본을 만들어 분석에 활용

# raw_welfare = pd.read_spss('./input/')

# 복지패널 데이터와 같은 대규모 데이터는 변수의 수가 많고 변수명이 코드로 되어 있어
# 전체 구조를 한 눈에 파악하기 어려움
# 규모가 큰 데이터는 데이터 전체를 한 번에 파악하기보다 변수명을 쉬운 단어로 바꾼 다음
# 분석에 사용할 벼누를 하나씩 살펴봐야 함

# 5) 변수명 바꾸기
# 규모가 큰 조사 자료는 데이터의 특징을 설명해 놓은 코드북 codebook을 함께 제공
# 코드북에는 코드로 된 변수명과 값의 의미가 설명되어 있음
# 코드북을 보면 데이터의 특징이 어떠한지 감을 잡을 수 있고, 분석에 어떤 변수를 활용할지, 분석 방향의 아이디어를 얻을 수 있음
# 코드북의 파일명은 kowps_Codebook_2019.xlsx

# 코드북을 참고해 분석에 사용할 변수 7개의 이름을 알기 쉬운 단어로 바꿈.
# welfare = welfare.rename(columns={'h14_g3': 'sex',  # 성별
#                                   'h14_g4': 'birth',  # 태어난 연도
#                                   'h14_g10': 'marriage_type',  # 혼인 상태
#                                   'h14_g11': 'religion',  # 종교
#                                   'p1402_8aq1': 'income',  # 월급
#                                   'h14_eco9': 'code_job',  # 직업 코드
#                                   'h14_reg7': 'code_region'})  # 지역 코드

# 2) 2번째 파일

# 다양한 분석 주제를 다루는데, 분석마다 2단계로 진행

# 1단계 : 변수 검토 및 전처리
# 분석에 활용할 변수를 전처리.
# 변수의 특징을 파악하고 이상치와 결측치를 정제한 다음, 변수의 값을 다루기 편하게 바꿈.
# 전처리는 분석에 활용할 변수 각각 진행.

# 2단계 : 변수 간 관계 분석
# 전처리를 완료하면 본격적으로 변수 간 관계를 파악하는 분석을 함.
# 데이터를 요약한 표와 데이터의 특징을 쉽게 이해할 수 있는 그래프를 만든 다음 분석 결과를 해석.


# 2) 성별에 따른 월급 차이 - 성별에 따라 월급이 다를까?
# 분석 절차
# 1단계 : 변수 검토 및 전처리
# 성별 / 월급
# 2단계 : 변수 간 관계 분석
# 성별 월급 평균표 만들기 / 그래프 만들기

# 1. 성별 변수 검토 및 전처리하기
# 1) 변수 검토하기

# walfare = pd.read_csv('./input/Koweps_hpc16_2021_beta2.sav')
# print(walfare.head())

# 2) 전처리하기
# 코드북을 보면 성별 변수의 값이 1이면 남자, 2면 여자를 의미. 모른다고 답하거나 응답하지 않으면 9로 입력
# 이 정보를 바탕으로 데이터에 이상치가 있는지 검토하고, 분석할 때 제거하기 편하도록 NaN 을 부여해 결측치 처리
# 즉 값이 9인 경우 성별을 알 수 없어 분석에서 제외해야 하므로 결측 처리

# 이상치 확인
# wlafare['sex'].value_counts()

# 1,2만 있고 9나 다른 값이 없으니 이상치를 결측 처리하는 절차를 건너뛰어도 됨
# 만일 이상치가 있으면 이상치를 결측 처리한 후에 다음 결측치 확인

# 이상치 결측 처리
# sex 열에서 9인 값을 NaN으로 변경
# np.where(condition, T, F)
# walfare['sex'] = np.where(welfare['sex'] == 9, np.nan, welfare['sex'])

# 결측치 확인
# welfare['sex'].isna().sum()


# 성별이 1, 2로 되어 있어, 값의 의미를 이해하기 쉽도록 문자 male과 female로 변경
# 변경 후 잘 반영이 되었는지 value_counts()와 countplot()을 이용해 바꾼 값이 잘 반영이 됐는지 출력 결과를 확인

# 성별 항목 이름 부여
# welfare['sex'] = np.where(welfare['sex'] ==1, 'male', 'female')

# welfare['sex'].value_counts()

# 빈도 막대 그래프 만들기
# sns.countplot(data=welfare, x='sex')
# plt.show()

# 작업한 데이터프레임을 csv로 저장
# welfare.to_csv('./data/Koweps_hpwc14_2019_beta2_step_02.csv', index=False)


# 2) 월급 변수 검토 및 전처리하기

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# welfare = pd.read_csv('./data/Koweps_hpwc14_2019_beta2_step_02.csv')
# welfare['sex'].haed()

# 1) 변수 검토하기
# 코드북을 보면 월급은 '일한 달의 평균 임금'을 의미하여 1만원 단위로 기록
# 변수 이름은 income
# 성별은 범주 변수이므로 df.value_counts()를 이용해 범주별 빈도를 확인하면 특징을 파악할 수 있음
# 하지만 월급은 연속 변수이므로 df.value_acount()을 이용하면 너무 많은 항목이 출력되어 알아보기 어려움
# 연속 변수는 df.describe()로 요약 통계량을 확인해야 특징을 파악할 수 있음
# welfare['income'].dtype

# welfare['income'].describe() # 요약 통계량 구하기

# 출력 결과를 보면 float64 타입이고, 0 ~ 1,092만원의 값을 지님
# 150 ~ 345 만원에 가장 많이 분포하고 평균은 268만원, 중앙값은 평균보다 작은 220만원으로
# 전반적으로 낮은 쪽에 치우침 -> 월급이 평균값보다 낮은 사람이 50% 이상

# 히스토그램을 만들어 분포를 확인
# sns.hisplot(data=welfare, x='income') # 히스토그램 만들기
# plt.show()


# 2) 전처리 하기
# 코드북을 보면 월급은 만원 단위로 되어 있고, '모름/무응답'은 9999.

# welfare['income'].describe() # 이상치 확인

# welfare['income'].isne().sum() # 결측치 확인 14418

# 출력 결과를 보면 최소값은 0 ~ 1,092 이고 결측치 9,884개가 있음
# 즉 9999가 입력된 데이터는 없음
# 이상치를 결측 처리하는 절차를 건너뛰어도 됨

# 만약 9999인 항목이 있다면 아래와 같이 이상치를 결측 처리하는 절차를 거쳐야 됨
# 이상치 결측 처리



# 3) 성별에 따른 월급 차이 분석하기

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# welfare = pd.read_csv('./data/Koweps_hpwc14_2019_beta2_step_02.csv')

# 1) 성별 월급 평균표 만들기

# income 결측치 제거 : dropna(subset=['income'])
# sex별 분리 : groupby('sex', as_index=False)
# income 평균 구하기 : agg(mean_income=('income', 'mean')
# sex_income = welfare.dropna(subset=['income']).groupby('sex', as_index=False).agg(mean_income=('income', 'mean'))
# sex_income = welfare.dropna(subset=['income'])
# sex_income = sex_income.groupby('sex', as_index=False)
# sex_income = sex_income.agg(mean_income=('income', 'mean'))

# 평균 남자 월급은 349만원, 여자 월급은 186만원으로, 남성이 여성보다 약 163만원이 많음

# 2) 그래프 만들기
# 분석 결과를 쉽게 이해할 수 있도록 성별 월급 평균표를 이용해 막대 그래프로 만듬

# 막대 그래프 만들기
# sns.barplot(data=sex_income, x = 'sex', y='mean_income')
# plt.show()


# 3) 나이와 월급의 관계 - 몇 살 때 월급을 가장 많이 받을까?

# 분석 절차
# 1단계 : 변수 검토 및 전처리
# 나이 / 월급
# 2단계 : 변수 간 관계 분석
# 나이에 따른 우러급 평균표 만들기 / 그래프 만들기

# 2) 전처리
# 코드북을 보면 태어난 연도는 '모름/무응답'일 경우 9999로 코딩
# 이 정보를 바탕으로 전처리

# welfare['birth'].describe() # 이상치 확인

# welfare['birth'].isna().sum() # 결측치 확인

# 이상치와 결측치가 없으므로 파생변수를 만드는 단계로 넘어감
# 만일 이상치가 발견되면 아래와 같이 전처리한 다음 분석을 진행

# 이상치 결측 처리
# welfare['birth'] = np.where(welfare['birth'] == 9999, np.nan, welfare['birth'])

# 결측치 확인
# welfare['birth'].isna().sum()

# 3) 파생변수 만들기 - 나이
# 2019년에 조사가 진행됐으니 2019에서 태어난 연도를 뺀 다음 1을 더해 나이를 구함

# 나이 변수 만들기
# df.assign(kworgs) : DataFrame에 새 열을 할당하는 메서드. kwargs : 새열이름 = 내용 형식으로 입력되는 키워드
# 콤마(,)를 통해 여러개를 입력
# welfare = welfare.assign(age= 2019 - welfare['birth'] + 1)
#
# welfare['age'].describe()

# 히스토그램 만들기
# sns.histplot(data=welfare, x ='age')
# plt.show()
#
# welfare.to_csv('./data/Koweps_hpwc14_2019_beta2_step_03.csv', mode= w)

# 2) 나이와 월급의 관계 분석하기

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# welfare = pd.read_csv('./data/Koweps_hpwc14_2019_beta2_step_03.csv')

# 1) 나이에 따른 월급 평균표 만들기
# 나이별 월급 평균표 만들기

# income 결측치 제거 : dropna(subset=['income'])
# age별 분리 : groupby('age')
# income 평균 구하기 : agg(mean_icome=('income', 'mean'))
# age_income = welfare.dropna(subset=['income']).groupby(['age']).agg(mean_income=('income','mean'))
# age_income.head()

# 2) 그래프 만들기
# 평균표를 이용해 그래프 작성, x축을 나이, y축을 월급으로 지정해 나이에 따른 월급의 변화를 나타낸 선 그래프 만듬

# 선 그래프 만들기
# sns.lineplot(data=age_income, x='age', y='mean_income')
# plt.show()









