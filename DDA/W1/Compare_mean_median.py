# if __name__ == '__main__':
# datalist.sort
def list_stats(datalist):
  n=len(datalist)
  sum=0
  for i in range(n):
    sum=sum+datalist[i]
  
  datalist.sort()
  if (n % 2 ==1):
    median=datalist[n//2]
  else:
    if (n==1):
      median=datalist[0]
    else:
      median=(datalist[n//2-1]+datalist[n//2])/2
  return (median,sum/n)



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)