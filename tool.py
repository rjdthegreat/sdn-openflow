def addRuleToGUI(switchNo,portNo):
	print "Import custom msg" 
	print switchNo
	print portNo
	with open("output.txt","a") as myfile:
		myfile.write(str(switchNo)+" "+str(portNo)+"\n")	
	print "End of message"	
