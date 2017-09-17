#!/usr/bin/python
from lineParse import lineParse
from lineParse import cleanText
import sys 


def refrences( docname , mode ):
	"""docname is the actual document name
		mode is the refrence

	"""
	f = open(docname, "r")
	searchlines = f.readlines()
	f.close 
	if (mode == "list"):
		all_refs = []
	for i, line in enumerate(searchlines):
		#print line 
		right = "["
		left = "]"
		indicies1, indicies2 = lineParse(line, right, left)
		#print indicies2
		# if we just want to list all the references
		if (mode == "list"): 
			# none found otherwise
			if len(indicies1) != 0:
					for r in range(0, len(indicies1)):
						# now we have to see if multiple references exist 
						interest = line[int(indicies1[r]) +1:int(indicies2[r])]
						if "," in interest:
							# found multiple 
							indy1, indy2 = lineParse(interest, ",", ",")
							len_indy = len(indy1)
							previous_indy = 0
							count = 0
							while count < len_indy:
								new_listing = cleanText(interest[previous_indy:int(indy1[count])])
								if new_listing not in all_refs:
									print "@misc{" + new_listing + ",\n" + "\tauthor={" + new_listing +"},\n}"
									all_refs.append(new_listing)
								previous_indy = int(indy1[count])
								count += 1
							# last print statement for the last element 
							new_listing = cleanText(interest[int(indy1[count - 1]):len(interest)])
							if new_listing not in all_refs:
								print "@misc{" + new_listing + ",\n" + "\tauthor={" + new_listing +"},\n}"
								all_refs.append(new_listing)	
						else:
							# no multiple references
							new_listing = cleanText(interest)
							if new_listing not in all_refs:
								print "@misc{" + new_listing + ",\n" + "\tauthor={" + new_listing +"},\n}"
								all_refs.append(new_listing)
						#print "hi"
			        	#print "\tauthor={" + line[int(indicies1[r]) +1:int(indicies2[r])] +"},"
			        	#print "}"

		elif (mode == "latex"):
			# found reference 
			if len(indicies1) != 0:
				str_line = str(line)
				# update the way references show up 
				str_line = str_line.replace("[", "~\cite{")
				str_line = str_line.replace("]","}")
				print str_line
			else:
				print line
	if mode	 == "list": 
		print all_refs



print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

refrences(str(sys.argv[1]),str(sys.argv[2]))