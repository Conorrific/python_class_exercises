a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
for number in a:
    if number % 2 == 0:
        print(number)
a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
for number in a:
    if number % 2 == 1:
        print(number)

def count_small(numbers):
  total = 0
  for n in numbers:
    if n < 10:
      total = total + 1
  return total
lotto = [4, 8, 15, 16, 23, 42]
small = count_small(lotto)
print(small)

import this