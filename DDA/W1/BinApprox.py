# Write your median_bins and median_approx functions here.
import numpy as np
import math
def median_bins(list,B):
  a=np.array(list,dtype=float)
  std=np.std(a)
  mu=np.mean(a)
  minval=mu-std
  width=2*std/B
  bins=np.zeros(B,dtype=int)
  lowcount=0
  for i in range(len(a)):
    #print((a[i]-minval)/width)
    index=int(math.floor((a[i]-minval)/width)) # Why // not work???
    #print(index)
    if index<0:
      lowcount+=1
    else:
      if index>=B:
        continue
      else:
        bins[index]+=1
  return (mu,std,lowcount,bins)

def median_approx(list,B):
  mu,std,lowcount,bins=median_bins(list,B)
  half=(len(list)+1)/2
  for i in range(B):
    lowcount+=bins[i]
    if lowcount>=half:
      return mu-std+(2*std)/B*(i+0.5)
  return mu+std-(2*std)/B*0.5

# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
  
  print( median_bins([0, 1], 5))
  print(median_approx([0, 1], 5))
  print(int(math.floor(1/0.2)))