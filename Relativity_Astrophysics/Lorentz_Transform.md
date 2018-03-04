## The Lorentz Transformation: Relating time and space for different reference frames
* Set forth the mathematical form of the Lorentz transformation.
* Explain it's basis and work through a few reality checks.
* Derive the explicit form for the Lorentz transformation.

##  Lorentz Transformation 的推導
由
* 線性變換

$$\begin{array}{rcl}
\Delta x&=&A\Delta x'+B\Delta t'\\
\Delta t&=&C\Delta x'+D\Delta t'
\end{array}$$
* Lorentz interval 不變性

推導Lorentz Transform

### **考慮 $\Delta x'=0$ 的特殊情形**
$$\begin{array}{rcl}
\Delta x&=&B\Delta t'\\
\Delta t&=&D\Delta t'
\end{array}$$
因為 $\beta=\frac{\Delta x}{\Delta t}=\frac{B}{D}$，所以 $B=\beta D$。


因為 $(\Delta t)^2-(\Delta x)^2=(D^2-B^2)(\Delta t')^2=D^2(1-\beta^2)(\Delta t')^2$，根據Lorentz interval的不變性，
$D^2(1-\beta^2)=1$，因此 $D=\frac{1}{\sqrt{1-\beta^2}}=\gamma$，$B=\beta\gamma$。

### **考慮一般情形**
$$\begin{array}{rcl}
\Delta x&=&A\Delta x'+\beta\gamma\Delta t'\\
\Delta t&=&C\Delta x'+\gamma\Delta t'
\end{array}$$

因為 $(\Delta t)^2-(\Delta x)^2=(C^2-A^2)(\Delta x')^2+\gamma^2(1-\beta^2)(\Delta t')^2+2(C\gamma-A\beta\gamma)\Delta x'\Delta t'$，根據Lorentz interval的不變性，

$$\begin{array}{rcl}
C&=& \beta A \\
C^2-A^2&=&-1
\end{array}$$

得到 $A=\gamma, C=\beta\gamma$。

所以 Lorentz Transform 為

$$\begin{array}{rcl}
\Delta x&=&\gamma\Delta x'+\beta\gamma\Delta t'\\
\Delta t&=&\beta\gamma\Delta x'+\gamma\Delta t'
\end{array}$$

其中的 $\gamma=\frac{1}{1-\beta^2}$ 為 Lorentz factor。

### Lorentz transform 與速度相加
$$\frac{\Delta x}{\Delta t}=\frac{\gamma \Delta x'+\beta\gamma\Delta t'}{\beta\gamma\Delta x'+\gamma\Delta t'}=\frac{\gamma u'+\beta\gamma}{\beta\gamma u'+\gamma}=\frac{u'+\beta}{1+u'\beta}$$

```
def velocity_add(u,v):
  return (u+v)/(1+u*v)

print(velocity_add(0.9,0.9))
# 0.994475138121547
```
### 完整的 Spacetime Lorentz Transform
$$\left(\begin{array}{r}
\Delta t\\
\Delta x\\
\Delta y\\
\Delta z
\end{array}\right)=
\left(\begin{array}{cccc}
\gamma & \beta\gamma & 0 & 0\\
\beta\gamma & \gamma & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1
\end{array}\right)
\left(\begin{array}{r}
\Delta t'\\
\Delta x'\\
\Delta y'\\
\Delta z'
\end{array}\right)$$

## Moving Train

### Using ruler to determine the length of the train
Two events occur simultaneously at two ends of train in ground frame, $\Delta t=0$ and $\Delta x=L$ is the length of train measured in ground frame.

因為 $\Delta t=0$，所以 $\gamma \Delta t'+\beta\gamma \Delta x'=0$，得到 $\Delta t'=-\beta \Delta x'$。由此 

$$\Delta x=\gamma \Delta x'+\beta\gamma\Delta t'=\gamma(1-\beta^2)\Delta x'=\frac{\Delta x'}{\gamma}$$
```
20/np.sqrt(1-0.9**2)
# 45.883146774112362
20/np.sqrt(1-0.0001**2)
# 20.000000100000001
```
### Using passage of time to determine the length of the train
Two events are two ends of train pass origin of ground frame.

因為 $\Delta x=0$，所以 $\gamma \Delta x'+\beta\gamma \Delta t'=0$，得到 $\Delta t'=- \Delta x'/\beta$。由此 

$$\Delta t=\gamma \Delta t'+\beta\gamma\Delta x'=\beta\gamma(1-\beta^{-2})\Delta x'=\frac{-\Delta x'}{\gamma\beta}$$

則

$$L=\beta \Delta t=\frac{-\Delta x'}{\gamma}$$

## supernova 1987A
[supernova 1987A](http://hubblesite.org/news_release/news/2007-10)

[SN1987a.pdf](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a37558bf7307277c7462948623d241f8/c4x/CornellX/Astro2290x/asset/SN1987a.pdf)

## Star Crossed Lovers or Star Wars
[Star Crossed Lovers](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/60510da0fac186d9bb3d62a632b485ae/c4x/CornellX/Astro2290x/asset/lovers.pdf)

## 摘要
* Determined how to combine velocities in special relativity (the Law of Addition of Velocities).
Contrasted this result with the simple addition of velocities of Galilean physics.
* Found the Galilean result to be a good approximation when velocities are small compared to the  speed of light and light travel times are negligible compared to time intervals of interest.
* Derived the Lorentz transformation.
* Analyzed length measurement and simultaneity.
Reviewed the astrophysical significance of SN1987a.
Studied how the line of simultaneity depends upon relative motion.
* Considered the consequences for causality if faster than light travel were possible.