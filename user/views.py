from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .froms import LoginForm, SignUpForm


def index(request):
    return render(request,'index.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect ('login_view')
        else:
            msg = 'form is not vaild'
            
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            Confirm_password = form.cleaned_data.get('Confirm password')
            user = authenticate(username = username, password = password, Confirm_password=Confirm_password)
            if user is not None and user.is_admin:
               login(request,user)
               return redirect('admin')
            elif user is not None and user.is_doctor:
               login(request,user)
               return redirect('doctor')
            elif user is not None and user.is_patient:
                login(request,user)
                return redirect('patient')
            else :
               msg = 'Invalid'
        else:
            msg = 'error validating form'
    return render(request, 'Login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')
        
def doctor(request):
    return render(request,'doctor.html')
        

def patient(request):
    return render(request,'patient.html')
        

        
    
    

