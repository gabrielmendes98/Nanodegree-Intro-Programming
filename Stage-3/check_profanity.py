import urllib.request

def read_text():
	quotes = open("C:\\Users\\GABRIEL\\Desktop\\movie_quotes.txt")
	contents_of_file = quotes.read()
	#print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(contents_of_file):
	connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+contents_of_file)
	output = connection.read()
	if "true" in output:
		print ("Profanity Alert!")
	elif "false" in output:
		print ("This document has no curse words!")
	else:
		print ("There is something wrong... Try again.")
	connection.close()

read_text()
