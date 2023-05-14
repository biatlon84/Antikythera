import math
from vsop87 import *
TWOPI=6.283185307179586477
PI=3.141592653589793238

def spherical2rectangular(spher):
    RA = spher[0]
    Decl = spher[1]
    r = spher[2]
    x = r * math.cos(RA) * math.cos(Decl)
    y = r * math.sin(RA) * math.cos(Decl)
    z = r * math.sin(Decl)
    return (x, y, z)


def rectangular2spherical(x, y, z):
    XsqPlusYsq = x ** 2 + y ** 2
    r = math.sqrt(XsqPlusYsq + z ** 2)  # r
    elev = math.atan2(z, math.sqrt(XsqPlusYsq))  # theta
    az = math.atan2(y, x)  # phi
    az += TWOPI
    return az % TWOPI, elev, r


def sun2planet(planet_x, planet_y, planet_z, earth_x, earth_y, earth_z):
    x_geoc = (planet_x - earth_x)
    y_geoc = (planet_y - earth_y)
    z_geoc = (planet_z - earth_z)
    return rectangular2spherical(x_geoc, y_geoc, z_geoc)


def positions(planet, earth, www):
    posr = spherical2rectangular(planet)
    earth_r = spherical2rectangular(earth)
    return sun2planet(posr[0], posr[1], posr[2], earth_r[0], earth_r[1], earth_r[2])


def angle(an, shift):
    return math.atan2(math.sin(an), math.cos(an) + shift)


def solveKepler(M, e):
    E, Eprime = 0, PI
    while math.fabs(E - Eprime) > 1e-7:
        cosE = math.cos(Eprime)
        E = Eprime
        Eprime = (M - e * (E * cosE - math.sin(E))) / (1 - e * cosE)
    return Eprime


def vr(m, e, a):
    ean = solveKepler(m, e)
    x = a * (math.cos(ean) - e)
    y = a * math.sqrt(1 - e * e) * math.sin(ean)
    r = math.sqrt(x * x + y * y)
    v = math.atan2(y, x)
    return v, r


def true_a(angle_rad, orb_param):
    perihelion = orb_param[0]
    eccentricity = orb_param[1]
    radius = orb_param[2]

    mean_anomaly = angle_rad - perihelion
    true_anomaly = vr(mean_anomaly, eccentricity, radius)

    rA = true_anomaly[0]
    ra = (TWOPI * 2 + rA + perihelion) % TWOPI
    r = true_anomaly[1]
    return ra, 0, r

def mercury_87(days):
    tytyt = vsop87_my(days, 0)  # mercury
    sub = vsop87_my(days, 8)  # earth

    sher = positions(tytyt, sub, True)
    return sher

def venus_87(days):
    tytyt = vsop87_my(days, 1)  # venus
    sub = vsop87_my(days, 8)  # earth

    sher = positions(tytyt, sub, True)
    return sher


def mars_87(days):
    tytyt=vsop87_my(days,2)#mars
    sub= vsop87_my(days,8)#earth

    sher = positions(tytyt, sub, True)
    return sher

def jupiter_87(days):
    tytyt=vsop87_my(days,3)#jupiter
    sub= vsop87_my(days,8)#earth

    sher = positions(tytyt, sub, True)
    return sher

def saturn_87(days):
    tytyt=vsop87_my(days,4)#saturn
    sub= vsop87_my(days,8)#earth

    sher = positions(tytyt, sub, True)
    return sher

def uranus_87(days):
    tytyt=vsop87_my(days,5)#uranus
    sub= vsop87_my(days,8)#earth

    sher = positions(tytyt, sub, True)
    return sher

def neptune_87(days):
    tytyt=vsop87_my(days,6)#neptune
    sub= vsop87_my(days,8)#earth

    sher = positions(tytyt, sub, True)
    return sher

