from django.shortcuts import render
# Create your views here.
from .ScanReseau import TestR
from .ScanPort import Test
from .ScanSystem import Test1
from .ScanAgressif import TestA
from .models import Articles,ArticlesForm

from .forms import ScanForm
import nmap
import subprocess
import os



def show(request):
    articles = Articles.objects.all()
    return render(request, 'articles/show.html' , {'articles': articles })


def addArticle(request):

    form = ArticlesForm(request.POST or None, request.FILES)
    if form.is_valid():
        article = Articles()

        article.titre = form.cleaned_data["titre"]
        article.body = form.cleaned_data["body"]
        article.image = form.cleaned_data["image"]
        
        article.save()

    return render(request, 'articles/addArticle.html', {'form': form})


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

def ScanSystem(request):
    poss=Test1.testsystem()
    return  render(request, 'articles/ScanSystem.html', {'poss':poss})

def ScanAgressif(request):
    po=TestA.testagressif()
    return  render(request, 'articles/ScanAgressif.html', {'po':po})

def Apropos(request):
    return  render(request, 'articles/Apropos.html')


def scan(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        res = ""
        target = ""
        erreur = ""
        form = ScanForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nmScan = nmap.PortScanner()
            print(form)
            target = request.POST['target']

            try:
                resultat = nmScan.scan(hosts=target, arguments='-O')
                ports = resultat['scan'][target]['tcp']
                res = []
                i=1
                for i in ports:
                        porti = ports[i]
                        print(porti['state'])

                        res.append({'port':i,'state':porti['state'], 'name':porti['name'], 'product':porti['product'], 'version':porti['version']})
            except:
                erreur = "veuillez entrer une adresse IP valide"
        return render(request, "articles/scan_result.html", {"resultat": res, "target": target, "erreur": erreur})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScanForm()
        return render(request, 'articles/scan_form.html', {'form': form})

def scanSimple(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        res = ""
        target = ""
        erreur = ""
        form = ScanForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nmScan = nmap.PortScanner()
            print(form)
            target = request.POST['target']

            try:
                resultat = nmScan.scan(hosts=target, arguments='-sV')
                ports = resultat['scan'][target]['tcp']
                res = []
                i=1
                for i in ports:
                        porti = ports[i]
                        print(porti['state'])

                        res.append({'port':i,'state':porti['state'], 'name':porti['name'], 'product':porti['product'], 'version':porti['version']})
            except:
                erreur = "veuillez entrer une adresse IP valide"
        return render(request, "articles/scansimple_result.html", {"resultat": res, "target": target, "erreur": erreur})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScanForm()
        return render(request, 'articles/scansimple_form.html', {'form': form})

def scanAgressif(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        res = ""
        target = ""
        erreur = ""
        form = ScanForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nmScan = nmap.PortScanner()
            print(form)
            target = request.POST['target']

            try:
                resultat = nmScan.scan(hosts=target, arguments='-osscan-guess')
                ports = resultat['scan'][target]['tcp']
                res = []
                i=1
                for i in ports:
                        porti = ports[i]
                        print(porti['state'])

                        res.append({'port':i,'state':porti['state'], 'name':porti['name'], 'product':porti['product'], 'version':porti['version']})
            except:
                erreur = "veuillez entrer une adresse IP valide"
        return render(request, "articles/scanagressiff_result.html", {"resultat": res, "target": target, "erreur": erreur})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScanForm()
        return render(request, 'articles/scanagressiff_form.html', {'form': form})



def scanReseau(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        target = ""
        erreur = ""
        res = ""
        form = ScanForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nma = nmap.PortScanner()
            print(form)
            target = request.POST['target']
            try:
                result = nma.scan(hosts=target, arguments='-sP')
                res = []
                print(result)
                hosts_list = [x for x in nma.all_hosts()]
                t = len(hosts_list)
                for i in range(0, t):
                    print("Hôte: ", hosts_list[i])
                    host = hosts_list[i]
                    print("         Nom: ", nma[host]['hostnames'])

                    print("         Adresses: ", nma[host]['addresses'])
                    print("         AdresseIPv4: ", nma[host]['addresses']['ipv4'])
                    try:
                         print("         AdresseMAC: ", nma[host]['addresses']['mac'])
                         adresseMAC = nma[host]['addresses']['mac']
                    except:
                        print("       AdressesMAC: none")
                        adresseMAC = "  none"
                    print("         Etat: ", nma[host]['status'])
                    print("         Etat: ", nma[host]['status']['state'])
                    print()
                    res.append({'host':hosts_list[i], 'state':nma[host]['status']['state'], 'hostname':nma[host]['hostnames'], 'adresseIPv4':nma[host]['addresses']['ipv4'], 'adresseMAC':adresseMAC})
            except:
                erreur = "veuillez entrer une addresse réseau valide"
        return render(request, "articles/scan_reseau_result.html", {"resultat": res, "result": result, "erreur": erreur})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScanForm()
        return render(request, 'articles/scan_reseau_form.html', {'form': form})

def pentestSys(request):
    return render(request, "articles/pentestSys.html", {})

def pentestWeb(request):
    return render(request, "articles/pentestWeb.html", {})

def collecte(request):
    col = "collecte d'informations"
    return render(request, "articles/collecte.html", {"col": col})

