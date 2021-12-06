from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
import hashlib
import datetime
from django.db.models import Q
import os
# Create your views here.
def index(request):
	query=pets_tbl.objects.all()
	return render(request,'index.html',{'query':query})

def contact(request):
	return render(request,'contact.html')

def about(request):
	return render(request,'about.html')

def gallery(request):
	query=pets_tbl.objects.all()
	return render(request,'gallery.html',{'query':query})
def userregister(request):
	if request.method=="POST":
		uname=request.POST['name']
		uphone=request.POST['phone']
		uemail=request.POST['email']
		upassword=request.POST['psw']

		add=user_tbl(username=uname,phoneno=uphone,email=uemail,password=upassword)
		add.save()
		return render(request,'userregistration.html')
	else:
		return render(request,'userregistration.html')
	    

def shopregister(request):
	if request.method=="POST":
		sname=request.POST['shopname']
		# print(sname)
		saddress=request.POST['address']
		sphone=request.POST['phoneno']
		semail=request.POST['email']
		spassword=request.POST['password']
		x=shop_tbl(shopname=sname,address=saddress,phoneno=sphone,email=semail,password=spassword)
		x.save()
		return render(request,'shopregistration.html')
	else:
		return render(request,'shopregistration.html')


def petsregister(request):
	if request.method=="POST":
		pcategory=request.POST['category']
		pname=request.POST['name']
		pgender=request.POST['gender']
		page=request.POST['age']
		pcolour=request.POST['colour']
		pdescription=request.POST['description']
		pquantity=request.POST['quantity']
		pprice=request.POST['price']
		pfile=request.FILES['myfile']
		add=pets_tbl(category=pcategory,name=pname,gender=pgender,age=page,colour=pcolour,description=pdescription,quantity=pquantity,price=pprice,file=pfile)
		add.save()
		return render(request,'petsregister.html')
	else:
		return render(request,'petsregister.html')


def viewtbl(request):
	query=user_tbl.objects.all()
	query1=shop_tbl.objects.all()
	query2=pets_tbl.objects.all()
	return render(request,'viewtbl.html',{'data':query ,'data1':query1,'data2':query2})

	   
def petshome(request):
	if request.session.has_key('myid'):
		pid=request.GET['id']
		pets=pets_tbl.objects.all().filter(id=pid)
		if pets:
			return render(request,'petshome.html',{'pets':pets})
		else:
			return render(request,'petshome.html')
	else:
		return HttpResponseRedirect('/userlogin/')
    



def petsupdate(request):
	if request.method=="GET":
		pid=request.GET['id']
		pets=pets_tbl.objects.all().filter(id=pid)
		if pets:
			return render(request,'petsupdate.html',{'pets':pets})
		else:
			return render(request,'petsupdate.html')		


# def petsedit(request):
# 	if request.method=="POST":
# 		pid=request.GET['id']
# 		category=request.POST['category']
# 		name=request.POST['name']
# 		gender=request.POST['gender']
# 		age=request.POST['age']
# 		colour=request.POST['colour']
# 		description=request.POST['description']
# 		price=request.POST['price']
# 		# file=request.FILES['myfile']
# 		imgup=request.POST['img']
# 		if imgup=='Yes':
# 			image1=request.FILES['myfile']
# 		oldrec=pets_tbl.objects.all().filter(id=pid)
# 		updrec=pets_tbl.objects.get(id=pid)
# 		for x in oldrec:
# 			imgurl=x.image.url
# 	pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(_file_)))+imgurl
# 	if os
# 		pets_tbl.objects.filter(id=pid).update(category=category,name=name,gender=gender,age=age,colour=colour,description=description,price=price,file=file)
# 		query=pets_tbl.objects.all()
# 		# query1=teacher_tbl.objects.all()
# 		return render (request,'viewtbl.html',{'data':query})
# 	else:
# 		query=pets_tbl.objects.all()
# 		# query1=teacher_tbl.objects.all()
# 		return render (request,'viewtbl.html',{'data':query})

