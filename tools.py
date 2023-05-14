import math
import datetime
TWOPI=6.283185307179586477
PI=3.141592653589793238

year   =365.2421897

# corretion for dif betvine spring eqanox j2000 and the ziro of the hands
j2000_start = 946728000  # date="1/1/2000" 12

equinox = 0.5 - (100.46435 / 360)

#correction for leap year
cor_c=59-0.5

colck_scale =(385,  # radius
              400,  #center of the clock X
              400,  #center of the colck Y
              800,
              800)
r = colck_scale[0]
xc = colck_scale[1]
yc = colck_scale[2]
x = colck_scale[3]
y = colck_scale[4]

def true_an(fraction_of_year):
    # Perihelion = 0.88/365.24219 #102.94719 deg j2000
    Perihelion=102.94719/360
    Perihelion=0.5-Perihelion
    eccentricity = 0.01671022  # Earth's orbital eccentricity
    # eccentricity = 0.3
    # Perihelion = 0
    mean_anomaly = 2 * math.pi * (fraction_of_year+Perihelion)
    eccentric_anomaly = mean_anomaly + eccentricity * math.sin(mean_anomaly)
    true_anomaly = 2 * math.atan2(math.sqrt(1 + eccentricity) * math.sin(eccentric_anomaly / 2),
                                  math.sqrt(1 - eccentricity) * math.cos(eccentric_anomaly / 2))
    y=(true_anomaly / (2 * math.pi))-Perihelion
    return (y+2)%1

def jan_to_equ(day_sw):
    day_sw+=1
    return (day_sw - equinox)%1

def equ_to_jan(day_sw):
    return (day_sw + equinox)%1


def leap_corr(j2000_days):
    cor_z = j2000_days / 128  # correction 365.25 * 128
    cor_z = (-cor_z * 4)
    leap_yea =((j2000_days-cor_c)%(365.25*4))
    leap_yea+=(cor_c+cor_z)
    x=1-leap_yea/(365.25*4)
    return x

def min(s):
    dg = s * 360
    sss = (dg % 1) * 60
    return str(math.floor(dg))+"      "+str(sss)

def days_to_yday(days):
    # days-=36889
    # Calculate datetime object for J2000
    j2000 = datetime.datetime(2000, 1, 1, 0, 0, 0)
    # Calculate datetime object for the input number of days
    input_date = j2000 + datetime.timedelta(days=days)
    # Get the day of the year for the input date
    day_of_year = input_date.timetuple().tm_yday
    return day_of_year-1
