fh=open('prac-1.txt','w')
Fahrenheit = 98
a=(Fahrenheit-32)*5/9
fh.write('Temperature in celsius: ' +str(a)+'\n')
Celsius = 57
b=(Celsius*9/5)+32
fh.write('Temperature in Fahrenheit : ' +str(b)+'\n')
fh.close()