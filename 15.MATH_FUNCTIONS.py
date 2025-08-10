#MATH FUNCTIONS IN PYTHON
import math # module
print("FUNCTIONS AND METHODS IN MATH MODULE : \n")
print(dir(math))
print("\n")
#round(value,how many poinnts)
print("ROUND() FUNCTION : ",round(-3.77812,3))
#abs(value)
print("ABS() FUNCTION : ",abs(-5))
print("\nNUMBER-THEORITICAL REPRESENTATION FUNCTIONS : \n")
#ceil(value) if +ve=>+1 , -ve=>same
print("CEIL() FUNCTION (+ve) : ",math.ceil(3.3))
print("CEIL() FUNCTION (-ve) : ",math.ceil(-3.3))
#floor(value) if +ve=>same , -ve=>+1
print("FLOOR() FUNCTION (+ve) : ",math.floor(3.3))
print("FLOOR() FUNCTION (-ve) : ",math.floor(-3.3))
#trunc(value) for +ve or -ve =>same
print("TRUNC() FUNCTION (+ve) : ",math.trunc(3.3))
print("TRUNC() FUNCTION (-ve) : ",math.trunc(-3.3))
#comb(n,k) [n>k] , formula=>n! / (k!*(n-k)!)
print("COMB() FUNCTION : ",math.comb(3,2))
#copysign(x,y) , copy sign of 'y' to 'x' 
print("COPYSIGN() FUNCTION : ",math.copysign(1,-2)) #return in 'float'
#fabs(value)  , '0' to 'value' distance
print("FABS() FUNCTIOn : ",math.fabs(4-5)) # return in 'float'
#ffactorial(value) [value>=0]
print("FACTORIAL() FUNCTION : ",math.factorial(5))
#fmod(x,y) if x>y =>remainder or x<y => x
print("FMOD() FUNCTION(x>y) : ",math.fmod(33,2))#return in 'float'
print("FMOD() FUNCTION(x<y) : ",math.fmod(2,33))#return in 'float'
#remainder(x,y) =>same as fmod()
print("REMAINDER() FUNCTION(x>y) : ",math.remainder(33,2))#return in 'float'
print("REMAINDER() FUNCTION(x<y) : ",math.remainder(2,33))#return in 'float'
#frexp(x) => return (m,e) , formula=>x=m*(2**e)
print("FREXP() FUNCTION : ",math.frexp(1))
#ldexp(m,e) => return x , formula=>x=m*(2**e)
print("LDEXP() FUNCTION : ",math.ldexp(0.5,1))#return in 'float'
#fsum(list or tuple) , return sum of list or tuple members
print("FSUM() FUNCTION : ",math.fsum((1.1,2,3)))#return in 'float'
print("GCD() FUNCTION : ",math.gcd(16,8,4))#GCD(Greatest Common Divisor)
print("LCM() FUNCTION : ",math.lcm(16,8,4))#LCM(Least Common Multiple)
#isclose(x,y,abs_tol) , if "true" when (x-y)<=abs_tol , defult abs_tol=0 , else "false"
print("ISCLOSE() FUNCTION(true) : ",math.isclose(1.1,1.3,abs_tol=0.2))
print("ISCLOSE() FUNCTION(flase) : ",math.isclose(1.1,1.3))
print("ISCLOSE() FUNCTION(true) : ",math.isclose(1,1))
#isfinite(value) , if value==finite number then "true" , else "false"
print("ISFINITE() FUNCTION(ture) : ",math.isfinite(1.25))
print("ISFINITE() FUNCTION(false) : ",math.isfinite(math.inf))
#isinf(value) , if value==infinite number then "true" , else "false"
print("ISINF() FUNCTION(true) : ",math.isinf(math.inf))
print("ISINF() FUNCTION(false) : ",math.isinf(1.2))
#isnan(vale) , if value==not anumber then "true" , else "false"
print("ISNAN() FUNCTION(true) : ",math.isnan(math.nan))
print("ISNAN() FUNCTION(false) : ",math.isnan(12.3))
#isqrt(value) return square root of value
print("ISQRT() FUNCTION : ",math.isqrt(2))
#modf(value) return (fractional,integral) of value
print("MODF() FUNCTION : ",math.modf(3.14))#return in 'float'
#nextafter(value,end) return nextafter value of 'value' by moving towars 'end'
print("NEXTAFTER() FUNCTION : ",math.nextafter(-2,3))#return in 'float'
#perm(n,k) [n>k] , formula=>n! / (n-k)!
print("PERM() FUNCTION : ",math.perm(2,1))
#prod(list or tuple,start) return product of list or tuple members by start with 'start' value , default value of start=1
print("PROD() FUNCTION(with start=2) : ",math.prod((1,2,3),start=2))
print("PROD() FUNCTION(defult start) : ",math.prod([1,2,3]))
print("ULP() FUNCTION : ",math.ulp(1))#ULP(unit of least precision)
print("\nPOWER AND LOGARITHMIC FUNCTIONS : \n")
#exp(x) return e power x [e=2.718281..]
print("EXP() FUNCTION : ",math.exp(1))
#expm1(x) return (exp(x)-1)
print("EXPM1() FUNCTION : ",math.expm1(3))
#log(x,base) return log(x) with base , default base=e [e=2.718281..]
print("LOG() FUNCTION(with base=10) : ",math.log(10,10))#return in 'float'
print("LOG() FUNCTION(with defult base=e) : ",math.log(10))#return in 'float'
#lof1p(x) return log(1+x) with base=e [e=2.718281..]
print("LOG1P() FUNCTION : ",math.log1p(9))#return in 'float'
#log2(x) return log(x) with base=2 
print("LOG2() FUNCTION : ",math.log2(10))#return in 'float'
#log10(x) return log(x) with base=10
print("LOG10() FUNCTION : ",math.log10(1))
#pow(x,y) return x power y
print("POW() FUNCTION : ",math.pow(2,3))#return in 'float'
#sqrt(value) return square root of 'value'
print("SQRT() FUNCTION : ",math.sqrt(16))#return in 'float'
print("\nTRIGONOMETRIC FUNCTIONS : \n")
#acos(value) return cos degree #cos 0=1 
print("ACOS() FUNCTION : ",math.acos(1))#return in 'float'
#cos(degree) return cos value #1=cos 0
print("COS() FUNCTION : ",math.cos(0))#return in 'float'
#asin(value) return sin degree #sin 90=1
print("ASIN() FUNCTION : ",math.asin(1))#return in 'float'
#sin(degree) return sin value #1=sin 90
print("SIN() FUNCTION : ",math.sin(90))#return in 'float'
#atan(value) return tan degree #tan 45=1
print("ATAN() FUNCTION : ",math.atan(1))#return in 'float'
#tan(degree) return tan value #1=tan 45
print("TAN() FUNCTION : ",math.tan(45))#return in 'float'
#dist((x1,y1),(x2,y2)) => formula=>sqrt((x1-x2)**2+(y1-y2)**2)
print("DIST() FUNCTION : ",math.dist((1,2),(2,1)))#return in 'float'
#hypot(a,b,c,d,....) => formula=>sqrt(a*a+b*b+c*c+d*d+....)
print("HYPOT() FUNCTION : ",math.hypot(1,1,1,1))#return in 'float'
print("\nANGULAR CONVENTION : \n")
print("DEGREES() FUNCTION : ",math.degrees(2))#radians to degrees
print("RADIANS() FUNCTION : ",math.radians(114.591))#degrees to radians
print("\nCONSTANTS : \n")
print("PI : ",math.pi)
print("E : ",math.e)
print("TAU or 2*PI : ",math.tau)
print("INFINITE NUMBER : ",math.inf)
print("NOT A NUMBER : ",math.nan)










