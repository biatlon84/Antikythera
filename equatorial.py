import math
def ecliptic2equatorial(xeclip, yeclip, zeclip, oblecl):
    """Transform ecliptic to equatorial projection.

    Args:
        xeclip: value on x axis of ecliptic plane.
        yeclip: value on y axis of ecliptic plane.
        zeclip: value on z axis of ecliptic plane.
        oblecl: obliquity of the ecliptic, approximately 23.4 degrees for earth

    Returns:
        tuple: x, y, z equatorial projection

    """
    #    oblecl = math.radians(oblecl)

    xequat = xeclip
    yequat = yeclip * math.cos(oblecl) - zeclip * math.sin(oblecl)
    zequat = yeclip * math.sin(oblecl) + zeclip * math.cos(oblecl)

    return (xequat, yequat, zequat)


def equatorial2ecliptic(xequat, yequat, zequat, oblecl):

    """Transform equatorial to ecliptic projection.

    Args:
        xequat: value on x axis of equatorial plane
        yequat: value on y axis of equatorial plane
        zequat: value on z axis of equatorial plane
        oblecl: obliquity of the ecliptic, approximately 23.4 degrees for earth

    Returns:
        tuple: x, y, z ecliptic projection

    """

    #    oblecl = math.radians(oblecl)
    xeclip = xequat
    yeclip = yequat * math.cos(-oblecl) - zequat * math.sin(-oblecl)
    zeclip = yequat * math.sin(-oblecl) + zequat * math.cos(-oblecl)
    return (xeclip, yeclip, zeclip)

    def convert_coordinat(ra, dec, r,days):
    rad = (ra, dec, r)
    oblecl = 23.439 - 0.0000004 * days  # Obliquity of Ecliptic
    vv1, vv2, vv3 = spherical2rectangular(rad)
    vvv1, vvv2, vvv3 = equatorial2eclipticy(vv1, vv2, vv3, oblecl*math.pi/180)
    equatorial2ecliptic = rectangular2spherical(vvv1, vvv2, vvv3)
    return equatorial2ecliptic
