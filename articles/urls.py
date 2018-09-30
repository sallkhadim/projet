from django.conf.urls import url
from.import views

urlpatterns = [
    url(r'^ScanPort/$',views.ScanPort, name="ScanPort"),
    url(r'^show/$',views.show, name="show"),
    url(r'^addArticle/$',views.addArticle, name="addArticle"),
    url(r'^ScanReseau/$',views.ScanReseau, name="ScanReseau"),
    url(r'^ScanAgressif/$',views.ScanAgressif, name="ScanAgressif"),
    url(r'^ScanSystem/$',views.ScanSystem, name="ScanSystem"),
    url(r'^Apropos/$',views.Apropos, name="Apropos"),
    
    url(r"^pentestSys/$", views.pentestSys, name="pentestSys"),
    url(r"^pentestSys/collecte/$", views.collecte, name="collecte"),
    url(r"^pentestSys/collecte/scanPorts/$", views.scan, name="scan"),
    url(r"^pentestSys/collecte/scanPorts/osetport$", views.scanSimple, name="scanSimple"),
    url(r"^pentestSys/collecte/scanPorts/agressif$", views.scanAgressif, name="scanAgressif"),
    url(r"^pentestSys/collecte/scanRéseau/$", views.scanReseau, name="scanReseau"),

]  
