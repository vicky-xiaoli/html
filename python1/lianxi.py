num=[12,37,5,42,8,3]
nu = []
mu = []
for i in range (0,len(num)):
    if num[i] % 2 == 1:
        nu.append(num[i])
    else:
        mu.append(num[i])
print(mu)
print(nu)