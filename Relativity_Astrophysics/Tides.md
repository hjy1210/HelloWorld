## Gravity's Rainbow
* Infer the bending of light from a thought experiment.
* Visualize tidal fields.
* Discover that tidal fields limit the size of the free fall lab.
* Estimate the height of tides on the Earth, our own free fall frame.
* Describe how tidal fields can disrupt objects.
* Take a trip to the Galactic center.
* Anticipate that this spring an object will venture too close to the black hole and be tidally disrupted.

## Tides
地球半徑R，地球質量M，月球質量m，月地距d，小質點質量n，潮汐差h。
* 高低潮受地球引力差 $GM n(\frac{1}{(R-h)^2}-\frac{1}{(R+h)^2})\approx 4Mh/R^3$
* 受月球引力差 $Gm n(\frac{1}{(d-R-h)^2}-\frac{1}{(d+R+h)^2})\approx 4mR/d^3$
* 兩者互相抵消，因此：$h\approx \frac{mR^4}{Md^3}$

```
def tides(R,M,m,d):
  return m*R**4/M/d**3

from astropy import constants as const
from astropy import units as u
print(tides(const.R_earth,const.M_earth,7.342e22*u.kg,384400*u.km).decompose())
# 月球造成的潮汐 0.358165060489809 m
print(tides(const.R_earth,const.M_earth,const.M_sun,1*u.au).decompose())
# 太陽造成的潮汐 0.16457465909114394 m
```

[Tidal locking](https://en.wikipedia.org/wiki/Tidal_locking)

[Alpha Centauri Bb](https://en.wikipedia.org/wiki/Alpha_Centauri_Bb)

[tides-notes.pdf](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/2eae9941bb170f59ee5957807f9c4e7b/c4x/CornellX/Astro2290x/asset/tides-notes.pdf)