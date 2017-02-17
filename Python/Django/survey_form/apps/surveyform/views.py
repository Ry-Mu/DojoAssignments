from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0

    return render(request, 'surveyform/index.html')

def process(request):
    print (request.method)
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        request.session['count'] += 1
    return redirect('/result')

def result(request):
    print "test"
    print request.session['comments']
    # return render(request, 'surveyform/index.html')
    return render(request, 'surveyform/result.html')

def back(request):
    return redirect('/')
# Create your views here.
