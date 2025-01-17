from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
import string, random
from django.http import JsonResponse
from . models import Passwd
from . forms import PmForm



# Create your views here.


def index(request):
    return render(request,'index.html')


@login_required(login_url='login')
def add(request):
    frm=PmForm
    if request.POST:
        frm=PmForm(request.POST)
        if frm.is_valid:
            inst = frm.save(commit=False)
            inst.userid = request.user
            inst.save()
            return redirect('dashboard')
        else:
            frm=PmForm
    return render(request,'PM.html',{'frm':frm})


@login_required(login_url='login')
def edit(request, pk):
    inst_to_edit = Passwd.objects.get(pk=pk)
    if request.method == "POST":
        frm = PmForm(request.POST, instance=inst_to_edit)
        if frm.is_valid():
            frm.save() 
            return redirect('dashboard')    
    else: 
        frm = PmForm(instance=inst_to_edit)
    return render(request, 'PM.html', {'frm': frm})



from django.contrib import messages
@login_required(login_url='login')
def view(request):
    if request.user.is_authenticated:
        passwords=Passwd.objects.all()
        response = render(request,'view.html',{'passwords':passwords})
        #respo.set_cookie('visits',visits)
        return response



@login_required(login_url='login')
def delete(request,pk):
    inst=Passwd.objects.get(pk=pk)
    inst.delete()
    passwords=Passwd.objects.all()
    return render(request,'view.html',{'passwords':passwords})


@login_required(login_url='login') # Redirect to login if not authenticated
def dashboard(request):
    messages.success(request, f"Logged in as {request.user}")
    user_pass = Passwd.objects.filter(userid=request.user)
    return render(request, 'dashboard.html', {'user_pass': user_pass})

def generate_password(request):
    length = int(request.GET.get('length', 12))
    include_uppercase = request.GET.get('uppercase') == 'true'
    include_numbers = request.GET.get('numbers') == 'true'
    include_special = request.GET.get('special') == 'true'

    characters = list(string.ascii_lowercase)
    if include_uppercase:
        characters.extend(string.ascii_uppercase)
    if include_numbers:
        characters.extend(string.digits)
    if include_special:
        characters.extend(string.punctuation)

    password = ''.join(random.choice(characters) for _ in range(length))
    return JsonResponse({'password': password})




    
    
 