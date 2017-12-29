from astropy.time import Time,TimeDelta
from astropy.coordinates import get_sun,FK5,PrecessedGeocentric,get_body
from astropy import coordinates as coord
from astropy import constants as const
from astropy.coordinates import SkyCoord
import math
import numpy as np

jieqinames=["春分","清明","穀雨","立夏","小滿","芒種","夏至","小暑","大暑","立秋",
              "處暑","白露","秋分","寒露","霜降","立冬","小雪","大雪","冬至","小寒","大寒","立春","雨水","驚蟄"]
moonshapenames=['朔月','上弦','望月','下弦']
def CCTerm2(start,end,type):
    eighthours=TimeDelta(8*3600,format='sec')
    second=TimeDelta(1,format='sec')
    def termtime(start,end,code):
      middle=start+0.5*(end-start)
      # print((end-start).to('second').value)
      if (end-start).to('second').value<1:
        return ((code+1)%bincount,middle.value)
      gmttime=middle-eighthours
      if type=='jieqi':
        middlecode=get_body('sun', gmttime,  ephemeris='jpl').\
          transform_to(coord.GeocentricTrueEcliptic(equinox=gmttime)).lon.deg // sec
      else:
        sunlongitude=get_body('sun', gmttime,  ephemeris='jpl').\
          transform_to(coord.GeocentricTrueEcliptic(equinox=gmttime)).lon.deg
        moonlongitude=get_body('moon', gmttime,  ephemeris='jpl').\
          transform_to(coord.GeocentricTrueEcliptic(equinox=gmttime)).lon.deg
        middlecode=((moonlongitude-sunlongitude) % 360) //sec
      if middlecode==code:
        return termtime(middle,end,code)
      else:
        return termtime(start,middle,code)

    #print(type)
    start=Time(Time(start,out_subfmt='date').iso)
    end=Time(Time(end,out_subfmt='date').iso)
    daycount=int(round((Time(end)-Time(start)).value))
    # print(start,end,daycount)
    # print(daycount)
    times=start+np.linspace(0.,1.,daycount+1)*(end-start+TimeDelta(3,format='sec')) # 考量潤秒，故加上3秒
    times=Time(Time(times,out_subfmt='date').iso)
    gmttimes=times-eighthours
    if type=='jieqi':
        diflongitudes= get_body('sun', gmttimes,  ephemeris='jpl').\
            transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
        sec=15
    else:
        sunlongitudes=get_body('sun', gmttimes,  ephemeris='jpl').\
            transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
        moonlongitudes=get_body('moon', gmttimes,  ephemeris='jpl').\
            transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
        diflongitudes=(moonlongitudes-sunlongitudes)%360
        sec=90
    res=[]
    bincount=360//sec
    #print(diflongitudes//sec)
    difcode=np.array(diflongitudes//sec,dtype=np.int16)
    difcode=difcode % bincount
    for i in range(len(diflongitudes)-1):
      if difcode[i]!=difcode[i+1]:
        res.append(termtime(times[i],times[i+1],difcode[i]))
    return res


# CCTerm 用來計算從起始日(start)到結束日(end)這段時間的節氣(type='jieqi')或朔望月(type='moon')的日子。
# 函數值為清單(list)，其元素由編號(code)與日期(date)所組成。
def CCTerm1(start,end,type,detail=False):
    eighthours=TimeDelta(8*3600,format='sec')
    onehour=TimeDelta(3600, format='sec')
    oneminute=TimeDelta(60, format='sec')
    onesecond=TimeDelta(1, format='sec')
    oneday=TimeDelta(1, format='jd')
    def diff(d1,d2,mod):
      dif=(d1-d2) % mod
      if dif>mod/2.0:
        dif=dif-mod
      return dif

    def termtime(daytime,unit='hour'):
        if unit=='hour':
            times=daytime+onehour*np.linspace(0,24,25)
        elif unit=='minute':
            times=daytime+oneminute*np.linspace(0,60,61)
        else:
            times=daytime+onesecond*np.linspace(0,60,61)
        gmttimes=times-eighthours
        if type=='jieqi':
            diflongitudes=get_body('sun', gmttimes,  ephemeris='jpl').\
                transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
        else:
            sunlongitudes=get_body('sun', gmttimes,  ephemeris='jpl').\
                transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
            moonlongitudes=get_body('moon', gmttimes,  ephemeris='jpl').\
                transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
            diflongitudes=(moonlongitudes-sunlongitudes)%360
        difmod=diflongitudes % sec
        for i in range(0,len(diflongitudes)-1):
            d1=diff(difmod[i],0,sec)
            d2=diff(difmod[i+1],0,sec)
            if d1<=0 and d2>0:
                if unit=='hour':
                    return(termtime(times[i],unit='minute')) 
                elif unit=='minute':
                    return(termtime(times[i],unit='second')) 
                else:
                    return((int(math.floor(diflongitudes[i+1]/sec)),times[i].value))

        return((-1,''))
    #print(type)
    daycount=int(round((Time(end)-Time(start)).value))
    #print(daycount)
    times=Time(start)+oneday*np.linspace(0,daycount,daycount+1)
    times=Time(Time(times,out_subfmt='date').iso)
    gmttimes=times-eighthours
    if type=='jieqi':
        diflongitudes= get_body('sun', gmttimes,  ephemeris='jpl').\
            transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
        sec=15
    else:
        sunlongitudes=get_body('sun', gmttimes,  ephemeris='jpl').\
            transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
        moonlongitudes=get_body('moon', gmttimes,  ephemeris='jpl').\
            transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
        diflongitudes=(moonlongitudes-sunlongitudes)%360
        sec=90
    res=[]
    difmod=diflongitudes % sec
    for i in range(0,len(diflongitudes)-1):
        d1=diff(difmod[i],0,sec)
        d2=diff(difmod[i+1],0,sec)
        if d1<=0 and d2>0:
            if detail==True:
                res.append(termtime(times[i],'hour'))
            else:
                times.out_subfmt='date'
                res.append((int(math.floor(diflongitudes[i+1]/sec)),times[i].value))
    return(res)

def CCTerm(start,end,type):
    eighthours=TimeDelta(8*3600,format='sec')
    def termtime(daytime,daytime2,code,unit='hour'):
        if unit=='hour':
            times=daytime+np.linspace(0.,1.,25)*(daytime2-daytime)
        elif unit=='minute':
            times=daytime+np.linspace(0.,1.,61)*(daytime2-daytime)
        else:
            times=daytime+np.linspace(0.,1.,61)*(daytime2-daytime)
        gmttimes=times-eighthours
        if type=='jieqi':
            diflongitudes=get_body('sun', gmttimes,  ephemeris='jpl').\
                transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
        else:
            sunlongitudes=get_body('sun', gmttimes,  ephemeris='jpl').\
                transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
            moonlongitudes=get_body('moon', gmttimes,  ephemeris='jpl').\
                transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
            diflongitudes=(moonlongitudes-sunlongitudes)%360
        difcode=diflongitudes // sec
        difcode=[int(difcode[i]) for i in range(len(difcode))]
        for i in range(len(difcode)-1):
          if difcode[i+1]!=code:
            if unit=='hour':
              return termtime(times[i],times[i+1],code,"minute")
            else:
              if unit=='minute':
                return termtime(times[i],times[i+1],code,"second")
              else:
                return ((code+1) % (360//sec),(times[i]+0.5*(times[i+1]-times[i])).value)
        return (-1,"")

    start=Time(Time(start,out_subfmt='date').iso)
    end=Time(Time(end,out_subfmt='date').iso)
    daycount=int(round((Time(end)-Time(start)).value))
    # print(start,end,daycount)
    # print(daycount)
    times=Time(start)+np.linspace(0.,1.,daycount+1)*(end-start+TimeDelta(3,format='sec')) # 考量潤秒，故加上3秒
    times=Time(Time(times,out_subfmt='date').iso)
    gmttimes=times-TimeDelta(8*3600,format='sec')
    if type=='jieqi':
        diflongitudes= get_body('sun', gmttimes,  ephemeris='jpl').\
            transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
        sec=15
    else:
        sunlongitudes=get_body('sun', gmttimes,  ephemeris='jpl').\
            transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
        moonlongitudes=get_body('moon', gmttimes,  ephemeris='jpl').\
            transform_to(coord.GeocentricTrueEcliptic(equinox=gmttimes)).lon.deg
        diflongitudes=(moonlongitudes-sunlongitudes)%360
        sec=90
    res=[]
    difcode=diflongitudes // sec
    difcode=[int(difcode[i]) for i in range(len(difcode))]
    for i in range(len(difcode)-1):
      if difcode[i]!=difcode[i+1]:
        res.append(termtime(times[i],times[i+1],difcode[i],'hour'))
    return res

if __name__ == '__main__':
  import time
  from astropy.time import Time,TimeDelta
  start = time.perf_counter()
  # Cost 7.2305572551966 seconds
  # jieqi=CCTerm1('2017-1-1','2018-3-1','jieqi',True)
  # Cost 25.923758546796343 seconds
  # jieqi=CCTerm2('2017-1-1','2018-3-1','jieqi')
  # Cost 7.019582279715201 seconds
  # jieqi=CCTerm('2017-1-1','2018-3-1','jieqi')
  # Cost 27.93920745377538 seconds
  # darkmoon=CCTerm1('2017-1-1','2018-3-1','moon',True)
  # Cost 107.03038314219037 seconds
  # darkmoon=CCTerm2('2017-1-1','2018-3-1','moon')
  # Cost 28.08751382142731 seconds
  darkmoon=CCTerm('2017-1-1','2018-3-1','moon')
  spent = time.perf_counter() - start
  print("Cost {0} seconds".format(str(spent)))
  #for code,date in jieqi:
  #  print(jieqinames[code]+' '+date)
  for code,date in darkmoon:
    print(moonshapenames[code]+' '+date)