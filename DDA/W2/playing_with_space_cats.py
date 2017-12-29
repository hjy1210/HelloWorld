# Write your import_bss function here.
# bss.dat, table2.dat fromhttp://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775
# super.csv, cutdown version of mCl1_B21.5_R20_noStepWedges.csv.gz
#    from http://ssa.roe.ac.uk/allSky
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


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)