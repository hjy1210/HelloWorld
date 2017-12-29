# fits.open, np.argmax
import numpy as np
from astropy.io import fits
def load_fits(file):
  hdulist=fits.open(file)
  data=hdulist[0].data
  r,c=data.shape
  index=np.argmax(data)
  return (index//c, index%c)
