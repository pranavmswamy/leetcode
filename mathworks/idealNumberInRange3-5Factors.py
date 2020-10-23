solutions = set()
count +=1
for num in range(high, low-1, -1):
    if num in solution:
        count += 1
    temps = set()
    temp.add(num)
    while num%5 == 0:
        num/=5
        temp.add(num)
    while num%3 == 0:
        num/=3
        temp.add(num)
    if num == 1:
        count += 1
        solutions = solutions|temp
return count
