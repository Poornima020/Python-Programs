tuple1 = ()
tuple2 = ()
l1=list(tuple1)
l2=list(tuple2)
count = int(input("Enter the total count of elements :"))
print("enetr elements tuple1")
for i in range(0,count):
 l1.append(int(input()))
print("enter elemets tuple2")
for i in range(0,count):
 l2.append(str(input()))
tuple1=tuple(l1)
tuple2=tuple(l2)
print("tuple1:",tuple1)
print("tuple2:",tuple2)
tuple3 = (max(tuple1),max(tuple2))
print("Max of tuple1 & tuple2",tuple3)
