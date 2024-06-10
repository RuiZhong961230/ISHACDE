########################################################################
# _______ ___________ ______ ______ ___ ___
# / _____||___ ____| / __ \ | _ \ \ \ / /
# | | __ | | | | | | | |_) | \ V /
# | | |_ | | | | | | | | ___/ > <
# | |__| | | | | |__| | | | / _ \
# \______| |__| \______/ |__| /__/ \__\
#
#       Version 1.0
# GTOPX - Space Mission Benchmarks
# --------------------------------
# This is an example program to test evaluate the ten
# benchmark instances of GTOPX, which are:
#
#  No. 1 : Cassini1
#  No. 2 : Cassini2
#  No. 3 : Messenger (reduced)
#  No. 4 : Messenger (full)
#  No. 5 : GTOC1
#  No. 6 : Rosetta
#  No. 7 : Sagas
#  No. 8 : Cassini1-MINLP
#  No. 9 : Cassini1-MO
#  No. 10 : Cassini1-MO-MINLP
#
# For each benchmark, the number of objetives (o), variables (n)
# and constraints (m) are given. Note that benchmark 8 and 10 include
# integer (discrete) variables, which are located at the end of the
# solution vector "x". The arrays "xl" and "xu" denote the lower and
# upper bounds (also called box-constraints) for each benchmark. The
# array "x" given in this file is the best known solution vector.
#
# For further information on GTOPX, see here:
#
# http://www.midaco-solver.com/index.php/about/benchmarks/gtopx
#
# For further information on ESA's original GTOP, see here:
#
# https://www.esa.int/gsp/ACT/projects/gtop/
#
########################################################################
import ctypes
from ctypes import *
import os.path
########################################################################
pi = 3.14159265359


def gtopx(benchmark, x, o, n, m):
  if (os.name == "posix"):
      lib_name = "gtopx.so"  # Linux//Mac/Cygwin
  else:
      lib_name = "gtopx.dll"  # Windows
  lib_path = os.path.dirname(os.path.abspath(__file__)) + os.path.sep+lib_name
  CLIB = ctypes.CDLL(lib_path)
  f_ = (c_double * o)()
  benchmark_ = c_long(benchmark)
  x_ = (c_double*n)()
  for i in range(0, n):
      x_[i] = c_double( x[i])
  if (m > 0):
      g_ = (c_double * m)()
  if (m ==0):
      g_ = (c_double * 1)()
  CLIB.gtopx(benchmark_, f_, g_, x_)
  f = [0.0] * o
  g = [0.0] * m
  for i in range(0, o):
      f[i] = f_[i]
  for i in range(0, m):
      g[i] = g_[i]
  return f, g


########################################################################
######################### INFORMATION FUNCTION #############################
########################################################################
def Cassini1_info():
    n = 6  # number of variables
    xl = [-1000.0, 30.0, 100.0, 30.0, 400.0, 1000.0]  # lower bounds
    xu = [0.0, 400.0, 470.0, 400.0, 2000.0, 6000.0]  # upper bounds
    xbest = [-789.783943378288200,  158.323732108266285, 449.385881146596375, 54.716205454453835,  1024.696123466647350, 4552.813287140832472]  # best known solution
    return n, xl, xu, xbest


def Cassini2_info():
    n = 22  # number of variables
    xl = [-1000.0, 3.0, 0.0, 0.0, 100.0, 100.0, 30.0, 400.0, 800.0, 0.01, 0.01, 0.01, 0.01, 0.01, 1.05, 1.05, 1.15, 1.7,
          -pi, -pi, -pi, -pi]
    xu = [0.0, 5.0, 1.0, 1.0, 400.0, 500.0, 300.0, 1600.0, 2200.0, 0.9, 0.9, 0.9, 0.9, 0.9, 6.0, 6.0, 6.5, 291.0, pi,
          pi, pi, pi]
    xbest = [-779.892433765485862, 3.269389635419130, 0.529407294615286, 0.381751843366415, 168.170645682811767,
         424.058270269247089, 53.307534897793914, 589.771798786665386, 2199.999664613031655, 0.774320294727850,
         0.535144168179482, 0.010162398685082, 0.143320205523028, 0.342141889743363, 1.358780632871789,
         1.050000000000000, 1.306778082760443, 69.812518900340208, -1.593182624457761, -1.959566444199341,
         -1.554766541909198, -1.513431338508497]
    return n, xl, xu, xbest


def Messenger1_info():
    n = 18  # number of variables
    xl = [1000.0, 1.0, 0.0, 0.0, 30.0, 30.0, 30.0, 30.0, 0.01, 0.01, 0.01, 0.01, 1.1, 1.1, 1.1, -pi, -pi, -pi]
    xu = [4000.0, 5.0, 1.0, 1.0, 400.0, 400.0, 400.0, 400.0, 0.99, 0.99, 0.99, 0.99, 6.0, 6.0, 6.0, pi, pi, pi]
    xbest = [1171.409193645348751, 1.416813313841063, 0.378357145940231, 0.500444156719544, 400.000000000000000,
             178.660500793105172, 299.257943316104672, 180.676511826540832, 0.236306459404079, 0.010000000000000,
             0.832671030271973, 0.313063859849465, 1.773712475346063, 3.035650952106482, 1.100000000000000,
             1.350498194299928, 1.094691285475327, 1.344639678649996]
    return n, xl, xu, xbest


