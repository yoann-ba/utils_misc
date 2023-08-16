

import numpy as np


# SEE BOTTOM



# converts an angle in degrees to an angle in radians
def degree_to_rad(degree_angle):
    return (np.pi/180) * degree_angle

# converts an angle in radians to an angle in degrees
def rad_to_degree(rad_angle):
    return (180/np.pi) * rad_angle

# converts a Degree, (Arc)Minute, (Arc)Second angle to degrees
def DMS_to_degree(degree, minute, second):
    return degree + (minute/60) + (second/3600)

# long, lat in radians
# consider north and east as positive, but should work regardless
# spherical approximation, 0.05 - 0.10 % error around france's latitude
# slow, lots of trigonometry
def ed_williams_dist(long1, lat1, long2, lat2):
    
    R = 6366710
    
    delta_long = long1 - long2
    delta_lat = lat1 - lat2
    
    d = np.sin(delta_lat/2)**2 + np.cos(lat1)*np.cos(lat2) * np.sin(delta_long/2)**2
    d = 2 * np.arcsin(np.sqrt(d))
    
    return d*R

# lat in degree
# creates the correction constants necessary for the distance function
def cheap_ruler_constants(lat):
    
    m = 1000 # 1000 for meters
    
    c = np.cos(degree_to_rad(lat))
    c2 = 2 * c * c - 1
    c3 = 2 * c * c2 - c
    c4 = 2 * c * c3 - c2
    c5 = 2 * c * c4 - c3
    
    kx = m * (111.41513 * c - 0.09455 * c3 + 0.00012 * c5)  # longitude correction
    ky = m * (111.13209 - 0.56605 * c2 + 0.0012 * c4) # latitude correction
    
    return kx, ky

# long, lat in degrees
# better approximation of Vincenty's formula, also faster
# <0.00% error for france's latitude and <100 km distance
# could try being Numba'd for speed if desired
def cheap_ruler_distance(long1, lat1, long2, lat2, kx, ky):
    
    dx = (long1 - long2) * kx
    dy = (lat1 - lat2) * ky
    return np.sqrt(dx * dx + dy * dy)

# long, lat in degrees
# delta lat, delta lon version
def cheap_ruler_distance_delta(delta_lat, delta_lon, kx, ky):
    
    dx = delta_lon * kx
    dy = delta_lat * ky
    return np.sqrt(dx * dx + dy * dy)


##########
## demo ##

# long1, lat1, long2, lat2 = ... # in degrees
#
# kx, ky = cheap_ruler_constants(0.5*(lat1+lat2))
# 
# cheap_ruler_distance(long1, lat1, long2, lat2, kx, ky)

##########


#############
## sources ##

# Vincenty computes the distance on the earth to the milimeter
# way too complicated
# https://en.wikipedia.org/wiki/Vincenty%27s_formulae#Inverse_problem

# Haversine == Ed Williams assumes the earth is spherical
# needs a lot of trigonometry, so slow
# https://www.movable-type.co.uk/scripts/latlong.html
# http://edwilliams.org/avform147.htm
# https://en.wikipedia.org/wiki/Haversine_formula

# Cheap ruler assumes the eart is flat at small distances
# approximates Vincenty better, also runs faster (no trig)
# https://blog.mapbox.com/fast-geodesic-approximations-with-cheap-ruler-106f229ad016
# https://www.govinfo.gov/content/pkg/CFR-2005-title47-vol4/pdf/CFR-2005-title47-vol4-sec73-208.pdf
# https://github.com/doublemap/cheap-ruler-python

#############