def delete(request):
		query=user_tbl.objects.all()
		uid=request.GET['id']
		users=user_tbl.objects.all().filter(id=uid).delete()

		query1=shop_tbl.objects.all()
		sid=request.GET['id']
		shops=shop_tbl.objects.all().filter(id=sid).delete()

		query2=pets_tbl.objects.all()
		pid=request.GET['id']
		pets=pets_tbl.objects.all().filter(id=pid).delete()
		return render(request,'viewtbl.html',{'data':query ,'data1':query1,'data2':query2})
		

def petsedit(request):
	if request.method=="POST":
		print("----------update inside post-----------")
		pid=request.GET['id']
		category=request.POST['category']
		name=request.POST['name']
		gender=request.POST['gender']
		age=request.POST['age']
		colour=request.POST['colour']
		description=request.POST['description']
		price=request.POST['price']
		
		# ii=request.session['sid']
		imgup=request.POST['img']
		if imgup=='Yes':
			image1=request.FILES['myfile']
			oldrec=pets_tbl.objects.all().filter(id=pid)
			updrec=pets_tbl.objects.get(id=pid)
			for x in oldrec:
				imgurl=x.file.url
				pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
				if os.path.exists(pathtoimage):
					os.remove(pathtoimage)
					print('Successfully deleted')
			updrec.file=image1
			updrec.save()
		
		pets_tbl.objects.filter(id=pid).update(category=category,name=name,gender=gender,age=age,colour=colour,description=description,price=price)
		query=user_tbl.objects.all()
		query1=shop_tbl.objects.all()
		query2=pets_tbl.objects.all()
		return render(request,'viewtbl.html',{'data':query ,'data1':query1,'data2':query2})
	elif request.method=="GET":
		# print("-----------------get update------------")
		# pid=request.GET['id']
		# query=pets_tbl.objects.all().filter(id=pid)
		# print("-----------------render page--------------")
		# return render(request,'viewtbl.html',{'data':query})
		pid=request.GET['id']
		query=user_tbl.objects.all()
		query1=shop_tbl.objects.all()
		query2=pets_tbl.objects.all().filter(id=pid)
		return render(request,'viewtbl.html',{'data':query ,'data1':query1,'data2':query2})


def pets_addcart(request):
	if request.session.has_key('myid'):
		if request.method=='POST':
			pids=request.GET['id']
			prd=pets_tbl.objects.all().filter(id=pids)
			for x in prd:
				unitprice=x.price
			qty=request.POST['qty']
			shipping=int(int(unitprice)*10/100)
			total=int(unitprice)*int(qty)+shipping
			# date= datetime.datetime.now()
			ii=request.session["myid"]
			print(ii)				
			uid=user_tbl.objects.get(id=ii)
			# x = datetime.datetime.now()
			pid=pets_tbl.objects.get(id=pids)
			ii=user_tbl.objects.get(id=ii)
			check=cart_tbl.objects.all().filter(userid=ii,pid=pids,unitprice=unitprice,total=total)
			if check:
				mypet=cart_tbl.objects.all().filter(userid=ii,status='pending')
				
				return render(request,'cart.html',{'query':mypet,'msgkey':'Already Add to cart'})
			else:
				tocart=cart_tbl(userid=ii,pid=pid,unitprice=unitprice,total=total,quantity=qty)
				tocart.save()
				thisprd=pets_tbl.objects.all().filter(id=pids)
				for x in thisprd:
					oldqty=x.quantity
				newqty=int(oldqty)-int(qty)
				pets_tbl.objects.all().filter(id=pids).update(quantity=newqty)
				mycart=cart_tbl.objects.all().filter(userid=ii,status='pending')
				grandtotal=0
				for x in mycart:
					grandtotal=int(x.total)+grandtotal
				mypet=cart_tbl.objects.all().filter(userid=ii,status='pending')
				
				return render(request,'cart.html',{'query':mypet,'gt':grandtotal,'msgkey':'Add to cart'})
	else:
		print("*************************************************************")
		return HttpResponseRedirect('/')

def buynow(request):
	if request.session.has_key('myid'):
		gt=request.GET['gt']
		if request.method=='GET':
			pid=request.GET.get('id')
			ii=request.session["myid"]
			pview=pets_tbl.objects.all().filter(id=pid)
			uview=user_tbl.objects.all().filter(id=ii)
			return render(request,'user_payment.html',{'pb':pview,'ub':uview,'amount':gt})

	else:
		return HttpResponseRedirect('/')



