sum = 0
count = 0
for i in range(100,1000):
    if i % 7 == 0 :
        sum += i
        count += 1
average = sum / count
print( "average : " , average)
