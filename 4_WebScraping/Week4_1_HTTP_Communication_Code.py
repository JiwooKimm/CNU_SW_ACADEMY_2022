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

# ### HTTP 통신 코드
# Python의 `request` 라이브러리를 이용해 HTTP 통신을 진행할 수 있다.  
#
# #### 0. `requests` 라이브러리 설치

# %pip install requests

# #### 1. 정보를 달라고 요청하기 GET
# (1) `requests` 라이브러리를 불러온 후, NAVER 홈 페이지를 요청한 후 응답 받기.

import requests as req
res=req.get("https://www.naver.com")
res

# Response [응답 코드]
# - 200 :OK! 문제 없음
# - 404 :Page non Found 

#Header 확인: `.headers`
res.headers

# 여러 정보 (e.g., 날짜, 시간, 인코더, ..)을 반환해줌

#Body를 텍스트 형태로 확인하기: .text
res.text[:1000]

# 이 경우, 단순히 글자를 1000개 가지고 옴..!
# 따라서 특정 속성(attribute)를 가져와야 할 필요 있음

# #### 2. 정보 갱신을 요청하기 POST  
# 항상 정보를 가져오기만 하는 경우는 없을 것.
# 우리의 정보를 제공하여 서버가 그에 따른 응답을 하도록 요청할 때도 있음. e.g.,**로그인**!  
# 이러한 요청을 처리하는 HTTP Method가 **POST**.  
# <br>
# POST 활용하기 위해 다음 사이트 이용해보자: https://webhook.site  
#
# <span style="#6E7A7F"> uniq address 생성해주는 서버 생성함!</span>
#

# +
#payload와 함께 POST를 보내보자: requests.post()
payload = {"name" : 'Hello' , "age" : 13}

res = req.post("https://webhook.site/9292ca53-f514-4109-aad7-33e180ca9c9c", payload)

#상태코드(status code) 확인: .status_code
res.status_code
