from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import den
from random import randint
import time
import os
app = Flask(__name__)

@app.route('/')
def my_form():
	names=den.getPops()
	index=randint(0,len(names)-1)
	title=names[index][0]
	ing=den.getIng(title)
	return render_template("index.html",title=title,ing=ing)

@app.route('/', methods=['POST'])
def my_form_post(names=None,index=None,title=None,ing=None,soda1=None, soda2=None,soda3=None,qa=None,startTime=None,timeA=None,gender=None,length=None,message=None,links=[],parts=[],Creators=[],caLinks=[]):
	links=[]
	parts=[]
	Creators=[]
	caLinks=[]
	startTime=time.time()
	soda1 = request.form['soda1']
	soda2 = request.form['soda2']
	soda3 = request.form['soda3']
	names=den.getPops()
	index=randint(0,len(names)-1)
	title=names[index][0]
	ing=den.getIng(title)
	if soda1!="No Other Soda" and soda2!="No Other Soda" and soda3!="No Other Soda":
		if soda1==soda2 or soda1==soda3 or soda3==soda2:
			message="Please Select Different Drinks"
			return render_template("index.html",message=message,title=title,ing=ing)
	qa=request.form['qa']
	links.append(soda1)
	links.append(soda2)
	links.append(soda3)
	links=den.findDen(links,qa)
	links=den.deleteDuplicates(links)
	for item in links:
		parts.append(den.getIng(item))
		Creators.append(den.getCreator(item))
		caLinks.append(den.getCrLinks(item))
	length=len(links)
	timeA = time.time() - startTime
	return render_template('link.html',links=links,soda3=soda3,soda2=soda2,soda1=soda1,length=length,timeA=timeA,parts=parts,caLinks=caLinks,Creators=Creators)

@app.route('/about')
def about():
	return redirect('https://plus.google.com/107108771936096317653/posts')

@app.route('/locate')
def locate():
	return render_template("locate.html")
@app.route('/add')
def addDen():
	return render_template('add.html')
@app.route('/add/', methods=['POST'])
def addDenPop(name=None,soda1=None,soda2=None,creator=None,cLink=None,soda3=None,qa=None,amount1=None,amount2=None,amount3=None,sodas=None,amounts=None,message=None,some_list=[],ing=None,inges={}):
	sodas=[]
	amounts=[]
	name = request.form['name']
	qa= request.form['qa']
	if qa=="y":
		name=str(name)+" (Alcohol)"
	if len(name)==0:
		message="Enter Name"
		return render_template("add.html",message=message)
	some_list=den.getNames()
	if any(name in s for s in some_list):
		message="Name already Taken :("
		return render_template("add.html",message=message)
	ing=request.form['ing']
	inges={name:ing}
	den.addIng(inges)
	soda1 = request.form['soda1']
	soda2 = request.form['soda2']
	soda3 = request.form['soda3']
	sodas.append(soda1)
	sodas.append(soda2)
	sodas.append(soda3)
	amount1 = request.form['amount1']
	amount2 = request.form['amount2']
	amount3 = request.form['amount3']
	if (int(amount1)+int(amount2)+int(amount3))!=10:
		message="Must add up to 100%"
		return render_template("add.html",message=message)
	amounts.append(amount1)
	amounts.append(amount2)
	amounts.append(amount3)
	den.add(name,sodas,amounts)
	creator=request.form['creator']
	cLink=request.form['cLink']
	if den.isLink(cLink):
		cLink=cLink
	else:
		cLink=den.turnToSearch(creator)
	inges={name:creator}
	den.addCreator(inges)
	inges={name:cLink}
	den.addCrLinks(inges)	
	return render_template("conf.html",name=name,ing=ing,cLink=cLink,creator=creator)

@app.route('/denData')
def denDat():
	return render_template("login.html")

@app.route('/login/', methods=['POST'])
def denDataPop(nameA=None,passA=None,message=None,names=[],dens=[],length=None):
	nameA = request.form['nameA']
	passA = request.form['passA']
	dens=[]
	names=[]
	if nameA=="abirshukla@gmail.com" and passA=="abir1":
		dens=den.getPops()
		for item in dens:
			names.append(item[0])
		length=len(names)
		return render_template("names.html",names=names,length=length)
	else:
		message="Wrong Password"
		return render_template("login.html",message=message)
	
@app.route('/denPop/<name>')
def greet(name,cLink=None,creator=None,ing=None,comments=[]):
	comments=[]
	cLink=den.getCrLinks(name)
	creator=den.getCreator(name)
	ing=den.getIng(name)
	comments=den.getComments(name)
	return render_template("drink.html",name=name,cLink=cLink,creator=creator,ing=ing,comments=comments)
@app.route('/addComment/<name>')
def comm(name):
	return render_template("comment.html",name=name)
@app.route('/comment/<name>', methods=['POST'])
def commF(name=None,newComment=None):
	name=request.form['name']
	newComment=request.form['newComment']
	den.addComment(name,newComment)
	return redirect("/denPop/"+str(name))
if __name__ == '__main__':
    app.run()






