#creating an empty tuple
tuple=()
print(tuple)

#creating tuples with integer elements
tuple1=(1,2,3)
print(tuple1)

#tuple with mixed datatypes
tuple3=(101,"sir",2000.0,"hr dept")
print(tuple3)

#creation of nested tuple
tuple4=("points",[1,2,3],(6,7,8,))
print(tuple4)

#tuple can be created wihtout parenthesis
#also called tuple packing
tuple5=101,"sam",15000,"HRDept"
print(tuple5)

#tuple unpacking is also possible
empid,empname,empsal,empdept=tuple5
print(empid)
print(empname)
print(empsal)
print(empdept)
print(type(tuple5))

#nested tuple
nest_tuple2=("hey",[1,2,3],(4,5,6))
print(nest_tuple2)
print(nest_tuple2[0][0])
print(nest_tuple2[2][0])
print(nest_tuple2[1][0])

