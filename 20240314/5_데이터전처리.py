# 2020년 건강검진 일부 데이터 엑셀 파일을 읽어와 동적인 시각화를 표현

# 1. 파일 불러오기
import pandas as pd
data = pd.read_excel('./input/health_screenings_2020_1000ea.xlsx')
print(data.head())
print(data.info())

# 2. 데이터 전처리
# 성별, 음주 여부, 흡연 상태에 대하여 숫자로 저장되어 있는 정보를 데이터 분석의 가독성을 높이기 위해
# 필요한 데이터만 추출

data6 = data[['gender', 'height', 'weight', 'waist', 'drinking', 'smoking']]
print(data6.head())

# 성별 데이터를 Male과 Female로 변경
data6.loc[data6['gender'] ==1, ['gender']] = 'Male'
data6.loc[data6['gender'] ==2, ['gender']] = 'Female'

# 음주 여부 0(비음주)는 Non-drinking, 1(음주)는 Drinking으로 변경
data6.loc[data6['drinking'] == 0, ['drinking']] = 'Non-drinking'
data6.loc[data6['drinking'] == 1, ['drinking']] = 'Drinking'

# 흡연상태 1(비흡연)과 2(흡연 끊음)을 Non-smoking으로 변경하고, 3(흡연)을 Smoking으로 변경
data6.loc[(data6['smoking'] == 1) | (data6['smoking'] == 2), ['smoking']] = 'Non-smoking'
data6.loc[data6['smoking'] == 3, ['smoking']] = 'Smoking'

print(data6.head())
print(data6.info())
#    gender  height  weight  waist      drinking      smoking
# 0    Male     165      60   72.1  Non-drinking  Non-smoking
# 1  Female     150      65   81.0  Non-drinking  Non-smoking
# 2  Female     155      55   70.0  Non-drinking  Non-smoking
# 3    Male     160      70   90.8  Non-drinking  Non-smoking
# 4  Female     155      50   75.2  Non-drinking  Non-smoking
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1000 entries, 0 to 999
# Data columns (total 6 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   gender    1000 non-null   object
#  1   height    1000 non-null   int64
#  2   weight    1000 non-null   int64
#  3   waist     1000 non-null   float64
#  4   drinking  1000 non-null   object
#  5   smoking   1000 non-null   object
# dtypes: float64(1), int64(2), object(3)
# memory usage: 47.0+ KB
# None


# 데이터 저장
data6.to_pickle('./output/data6.pickle')