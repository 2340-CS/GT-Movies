from django.shortcuts import render

# Create your views here.
def index(request):
    template_data = {}
    template_data['title'] = 'GTMovies Store'
    return render(request, 'moviesapp/index.html', {'template_data': template_data})
def about(request):
    template_data = {}
    return render(request, 'moviesapp/about.html', {'template_data': template_data})

