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

# ## 소수 만들기 
# **문제 설명**
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.  
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때  
# 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.  
# <br>
#
# **제한사항**  
#
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
# <br>
# **입출력 예**  
#
# nums	result
# [1,2,3,4]	1
# [1,2,7,6,4]	4
# 입출력 예 설명
# 입출력 예 #1
# [1,2,4]를 이용해서 7을 만들 수 있습니다.
#
# 입출력 예 #2
# [1,2,4]를 이용해서 7을 만들 수 있습니다.
# [1,4,6]을 이용해서 11을 만들 수 있습니다.
# [2,4,7]을 이용해서 13을 만들 수 있습니다.
# [4,6,7]을 이용해서 17을 만들 수 있습니다.
# ![image.png](attachment:image.png)
# ![image-2.png](attachment:image-2.png)

nums=[1,2,4]


# +
def solution(nums):

    def isprimeNum(integer):
        import math
        for j in range(2, int(math.sqrt(integer))+1):
            if integer%j == 0:
                return False
                break
        return True
    
    answer = 0
    
    import itertools as tools
    comb= list(tools.combinations(nums,3))
    ncomb= len(comb)

    
    if ncomb == 1:
        tot= sum(comb[0])
        if isprimeNum(tot) == True:
            answer += 1
            print (list(comb[0]),'를 이용해서 ', tot,'을(를) 만들 수 있습니다. n:', answer)
    else:
        for i in range(ncomb):
            tot= sum(comb[i])
    #         print(tot, comb[i])

            if isprimeNum(tot) == True:
                answer += 1
                print (list(comb[i]),'를 이용해서 ', tot,'을(를) 만들 수 있습니다. n:', answer)            
    return answer

solution(nums)
# -

10%10


# ## 폰켓몬
#
# **문제 설명**
# 당신은 폰켓몬을 잡기 위한 오랜 여행 끝에, 홍 박사님의 연구실에 도착했습니다. 홍 박사님은 당신에게 자신의 연구실에 있는 총 N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다고 했습니다.
# 홍 박사님 연구실의 폰켓몬은 종류에 따라 번호를 붙여 구분합니다. 따라서 같은 종류의 폰켓몬은 같은 번호를 가지고 있습니다. 예를 들어 연구실에 총 4마리의 폰켓몬이 있고, 각 폰켓몬의 종류 번호가 [3번, 1번, 2번, 3번]이라면 이는 3번 폰켓몬 두 마리, 1번 폰켓몬 한 마리, 2번 폰켓몬 한 마리가 있음을 나타냅니다. 이때, 4마리의 폰켓몬 중 2마리를 고르는 방법은 다음과 같이 6가지가 있습니다.
#
# 첫 번째(3번), 두 번째(1번) 폰켓몬을 선택
# 첫 번째(3번), 세 번째(2번) 폰켓몬을 선택
# 첫 번째(3번), 네 번째(3번) 폰켓몬을 선택
# 두 번째(1번), 세 번째(2번) 폰켓몬을 선택
# 두 번째(1번), 네 번째(3번) 폰켓몬을 선택
# 세 번째(2번), 네 번째(3번) 폰켓몬을 선택
# 이때, 첫 번째(3번) 폰켓몬과 네 번째(3번) 폰켓몬을 선택하는 방법은 한 종류(3번 폰켓몬 두 마리)의 폰켓몬만 가질 수 있지만, 다른 방법들은 모두 두 종류의 폰켓몬을 가질 수 있습니다. 따라서 위 예시에서 가질 수 있는 폰켓몬 종류 수의 최댓값은 2가 됩니다.
# 당신은 최대한 다양한 종류의 폰켓몬을 가지길 원하기 때문에, 최대한 많은 종류의 폰켓몬을 포함해서 N/2마리를 선택하려 합니다. N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어질 때, N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 그때의 폰켓몬 종류 번호의 개수를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# nums는 폰켓몬의 종류 번호가 담긴 1차원 배열입니다.
# nums의 길이(N)는 1 이상 10,000 이하의 자연수이며, 항상 짝수로 주어집니다.
# 폰켓몬의 종류 번호는 1 이상 200,000 이하의 자연수로 나타냅니다.
# 가장 많은 종류의 폰켓몬을 선택하는 방법이 여러 가지인 경우에도, 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return 하면 됩니다.
# ![image.png](attachment:image.png)
# 입출력 예 설명
# 입출력 예 #1
# 문제의 예시와 같습니다.
#
# 입출력 예 #2
# 6마리의 폰켓몬이 있으므로, 3마리의 폰켓몬을 골라야 합니다.
# 가장 많은 종류의 폰켓몬을 고르기 위해서는 3번 폰켓몬 한 마리, 2번 폰켓몬 한 마리, 4번 폰켓몬 한 마리를 고르면 되며, 따라서 3을 return 합니다.
#
# 입출력 예 #3
# 6마리의 폰켓몬이 있으므로, 3마리의 폰켓몬을 골라야 합니다.
# 가장 많은 종류의 폰켓몬을 고르기 위해서는 3번 폰켓몬 한 마리와 2번 폰켓몬 두 마리를 고르거나, 혹은 3번 폰켓몬 두 마리와 2번 폰켓몬 한 마리를 고르면 됩니다. 따라서 최대 고를 수 있는 폰켓몬 종류의 수는 2입니다.
#
#

