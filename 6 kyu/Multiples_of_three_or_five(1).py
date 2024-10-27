def solution(number):
  sum_num = 0
  for i in range(number):
    if (i % 3 == 0 or i % 5 == 0):
      sum_num += i
  return sum_num

#so sum_num is a variable that will contain the number of i in a range of numbers that can be 0 if divided by 3 or 5
# every time we get i divisible by 3 or 5, then sum_num will increase by i
#and so on until the loop ends
#and finally we return the sum of number(i) in the range of number that are divisible by 3 or 5 (sum_num).
