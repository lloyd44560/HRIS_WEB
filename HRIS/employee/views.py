from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,  logout
from django.contrib.auth.models import User  # Import the User model if needed
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.views import LogoutView


@login_required
def index(request):
    context = {
        'title': 'Django Templates',
        'message': 'This is a sample page using Django templates.'
    }
    return render(request, 'index.html', context)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print(f"Email: {email}, Password: {password}")  
        
        user = authenticate(request, username=email, password=password)
        print("User object:", user) 

        if user is not None:
            login(request, user)
          
            if user.is_superuser:
                return redirect('admin_dashboard')  
            else:
                return redirect('user_dashboard')  
        else:
            # Authentication failed, show error message
            error_message = "Invalid email or password. Please try again."
            print("Invalid email or password. Please try again.")  # Debugging statement
            return render(request, 'Login.html', {'error_message': error_message})
    else:
        return render(request, 'Login.html')



def pagelogout(request):
    logout(request)
    return redirect('/login')