def delete_cartitem(request):
	ii=request.session['myid']
	cid=request.GET['id']
	cartitem=cart_tbl.objects.all().filter(id=cid)
	for x in cartitem:
		itemid=x.pid.id
		quantity=x.quantity
		petdata=pets_tbl.objects.all().filter(id=itemid)
		for x in petdata:
			oldqty=x.quantity
		newqty=int(oldqty)+int(quantity)
		pets_tbl.objects.all().filter(id=itemid).update(quantity=newqty)
	
	cart_tbl.objects.all().filter(id=cid).delete()
	mycart=cart_tbl.objects.all().filter(userid=ii,status='pending')
	grandtotal=0
	for x in mycart:
		grandtotal=int(x.total)+grandtotal
	mypet=cart_tbl.objects.all().filter(userid=ii,status='pending')
	return render(request,'cart.html',{'query':mypet,'gt':grandtotal,'msg':'Successfully deleted'})

def cart(request):
	if request.session['myid']:
		ii=request.session['myid']
		mycart=cart_tbl.objects.all().filter(userid=ii,status='pending')
		grandtotal=0
		for x in mycart:
			grandtotal=int(x.total)+grandtotal
		mypet=cart_tbl.objects.all().filter(userid=ii,status='pending')
		return render(request,'cart.html',{'query':mypet,'gt':grandtotal})
	else:
		return HttpResponseRedirect('/')

def makepayment(request):
	if request.session['myid']:
		ids=request.session['myid']
		if request.method=='POST':
			amount=request.POST['amount']
			x = datetime.datetime.now()
			id1=user_tbl.objects.get(id=ids)
			topay=payment_tb(userid=id1,amount=amount,status='Paid',date=x)
			topay.save()
			cart_tbl.objects.all().filter(userid=ids,status='pending').update(status='Paid',date=x)
			check=payment_tb.objects.all().filter(userid=id1)
			if check:
				mypet=cart_tbl.objects.all().filter(Q(status="Paid") | Q(status="Processing") | Q(status="Shipping") | Q(status="Delivered"),userid=ids)
				return render(request,'user_order.html',{'query':mypet})
			else:
				mycart=cart_tbl.objects.all().filter(userid=ids,status='pending')
				grandtotal=0
				for x in mycart:
					grandtotal=int(x.total)+grandtotal
				mypet=cart_tbl.objects.all().filter(Q(status="Paid") | Q(status="Processing") | Q(status="Shipping") | Q(status="Delivered"),userid=ids)
				return render(request,'cart.html',{'query':mypet,'gt':grandtotal})
		else:
			return render(request,'cart.html')
	else:
		return render(request,'index.html')


def shopupdate(request):
	if request.method=="GET":
		sid=request.GET['id']
		shops=shop_tbl.objects.all().filter(id=sid)
		if shops:
			return render(request,'shopupdate.html',{'shops':shops})
		else:
			return render(request,'shopupdate.html')

def shopedit(request):
	if request.method=="POST":
		sid=request.GET['id']
		shopname=request.POST['shopname']
		address=request.POST['address']
		phoneno=request.POST['phoneno']
		email=request.POST['email']
		password=request.POST['password']
		# confirmpass=request.POST['password2']
		shop_tbl.objects.filter(id=sid).update(shopname=shopname,address=address,phoneno=phoneno,email=email,password=password)
		query1=shop_tbl.objects.all()
		query=user_tbl.objects.all()
		query2=pets_tbl.objects.all()
		return render(request,'viewtbl.html',{'data':query,'data1':query1,'data2':query2})
	else:
		query1=shop_tbl.objects.all()
		query=user_tbl.objects.all()
		query2=pets_tbl.objects.all()
		return render(request,'viewtbl.html',{'data':query,'data1':query1,'data2':query2})



def user_login(request):
	if request.method=="POST":
		email=request.POST['email']
		password=request.POST['password']
		log=user_tbl.objects.all().filter(email=email,password=password)
		if log:
			for x in log:
				request.session["myid"]=x.id
				ii=request.session["myid"]
				user=user_tbl.objects.all().filter(id=ii)
				return HttpResponseRedirect('/')
		else:
			return render(request,'index.html')
	else:
		return render(request,'index.html')


