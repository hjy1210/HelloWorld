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

將月球放在 $\vec{s}=(-d,0,0)$，月球質量m，地球質量M，地球半徑R，潮汐高h。

質點位置$\vec{r}=(x,y,z)$，質量n，$\Delta=\vec{r}-\vec{s}=(x+d,y,z)$，月球作用到質點的力

$$ \vec{F}= -\frac{Gmn}{|\Delta|^3}\Delta$$

$$\frac{\partial\vec{F}}{\partial x}=\frac{Gmn}{d^3}(2,0,0)$$
$$\frac{\partial\vec{F}}{\partial y}=\frac{Gmn}{d^3}(0,-1,0)$$
$$\frac{\partial\vec{F}}{\partial z}=\frac{Gmn}{d^3}(0,0,-1)$$
$$\begin{array}{rcl}\vec{F}&\approx&\vec{F_0}+\left(\frac{\partial\vec{F}}{\partial x}\right)_0 x+\left(\frac{\partial\vec{F}}{\partial y}\right)_0 y+\left(\frac{\partial\vec{F}}{\partial z}\right)_0 z\\
&=& \vec{F_0}+\frac{Gmn}{d^3}(2x,-y,-z)\end{array}$$

潮汐力

$$ \vec{F_t}=\frac{Gmn}{d^3}(2x,-y,-z)$$

從北極經地心移動到赤道，潮汐力對質點所做的功：

$$\begin{array}{rcl}\Delta E_T&=&\int \vec{F_t}\cdot \vec{r}\\
&=&\int_0^R \frac{Gmn}{d^3}ydy+\int_0^R \frac{Gmn}{d^3}2xdx\\
&=&\frac{3GmnR^2}{2d^3}
\end{array}$$

從北極經地心移動到赤道，位能的變化：

$$ \begin{array}{rcl}\Delta E_g&=&GMn(\frac{1}{R-h}-\frac{1}{R+h})\\
&\approx&\frac{GMn}{R^2}2h\end{array}$$

因為 $\Delta E_T=\Delta E_g$，故潮汐高度的估計

$$h=\frac{3mR^4}{4Md^3} $$

此一估計較有說服力。

## 摘要
* Explain why light is bent by gravitational fields without resorting to a calculation
* Sketch the shape of the forces due to the tidal field created by a distant point mass in a freely falling frame
* Estimate the strength of the tidal field across a body of a given size
* Estimate the spatial limits for a free falling frame in common situations (i.e. how a nearby massive star or planets intrudes on the idealized frame)
* Give several examples of astronomical systems which manifest tidal locking
* Explain how a black hole shreds a star that passes nearby
* Be prepared to notice news articles this spring that the black hole has swallowed a nearby object!