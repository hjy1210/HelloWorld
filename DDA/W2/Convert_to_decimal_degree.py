def hms2dec(h,m,s):
  return 15.0*(h+m/60.+s/3600.)
def dms2dec(d,m,s):
  if d>=0:
    return (d+m/60.+s/3600.)
  else:
    return (d-m/60.-s/3600.)
