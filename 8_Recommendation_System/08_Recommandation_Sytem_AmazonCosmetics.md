# Recommendation System : Amazon Cosmetics based on SVD

: Recommendation%20System%20Amazon%20Cosmetics%20based%20on%20SV%20098e3580a0b94740ade5a6ce3e1a8896/Week9_RS_Amazon_Cosmetics.ipynb, Recommendation%20System%20Amazon%20Cosmetics%20based%20on%20SV%20098e3580a0b94740ade5a6ce3e1a8896/Week9_RS_Amazon_Cosmetics.pdf
Day : Day 45
Topic: 추천시스템
Type: 과제
작성일시: 2022년 9월 13일 오후 3:11

### 아마존 뷰티 제품 평점 정보:

- 2M 개 이상의 고객 리뷰와 평점 정보를 포함한 데이터셋을 가지고 인기 제품 추천 엔진을 만들어 보자.

     (앞서 영화 추천과 비슷하게 진행 가능하다!)

- 데이터셋에는 총 4가지 정보가 포함되어 있다:
    - 사용자 ID
    - 상품 ID (ASIN이라 부른다)
    - 평점 정보 (1-5)
    - 평점이 주어진 시간
- 앞서 2일차와 4일차 강의 내용을 기반으로 인기도 기반의 추천과 SVD 기반의 추천을 만들어 보자

---