def logout(request):
	if request.session.has_key('myid'):
		del request.session["myid"]
		
		return HttpResponseRedirect('/')

def cancel(request):
	ids=request.session['myid']
	cart_tbl.objects.filter(userid=ids,status='pending').delete()
	mypet=cart_tbl.objects.all().filter(userid=ii,status='pending')
	return render(request,'cart.html',{'query':mypet})

def forget_pswd(request):
	if request.method=="POST":
		email=request.POST['email']
		log=user_tbl.objects.all().filter(email=email)
		if log:
			for x in log:
				userid=x.id
				print("***************",userid)
				return render(request,'forgetchangepswd.html',{"myid":userid})
		else:
			return render(request,'index.html')
	else:
		return render(request,'index.html')




def forgetchangepswd(request):
	if request.method=="POST":
		uid=request.GET['id']
		cartitem=user_tbl.objects.all().filter(id=uid)
		password=request.POST['newpassword']
		cpassword=request.POST['cpassword']
		if password==cpassword:
			user_tbl.objects.filter(id=uid).update(password=password)
			return render(request,'index.html')
		else:
			return render(request,'index.html',{"error":"password doesnot matched"})
	else:
		return render(request,'forgetchangepswd.html')
		




	

def view_profile(request):
	if request.session['myid']:
		ids=request.session['myid']
		users=user_tbl.objects.all().filter(id=ids)
		if users:
			return render(request,'userhome.html',{'data':users})
		else:
			return request(request,'index.html')


def change_pswd(request):
	if request.method=="POST":
		print("----------update inside post-----------")
		oldpassword=request.POST['oldpassword']
		newpassword=request.POST['newpassword']
		cpassword=request.POST['cpassword']
		uid=request.session['myid']
		oldcheck=user_tbl.objects.all().filter(id=uid)
		if oldcheck:
			for x in oldcheck:
				oldpwd=x.password
		if (oldpassword==oldpwd) and (newpassword==cpassword):
			user_tbl.objects.filter(id=uid).update(password=newpassword)
			up=user_tbl.objects.all().filter(id=uid)
			print("-----------------render page--------------")
			return render(request,'userhome.html',{'data':up,"success":'success password is changed'})
		else:
			return render(request,'changepswd.html',{"error":'error password not matched'})
	else:
		print("-----------------get update------------")
		# uid=request.session['myid']
		# up=user_tbl.objects.all().filter(id=uid)
		print("-----------------render page--------------")
		return render(request,'changepswd.html')



    
   



def adminindex(request):
	return render(request,'admin/index.html')


def admin_login(request):
	if request.method=="POST":
		email=request.POST['email']
		password=request.POST['password']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()
		log=admin_signup_tb.objects.all().filter(email=email,hpassword=hashpass)
		if log:
			for x in log:
				request.session["aid"]=x.id
				request.session["name"]=x.firstname
				ii=request.session["aid"]
				user=admin_signup_tb.objects.all().filter(id=ii)
				return HttpResponseRedirect('/adminindex/')
		else:
			return render(request,'admin/login.html')
	else:
		return render(request,'admin/login.html')  



def admin_signup(request):
	if request.method=="POST":
		fname=request.POST['firstname']
		lname=request.POST['lastname']
		email=request.POST['email']
		gender=request.POST['gender']
		password=request.POST['password']
		add=admin_signup_tb(firstname=fname,lastname=lname,email=email,gender=gender,password=password)
		add.save()
		return render(request,'admin/signup.html')

	else:
		return render(request,'admin/signup.html')


def admin_logout(request):
	if request.session.has_key('aid'):
		del request.session["aid"]
		del request.session["name"]
		
		return HttpResponseRedirect('/adminlogin/')





def pets_view(request):
		query=pets_tbl.objects.all().filter(status="approved")
		return render(request,'admin/petsview.html',{'data':query})

def users_view(request):
	query=user_tbl.objects.all().filter(status="approved")
	return render(request,'admin/usersview.html',{'data':query})

def continue_shopping(request):
	query=pets_tbl.objects.all()
	return render(request,'index.html',{'query':query})

