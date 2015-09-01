from decimal import *
from fractions import Fraction
from random import randint
def deleteDuplicates(lis):
	newLis=[]
	for item in lis:
		if item not in newLis:
			print "Delteing Dupes"
			newLis.append(item)
	return newLis
denPops=[["The DCB","Red Cream Soda","Red Cream Soda","Red Cream Soda","Red Cream Soda","Red Cream Soda","Diet Coke","Diet Coke","Diet Coke","Diet Coke","Diet Coke","Diet Coke"],
	["Dr. Love","Dr. Pepper","Dr. Pepper","Dr. Pepper","Dr. Pepper","Dr. Pepper","Mountain Dew Code Red","Mountain Dew Code Red","Red Cream Soda","Red Cream Soda"],
	["Citrus Slam","Mountain Dew","Mountain Dew","Mountain Dew","Mountain Dew","Mountain Dew","Sprite","Sprite","Sprite","Sprite","Sprite"],
	["Mid Day Lovin","Pink Lemonade","Pink Lemonade","Red Cream Soda","Red Cream Soda","Sprite","Sprite","Mountain Dew Code Red","Mountain Dew Code Red"],
	["Mr. Popular","Mountain Dew","Mountain Dew","Mountain Dew","Mountain Dew","Mountain Dew","Mountain Dew","Blue Powerade","Blue Powerade","Blue Powerade"],
	["The Goldbuster","Diet Mountain Dew","Diet Mountain Dew","Sprite","Sprite","Crush","Crush","Pink Lemonade","Pink Lemonade","Fruit Punch","Fruit Punch"],
	["Candied Brains","Mountain Dew","Mountain Dew","Mountain Dew","Crush","Crush","Crush","Red Cream Soda","Red Cream Soda",'Red Cream Soda'],
	["Test(Alcohol)","Mountain Dew","Mountain Dew","Mountain Dew"]]

ingredients={"The DCB": "1/2 Red Cream Soda, 1/2 Diet Coke","Dr. Love": "1/2 Dr. Pepper, 1/4 Red Cream Soda, 1/4 Mountain Dew Code Red",
	"Citrus Slam": "1/2 Mountain Dew, 1/2 Sprite",
	"Mid Day Lovin":"1/4 Pink Lemonade, 1/4 Sprite, 1/4 Mountain Dew Code Red, 1/4 Red Cream Soda",
	"Mr. Popular":"2/3 Mountain Dew, 1/3 Blue Powerade",
	"The Goldbuster":"1/5 Sprite, 1/5 Diet Mountain Dew, 1/5 Crush, 1/5 Pink Lemonade, 1/5 Fruit Punch",
	"Candied Brains":"1/3 Mountain Dew, 1/3 Crush, 1/3 Red Cream Soda"}
creators={"The DCB":"The Den","Dr. Love":"The Den"}
crLinks={"The DCB":"https://www.facebook.com/thesportsdenpage?_rdr=p","Dr. Love":"https://www.facebook.com/thesportsdenpage?_rdr=p"}
comments={}
def addComment(name,content):
	try:
		pastComments=comments[name]
		pastComments.append(content)
		comments.update({name:pastComments})
	except:
		comments.update({name:[content]})

def getComments(name):
	try:
		return comments[name]
	except:
		return ["No Comments so far"]
def addCreator(x):
	creators.update(x)
def addCrLinks(x):
	crLinks.update(x)
def getCreator(name):
	try:
		return creators[name]
	except: 
		return "Anynomous"
def getCrLinks(name):
	try:
		return crLinks[name]
	except: 
		return "https://www.facebook.com/thesportsdenpage?_rdr=p"

def getPops():
	return denPops
def findDen(arr,a):
	count=0
	res=[]
	if a=="eith":
		for i in range(0,len(denPops)):
			for soda in denPops[i]:
				for item in arr:
					if item==soda:
						res.append(denPops[i][0])
	else:
		for i in range(0,len(denPops)):
			if "Alcohol" not in str(denPops[i][0]):
				for soda in denPops[i]:
					for item in arr:
						if item==soda:
							res.append(denPops[i][0])
	return res

	new=GtoL(res)
	return new
def turnToSearch(text):
	search=text.replace(" ","%20")
	link="http://www.bing.com/search?q="+str(search)+"&qs=n&form=QBRE&pq="+str(search)+"&sc=9-6&sp=-1&sk=&cvid=6585c559beef41f3b942271b982e674a"
	return link
def isLink(url):
	if str(url).startswith("http"):
		return True
	return False
def addIng(x):
	ingredients.update(x)
def getNames():
	res=[]
	for item in denPops:
		res.append(item[0])
	return res

def GtoL(arr):
	g=arr[0]
	for i in range(0,len(arr)):
		if arr.count(g)<arr.count(arr[i]):
			g=arr[i]
			arr.insert(0, arr.pop(arr.index(arr[i])))
	new=deleteDuplicates(arr)
	return new
def getIng(name):
	try:
		return ingredients[name]
	except:
		return "Ingredients for this den pop is coming soon!"
def createNew():
	ans="Yes"
	name=raw_input("Name Of Den Pop: ")
	res=[name]
	while ans=="Yes":
		soda=raw_input("What soda: ")
		try:
			amount=int(int(raw_input("Precetnage of Cup Filled: "))/10)
			for i in range(0,amount):
				res.append(soda)
			print "Soda Gained!"
		except:
			print "Error Occured"
		ans=raw_input("Do you want to keep importing?")
	denPops.append(res)
	print res
def add(name,sodas,amounts):
	res=[str(name)]
	for i in range(0,len(amounts)):
		for k in range(0,int(amounts[i])):
			res.append(sodas[i])
	denPops.append(res)
	print res

"""
createNew()
print "Den Pops"
print "Below"
for item in denPops:
	print item[0]
names=["Title 1","Title 2","Title 3","Sup"]
ings=["This is 1","This is 2","This is 3","This is Sup"]
index=randint(0,len(names))
title=names[index]
ing=ings[index]
print title
print ing

"""

