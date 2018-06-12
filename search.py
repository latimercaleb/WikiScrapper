# Takes two args from the user
from sys import argv
from bs4 import BeautifulSoup as Bsoup

import wikipedia as wiki
import unicodedata
import urllib2

def formatLinks(links):
    formattedLinks = []
    for link in links:
        formattedLinks.append(link .encode('ascii','ignore'))
    return formattedLinks

def compareLists(list1,list2):
    if len(list1) < len(list2):
        return True
    else:
        return False
def generateNodeList(list):
    nodes=[]
    for i in list:
        node()
class node:
    def __init__(self,name,parent,children):
        self.name = name
        self.parent = parent
        self.children = children
    def getParent(self):
        return self.children
    def getChildren(self):
        return self.children

class graph:
    def __init__(self,node):
        self.nodes = node


scriptName, firstArg, secondArg = argv
rootPage = "https://en.wikipedia.org/wiki/"
startPage = rootPage + firstArg.replace(" ","_")
endPage = rootPage + secondArg.replace(" ","_")

print("Executing {0}! Your starting page is {1} and your end location is {2}...".format(scriptName,startPage,endPage))

#OLD Implementation
#Leverage wikipedia module, installed via pip to generate a list of links from the first and end pages

startPageLinks = wiki.WikipediaPage(firstArg).links
endPageLinks = wiki.WikipediaPage(secondArg).links

startPageLinksFormatted = formatLinks(startPageLinks)
endPageLinksFormatted = formatLinks(endPageLinks)

print(len(startPageLinksFormatted))
print(len(endPageLinksFormatted))

foundMatchedLink = False

# Match Links
