from django.shortcuts import render

# from forms_builder.forms import Form


# Create your views here.
def home(request):
    return render(request, 'pial/home.html')