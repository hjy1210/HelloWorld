# Write your find_closest function here
import numpy as np
def hms2dec(h,m,s):
      return 15.0*(h+m/60.+s/3600.)
def dms2dec(d,m,s):
  if d>=0:
    return (d+m/60.+s/3600.)
  else:
    return (d-m/60.-s/3600.)

def angular_dist(ra1,dec1,ra2,dec2):
  r1=np.radians(ra1)
  r2=np.radians(ra2)
  d1=np.radians(dec1)
  d2=np.radians(dec2)
  b=np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1-r2)/2)**2
  a=np.sin(np.abs(d1-d2)/2)**2
  return np.degrees(2.0*np.arcsin(np.sqrt(a+b)))

def import_bss():
  # id h m s d m s
  cat = np.loadtxt('bss.dat', usecols=range(1, 7))
  res=[]
  for i in range(len(cat)):
    res.append((i+1,hms2dec(cat[i][0],cat[i][1],cat[i][2]),dms2dec(cat[i][3],cat[i][4],cat[i][5])))
  return res

def find_closest(cat, ra, dec):
  """ra,dec is indegree"""
  min=angular_dist(cat[0][1],cat[0][2],ra,dec)
  id=cat[0][0]
  for i in range(1,len(cat)):
    dist=angular_dist(cat[i][1],cat[i][2],ra,dec)
    if dist<min:
      min=dist
      id=cat[i][0]
  return (id,min)



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  cat = import_bss()
  
  # First example from the question
  print(find_closest(cat, 175.3, -32.5))

  # Second example in the question
  print(find_closest(cat, 32.2, 40.7))
