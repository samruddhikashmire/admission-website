from django.shortcuts import render
from .models import * 
from random import randint 

# Create your views here.
def HomePage(request):
    return render(request,"app/Frontpage.html")


def AdmissionPage(request):
    return render(request,"app/Admission.html")


def SignupPage(request):
    return render(request, "app/signup.html")

def RegisterUser(request):
    fname = request.POST.get('firstname' , 'mydefaultvalue')
    lname = request.POST.get('lastname' , 'mydefaultvalue')
    email = request.POST.get('email' , 'mydefaultvalue')
    password = request.POST.get('password' , 'mydefaultvalue')
    cpassword = request.POST.get('cpassword', 'mydefaultvalue')

    user = UserMaster.objects.filter(email=email)
    
    if user :
        message = "User already exists"
        return render(request ,"app/signup.html" , {'msg' : message})
    else:
        if(password==cpassword):
           otp = randint(100000,999999)
           newuser=UserMaster.objects.create(otp = otp , email = email ,password=password)
           newcand=Candiadate.objects.create(user_id=newuser , Firstname = fname , Lastname = lname ,)
           message = "User is registerd sucessfully "
           return render(request,"app/otppage.html" , {'msg':message} , {'email' : email})
       
        
def OtpPage(request):
    return render(request, "app/otppage.html")

        
def OtpVerify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.filter(email=email)

    if user :
        if user.otp == otp:
            message = "OTP verifed "
            return render(request, "app/login.html" ,{'msg' : message} )
        else:
            message = "OTP is incorrect"
            return render(request , "app/otppage.html" , {"msg" : message})
    else:
        return render(request,"app/signup.html")
    

