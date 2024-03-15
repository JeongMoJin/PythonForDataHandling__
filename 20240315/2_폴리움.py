# 1) 지도 만들기
import pprint

import folium
import pandas as pd

# seoul_map = folium.Map(location=[37.55, 126.98], zoom_start=12)
#
# # 지도를 HTML 파일로 저장하기
# seoul_map.save('./output/seoul_map.html')
#
# # Map() 함수에 tiles 옵션을 적용하면 지도에 적용하는 스타일을 변경하여 지정할 수 있음
# import folium
#
# # 기본 값 : OpenStreetMap
# # tiles='cartodbpositron' : 단계 구분도가 잘 표현 되도록 밝은 색으로 바꿈
#
# seoul_map2 = folium.Map(location=[37.55, 126.98], zoom_start=15, tiles='Cartodb Positron')
# seoul_map2.save('./output/seoul_map2.html')
#
# seoul_map3 = folium.Map(location=[37.55, 126.98], zoom_start=12, tiles='cartodbpositrononlylabels')
# seoul_map3.save('./output/seoul_map3.html')
#
# # 3) 지도에 마커 표시하기
# # 서울 시내 주요 대학교의 위치 데이터를 데이터 프레임으로 변환하고, folium 지도에 위치를 표시
#
# import pandas as pd
#
# # 대학교 리스트를 데이터프레임 변환
# df = pd.read_excel('./input/서울지역 대학교 위치.xlsx')
# print(df.head())
#
# # 서울 지도 만들기
# seoul_map4 = folium.Map(location=[37.55, 126.98], zoom_start=12)
#
# # 대학교 위치정보를 Marker로 표시
# for name, lat, lng in zip(df['name'], df['위도'], df['경도']):
#     folium.Marker([lat, lng], popup=name).add_to(seoul_map4)
# seoul_map4.save('./output/seoul_map4.html')
#
#
# # 4) 지도에 원형 마커 표시
# import pandas as pd
# import folium
#
# # 대학교 리스트를 데이터프레임 변환
# df = pd.read_excel('./input/서울지역 대학교 위치.xlsx')
# print(df.head())
#
# # 서울 지도 만들기
# seoul_map5 = folium.Map(location=[37.55, 126.98], zoom_start=12, tiles='Cartodb Positron')
#
# # 대학교 위치정보를 CircleMarker로 표시
# # Marker() 대신 CircleMarker()를 사용. 원형 마커의 크기, 색상, 투명도 들을 설정할 수 있음
# for name, lat, lng in zip(df['name'], df['위도'], df['경도']):
#     folium.CircleMarker((lat, lng), popup=name,
#                         raidus = 10,  # 원의 반지름
#                         color='brown',
#                         fill=True,
#                         fill_color='coral',
#                         fill_opacity=0.7).add_to(seoul_map5)
#
# seoul_map5.save('./output/seoul_map5.html')
#
#
# # 5) 지도 영역에 단계 구분도 Choropleth Map 표시하기
# # 행정구역과 같이 지도 상의 어떤 경계에 둘러싸인 영역에 색을 칠하거나 음영 등으로 정보를 나타내는 시각화 방법
# # 전달하는 정보의 값이 커지면 영역에 칠해진 색이나 음영이 진해짐
#
# import pandas as pd
# import folium
# import json
#
#
# # 경기도 인구변화 데이터를 불려와서 데이터프레임으로 변환
# # 경기도 지역의 시군구별 인구변화 데이터 (2007 ~ 2017)
#
# df = pd.read_excel('./input/경기도인구데이터.xlsx', index_col='구분')
# print(df.head())
#
# df.columns = df.columns.map(str)
#
# # 경기도 시군구 경계 정보를 가진 geo-json 파일 불러오기
# # 경기도 행정구역  경계 지리 정보를 사용
#
# geo_path = './input/경기도행정구역경계.json'
# geo_data = json.load(open(geo_path, encoding='utf-8-sig'))
# pprint.pprint(geo_data)
# # 경기도 지도 만들기
# g_map = folium.Map(location=[37.5502, 126.982], zoom_start=9)
#
# # 출력할 연도 선택
# year = '2017'
#
# folium.Choropleth(geo_data=geo_data, # 지도 통계
#                   data=df[year], # 표시하려는 데이터
#                   columns=[df.index, df[year]], # 열 지정
#                   fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.3,
#                   threshold_scale=[10000, 100000, 300000, 500000, 700000],
#                   key_on = 'feature.properties.name',
#                   ).add_to(g_map)
#
# g_map.save('./output/g_map.html')


# 연습문제
# 필요한 정보만 데이터프레임으로 변경
# 남구, 달서구, 상권업종중분류명 : 이용,미용 지도에 표시

# df = pd.read_csv('./input/소상공인시장진흥공단_상가(상권)정보_대구_202312.csv')
# print(df.head())
# print(df.info())
#
# # 원하는 정보만 추출
# df2 = df[['상호명', '상권업종중분류명', '시군구명', '위도', '경도']]
# df3 = df2.loc[((df2['시군구명']== '남구') | (df2['시군구명'] == '달서구')) & (df2['상권업종중분류명'] == '이용·미용')]
# print(df3.head())
#
# # 대구 지도만들기 128.571230303876,35.8334982682276
# daegu_map = folium.Map(location=[35.83,128.56], zoom_start=12)
#
# for name, lat, lng in zip(df3['상호명'], df3['위도'], df3['경도']):
#     folium.Marker((lat, lng), popup=name).add_to(daegu_map)
#
# daegu_map.save('./output/daegu_map.html')

# 연습문제 2
# 경북 데이터 이용
# 필요한 정보만 데이터 프레임으로 변경
# 경산, 표준산업분류명: 커피전문점 지도에 표시

df = pd.read_csv('./input/소상공인시장진흥공단_상가(상권)정보_경북_202312.csv')

# 원하는 정보만 추출
df2 = df[['상호명', '표준산업분류명', '시군구명', '위도', '경도']]
df3 = df2[(df2['표준산업분류명'] == '커피 전문점') & (df2['시군구명'] == '경산시')]
print(df3.head())

# 경산 지도 만들기
gs_map = folium.Map(location=[35.82, 128.74], zoom_start= 12)

for name, lat, lng in zip(df3['상호명'], df3['위도'], df3['경도']):
    tooltip = folium.Tooltip(name, permanent= True)
    folium.CircleMarker((lat, lng), tooltip=tooltip).add_to(gs_map)

gs_map.save('./output/gs_map.html')


















