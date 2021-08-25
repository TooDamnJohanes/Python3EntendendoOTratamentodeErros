from statistics import mean
lista = [4,5,6,9,7,5,3,2,1,4,5,6,89,7,1,2,456,0,123,-4,-2,-456,-654,7,]
print(sorted(lista)[:len(lista)])

d = {'a':[1,2,3,4], 'b':[4,5,6]}
print(d)

for key, values in d.items():
    for i in values:
        print(i)

data = mean(lista)
data2 = sum(lista)/len(lista)
print(data2)
print(data)

prices = { 'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }
data = max(zip(prices.values(), prices.keys()))
data2 = min(zip(prices.values(), prices.keys()))
data3 = []
for value in prices.values():
    data3.append(value)
data3 = mean(data3)
print(data)
print(data2)
print(data3)