#I.G : @deeplearningindia
############################## LISTS ################################
#defining list SIMPLE
import time
l1=[1,2,3,4]
print("list 1" ,l1)

#Taking N inputs from user and storing in list SIMPLE METHOD
l2=[]
for i in range(4):
	a = int( input("Enter Values :") )
	l2.append(a) #appending the element of list

print("list 2 before sorting" ,l2)
l2.sort() #sorting the list
print("list 2 after sorting" ,l2)
l2.reverse() #reverse the list
print("list 2 after Reverse" ,l2)
#Printing the sum of all the elements of list
print("Sum of l2 :" , sum(l2) )

time.sleep(20)