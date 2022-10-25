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

# ### 윤리적으로 웹 스크래핑 / 크롤링 진행하기
#
# <br>
#
# #### robots.txt 🤖
# **robots.txt**는 <span style="background-color:#dcffe4">웹사이트 및 웹 페이지를 수집하는 로봇들의 무단 접근을 방지</span>하기 위해 만들어진 로봇 배제 표준 (robtos exclusion standard)이자 국제 권고안.  
# 일부 스팸 봇, 악성 목적을 지닌 가짜 클라이언트 로봇은 웹사이트에 진짜 클라이언트에 접근한다.  
# 그리고 무단으로 웹 사이트 정보를 긁어가거나, 웹 서버에 부하를 줄 수 있다.  
# 이러한 로봇들으 무분별한 접근을 통제하기 위해 마련된 것이 robots.txt!  
# 그래서 가끔 웹 서버에 요청을 보내도 거부 당하는 일이 있는데, 이것은 우리를 무단 봇으로 집작하고 웹 서버에서 접근을 막은 것..!  
# 따라서 우리는 브라우저에게 내가 스팸이나 악성 봇이 아니라 사람이라는 것을 알려주면 될 것이다.  
# <br>
# 이때 브라우저에게 전달하는 것이 **사용자 에이전트 (user agent) 정보** 인것!<br>
#
# <span style="color:gray">나의 User Agent: https://www.whatismybrowser.com/detect/what-is-my-user-agent/</span>
# <br>
#
# 사용자 에이전트는 '요청을 보내는 것의 주체'!  
# 웹의 경우 브라우저, 웹 페이지를 수집하는 봇, 다운로드 관리자, 웹에 접근하는 다른 앱 모두가 사용자 에이전트임.  
# 웹 서버에 요청할 때 사용자 에이전트 HTTP 헤더 (user agent HTTP header)에 나의 브라우저 정보를 전달하면 웹 서버가 나를 진짜 사용자로 인식할 수 있게 됨.  
# <br>
# ⚠️ 웹 스크래핑의 원칙:<br>
# <span style="color:#FF5471">
#     1. 요청하고자 하는 서버에 과도한 부하를 주지 않는다.<br>
#     2. 가져온 정보를 사용할 때 저작권과 데이터베이스권에 위배되지 않는지 주의한다.</span>

# #### 0. robots.txt 가져오기
# robots.txt는 웹 페이지의 메인 주소에 '/robots.txt'를 입력하면 확인 가능.
# e.g., google: www.google.com/robots.txt

# +
#requests 모듈을 불러온 후, 다음 웹사이트에 대한 robots.txt 정책 확인

import requests as req

res = req.get("https://www.naver.com/robots.txt")
# -

print(res.text)

# <span style="color:gray">여기서!<br></span>  
# - 'User-agent': 규칙이 적용되는 대상 사용자 에이전트
# - 'Disallow' : 크롤링을 금지할 웹 페이지
# - 'Allow': 크롤링을 허용할 웹 페이지 
#     
# <span style="color:gray">자세한 규약은 robots.txt 공식 홈페이지 참조!</span>

res= req.get("https://dailyearth.tistory.com/robots.txt")

print(res.text)


