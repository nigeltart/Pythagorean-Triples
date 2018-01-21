# A program to find Pythagorean triples
a_triple=[]
hypotenuse=5
triples=[]
triples.append(a_triple)
#print (triples)

while hypotenuse <100:
  base = 1
  height = hypotenuse-1
  #print ("before loop: ", base, height, hypotenuse)
  while height>base:
  	#print ("before if: , base, height, hypotenuse")
  	if base**2 + height**2 == hypotenuse**2:
  		a_triple = [base, height, hypotenuse]
  		height -=1
  		base +=1
  		print ("Found One: ", a_triple)
  		triples.append(a_triple)
  	elif base**2 + height**2 > hypotenuse**2:
  		height -=1
  	else:
  	  base +=1
  	  #base**2 + height**2 < hypotenuse**2
  hypotenuse +=1  
print ("There are", len(triples), "triples with hypotenuses up to", hypotenuse, ":")
print (triples)
