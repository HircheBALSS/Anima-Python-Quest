from numpy import sqrt

def is_triangle(a, b, c):
  if a <= 0 or b <= 0 or c <= 0:
    return False
  p = (a + b + c) / 2                         
  aire = sqrt(p * (p - a) * (p - b) * (p - c))
  if aire > 0: 
    return True
  else:
    return False