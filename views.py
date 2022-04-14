from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
#function for Home Page
def home(request):
    return render(request,"home.html")
#function for Signup Page
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        confpass = request.POST['confpass']

        #Checking if the username is available (Unique)
        if User.objects.filter(username=username):
            messages.error(request,"User name already Exist!")
            return redirect('home')
        #Checking if the email is new
        if User.objects.filter(email=email):
            messages.error(request,"Email name already Exist!") 
            return redirect('signin')
        #Checking if the length of password is greater than or equal to 6
        if len(pass1)<6:
            messages.error(request,"Password should be greater than or eual to 6")
        #Checking if the Password & confirm Password are same
        if pass1 != confpass:
            messages.error(request,"Passwords didn't match!")
            return redirect('home')
        myuser = User.objects.create_user(username,email,pass1)
        myuser.username = username
        myuser.save()

        messages.success(request, "Your Account has been successfully created!")
        return redirect('signin')
    return render(request,"signup.html")

#function for Signin Page
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        #Checking the details are matching or not
        if user is not None:
            login(request,user)
            username = user.username
            return render(request, "home.html", {'username':username})
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')
    return render(request,"signin.html")
#function for secpg Page
def secpg(request):
    return render(request,"secpg.html")
#function for iitname Page
def iitname(request):
    return render(request,"iitname.html")
#function for iitname2 Page
def iitname2(request):
    return render(request,"iitname2.html")
#function for staname Page
def staname(request):
    return render(request,"staname.html")
#function for staname2 Page
def staname2(request):
    return render(request,"staname2.html")
#function for IITJ Page
def IITJ(request):
    return render(request,"IITJ.html")
#function for IITBhil Page
def IITBhil(request):
    return render(request,"IITBhil.html")
#function for IITBBS Page
def IITBBS(request):
    return render(request,"IITBBS.html")
#function for IITB Page
def IITB(request):
    return render(request,"IITB.html")
#function for IITD Page
def IITD(request):
    return render(request,"IITD.html")
#function for IIDh Page
def IITDh(request):
    return render(request,"IITDh.html")
#function for IITDw Page
def IITDw(request):
    return render(request,"IITDw.html")
#function for IITGn Page
def IITGn(request):
    return render(request,"IITGn.html")
#function for IITGoPage
def IITGo(request):
    return render(request,"IITGo.html")
#function for IITG Page
def IITG(request):
    return render(request,"IITG.html")
#function forIITH Page
def IITH(request):
    return render(request,"IITH.html")
#function for IITI Page
def IITI(request):
    return render(request,"IITI.html")
#function for IITJm Page
def IITJm(request):
    return render(request,"IITJm.html")
#function for IITK Page
def IITK(request):
    return render(request,"IITK.html")
#function for IITKh Page
def IITKh(request):
    return render(request,"IITKh.html")
#function for IITM Page
def IITM(request):
    return render(request,"IITM.html")
#function for IITMn Page
def IITMn(request):
    return render(request,"IITMn.html")
#function for IITP Page
def IITP(request):
    return render(request,"IITP.html")
#function for IITPn Page
def IITPn(request):
    return render(request,"IITPn.html")
#function for IITR Page
def IITR(request):
    return render(request,"IITR.html")
#function for IITRo Page
def IITRo(request):
    return render(request,"IITRo.html")
#function for IITT Page
def IITT(request):
    return render(request,"IITT.html")
#function for IITV Page
def IITV(request):
    return render(request,"IITV.html")
