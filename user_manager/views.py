from django.shortcuts import render, HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def index(request):

    if request.method == 'POST':
        if request.POST['form'] == 'auth':
            authForm = AuthenticationForm(data=request.POST)
            #print authForm.is_bound
            #print authForm.is_valid()
            #print authForm.errors
            if authForm.is_valid():
                return HttpResponseRedirect('/thanks/')  # Redirect after POST
        elif request.POST['form'] == "reg":
            regForm = UserCreationForm(data=request.POST)
            if regForm.is_valid():
                return HttpResponseRedirect('/thanks/')
    else:
        authForm = AuthenticationForm()  # An unbound form
        regForm = UserCreationForm()

    context = {
               "request": request,
               "auth_form": authForm,
               }
    return render(request, "user_manager/layout.html", context)
