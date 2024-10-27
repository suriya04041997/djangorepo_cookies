# myapp/views.py

from django.shortcuts import render, redirect

def index(request):
    # Check for a cookie
    user_name = request.COOKIES.get('user_name')
    
    # If the cookie is not set, set it
    if not user_name:
        user_name = 'Guest'
        response = render(request, 'myapp/index.html', {'user_name': user_name})
        response.set_cookie('user_name', user_name)  # Set the cookie
        return response
    
    return render(request, 'myapp/index.html', {'user_name': user_name})

def set_cookie(request):
    # Set a cookie with a specific value
    response = redirect('index')
    response.set_cookie('user_name', request.POST.get('user_name', 'Guest'))
    return response

def delete_cookie(request):
    # Delete the cookie
    response = redirect('index')
    response.delete_cookie('user_name')
    return response
