# np.loadtxt, np.stack
import numpy as np
def mean_datasets(files):
  list=[]
  for i in range(len(files)):
    list.append(np.loadtxt(files[i],delimiter=","))
  data=np.stack(list)
  return np.round(np.mean(data,axis=0),1)
