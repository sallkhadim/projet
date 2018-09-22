from django.shortcuts import render
# Create your views here.
from .ScanReseau import TestR
from .ScanPort import Test
from .models import Articles,Blog,ArticlesForm

def show(request):
    articles = Articles.objects.all()
    return render(request, 'articles/show.html' , {'articles': articles })



def addArticle(request):
    sauvegarde = False
    form = ArticlesForm(request.POST or None, request.FILES)
    if form.is_valid():
        article = Articles()
        article.titre = form.cleaned_data["titre"]
        article.body = form.cleaned_data["body"]
        article.image = form.cleaned_data["image"]
        article.save()
        sauvegarde = True

    return render(request, 'articles/addArticle.html', {'form': form})



# def show1(request):
#     posts = Post.objects.all()
#     return render(request, 'articles/show.html' , {'article': article })

def menu(request):
    return render(request, 'articles/menu.html')

def acc(request):
    return render(request, 'articles/acc.html')

def ScanReseau(request):
    pos1=TestR.testreseau()
    return render(request, 'articles/ScanReseau.html', {'pos1':pos1})

def ScanPort(request):
    pos=Test.testport()
    return  render(request, 'articles/ScanPort.html', {'pos':pos})

def Apropos(request):
    return  render(request, 'articles/Apropos.html')


