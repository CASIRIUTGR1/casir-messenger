from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
               "example_attribute": "Hello, world",
               }
    return render(request, "user_manager/layout.html", context)


def newContact(request):
    pass 