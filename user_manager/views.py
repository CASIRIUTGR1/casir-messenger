from django.shortcuts import render,HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.


def index(request):

    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the the previous section
        form = AuthenticationForm(data=request.POST) # A form bound to the POST data

        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = AuthenticationForm() # An unbound form

    context = {
               "form": form,
               }
    return render(request, "user_manager/layout.html", context)