# +
def solution(nums):
    import numpy as np
    canget= len(nums)/2
    uniq= len(np.unique(nums))
    
    if canget > uniq:
        kind= uniq
    else: 
        kind= canget
        
        
    return kind

nums= [3,3,3,2,2,4]
solution(nums)


# -

# ## 게임 대진표
# △△ 게임대회가 개최되었습니다.  
# 이 대회는 N명이 참가하고, 토너먼트 형식으로 진행됩니다.  
# N명의 참가자는 각각 1부터 N번을 차례대로 배정받습니다. 그리고, 1번↔2번, 3번↔4번, ... , N-1번↔N번의 참가자끼리 게임을 진행합니다.  
# 각 게임에서 이긴 사람은 다음 라운드에 진출할 수 있습니다.  
# 이때, 다음 라운드에 진출할 참가자의 번호는 다시 1번부터 N/2번을 차례대로 배정받습니다.  
# 만약 1번↔2번 끼리 겨루는 게임에서 2번이 승리했다면 다음 라운드에서 1번을 부여받고, 3번↔4번에서 겨루는 게임에서 3번이 승리했다면  
# 다음 라운드에서 2번을 부여받게 됩니다.  
# 게임은 최종 한 명이 남을 때까지 진행됩니다.
#
# 이때, 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 궁금해졌습니다.  
# 게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B가 함수 solution의 매개변수로 주어질 때,  
# **처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지** return 하는 solution 함수를 완성해 주세요.  
# 단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정합니다.  
#
# <br><br>
# **제한사항**
# N : 21 이상 220 이하인 자연수 (2의 지수 승으로 주어지므로 부전승은 발생하지 않습니다.)
# A, B : N 이하인 자연수 (단, A ≠ B 입니다.)
#
# **입출력 예**
# ![image.png](attachment:image.png)
# **입출력 예 설명**
# *입출력 예 #1*
# 첫 번째 라운드에서 4번 참가자는 3번 참가자와 붙게 되고, 7번 참가자는 8번 참가자와 붙게 됩니다. 항상 이긴다고 가정했으므로 4번 참가자는 다음 라운드에서 2번이 되고, 7번 참가자는 4번이 됩니다. 두 번째 라운드에서 2번은 1번과 붙게 되고, 4번은 3번과 붙게 됩니다. 항상 이긴다고 가정했으므로 2번은 다음 라운드에서 1번이 되고, 4번은 2번이 됩니다. 세 번째 라운드에서 1번과 2번으로 두 참가자가 붙게 되므로 3을 return 하면 됩니다.

# +
def solution(n,a,b):
    import math
    print('a: ',a,", b: ",b)
    answer = 0
    for i in range(int(math.log2(n))):
        compA = a-1 if a%2 == 0 else a+1
        print(compA)
        if compA == b:
            answer= i+1
            return answer
            break
        else:
            a= a//2 if a%2==0 else (a+1)//2
            b= b//2 if b%2==0 else (b+1)//2
            print('a: ',a,", b: ",b)
    return answer


solution(8, 4, 7)

# -

