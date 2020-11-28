import sympy as sy

x = sy.symbols('x')

int1 = sy.integrate(x**2,(x,0,1))
print("The definite integral of x^4 between 0 and 1 is", int1 )
int2 = sy.integrate(sy.sin(x),(x,-sy.pi,sy.pi)) 
print("The definite integral of sin(x) between -pi and pi is", int2 )
int3 = sy.integrate(-sy.cos(x),(x,0,sy.pi/2))
print("The definite integral of -cos(x)  between 0 and pi/2 is", int3 )
