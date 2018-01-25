# A program to find Pythagorean triples

#Initialise
a_triple=[] #Pythagorean triples will be stored as a list: [base, height, hypotenuse]
hypotenuse=5 #smallest possible
triples=[] #the list of Pythagorean triples (lists) found so far, initialised to empty list
#triples.append(a_triple)
#print (triples)

#Main loop checks each hypotenuse up to a programmed maximum (100 here)
while hypotenuse <100:
  #height could be one less than hypotenuse
  height = hypotenuse-1 
  #don't need to check base=1; jump straight to sqrt (hyp**2 - (hyp-1)**2)
  base = int((2*hypotenuse+1)**0.5) 
  while height>base: #not crossed over yet
  	if base**2 + height**2 == hypotenuse**2: #Pythagorean triple found
  		a_triple = [base, height, hypotenuse] #store the triple as a list
  		triples.append(a_triple) #add it to the main list of triples
  		height -=1
  		base +=1
  	elif base**2 + height**2 > hypotenuse**2: #sum of two squares too high, so decrement height
  		height -=1
  	else: #sum of two squares too low, so increment base
  	  base +=1
  #base and hypotenuse now crossed over, eg it would already have found [4,3,5] as [3,4,5] 
  hypotenuse +=1  

#Output results
print ("There are", len(triples), "triples with hypotenuses up to", hypotenuse, ":")
for index in range(len(triples)-1):
  print (triples[index])
