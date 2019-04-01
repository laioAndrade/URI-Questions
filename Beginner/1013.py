import math
x = input().split(" ")
a = int(x[0])
b = int(x[1])
c = int(x[2])

maiorAB = (a+b+math.fabs(a-b))/2
maior = (maiorAB+c+math.fabs(maiorAB-c))/2

print("%d eh o maior" %(maior))