# Import the running_stats function
from helper import running_stats
from astropy.io import fits
import numpy as np
import math
# Write your median_bins_fits and median_approx_fits here:
def median_bins_fits(files,B):
  mean,std=running_stats(files)
  # print(mean.shape,std.shape)
  #print(std==0)
  minval=mean-std
  maxval=mean+std
  width=(2/B*std)
  #print(width==0)
  left_bin=np.zeros(mean.shape)
  bins=np.zeros((mean.shape[0],mean.shape[1],B))
  R,C=mean.shape
  #print(R,C)
  for i in range(len(files)):
    data=fits.open(files[i])[0].data
    #print(data)
    for r in range(R):
      for c in range(C):
        if data[r,c]<minval[r,c]:
          left_bin[r,c]+=1
        else:
          #print(r,c,data[r,c],minval[r,c],width[r,c])
          if width[r,c]==0:
            index=0
          else:
            index=int(math.floor((data[r,c]-minval[r,c])/width[r,c]))
          if index>=B:
            continue
          else:
            bins[r,c,index]+=1
  return mean,std,left_bin, bins 

def singleMedian(mean,std,left_bin,bins,half):
  B=len(bins)
  width=2*std/B
  for b in range(B):
    left_bin+=bins[b]
    if left_bin>=half:
      return mean-std+width*(b+0.5)
  return mean+std-width*0.5
      

def median_approx_fits(files,B):
  mean,std,left_bin,bins=median_bins_fits(files,B)
  R=mean.shape[0]
  C=mean.shape[1]
  half=(len(files)+1)/2
  median=np.zeros(mean.shape)
  for r in range(R):
    for c in range(C):
      median[r,c]=singleMedian(mean[r,c],std[r,c],left_bin[r,c],bins[r,c,:],half)
  return median

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with examples from the question.
  mean, std, left_bin, bins = median_bins_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  median = median_approx_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
  print(mean[100,100])
  print(std[100,100])
  print(left_bin[100,100])
  print(bins[100,100,:])
  print(median[100,100])
  mean, std, left_bin, bins = median_bins_fits(['image{}.fits'.format(str(i)) for i in range(11)], 4)
  median = median_approx_fits(['image{}.fits'.format(str(i)) for i in range(11)], 4)
  print(mean[100,100])
  print(std[100,100])
  print(left_bin[100,100])
  print(bins[100,100,:])
  print(median[100,100])
