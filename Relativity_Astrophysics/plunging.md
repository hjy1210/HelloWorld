## Schwarzschild Geometry
$$d\tau^2=(1-\frac{2M}{r})dt^2-\frac{1}{1-\frac{2M}{r}}dr^2-r^2d\phi^2$$

## 考慮向黑洞中心運動的質點。

給定首尾兩事件(0,d_0),(T,d_T)，質點m移動的世界線遵循年齡極質原則。

令 r(t) 為質點的運動軌跡，則其在首尾兩事件間的年齡為

$$\begin{array}{rcl}\int_0^T \frac{d\tau}{dt}dt&=&\int_0^T \frac{\sqrt{(1-\frac{2M}{r})dt^2-\frac{1}{1-2M/r}dr^2}}{dt}dt\\
 &=&\int_0^T \sqrt{(1-\frac{2M}{r})-\frac{1}{1-\frac{2M}{r}}\dot{r}^2}dt\\
 &\equiv& \int_0^T L(r,\dot{r}) dt
\end{array}$$

由[變分法](https://en.wikipedia.org/wiki/Calculus_of_variations)，$r(t)$ 必須每滿足[Beltrami identity](Beltrami identity)

$$L-\dot{r}\frac{\partial L}{\partial \dot{r}}=\text{const} $$


整理得

$$L-\dot{r}\frac{-\frac{\dot{r}}{1-\frac{2M}{r}}}{L}=\frac{1-\frac{2M}{r}}{L}=\text{const}$$

也就是說，直接向黑洞中心運動的質點之軌跡滿足方程式

$$(1-\frac{2M}{r})\frac{dt}{d\tau}=\text{const}$$

在無限遠處，是特殊相對論的範疇，滿足 $\frac{dt}{d\tau}=\frac{E}{m}$，故 const=$\frac{E}{m}$，從而

$$\frac{E}{m}=(1-\frac{2M}{r})\frac{dt}{d\tau}$$

### 無限遠處觀點，質點m從無限遠處靜止出發
 若質點m從無限遠處靜止出發，則 $E=m$，此時 $r(t)$ 滿足

$$(1-\frac{2M}{r})\frac{dt}{d\tau}=1$$

### 無限遠處觀點，質點m從無限遠處以初速 $v$ 出發
若質點m從無限遠處以初速 $v$ 出發，則 $E=m\frac{1}{\sqrt{1-v^2}}\equiv m\gamma$，此時 $r(t)$ 滿足

$$(1-\frac{2M}{r})\frac{dt}{d\tau}=\frac{1}{\sqrt{1-v^2}}$$

### 無限遠處觀點，質點m從$r_0$處靜止出發，能量多少？
式子
$\frac{E}{m}=(1-\frac{2M}{r})\frac{dt}{d\tau}$ 中的 $d\tau=dt_{\text{shell}}=\sqrt{1-\frac{2M}{r_0}}dt$，故


$$\frac{E}{m}=\sqrt{1-\frac{2M}{r_0}}$$

### 無限遠處觀點，無限遠處出發的自由落體，$\frac{dr}{dt}=?$
$$\begin{array}{rcl}1&=&(1-\frac{2M}{r})\frac{dt}{d\tau}\\
&\equiv&f \frac{dt}{d\tau}\\
&=&f\frac{dt}{\sqrt{fdt^2-\frac{1}{f}dr^2}}\\
&=&f\frac{dt}{\sqrt{f-\frac{1}{f}\dot{r}^2}dt}
\end{array}$$
故

$$ f^2=f-\frac{1}{f}\dot{r}^2
$$

$$\dot{r}^2=f^2-f^3=f^2(1-f)=(1-\frac{2M}{r})^2\frac{2M}{r}$$

所以

$$\dot{r}=-(1-\frac{2M}{r})\sqrt{\frac{2M}{r}}$$

### Shell觀點，無限遠處出發的自由落體，$\frac{dr_\text{shell}}{dt_\text{shell}}=?$

$$\begin{array}{rcl}\frac{dr_\text{shell}}{dt_\text{shell}}&=&\frac{\sqrt{1/f}dr}{\sqrt{f}dt}\\
&=&\frac{dr}{fdt}=\frac{\dot{r}}{f}\\
&=&-\sqrt{\frac{2M}{r}}
\end{array}$$

### Shell觀點，無限遠處出發的自由落體，經過身邊時觀察到的能量 $E_\text{shell}=?$
$$E_\text{shell}=m\frac{dt_\text{shell}}{d\tau_\text{shell}}=m\frac{1}{\sqrt{1-(\frac{dr_\text{shell}}{dt_\text{shell}})^2}}=\frac{m}{\sqrt{1-\frac{2M}{r}}}=\frac{E}{\sqrt{1-\frac{2M}{r}}}$$

### 自由落體觀點，無限遠處靜止出發的自由落體，穿過$2M$之後經過多久到達黑洞中心

$$\begin{array}{rcl} 
\int_{2M}^0 \frac{d\tau}{dr}dr&=&\int_{2M}^0 \frac{\sqrt{f-\frac{\dot{r}^2}{f}}}{\dot{r}}dr\\
&=&-\int_{2M}^0\sqrt{\frac{f}{\dot{r}^2}-\frac{1}{f}}dr\\
&=&-\int_{2M}^0\sqrt{\frac{f}{f^2\frac{2M}{r}}-\frac{1}{f}}dr\\
&=&-\int_{2M}^0\sqrt{\frac{\frac{r}{2M}-1}{f}}dr\\
&=&-\int_{2M}^0\sqrt{\frac{\frac{r-2M}{2M}}{1-\frac{2M}{r}}}dr\\
&=&-\int_{2M}^0\sqrt{\frac{r}{2M}}dr\\
&=&\sqrt{\frac{1}{2M}}\frac{2}{3}(2M)^{\frac{3}{2}}\\
&=&\frac{4}{3}M
\end{array}$$

### 自由落體觀點，靜止出發的自由落體，穿過$2M$到達黑洞中心所耗時間的最大值

設自由落體從 $r=r_0$ 出發，由 $2M$ 到中心的時間用 $T_{r_0}$ 表示，則 $\lim_{r_0->2M^+}T_{r_0}$ 為所求的值。

自由落體從 $r=r_0$ 出發，遵循的方程式為
$$\frac{E}{M}=\sqrt{1-\frac{2M}{r_0}}=(1-\frac{2M}{r})\frac{dt}{d\tau}\equiv f\frac{dt}{d\tau}$$

$$\frac{d\tau}{dt}=f\sqrt{\frac{r_0}{r_0-2M}}\equiv f K$$

另一方面

$$
\frac{d\tau}{dt}=\sqrt{f-\frac{\dot{r}^2}{f}}
$$

結合上面兩式，得到
$$
\dot{r}=-f\sqrt{1-fK^2}
$$

接著

$$
d\tau=\frac{d\tau}{dr}dr=\frac{\frac{d\tau}{dt}}{\frac{dr}{dt}}dr=\frac{fK}{-f\sqrt{1-fK^2}}dr
=\frac{-1}{\sqrt{\frac{1}{K^2}-f}}dr$$

最後
$$
\begin{array}{rcl}
\lim_{r_0->2M^+}T_{r_0}&=&\lim_{r_0->2M^+}\int_{2M}^0 \frac{-1}{\sqrt{\frac{1}{K^2}-f}}dr\\
&=&\lim_{K->\infty}\int_{2M}^0 \frac{-1}{\sqrt{\frac{1}{K^2}-f}}dr\\
&=&\int_{2M}^0\frac{-1}{\sqrt{-f}}dr\\
&=&\int_{0}^{2M}\frac{1}{\sqrt{\frac{2M}{r}-1}}dr\\
&=&4M\int_0^\infty\frac{1}{(1+u^2)^2}du\ [\text{變數變換}u=\sqrt{\frac{2M}{r}-1}]\\
&=&4M\int_0^{\pi/2}\cos^2\theta d\theta\ [\text{變數變換}u=\tan\theta]\\
&=&\pi M
\end{array}
$$
