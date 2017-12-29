# Write your crossmatch function here.
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

def import_super():
# ra.deg, dec.deg
  cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  res=[]
  for i in range(len(cat)):
    res.append((i+1,cat[i][0],cat[i][1]))
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

def crossmatch(bss_cat, super_cat, max_dist):
  match=[]
  mismatch=[]
  for i in range(len(bss_cat)):
    id,min=find_closest(super_cat,bss_cat[i][1],bss_cat[i][2])
    if min<=max_dist:
      match.append((bss_cat[i][0],id,min))
    else:
      mismatch.append(bss_cat[i][0])
  return match,mismatch



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
