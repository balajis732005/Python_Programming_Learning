# SET METHODS
print("SET ARE IMMUTABLE AND CANT'N STORE DUPLICATE VALUES")
set1=set(map(int,input("Enter a set : ").split()))
print(type(set1))
set1.add(6)
print("ADD () : ",set1)
copy_set1=set1.copy()
print("COPY () : ",copy_set1)
set2={5,4,3,2,1}
print("ISDISJOINT () [set1 is set2] : ",set1.isdisjoint(set2))
print("ISDISJOINT () [set2 is set1] : ",set2.isdisjoint(set1))
print("ISSUPERSET () [set1 is set2] : ",set1.issuperset(set2))
print("ISSUPERSET () [set2 is set1] : ",set2.issuperset(set1))
a={1,2,3}
b={1,2,3,4,5}
print("ISSUBSET () [a is b] : ",a.issubset(b))
print("ISSUBSET () [b is a] : ",b.issubset(a))
a.update(b)
print("UPDATE () : ",a)
a.clear()
print("CLEAR () : ",a)
b.discard(5)
print("DISCARD () : ",b)
set3={'A','B','C','D','E'}
set3.remove("C")
print("REMOVE () : ",set3)
set3.pop()# remove random item from set
print("POP () : ",set3)
x=frozenset(set3)
print("FROZENSET () : ",x)

# SET OPERATORS

set_A={1,2,3,4,5}
set_B={'A','B','C','D','E'}
print("UNION () : ",set_A.union(set_B),"OR",set_A|set_B)
set_C={'A','B',1,2}
set_D={1,2,'C','D'}
print("INTERSECTION () : ",set_C.intersection(set_D),"OR",set_C&set_D)
set_C.intersection_update(set_D)
print("INTERSECTION_UPDATE () : ",set_C)
set_E={1,2,3,4}
set_F={1,2,0,9}
print("DIFFERENCE () : ",set_E.difference(set_F),"OR",set_E-set_F)
set_E.difference_update(set_F)
print("DIFFERENCE_UPDATE () : ",set_E)
set_G={1,2,3,4}
set_H={5,6,3,4}
print("SYMMETRIC_DIFFERENCE () : ",set_G.symmetric_difference(set_H),"OR",set_G^set_H)
set_G.symmetric_difference_update(set_H)
print("SYMMETRIC_DIFFERENCE_UPDATE () : ",set_G)
# WE CAN'T ADD ANYTHING IN FROZENSET
x.add('X')
