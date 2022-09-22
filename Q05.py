#백준 10986번
#연속된 구간의 합 => 사용 알고리즘 prefix sum
#모듈러연산 (A + B) % C와 (A%C + B%C) % C의 결과는 동일
#[i, j] 구간의 합은 sum[j] - sum[i-1]

#문제풀이: (sum[j] - sum[i-1]) % M 이 0인 순서쌍 (i, j)의 개수?
# (sum[j]-sum[i-1])%M = 0
# ==> sum[j]%M-sum[i-1]%M = 0
# ==> sum[j]%M = sum[i-1]%M
# sum[j]%M와 sum[i-1]%M 의 값이 0일 경우도 포함시키기


#반복문으로 여러줄 입력받는 상황 시,
#시간초과 뜨니까 input 초기화시켜서 입력받기
import sys, math
input = sys.stdin.readline

n,m = map(int, input("숫자갯수, 나눌수:").split())
num = list(map(int, input("숫자입력:").split()))

#나머지만 담는 배열 생성
sum = [0]*(n+1)

for i in range(1,n) :
    num[i] += num[i-1] #누적합으로 갱신
    sum[num[i]%m] +=1 #해당 누적합을 m으로 나눴을 때 나머지라는 값에 1추가

#0의 갯수 + 나머지가 같은 것들의 조합
ans = sum[0]

for i in sum:
    if i >= 2:
        ans += math.comb(i,2)
print(ans)