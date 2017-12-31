import astropy.units as u
from astropy.coordinates import PrecessedGeocentric,get_body,solar_system_ephemeris,Angle
from astropy.time import Time,TimeDelta
import astropy.constants as const

import numpy as np

def obj_sight(date,objname,diskanglestr,lonstr,latstr,tzinhours):
    """
    date: string, date of observing. 
    objname : string, name of sun, moon or planet in solar system.
    diskanglestr : string, apparent angle of objname.
    lonstr : string, longitute of observing location on earth.
    latstr : string, latitute of observing location on earth.
    ltzinhours : float, time zone in hours of observing location.
    return : print out rise time, set time, transit time and cooresponding alt/az.
    """
    lon=Angle(lonstr)
    lat=Angle(latstr)
    halfdisk=Angle(diskanglestr)*0.5
    date=Time(Time(date,out_subfmt='date').iso)
    times=date+np.linspace(0.,1440.,1441)*TimeDelta(60,format='sec')  # 每分鐘計算位置
    deltat=tzinhours*TimeDelta(3600,format='sec')
    a=const.R_earth.to('m').value       # 地球半徑
    with solar_system_ephemeris.set('jpl'):
        n=len(times)
        gmttimes=times-deltat   # 世界時間 UTC
        # 標的物在及時赤道座標系統座標
        bodies=get_body(objname,gmttimes).transform_to(PrecessedGeocentric(equinox=gmttimes))  
        sides=gmttimes.sidereal_time('apparent', 'greenwich')+lon    # local sidereal time
        x=bodies.cartesian.x.to('m').value        # x,y,z為標的物在及時赤道座標系統的直角座標   
        y=bodies.cartesian.y.to('m').value
        z=bodies.cartesian.z.to('m').value
        px=np.array(a*np.cos(lat)*np.cos(sides))  # px,py,pz 為觀測地在及時赤道座標系統的直角坐標
        py=np.array(a*np.cos(lat)*np.sin(sides))
        pz=np.array(a*np.sin(lat)*np.ones(n))
    positions=np.vstack((px,py,pz)).T  # n x 3 array
    objs=np.vstack((x,y,z)).T          # n x 3 array
    # e_z 的每一行為天頂方向單位向量，e_n的每一行為地表往北單位向量，e_e的每一行為地表往東單位向量
    e_z=np.vstack((np.cos(lat)*np.cos(sides),np.cos(lat)*np.sin(sides),np.sin(lat)*np.ones(n)))  # 3 x n
    e_n=np.vstack((-np.sin(lat)*np.cos(sides),-np.sin(lat)*np.sin(sides),np.cos(lat)*np.ones(n))) # 3 x n
    e_e=np.vstack((-np.sin(sides),np.cos(sides),np.zeros(n)))                 # 3 x n
    coords=np.zeros((n,3))   # coords 的每一列代表標的物在地表座標系統的直角坐標
    az=np.zeros(n)           # az 標的物的方位角，北方為0，往東為正，正東方90度，正南方180度，正西方270度。
    alt=np.zeros(n)          # alt 標的物的仰角
    for i in range(n):
        coords[i]=np.array(np.vstack((e_e[:,i],e_n[:,i],e_z[:,i]))).dot(objs[i]-positions[i])
        r=np.sqrt(coords[i][0]**2+coords[i][1]**2)
        rho=np.sqrt(coords[i][0]**2+coords[i][1]**2+coords[i][2]**2)
        alt[i]=np.arcsin(coords[i][2]/rho)*180/np.pi
        az[i]=np.arctan2(coords[i][0],coords[i][1])*180/np.pi
        if az[i]<0:
            az[i]=az[i]+360
    thresh=-(halfdisk+Angle("0d34m0s")).deg   # 大氣折射，讓光線轉彎了34角分
    altdiff=alt-thresh        # altdif 變號的時候就是標的物升起或沉沒的區間，用內插進行估計
    for i in range(len(times)-1):
        if altdiff[i]*altdiff[i+1] <=0 :
            t=times[i]+(times[i+1]-times[i])*(0-altdiff[i])/(altdiff[i+1]-altdiff[i])
            if altdiff[i]<0:
                print("Rise",t,"Az",az[i])
            else:
                print("Set",t,"Az",az[i])
        if not (az[i] // 180 == az[i+1] // 180) and alt[i]>0:
            if np.abs(az[i]-180)<30:
                ratio=(180-az[i])/(az[i+1]-az[i])
                t=times[i]+(times[i+1]-times[i])*ratio
                print("Transit",t,"Alt",alt[i]+(alt[i+1]-alt[i])*ratio,"Az","South")
            else:
                left=az[i]
                right=az[i+1]
                if left>300:
                    left=left-360
                if right>300:
                    right=right-360
                ratio=(0-left)/(az[i+1]-az[i])
                t=times[i]+(times[i+1]-times[i])*ratio
                print("Transit",t,"Alt",alt[i]+(alt[i+1]-alt[i])*ratio,"Az","North")
# 台北(東經121.5654度，北緯25.032969度，時差+8小時)，標的物太陽(sun)的視角32角分。
# Ex.1
# 用下面指令列印出2018年1月1日在台北的日出、日落、中天時刻以及方位與仰角。
# obj_sight('2018-1-1','sun','0d32m0s','121.5654d','25.032969d',8) 
# Rise 2018-01-01 06:38:47.130 Az 115.066472753
# Transit 2018-01-01 11:57:09.418 Alt 41.9575847767 Az South
# Set 2018-01-01 17:15:36.479 Az 244.828654564
# Ex.2
# obj_sight('2017-12-10','moon','0d32m0s','121.5654d','25.032969d',8)  
# Transit 2017-12-10 05:38:22.471 Alt 73.5230263955 Az South
# Set 2017-12-10 12:05:02.922 Az 278.440772592
# Ex.3
# obj_sight('2017-12-4','moon','0d32m0s','121.5654d','25.032969d',8)
# Set 2017-12-04 06:37:52.044 Az 290.09123571
# Rise 2017-12-04 17:54:55.105 Az 68.7458437964

