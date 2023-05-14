import math
from data87 import *

#x = Sum{T ^ alpha * A * cos(B + C * T)}
MJD0=2415020.0
TWOPI=6.283185307179586477
PI=3.141592653589793238
VSOP_A1000=365250.0	#/* days per millenium */
VSOP_MAXALPHA=5		#/* max degree of time */
J2000 = (2451545.0 - MJD0)     # yes, 2000 January 1 at 12h */
VSOP_ASCALE=1e8 #/ * amplitude factor as stored * /

def vsop87_my(mj, obj):
    vx_map = [
        vx_mercury, vx_venus, vx_mars, vx_jupiter,
        vx_saturn, vx_uranus, vx_neptune, None, vx_earth,
    ]
    vn_map = [
        vn_mercury, vn_venus, vn_mars, vn_jupiter,
        vn_saturn, vn_uranus, vn_neptune, None, vn_earth,
    ]
    vx_obj = vx_map[obj]
    vn_obj = vn_map[obj]

    t = [0.0] * (VSOP_MAXALPHA + 1)
    i = 0
    cooidx = 0
    alpha = 0
    if obj == 7 or obj > 8:
        return 2

    ret = [0.0] * 3

    t[0] = 1.0
    t[1] = mj / VSOP_A1000
    for i in range(2, VSOP_MAXALPHA + 1):
        t[i] = t[i - 1] * t[1]
    for cooidx in range(3):
        alpha = 0
        while vn_obj[alpha+1][cooidx]:
            term = 0.0
            for i in range(vn_obj[alpha][cooidx], vn_obj[alpha+1][cooidx]):
                a, b, c, arg = vx_obj[i][0], vx_obj[i][1], vx_obj[i][2], vx_obj[i][1] + vx_obj[i][2] * t[1]
                term += a * math.cos(arg)
            ret[cooidx] += t[alpha] * term
            alpha += 1

    for i in range(3):
        ret[i] /= VSOP_ASCALE

    ret[0] -= (ret[0] // TWOPI) * TWOPI
    return ret
