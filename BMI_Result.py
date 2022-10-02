W=int(input('Please Enter your weight in Kilogram(Kg) : '))
H=float(input('Please Enter your height in Meter(m) : '))
ans = float((W/H**2))
print('%.1f' % ans)
if ans<=18.4:
    print('Underweight')
elif ans>=18.4 and ans<=24.9:
    print('Normal')
else:
    print('Overweight')