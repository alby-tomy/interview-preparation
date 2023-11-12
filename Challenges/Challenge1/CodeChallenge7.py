setA = {1,"A",3,"B","C","D",8,9,10}
print("Set A : ",setA)
setA.add(11)
print("updated : ",setA)
setA.remove("A")
print("Updated set removed A : ",setA)
setB = {1,2,3,"B"}
print("Set B : ",setB)
unionAB = setA.union(setB)
print("setA U setB : ",unionAB)
differenceAB = setA.difference(setB)
print("Difference A and B : ",differenceAB)
