a = 1.0123456789012345679
b = 1.0123456789012345670

print(bool(a == b))

EPS = 0.000001

print(bool(abs(a - b) < EPS))