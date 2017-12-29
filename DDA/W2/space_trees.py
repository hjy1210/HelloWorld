# Write your crossmatch function here.
import numpy as np
import numpy as np
import time
from astropy.coordinates import SkyCoord
from astropy import units as u

def crossmatch(cat_1, cat_2, max_dist):
  """ cat_2,cat_2 are Nx2 array. max_dist is scalar, all of float(degree) 
  results: 
    match: a list of id1,id2,mindistance(degree)
    mismatch: a list of id1
  """
  start = time.perf_counter()
  sky_cat1 = SkyCoord(cat_1*u.degree, frame='icrs')
  sky_cat2 = SkyCoord(cat_2*u.degree, frame='icrs')
  closest_ids, closest_dists, closest_dists3d = sky_cat1.match_to_catalog_sky(sky_cat2)

  # print(cat1,cat2,max_dist)
  match=[]
  mismatch=[]
  for i in range(len(sky_cat1)):
    if closest_dists[i].value<=max_dist:
      match.append((i,closest_ids[i],closest_dists[i].value))
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
