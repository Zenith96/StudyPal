from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #The data is stored inside form.cleaned_data
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
        else:
            form = UserRegisterForm() 

        return render(request , 'users/register.html',{'form':form})



