# Write your crossmatch function here.
import numpy as np
import time
def angular_dist(r1,d1,r2,d2):
  """ all angle are in radian"""
  b=np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1-r2)/2)**2
  a=np.sin(np.abs(d1-d2)/2)**2
  return 2.0*np.arcsin(np.sqrt(a+b))

def find_closest(cat, ra, dec):
  """ra,dec is radian"""
  min=angular_dist(cat[0][0],cat[0][1],ra,dec)
  id=0
  n=len(cat)
  for i in range(1,n):
    dist=angular_dist(cat[i][0],cat[i][1],ra,dec)
    if dist<min:
      min=dist
      id=i
  return (id,min)
def crossmatch(cat_1, cat_2, max_dist):
  """ cat_2,cat_2 are Nx2 array. max_dist is scalar, all of float(degree) 
  results: 
    match: a list of id1,id2,mindistance(degree)
    mismatch: a list of id1
  """
  start = time.perf_counter()
  max_dist=np.radians(max_dist)
  cat1=np.radians(cat_1)
  cat2=np.radians(cat_2)
  # print(cat1,cat2,max_dist)
  match=[]
  mismatch=[]
  for i in range(len(cat1)):
    id,min=find_closest(cat2,cat1[i][0],cat1[i][1])
    if min<=max_dist:
      match.append((i,id,np.degrees(min)))
    else:
      mismatch.append(i)
  
  spent = time.perf_counter() - start
  return match,mismatch,spent

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)