def Messenger2_info():
    n = 26  # number of variables
    xl = [1900.0, 2.5, 0.0, 0.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 1.1, 1.1,
          1.05, 1.05, 1.05, -pi, -pi, -pi, -pi, -pi]
    xu = [2300.0, 4.05, 1.0, 1.0, 500.0, 500.0, 500.0, 500.0, 500.0, 600.0, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99, 6.0,
          6.0, 6.0, 6.0, 6.0, pi, pi, pi, pi, pi]
    xbest = [2037.877864567844426, 4.050000190734863, 0.556720539555961, 0.634706307625142, 451.651542959219398,
         224.694006511996577, 221.438483720560384, 266.073371482564824, 357.959170121390741, 534.104338857377456,
         0.482413583122892, 0.733817341605811, 0.699337665254241, 0.740616124926094, 0.828723386566668,
         0.902861270673425, 1.723741116076976, 1.100000023841858, 1.049999952316284, 1.049999952316284,
         1.049999952316284, 2.767484583120401, 1.573418587459163, 2.629307841350829, 1.622878432547001,
         1.609458990319683]
    return n, xl, xu, xbest


def GTOC1_info():
    n = 8
    xl = [3000.0, 14.0, 14.0, 14.0, 14.0, 100.0, 366.0, 300.0]
    xu = [10000.0, 2000.0, 2000.0, 2000.0, 2000.0, 9000.0, 9000.0, 9000.0]
    xbest = [6810.405216554911021, 168.374697626641421, 1079.474093199302388, 56.387311981695156, 1044.092886333879960,
         3820.841817730225102, 1044.327260191322694, 3397.213494950476161]
    return n, xl, xu, xbest


def Rosetta_info():
    n = 22
    xl = [1460.0, 3.0, 0.0, 0.0, 300.0, 150.0, 150.0, 300.0, 700.0, 0.01, 0.01, 0.01, 0.01, 0.01, 1.06, 1.05, 1.05,
          1.05, -pi, -pi, -pi, -pi]
    xu = [1825.0, 5.0, 1.0, 1.0, 500.0, 800.0, 800.0, 800.0, 1850.0, 0.9, 0.9, 0.9, 0.9, 0.9, 9.0, 9.0, 9.0, 9.0, pi,
          pi, pi, pi]
    xbest = [1542.802723, 4.478444171, 0.73169868, 0.878289696, 365.2423131, 707.7546444, 257.3238516, 730.4837236, 1850.0,
         0.512067, 0.810371727, 0.2758878, 0.119192979, 0.43674223, 2.657626174, 1.05, 3.197806169, 1.056221792, -1.253888118,
             1.78760233, -1.594671417, -1.977325495]
    return n, xl, xu, xbest


def Sagas_info():
    n = 12
    xl = [7000.0, 0.0, 0.0, 0.0, 50.0, 300.0, 0.01, 0.01, 1.05, 8.0, -pi, -pi]
    xu = [9100.0, 7.0, 1.0, 1.0, 2000.0, 2000.0, 0.9, 0.9, 7.0, 500.0, pi, pi]
    xbest = [7020.097177851856031, 5.345389359284895, 0.000448998383992, 0.500375810090538, 789.417121854524453,
             483.997594689921016, 0.494622005701901, 0.010000000000000, 1.050000000000000, 10.852293531100093,
             -1.572146302248028, 1.945325688944222]
    return n, xl, xu, xbest


########################################################################
######################### OBJECTIVE FUNCTION #############################
########################################################################
def penalty(f, g):
    w = 1e7  # penalty coefficient
    epsilon = 1e-4  # threshold
    p = 0
    if len(g) > 0:
        for con in g:
            if con >= -epsilon:
                pass
            else:
                p += w * -con
    return f[0] + p


def Cassini1(X):
    benchmark = 1
    n = 6  # number of variables
    m = 4  # number of constraints
    [f, g] = gtopx(benchmark, X, 1, n, m)  # evaluate solution x
    return penalty(f, g)


def Cassini2(X):
    benchmark = 2
    n = 22  # number of variables
    m = 0  # number of constraints
    [f, g] = gtopx(benchmark, X, 1, n, m)  # evaluate solution x
    return penalty(f, g)


def Messenger1(X):
    benchmark = 3
    n = 18  # number of variables
    m = 0  # number of constraints
    [f, g] = gtopx(benchmark, X, 1, n, m)  # evaluate solution x
    return penalty(f, g)


def Messenger2(X):
    benchmark = 4
    n = 26  # number of variables
    m = 0  # number of constraints
    [f, g] = gtopx(benchmark, X, 1, n, m)  # evaluate solution x
    return penalty(f, g)


def GTOC1(X):
    benchmark = 5
    n = 8  # number of variables
    m = 6  # number of constraints
    [f, g] = gtopx(benchmark, X, 1, n, m)  # evaluate solution x
    return penalty(f, g)


def Rosetta(X):
    benchmark = 6
    n = 22  # number of variables
    m = 0  # number of constraints
    [f, g] = gtopx(benchmark, X, 1, n, m)  # evaluate solution x
    return penalty(f, g)


def Sagas(X):
    benchmark = 7
    n = 12  # number of variables
    m = 2  # number of constraints
    [f, g] = gtopx(benchmark, X, 1, n, m)  # evaluate solution x
    return penalty(f, g)
