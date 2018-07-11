from django.shortcuts import render
from django.http import HttpResponse

from .models import Articles

# Create your views here.
def index(request):
    articles = Articles.objects.all()
    # import pdb;pdb.set_trace()
    return render(request, 'posts/index.html', { 'articles' : articles })

def details(request, id):
    article = Articles.objects.get(id=id)
    # import pdb;pdb.set_trace()
    return render(request, 'posts/details.html', { 'article' : article })