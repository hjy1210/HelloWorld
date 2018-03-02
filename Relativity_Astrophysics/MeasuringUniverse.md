
$$G\frac{Mm}{r^2}=ma$$

$$\frac{GM}{r^2}=a$$


```{python}
G=6.67e-8
M_oplus=5.974e27
R_oplus=6.371e8
print("地表加速度",G*M_oplus/R_oplus**2)
# 981.6933
M_odot=1.99e33
R_odot=6.96e10
print("太陽表面加速度",G*M_odot/R_odot**2)
# 27400.62
```
## 地表附近，自由落體到地表的速度與高度的關係
* $d=\frac{1}{2} g t^2$
* $v=gt$
* $d=\frac{1}{2} g(v/g)^2=\frac{v^2}{2g}$
* $v=\sqrt{2gd}$

```
import numpy as np
print(np.sqrt(2*981.6933*100))
print(np.sqrt(2*981.6933*100)))
```
## 地表遠處，自由落體到地表的速度與距離的關係
從距地心 $d$ 的地方掉到地表時的速度
* $GMm(1/R-1/d)=\frac{1}{2}mv^2$
* $v=\sqrt{\frac{2GM(d-R)}{Rd}}$
* 當 $d>>R$ 時，$v=\sqrt{\frac{2GM}{R}}$
```
au=1.496e13
print(np.sqrt((2*G*M_oplus*(10*au-R_oplus)/R_oplus/au/10))/100000)
print(np.sqrt((2*G*M_oplus/R_oplus))/100000)

```
## 自由落體
[The Apollo 15 Hammer-Feather Drop](https://nssdc.gsfc.nasa.gov/planetary/lunar/apollo_15_feather_drop.html)

[Feather Drop 2](https://www.youtube.com/watch?time_continue=6&v=4z8g8OSOMzY)

## 足球場當作實驗室
要分清楚看見的兩種意思：
* 真的看見
* 推論/會商後的解論

[Apparent Superluminal Motion in 3C279](http://images.nrao.edu/AGN/Quasars/387)

下圖中，看起來類星體(QSO:Quasi-stellar object or quasar)噴出來的物件移動的速度比光速還快，此處的速度是看見的速度，不是推論得的速度。

* $\Delta t_{app}=\frac{c\Delta_t-v\Delta_t \cos\theta}{c}$
* $\Delta x=v\Delta t\sin\theta$
* $v_{app}=\frac{\Delta x}{\Delta t_{app}}=\frac{v\sin\theta}{1-\frac{v}{c}\cos\theta}$

![3C279](3C279.jpg)

## Setting up a lab
Measurements and freely falling frames in special relativity: 

* To perform our measurements, we need rulers and synchronized clocks.
* In freely falling frame A, particles at rest stay at rest; those moving do so at constant velocity. 
* Once we identify a suitable frame A, we can use any frame moving at constant velocity with respect to A.
* Different frames assign different coordinates to the same event; all agree on whether or not motion is unaccelerated; they can differ on directions of velocity or whether objects are at rest or not.
* The speed in each frame is measured with its own clocks and rulers; do not mix measurements from different frames!
* For two frames A and B: The speed of A in B is equal and opposite to the speed of B in A.

## Summary
* We adopted a freely falling frame to annul gravity.  This simplifies the behavior of particles not subject to other forces: those particles at rest stay at rest; those moving do so at constant velocity.
* We described how a multiplicity of equivalent freely falling frames are implied by the existence of just one such frame.
* We filled the lab with observers, rulers and clocks and this is now our ideal laboratory. We're well prepared to start doing physics.
* We recognized some of the essential differences between working in a lab environment and in observing astronomical phenomena.