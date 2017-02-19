from django.shortcuts import render
def index(request):
    return render(request, 'randword/index.html')


# Create your views here.
# def random_word(request):
    
