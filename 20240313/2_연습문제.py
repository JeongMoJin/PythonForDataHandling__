# import pandas as pd
#
# # covid = pd.read_csv('./input/covid.csv', encoding='ANSI')
# # print(covid.head())
# #
# # # 2. '사례수'가 가장 높은 항목의 모든 정보를 출력
# # # 조건문과 불 인덱싱 사용
# # covid_tmp = covid['사례수'] == covid['사례수'].max()
# # print(covid[covid_tmp])
# #
# # # 3. '증가율'이 높은 3개의 항목을 출력
# # # 증가율이 높은 순서대로 정렬 후 3개의 행을 선택
# # df2 = covid.sort_values(['증가'], ascending=False)
# # print(df2.head(3))
# # # print(covid.sort_values(by=['증가'], ascending=False).head(3))
# #
# # # 수강과 교수 데이터파일을 이용하여 다음 문제를 해결
# #
# # # 1) 두 데이터프레임을 merge()를 사용해서 결합해서 출력하세요
# # signup = pd.read_csv('./input/signup.csv', encoding='ANSI')
# # print(signup.head())
# #
# # professor = pd.read_csv('./input/professor.csv', encoding='ANSI')
# # print(professor.head())
# #
# # table_merge = pd.merge(signup, professor)
# # print(table_merge.head())
# #
# # # 2) 교수 테이블에서 학과별 인원 수를 출력하세요. (count() 사용)
# # stu_count = table_merge.value_counts('학과')
# # print(stu_count)
#
#
#
# #'서울특별시 코로나19 백신 예방접종현황'에 대한 정보를 가지고 있는 데이터 파일 (vaccine.csv)을 이용하여 모든 문제를 차례대로 수행하세요.
#
# # 필드명 : 설명
# # date : 접종일
# # subject : 접종대상자
# # day1num : 당일 1차 접종자 수
# # day1sum : 1차 접종 누계
# # day1rate : 1차 접종률
# # day2num : 당일 2차 접종자 수
# # day2sum : 2차 접종 누계
# # day2rate : 2차 접종률
#
# # 1) csv파일을 불러와서 하위 5행의 데이터를 확인.
# # 2) 필요없는 열을 삭제한 후 출력
# # 삭제할 열 : day1sum, day1rate, day2sum, day2rate
# # 3) 데이터프레임의 기초통계량을 확인
# # 4) 새로운열("월")을 생성한 후 데이터 날짜의 월을 입력
# #  5) 월별 평균을 출력
#
#
# vaccine = pd.read_csv('./input/vaccine.csv', encoding='ANSI')
# # 1) csv파일을 불러와서 하위 5행의 데이터를 확인.
# print(vaccine.sort_values('date', ascending=True).head())
# # 2) 필요없는 열을 삭제한 후 출력
# vaccine1 = vaccine.drop(['day1sum', 'day1rate', 'day2sum', 'day2rate'], axis=1).head()
# print(vaccine1)
# # 3) 데이터프레임의 기초통계량을 확인
# print(vaccine1.describe())
# # 4) 새로운열("월")을 생성한 후 데이터 날짜의 월을 입력
# vaccine1['월'] = vaccine.date.astype(str).str.slice(5,7)
# print(vaccine1)
#
# #  5) 월별 평균을 출력
# vaccine2 = vaccine1[['day1num', 'day2num', '월']].groupby('월').mean()
# print(vaccine2)
#
#
#
# # 경산에 있는 커피 전문점(표준산업분류명 기준)을 동(법정동 기준)별로 몇개가 있는지 출력(출력 기준은 법정동 가나다 순)
#
# sosang_kb = pd.read_csv('./input/.csv')
# sosang_kb_ks = sosang_kb[sosang_kb['시군구명'] == '경산시']
# print(sosang_kb_ks.head())
#
#
# #2. 경산에 밍ㅆ는 커피전문점만 골라냄
# df9 = sosang_kb_ks[sosang_kb_ks['표준산업분류명'] == '커피 전문점']
# print(df9)
#
# # case1
# # value_counts()를 이용해서 법정동에 몇개의 데이터가 있는지 반환 후 sort_index()를 이용하여 인덱스 값 기준으로 정렬
# print(df9.value_counts('법정동명').sort_index())
#
# # case2
# # '법정동명'으로 그룹을 나눈 후, 데이터의 고유번호인 '상가업소번호'의 개수를 카운팅
# print(df9.groupby('법정동명').count()['상가업소번호'])
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
