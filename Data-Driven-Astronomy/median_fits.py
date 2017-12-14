# Write your function median_FITS here:
import numpy as np
from astropy.io import fits
import time,sys
def median_fits(files):
  start = time.perf_counter()
  list=[]
  for i in range(len(files)):
    list.append(fits.open(files[i])[0].data)
  data=np.stack(list)
  median=np.median(data,axis=0)
  seconds=time.perf_counter()-start
  return (median,seconds,sys.getsizeof(data)/1024)



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])