# ## 숫자게임
# **문제 설명**  
#
# xx 회사의 2xN명의 사원들은 N명씩 두 팀으로 나눠 숫자 게임을 하려고 합니다.  
# 두 개의 팀을 각각 A팀과 B팀이라고 하겠습니다. 숫자 게임의 규칙은 다음과 같습니다.  
# <br>
#
# 먼저 모든 사원이 무작위로 자연수를 하나씩 부여받습니다.  
# 각 사원은 딱 한 번씩 경기를 합니다.  
# 각 경기당 A팀에서 한 사원이, B팀에서 한 사원이 나와 서로의 수를 공개합니다.  
# 그때 숫자가 큰 쪽이 승리하게 되고, 승리한 사원이 속한 팀은 승점을 1점 얻게 됩니다.  
#
# 만약 숫자가 같다면 누구도 승점을 얻지 않습니다.  
# 전체 사원들은 우선 무작위로 자연수를 하나씩 부여받았습니다.  
# <br>
# 그다음 A팀은 빠르게 출전순서를 정했고 자신들의 출전 순서를 B팀에게 공개해버렸습니다.  
# B팀은 그것을 보고 자신들의 최종 승점을 가장 높이는 방법으로 팀원들의 출전 순서를 정했습니다.  
# 이때의 B팀이 얻는 승점을 구해주세요.  
# <br>
# A 팀원들이 부여받은 수가 출전 순서대로 나열되어있는 배열 A와 i번째 원소가 B팀의 i번 팀원이 부여받은 수를 의미하는 배열 B가 주어질 때,  
# B 팀원들이 얻을 수 있는 최대 승점을 return 하도록 solution 함수를 완성해주세요.  
# <br>
# **제한사항**
# A와 B의 길이는 같습니다.  
#
# A와 B의 길이는 1 이상 100,000 이하입니다.  
#
# A와 B의 각 원소는 1 이상 1,000,000,000 이하의 자연수입니다.  
# <br>
# **입출력 예**
#  ![image.png](attachment:image.png)
#  
#
# **입출력 예 #1**  
#  ![image-2.png](attachment:image-2.png)
#
#
# A 팀은 숫자 5를 부여받은 팀원이 첫번째로 출전하고, 이어서 1,3,7을 부여받은 팀원들이 차례대로 출전합니다.  
#
# B 팀원들을 4번, 2번, 3번, 1번의 순서대로 출전시킬 경우 팀원들이 부여받은 숫자들은 차례대로 8,2,6,2가 됩니다.  
# 그러면, 첫 번째, 두 번째, 세 번째 경기에서 승리하여 3점을 얻게 되고, 이때가 최대의 승점입니다.  
# <br>
#
# **입출력 예 #2**
#
# B 팀원들을 어떤 순서로 출전시켜도 B팀의 승점은 0점입니다.
#

# #### Try 1:
# B에 주어진 숫자들의 가능한 배열들을 모두 A와 순차 탐색한다.
# 1. 주어진 배열 B가 가질 수 있는 순열들을 리스트 형태로 저장한다.
# 2. 리스트의 요소를 for문 이용하여 순차적으로 A와 비교한다.  
#   2-1. 리스트의 i번째 요소 (i번째 순열)을 다시 for문을 이용해 A와 순차 비교한다.  
#   2-2. A보다 크면 score 점수 +1하며, i번째 요소를 모두 검토하면 (j=마지막 수 일 때) score는 answer에 저장하고 다시 0으로 리셋한다.  
#   2-3. i번 반복
# 3. answer에 저장된 score 중 가장 높은 점수를 반환한다.
#
#

# +
def solution(A, B):
    if min(A) >= max(B):
        return 0
    
    import itertools as tools
    perm= list(tools.permutations(B,len(B)))
    answer= []
    score= 0
    for i in range(len(perm)):
        permB= perm[i]
        for j in range(len(permB)):        
            if permB[j] > A[j]:
                score += 1
        if score >= len(B):
            return max(answer)
            break
        answer= answer+[score]
        score=0
    maxscore= max(answer)
#     answer= np.array(answer)
#     idx= np.where(answer == maxscore)[0]
    
#     print('idx: ',idx)
    
#     for k in idx:
#         print(perm[k])
    return maxscore

A=[5,2,3,7]
B=[2,2,6,8]
solution(A,B)


# -

# #### *문제점*  
#
# 가능한 모든 배열에 대해 모두 순차 비교를 하기 때문에 시간이 너무 많이 걸린다.  
# 이 문제는 B의 배열 순서에 영향을 받기 때문에 B의 순열(서로 다른 nn개의 원소에서 rr개를 중복없이 순서에 상관있게 선택하는 나열)이  
# B가 가질 수 있는 나열들 이다.  
# 따라서 이 테스트와 같이 경기를 치를 수 있는 사원이 팀당 4명일 경우  
# B팀이 낼 수 있는 순열의 갯수는 $_{n}P_{r} = \frac{n\!}{(n-r)\!}$ 이므로 24이다.  
# 이를 A팀과 순차 비교는 24*4회 이며,
# 팀 당 4명이 아니라 수가 늘어나면 상당힌 시간이 걸릴 것이다.  
#
# 이 문제에서 본질은 **얻을 수 있는 최대 점수** 이므로 배열의 순열을 고려할 필요가 없다는 점을 간과하였다.  
#
#

# #### Try 2:  
# A팀과 B팀이 뽑은 수를 정렬하여 순차 비교한다.  
# 첫번째 시도와 달리 최대 비교 횟수는 팀 원들이 부여받은 숫자의 갯수 이다.  
# <br>
# 오름차순 정렬한 A팀 숫자와 B팀의 숫자의 배열을 각각 a,b라고 한다.  
# 이때, a의 최솟값이 b의 최댓값보다 크다면 나머지 b의 값들 모두 a보다 작을 것이다.  
# 이 경우 즉시 score = 0 을 반환한다.
#
#

