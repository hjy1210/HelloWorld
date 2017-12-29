import numpy as np
def calc_stats(filepath):
  data = np.loadtxt(filepath, delimiter=',')
  return (np.round(np.mean(data),1),np.round(np.median(data),1))
