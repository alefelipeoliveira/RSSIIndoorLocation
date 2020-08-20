###########################################################
# Edited from:
# Cell Phone Trilateration Algorithm - 101 computing
# https://www.101computing.net/cell-phone-trilateration-algorithm/
###########################################################

from pathloss import calculate_distance
from error import error

#A function to apply trilateration formulas to return the (x,y) intersection point of three circles
def track(x1,y1,r1,x2,y2,r2,x3,y3,r3):
  A = 2*x2 - 2*x1
  B = 2*y2 - 2*y1
  C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
  D = 2*x3 - 2*x2
  E = 2*y3 - 2*y2
  F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
  x = (C*E - F*B) / (E*A - B*D)
  y = (C*D - A*F) / (B*D - A*E)
  return x,y

def Trilateration(Positions, Anchors, Pathloss_model):

  n, C = Pathloss_model['n'][0], Pathloss_model['C'][0]

  d_A, d_B, d_C, x_calc, y_calc, error_list = [], [], [], [], [], []

  for x in list(Positions['RSSI A']):
    d_A.append(calculate_distance(x, n, C))

  for x in list(Positions['RSSI B']):
      d_B.append(calculate_distance(x, n, C))

  for x in list(Positions['RSSI C']):
      d_C.append(calculate_distance(x, n, C))

  Positions['d_A'], Positions['d_B'], Positions['d_C'] = d_A, d_B, d_C

  for i in range(len(list(Positions['x']))):
    x,y = track(Anchors['x'][0],Anchors['y'][0],Positions['d_A'][i],Anchors['x'][1],Anchors['y'][1],Positions['d_B'][i],
    Anchors['x'][2],Anchors['y'][2],Positions['d_C'][i])
    x_calc.append(x)
    y_calc.append(y)
    error_list.append(error(x, Positions['x'][i], y, Positions['y'][i]))

  Positions['x_calc'], Positions['y_calc'], Positions['error']  = x_calc, y_calc, error_list

  return Positions
