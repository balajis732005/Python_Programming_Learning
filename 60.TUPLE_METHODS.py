# TUPLE METHODS
print("TUPLES ARE IMMUTABLE ")
tuple1=tuple(map(int,input("Enter a tuple : ").split()))
print(type(tuple1))
print("TUPLE SLICING  : ",tuple1[0:6:2])
a=(1)
b=(1,)
print("TYPE () [a=(1)] : ",type(a))
print("TYPE () [b=(1,)] : ",type(b))
tuple2=(2,4,6,8,0)
print("CONCATINATE TUPLE : ",tuple1+tuple2)
print("NESTED TUPLE : ",(tuple1,tuple2))
tuple_doop=(1,1,2,2,3,3,4,4,5,5)
print("DUPLICATE TUPLE : ",tuple_doop)
c=("BALAJI",)*5
print("REPEATING TUPLE : ",c)
print("COUNT () : ",tuple_doop.count(3))
print("INDEX () : ",tuple1.index(3))
d=zip(tuple1,tuple2)
print("ZIP () : ",tuple(d))


