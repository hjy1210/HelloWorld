import numpy as np
from astropy.io import fits
def mean_fits(fitsfiles):
  list=[]
  for i in range(len(fitsfiles)):
    list.append(fits.open(fitsfiles[i])[0].data)
  data=np.stack(list)
  return np.mean(data,axis=0)
