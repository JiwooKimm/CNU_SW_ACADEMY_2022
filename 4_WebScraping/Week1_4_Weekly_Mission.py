# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Mission 1. Neflix and Code
#
# 호주니는 요즘 넷플릭스를 보는데 심취해있다. 최근 넷플릭스와 협업하는 K-Contents가 늘어가는 것을 보면서 자부심을 느끼는 한편,  
# 넷플릭스에 얼마나 많은 한국 작품이 있는지 궁금해졌다. 호주니를 도와 넷플릭스에 얼마나 많은 한국 작품이 있는지 알아보자.
#
# ![image.png](attachment:image.png)
#
# -----
# ### Mandatory Part:
# 넷플릭스 데이터가 주어졌을 때, 다음 질문에 답하시오:  
# Q1. 한국 작품은 총 얼마나 있는가?
#
# - country column을 기준으로 한다.
# - "South Korea"인 경우만 인정한다. ("US, South Korea"는 인정하지 않음)
#
# ### Bonus Part:
# Q2. 가장 많은 작품이 올라간 국가는 어디이고, 얼마나 많은 작품이 있는가?  
# country column을 기준으로 한다.  
# 단일 국가인 경우를 기준으로 결과를 구해보자.

import numpy as np
import pandas as pd

root= '/Users/jiwookim/Library/Mobile Documents/com~apple~CloudDocs/Documents/Academy/2022CNU_SW_ACADEMY/Programmers/netflix_titles.csv'
netflix= pd.read_csv(root)
netflix.head(20)
# netflix.columns
# netflix.shape


# +
print(pd.isna(netflix['country']).sum())
netflix.dropna(axis=0, subset=['country'], inplace= True)
print(pd.isna(netflix['country']).sum())
netflix.head()
# # netflix.dropna?

# +
cond= netflix['country'] == 'South Korea'
print(cond.sum())
print(cond.value_counts())
N_Kcontents= cond.value_counts()[1]

print('A number of K-contents on Netflix is', N_Kcontents)
# -

netflix['country']

multi_country= netflix["country"].str.contains(",")
multi_country

# +
single_country= netflix[multi_country == 0]

print(len(single_country))
single_country.head()

# -

netflix['country'].describe()


top_country= netflix['country'].describe().top #United State


# +
N_top_country= (netflix['country'] == top_country).sum()

print("The single country produced the most content is the %s, producing a total of %i."%(top_country,N_top_country))
# -

# ------
# -------
# ## Mission 2. 가즈아!
#
# 서울의 소시민 나일론 마스크는 요즘 가상화폐에 푹 빠져있다. 매일매일 극락과 지옥을 오가는 매운맛에 정신을 못 차리고 있는데, 그의 친구인 호주니는 그에게 정신차리게 하기 위해 비트코인 광풍이 일었던 2017년 한 해의 가격의 변화를 보여주려고 한다. 그런데 매일매일의 데이터를 보여주는 것보다 이것의 추세를 표현해주면 좋겠다는 생각이 들어 Moving Average(이동평균법) 를 도입하고자 한다. 호주니를 도와 마스크씨를 설득해보자.
#
# ![image.png](attachment:image.png)
#
# -----
# ### Mandatory Part
# 다음 데이터가 주어졌을 때 2016.6 ~ 2017.6 기간의 5-MA(Moving Average) 비트코인 가격 그래프를 그려주세요.
#
# - 선의 색깔은 노란색(#f2a900) 으로 해야합니다.
# - x-axis label과 y-axis label은 적절한 텍스트로 추가되어야 합니다.
# - 이동평균의 기준은 Open Column으로 계산합니다.
# - 이외에도 그래프를 알아보기 쉽게 하기 위한 정보(Text, Facet 등)을 추가하는 것도 좋습니다.  
#
# (https://www.kaggle.com/datasets/rishidamarla/bitcoin-prices-20112015)
#
# 💡 이동평균(Moving Average)법은 시계열 데이터를 표현하는 데에 많이 사용하는 방법 중 하나입니다.  
#

import matplotlib.pyplot as plt
# %matplotlib inline

bit= pd.read_csv('/Users/jiwookim/Library/Mobile Documents/com~apple~CloudDocs/Documents/Academy/2022CNU_SW_ACADEMY/Programmers/BitCoin.csv')
bit.head()

# +
bit['ymd']=pd.to_datetime(bit['Date'])

bit.head(3)

# +
ym= bit['ymd'].dt.year + (bit['ymd'].dt.month)/120 #e.g., yyyy년 12월 >>> yyyy.1, yyyy년 6월 >>>> yyyy.05
bit['cond']=ym
bit1617= bit[(bit['cond'] >= 2016.05 ) & (bit['cond'] <= 2017.05)]

bit1617=bit1617[::-1] #https://rfriend.tistory.com/518 [::-1] & flip 비교


bit1617.sort_values(by='ymd', inplace=True) 

bit1617.set_index(keys=bit1617.ymd, inplace=True)
bit1617.head(20)

# +
mavr= np.convolve(bit1617.Open, np.ones(5), 'valid') / 5
nanarr= np.empty(4)
nanarr[:]= np.nan
mavr= np.append(nanarr,mavr)

bit1617['movingAvr']=mavr
bit1617.head()

# +
plt.figure(figsize=(13,5))
# # plt.plot?
plt.plot(bit1617.Open, color='gray', alpha= 0.6, label= 'Daily')
plt.plot(bit1617.movingAvr, color='#f2a900', label='5-days moving avaeraged')
plt.xlabel('Data [yyyy-mm]')
plt.ylabel('Open price')

plt.legend(frameon= False)

plt.grid(True, axis='y', color='gray', alpha=0.4, linestyle=':')
plt.grid(True, axis='x', color='gray', alpha=0.4, linestyle=':')

plt.show()
# -

# 해당 그래프를 본 나일론 마스크씨는 정신을 차렸다. 정확히는 비트코인만 바라본 본인을 말이다.   
# 정말 많은 가상화폐가 있는데 비트코인만 바라본 본인을 돌아보게 되었다. 더불어 가장 핫한 코인인 이더리움 또한 관심이 생겼는데,   
# 마스크씨는 2017년 한 해에 이 두개의 추세를 비교하고싶어한다.  
# 마스크씨를 도와 비트코인과 이더리움의 가격 추세 비교를 도와주자.
