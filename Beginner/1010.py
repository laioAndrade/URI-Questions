p1 = input().split(" ")
p2 = input().split(" ")

c1 = int(p1[0])
n1 = int(p1[1])
pr1 = float(p1[2])

c2 = int(p2[0])
n2 = int(p2[1])
pr2 = float(p2[2])

total = (n1*pr1) + (n2*pr2)
print("VALOR A PAGAR: R$ %.2f" %total)