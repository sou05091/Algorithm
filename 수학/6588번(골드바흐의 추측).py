# 시간 초과
# 모든 소수를 구하는 방법
def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
    if(a%2==0):
        return False
  return True

# 덧셈 경우의수 구하는 방법
def find_sum(arr, target):
    result = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                result.append((arr[i],arr[j]))         
    return result

while True:
    n = int(input())
    if n == 0:
        break
    rs = []
    for i in range(n+1):
        if(isPrime(i)):
            rs.append(i)
    result = find_sum(rs,n)
    if len(result) == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        print(f"{n} = {result[0][0]} + {result[0][1]}")



#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 말도 안되는 gpt의 정답
import sys

def eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i] == True:
            for j in range(i * 2, n + 1, i):
                sieve[j] = False

    return sieve

sieve = eratosthenes(1000000)
primes = [i for i in range(2, 1000001) if sieve[i]]

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    for prime in primes:
        if sieve[n - prime]:
            print(f"{n} = {prime} + {n - prime}")
            break