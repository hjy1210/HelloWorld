# Write your mean_datasets function here
import numpy as np
def mean_datasets(files):
  list=[]
  for i in range(len(files)):
    list.append(np.loadtxt(files[i],delimiter=",")) # np.loadtxt load a 2d array of data
  data=np.stack(list)
  return np.round(np.mean(data,axis=0),1)

  


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))
  # Run your function with the second example from the question:
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
