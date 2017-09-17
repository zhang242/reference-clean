"""
This function takes a line of code and exports two arrays of indicies, 
one for the start indicies and one for the end indicies as per the inputs  

"""

def lineParse( s, first, second ):
	# input check 
	if (first not in s) or (second not in s):
		indicies1 = []
		indicies2 = []	
		return indicies1, indicies2
	else:
		indicies1 = [y for y, x in enumerate(s) if x == first]
		indicies2 = [t for t, g in enumerate(s) if g == second]
		return indicies1,indicies2

"""
This function cleans up the header of the string 
"""
def cleanText(t):
	cleaned = ""
	length = len(t)
	start = 0 
	while t[start] == " " or t[start] == ",":
		start+=1
	cleaned = t[start:length]
	# print cleaned
	return cleaned



#indi1, indi2 = lineParse("hello there", "e", "e")
#print indi1, indi2

cleanText(", what do you know")

test_str = " hello there [me here]"
test_str = test_str.replace("[" ,"%")
test_str = test_str.replace("]", "%")
print test_str