def solution(A,B):
    a= sorted(A)
    b= sorted(B)
    
    score = 0
    
    if a[0] >= b[-1]:
        return score
    else:
        for i in range(len(a)):
            if a[i] < b[i]:
                score += 1 
        return score



# +
A=[5,1,3,7]
B=[2,2,6,8]

a=sorted(A)
b= sorted(B)
print(a,b)
solution(A,B)

# +
A=[2,2,2,2]
B=[1,1,1,1]

a=sorted(A)
b= sorted(B)
print(a,b)
solution(A,B)


# -

# #### 문제점
# logic에 구멍이 있다.  
# 조건을 추가할 필요가 있을 것 같다.  
# <br>
#
# #### Try 2-1:
# 0. A와 B를 내림차순 정렬하여 각각 a, b라 한다.
# 1. A팀 또는 B팀이 완승하는 경우  
#     1-1. a의 최솟값이 b의 최댓값보다 같거나 크다면, 나머지 b의 값들 모두 a보다 작을 것이다. 이 경우 score = 0.  
#     1-2. a의 최댓값이 b의 최솟값보다 작다면, 모든 b는 a보다 클것이다. 이 경우 score = b의 길이. 
# 2. 내림차순의 a와 b를 순차 비교하여 점수를 update한다.  
#    2-1. a[i] > b[i]라면, a 배열의 그 다음 큰 수와 (a[i+1]과 b[i]) 비교한다.
#         a[i+n] 과 b[i] 비교 끝났다면 (a[i+n] < b[i]의 결과 얻었다면), b[i+1]은 a[i+n+1]부터 비교 하여야 한다. 
#         2-2-1. 이 때 
#         2-2-2. a와 b의 비교가 끝나면 배열에서 없애버린다. 
# + 2-2-1과 2-2-2의 효율을 비교한다.
#   2-2-1: for와 while 과다복용으로 무한 시간 걸린다^_^...& a의 index 지정이 상당히 복잡해짐
#   2-2-2.
#

#2-2-1/
def solution(A,B):
    a= sorted(A, reverse=True)
    b= sorted(B, reverse=True)
    
    score = 0
    
    if a[-1] >= b[0]:
        score = 0
    elif a[0] < b[-1]:
        score = len(b)
    else:
        while a != []:
            print(a,b, score)
#             if a == []:
#                 break
            if a[0] >= b[0]:
                del a[0]
            else: 
                score +=1
                del a[0], b[0]
                
    return score



# +
A=[5,1,3,7]
B=[2,2,6,8]

solution(A,B)

# +
A=[2,2,2,2]
B=[1,1,1,1]

solution(A,B)

# +
A=[1,1,1,1]
B=[3,3,3,3]

solution(A,B)


# -

# ![image.png](attachment:image.png)
#
# #### Try2-1의 효율을 위한 약간의 수정 
# 리스트에서 요소를 제거하는 방법에는 del <list[index]>, <list>.pop(<index>), <list>.remove(<value>)가 있다.  
#     del은 리스트의 인덱스 지정 \& 제거.
#     pop은 리스트의 인덱스 지정 \& 추출값 반환 \& 원래의 리스트에서 제거. 디폴트는 -1.  
#     remove는 리스트에서 값 지정 \& 리스트에서 동일한 값 중 가장 처음 값 제거.  
# 하는 방식이다.  
# index또는 값을 지정해 주었을 때 시간 복잡도는 모두 O(n)이나,  
# 그 중에서 pop은 값을 뽑아내야하기 때문에 조금 더 걸린다는 강의 내용이 있었다.  
#     
# <br>  
#     
# 그러나 list.pop()을 하면 가장 리스트를 뒤질 필요 없이 가장 뒤의 값을 뽑기 때문에 시간 복잡도가 O(1)이다.  
#
# 따라서 del a[0], b[0] 대신 a.pop을 이용 할 수 있도록 수정하여 비교한다.
#     

def solution(A,B):
    a= sorted(A)
    b= sorted(B)
    
    score = 0
    
    if a[0] >= b[-1]:
        score = 0
    elif a[-1] < b[0]:
        score = len(b)
    else:
        while a != []:
            if a[-1] >= b[-1]:
                a.pop()
            else: 
                score +=1
                a.pop()
                b.pop()
                
    return score


# ![image.png](attachment:image.png)
# 효율성 채점 결과 차이 없었다.  
# 아마도 del a[0] 도 a.pop()과 동일하게 리스트에서 해당하는 index를 탐색할 필요 없이 바로 첫 값이기 때문일 것 같다.
#
#
