from django.shortcuts import render, redirect, HttpResponse
# from django.contrib import messages
# from django.contrib.auth import logout, login, authenticate
# from .forms import UserForm, UserProfileForm


from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return render(request, 'users/home.html')


# def user_logout(request):
#     logout(request)
#     messages.success(request, "You logged out")
#     return redirect("home")



# def register(request):
#     form_user = UserForm()
#     form_profile = UserProfileForm()

#     context = {
#         "form_user" : form_user,
#         "form_profile" : form_profile
#     } 

#     return render(request, "user/register.html", context)









# def user_login(request):
#     form = AuthenticationForm(request, data=request.POST)

#     if form.is_valid():
#         user = form.get_user()
#         login(request, user)
#         return redirect("home")

#     return render(request, "users/user_login.html", {"form" : form} )

    ##user = authenticate(username=username, password=password)

    #else:
            #messages.error(request, 'Login Failed!')
           # return redirect('login')