# Takes two args from the user
from sys import argv

scriptName, firstArg, secondArg = argv
rootPage = "https://en.wikipedia.org/wiki/"
startPage = rootPage + firstArg.replace(" ","_")
endPage = rootPage + secondArg.replace(" ","_")
print("Executing {0}! Your starting page is {1} and your end location is {2}".format(scriptName,startPage,endPage))

