```
import astropy.units as u
import numpy as np
def ex89():
  vb=np.array([10.0,0.0])*u.m/u.s
  va=np.array([0.0,15.0])*u.m/u.s
  ma=1000*u.kg
  mb=2000*u.kg
  #m=ma+mb
  p= (ma*va+mb*vb)
  print("momentum=",p)
  print("velocity=",p/(ma+mb))
  return (p,p/(ma+mb))

res=ex89()
np.linalg.norm(res[1].value)*res[1].unit
```