[Traces of Sabzill ](https://www.notion.so/Traces-of-Sabzill-e0b594223dc94e1185ae66d646b45949)

### 0. 데이터와 필요 라이브러리 불러오기

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
# !wget "https://grepp-reco-test.s3.ap-northeast-2.amazonaws.com/ratings_Beauty.csv"
amazon_ratings = pd.read_csv("https://grepp-reco-test.s3.ap-northeast-2.amazonaws.com/ratings_Beauty.csv")
```

**0-1. 데이터 확인** 

```python
print(amazon_ratings.info())
print(amazon_ratings.shape)
print(amazon_ratings.isna().sum())
amazon_ratings = amazon_ratings.dropna() #4가지 정보 중에 하나라도 비어있는 레코드들 drop
print(amazon_ratings.head())
print(amazon_ratings.shape)
amazon_ratings.describe()
```

데이터의 기술통계 확인한다. 

```python
amazon_ratings.describe()
```

평점에 따른 데이터의 분포도 확인해본다. 

```python
rate_count= pd.DataFrame(amazon_ratings.groupby('Rating')['ProductId'].count())
rate_count.rename(columns={'ProductId':'count'}, inplace= True)
rate_count
```

![Untitled](Recommendation%20System%20Amazon%20Cosmetics%20based%20on%20SV%20098e3580a0b94740ade5a6ce3e1a8896/Untitled.png)

```python
# Rating versus count

product_rating = amazon_ratings.groupby('ProductId')['Rating'].mean()
product_rating_count = amazon_ratings.groupby('ProductId')['Rating'].count()
unreliability = amazon_ratings.groupby('ProductId')['Rating'].std(ddof = -1)
unique_products_list = amazon_ratings.ProductId.unique()

data_model = pd.DataFrame({'Rating': product_rating[unique_products_list],
                           'Count': product_rating_count[unique_products_list], 
                          'Unreliability': unreliability[unique_products_list]})

data_model= data_model[data_model.Count >= 10] # 평점 갯수 10개 이상인것만 표출
sns.set_style('ticks')
plt.figure(num=None, figsize=(11.7, 8.27), dpi=100, facecolor='w', edgecolor='k')

ax = data_model.plot(kind='scatter', x='Rating', y='Count', color='dodgerblue', alpha=0.1)
plt.ylim([0,3000])
plt.show()
```

![Untitled](Recommendation%20System%20Amazon%20Cosmetics%20based%20on%20SV%20098e3580a0b94740ade5a6ce3e1a8896/Untitled%201.png)

전반적으로 높은 점수를 준 것을 볼 수 있다. 

---

### 1. 메모리 베이스 추천 시스템

**1.1. 인기도 기반 추천**

정보가 없는 유저들에게 가장 쉽게 해 줄 수 있는 추천 방식!

일단 리뷰 수 가장 많은 상품 10개 뽑아본다. 

```python
popular_products = pd.DataFrame(amazon_ratings.groupby('ProductId')['Rating'].count())

most_popular = popular_products.sort_values('Rating', ascending=False)
most_popular.head(10)
```

```python
most_popular.head(10).plot(kind = "bar", color= 'dodgerblue', legend= False)
plt.ylabel('# of Review')
plt. show()
```

![Untitled](Recommendation%20System%20Amazon%20Cosmetics%20based%20on%20SV%20098e3580a0b94740ade5a6ce3e1a8896/Untitled%202.png)

![Untitled](Recommendation%20System%20Amazon%20Cosmetics%20based%20on%20SV%20098e3580a0b94740ade5a6ce3e1a8896/Untitled%203.png)

단순히 리뷰가 많다고 인기 좋은 것은 아니기 때문에 리뷰 & 평점 고려해서 추천해본다.

리뷰 수가 `nReview_thr` 만큼, 평균 평점 `Rate_thr`가 4점 이상인 제품들로 추천해보겠다.

```python
def Rec_popular(nRec, nReview_thr, Rate_thr):
  AMZ_cos= pd.DataFrame(amazon_ratings.groupby('ProductId')['Rating'].mean()) # ProductId 에 따른 Rating의 평균값 groupby     
  AMZ_cos.rename(columns={'Rating':'Mean_Rate'}, inplace=True) # column name 'Rating' -> 'Mean_Rate'

  AMZ_cos['Nreview']=popular_products # 제품명에 따른 리뷰 갯수 열 추가 ('Nreview')
  AMZ_cos= AMZ_cos.sort_values('Nreview', ascending=False) # 제품의 리뷰가 많은 순으로 재정렬

  Top_cos= AMZ_cos[(AMZ_cos['Nreview'] >= nReview_thr) & (AMZ_cos['Mean_Rate'] >= Rate_thr)] # 리뷰 100개 이상, 평균 평점 4 이상 추출

  Top_cos.sort_values('Mean_Rate', ascending=False)
  
  recommendU= list(Top_cos.head(nRec).index)

  print("The Top %i cosmetics on Amazon now ! \n"%nRec, recommendU)

nReview_thr= 100
Rate_thr= 4

Rec_popular(10, nReview_thr, Rate_thr)
```

리뷰 수 100개 이상, 평균 평점 4점 이상인 제품 Top-10은 위와 같다.

---

### 2. 모델 기반 추천 시스템

유저의 평점을 예측하여 평점을 준 적 없는 (== 즉, 정보가 없는) 유저에게도 아이템을 추천할 수 있도록 하는 것이 목표!

**2-0. 평점 예측하는 방법은 주로 SVD를!** 

간단히 하자면 아래 그림 그 잡채,,

![https://velog.velcdn.com/images%2Fvvakki_%2Fpost%2Fefb8e47e-25c8-48bb-909b-a579f6b67b02%2Fimage.png](https://velog.velcdn.com/images%2Fvvakki_%2Fpost%2Fefb8e47e-25c8-48bb-909b-a579f6b67b02%2Fimage.png)

우리가 아는 정보는 유저와 유저가 매긴 평점이다. 
(*이 평점이 csv에 들어있다면 우리는 보통 pandas DataFrame형태로 불러와 `data`라는 이름을 붙여준다)*

데이터로부터 아이템과 유저 리스트를 만들어 그들의 평점을 표(행렬)로 만들면 

User-Item Matrix와 같은 형태의 데이터가 되고, 

모든이들이 모든 아이템에 평점을 남긴 것은 아니기 때문에 값이 있는 곳보다 없는 곳이 더 많다. 
( → so called, **Sparse Matrix** )

이 행렬을 소인수 분해 하듯이 

유저간 유사도 * (~~그림엔 없지만~~ 특이값 ≈ 특징의 강도) *  아이템 간 유사도 행렬을 구하여 결측값을 예측한다. 

[이 양반이 눈에 보이게 설명 굿](https://leebaro.tistory.com/entry/SVD%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%B6%94%EC%B2%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0)

**2-1. 모델 만들기 : SVD based !**

**i) 데이터 전처리**

효율적인 추천 시스템 구축을 위하여 평점을 10개 미만으로 받은 아이템은 제외하고 추천하겠다. 

```python
mProd_ratings = 10
filtered_items = amazon_ratings['ProductId'].value_counts() >= mProd_ratings
filtered_items = filtered_items[filtered_items].index.tolist()

amzRate_filtered = amazon_ratings[amazon_ratings['ProductId'].isin(filtered_items)]
print('The original data frame shape:\t{}'.format(amazon_ratings.shape))
print('The new data frame shape:\t{}'.format(amzRate_filtered.shape))
```

약 51만개 정도의 데이터 샘플이 지워졌다. 

**ii) Surprise SVD**

SVD를 간단히 구현하는 방법으로는 **Surprise** 패키지 또는 **sklearn**의 `truncatedSVD`를 이용하는 방법이 있다. 

나는 극강의 간단을 위해 Surprise를 써보겠다. 

Surprise의 동작 방식은 scikit-learn과 비슷하다. 

1. 객체 생성: `SVD()`
2. 학습: `.fit(<train set>)`
3. 예측:
    - 전체 test set 예측: `.test(<test set>)`
    - 단일 sample 예측: `.predict(<User Id>, <Item Id>`

유의 사항이 있는데, 반드시 **사용자 아이디, 아이템 아이디, 평점 데이터 순** 으로 되어있으며, header 없는 데이터셋만 적용 가능하다 !

- "surprise" 포멧으로 데이터를 불러올 수 있도록 해야함
- csv -> surprise 할 경우, 포멧을 지정해주어야 함 (`Reader`이용)

Surprise는 다양한 SVD 모델을 제공하며, 

`surprise.model_selection`의 `GridSearchCV` : 하이퍼 파라미터를 그리드 서치하여 최적 hyper parameter 찾아주고, 교차 검증 해준다. 

가장 노멀 알고리즘의 Hyper-parameter:

- `n_factors`: 축소 차원 수 ( ∑ 의 dimension)
- `n_epochs`: 전체 데이터 셋 훈련 횟수
- `lr_all`: learning rate

**ii)-1. 필요한 메서드 import**

```python
%pip install surprise
import surprise
from surprise import Dataset, dataset, Reader
from surprise.model_selection import GridSearchCV, cross_validate,train_test_split
from surprise import accuracy

import heapq

from collections import defaultdict
from operator import itemgetter
```

**ii)-2. Surprise DataFrame 형식으로 변환**

위에서 전처리 해준 데이터 (Pandas DataFrame type)를 surprise 타입으로 변환해준다 

```python
# """Pandas Dataframe 2 Surprise Dataframe"""

class Pd2Sur(dataset.DatasetAutoFolds):
    def __init__(self, df, reader):
        self.raw_ratings = [(uid, iid, r, None) for (uid, iid, r) in
                            zip(df['UserId'], df['ProductId'], df['Rating'])]
        self.reader=reader

reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines= 1)
data = Pd2Sur(amzRate_filtered, reader) # 평점이 10개 이하인 items를 제외 & 평점기록 있는 샘플들 데이터셋을 불러옴!
```

**ii)-3. 최적의 Algorithms / Hyper-params 탐색**

최적의 SVD 알고리즘 탐색을 위하여 반복문에 SVD, SVDpp, NormalPredictor, BaselineOnly를 수행한다. 

```python
from surprise import SVD, SVDpp, NormalPredictor, BaselineOnly

algos = []
# 모든 알고리즘을 literate화 시켜서 반복문을 실행시킨다.
for algorithm in [SVD(), SVDpp(), NormalPredictor(),BaselineOnly()]:
    
    # 교차검증
    results = cross_validate(algorithm, data, measures=['RMSE'], cv=3, verbose=False)
    
    # 결과 저장과 알고리즘 이름 추가
    tmp = pd.DataFrame.from_dict(results).mean(axis=0)
    tmp = tmp.append(pd.Series([str(algorithm).split(' ')[0].split('.')[-1]], index=['Algorithm']))
    algos.append(tmp)
    
pd.DataFrame(algos).set_index('Algorithm').sort_values('test_rmse')
```

![Untitled](Recommendation%20System%20Amazon%20Cosmetics%20based%20on%20SV%20098e3580a0b94740ade5a6ce3e1a8896/Untitled%204.png)

최적의 hyperparameter를 찾기위해 `GridSearchCV` :

3-fold validation 을 해준다!

```python
#@title
# """최적값 탐색 (GridSearchCV) & k-fold Validation"""
param_grid = {                # 탐색할 최적hyper-parameter 사전 지정 
    'n_epochs': [20,30],
    'lr_all': [0.005, 0.010],
    'n_factors' : [50,100]
}
gs= GridSearchCV(SVD, param_grid, measures=['rmse', 'mae'], cv=3)
gs.fit(data)

# RMSE
print("Best RMSE score attained: ", gs.best_score['rmse'])
print("Best RMSE params: ", gs.best_params['rmse'])

# MAE
print("Best RAE score attained: ", gs.best_score['mae'])
print("Best RAE params: ", gs.best_params['mae'])

#@title
svd= gs.best_estimator['rmse']
trn= data.build_full_trainset() # 모든 데이터 샘플을 train set으로!
svd.fit(trn)
```

Baseline을 고려한 알고리즘의 성능이 가장 괜찮았으므로, Surprise.BaselineOnly 채택하여, 

epoch 20, learning rate 0.005로 설정한다. 

**ii)-4. Train-Test set**

scikit-learn과 비슷하게 surprise에도 데이터셋을 train, test로 나눠주는 메서드가 있다. 

7:3으로 나눠준다. 

```python
from surprise.model_selection import train_test_split
trn, tst = train_test_split(data, test_size=.3)
```

**Ii)-5. BaselineOnly 학습 & 피팅**

```python
from surprise import BaselineOnly

bsl_options = {
    "method": "sgd",
    "n_epochs": 20,
    "learning_rate": 0.005
}
BLO = BaselineOnly(bsl_options=bsl_options)
BLO.fit(trn)

pred=[]
pred= BLO.test(tst)
```

surprise 학습의 최적화 알고리즘은 sgd(stochastic gradient discent)와 als(alternating least squares).

sgd 방식은 als에 비해 빠르지만 성능은 als가 더 좋다 고 어디서 봤는데…?

해서 stochastic gradient discent 방식을 채택하여 빠른 추천을 받아볼 수 있게 하였다. 

```python
print("RMSE: ",accuracy.rmse(pred))
print("MAE: ", accuracy.mae(pred))
```

이 값들은 `pred` 에 surprise list 형태로 담겨있고, 

샘플의 user id, item id, 유저의 평점, 예측한 유저 평점 등이 튜플로 들어있다. 

```python
BLO.predict("A004511036AHSSV5O4SBY","9788071198")
```

이렇게.

판다스 데이터프레임 형태가 데이터 다루기에 더 편리하기 때문에 

user id, item id, 유저의 평점, 예측한 유저 평점을 열 값으로 가지는 데이터 프레임으로 변환해준다. 

```python
results_list=[]

for result in pred:
  results_list.append([result.uid, result.iid, result.r_ui, result.est])
  

results= pd.DataFrame(results_list,columns= ['UserId','ProductId','Rating','Pred_bl'])
results.head(10)
```

![Untitled](Recommendation%20System%20Amazon%20Cosmetics%20based%20on%20SV%20098e3580a0b94740ade5a6ce3e1a8896/Untitled%205.png)

**ii)-6. Performance**

포포몬쓰 계산

```python
from sklearn import metrics

def scoring(y_true, y_pred):
    r2= round(metrics.r2_score(y_true, y_pred)*100,3)
    
    corr= round(np.corrcoef(y_true, y_pred)[0,1],3)
    mape= round(
        metrics.mean_absolute_percentage_error(y_true, y_pred)*100,3)
    rmse= round(metrics.mean_squared_error(y_true, y_pred, squared=False),3)
    
    df= pd.DataFrame({"R2":r2,
                     "Corr": corr,
                     "RMSE": rmse,
                     "MAPE":mape},
                    index=[0])
    return df

scoring(results.Rating, results.Pred_bl)
```

![?,,](Recommendation%20System%20Amazon%20Cosmetics%20based%20on%20SV%20098e3580a0b94740ade5a6ce3e1a8896/Untitled%206.png)

?,,

실제값과 예측값을 평균점수-리뷰수 산포도로 확인하여, 전체적인 분포가 경향을 잘 따르는지 확인한다. 

이렇게 보는 것이 적절한지 모르겠다.

더 적절한 가시화 방법이 뭔가이쓹까

```python
product_rating_predbl = results.groupby('ProductId')['Pred_bl'].mean()
product_rating_count_predbl = results.groupby('ProductId')['Pred_bl'].count()
product_rating_count_predbl= product_rating_count_predbl[product_rating_count_predbl > 0]
unreliability_predbl = results.groupby('ProductId')['Pred_bl'].std(ddof = -1)
unique_products_list_predbl = results.ProductId.unique()

data_model_predbl = pd.DataFrame({'Rating': product_rating_predbl[unique_products_list_predbl],\
                                 'Count': product_rating_count_predbl[unique_products_list_predbl], \
                                 'Unreliability': unreliability_predbl[unique_products_list_predbl]})

product_rating = results.groupby('ProductId')['Rating'].mean()
product_rating_count = results.groupby('ProductId')['Rating'].count()
product_rating_count= product_rating_count[product_rating_count > 0]
unreliability = results.groupby('ProductId')['Rating'].std(ddof = -1)
unique_products_list = results.ProductId.unique()

data_model = pd.DataFrame({'Rating': product_rating[unique_products_list],
                          'Count': product_rating_count[unique_products_list], 
                          'Unreliability': unreliability[unique_products_list]})

plt.figure(figsize=(6,4))

plt.scatter(data_model_predbl.Rating, data_model_predbl.Count, c='darkgrey', s=1, alpha= 0.8)
plt.scatter(data_model.Rating, data_model.Count, c='crimson', s=1, alpha= 0.05)

plt.xlabel('Rating')
plt.ylabel('Count')
plt.ylim([0,200])
plt.xlim([1,5])
plt.legend(['predicted', 'real'],markerscale=2, frameon= False)

plt.show()
```

![Untitled](Recommendation%20System%20Amazon%20Cosmetics%20based%20on%20SV%20098e3580a0b94740ade5a6ce3e1a8896/Untitled%207.png)

---

### 2-2. 추천해보자

```python
def recommend(user, data, nRecommend):
  
  products= data.ProductId.unique()
  Recommmendable=pd.DataFrame(index= products, columns=['Rate'])

  for it in products:
    pred_rate= BLO.predict(user, it, verbose=False).est
    Recommmendable.loc[it]= pred_rate

  Recommmendable.sort_values(by = 'Rate', ascending = False, inplace = True)
  Recommend4U= list(Recommmendable.index[:nRecommend])

  print("Top-%i Recommendation for %s! \n"%(nRecommend,user), Recommend4U)
```

데이터, 유저 등의 정보를 넣으면 학습까지 해주는 함수를 만들기에는 너무 복잡해서 일단

모델 학습을 시킨 다음 써먹을 수 있는 함수를 만든다. 

이때 모델 이름은 반드시 BLO 여야함,,ㅎ

유저 (`user`), 데이터 (`data`) , 추천 받을 갯수(`nRecommend`)를  인자로 넣으면,

데이터에 있는 모든 아이템에 대한 유저의 평점을 예측한다.

그 중 top `nRecommend` 개를 반환한다.  

```python
recommend('A004511036AHSSV5O4SBY', amazon_ratings, 15)
```

A004511036AHSSV5O4SBY 씨의 취향에 맞을지는 모르겠지만 일단 나는 추천해줬다. 

### future work,,

- 성능향상
    - 문제점: 추천에 16초나 걸림,,
    - 해결방안:
        - 유저가 이미 사용해 본 물건은 제외하고 추천하기?
    
- scikit-learn의 truncatedSVD 이용해서 성능 비교해보기
