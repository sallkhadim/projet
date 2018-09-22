from django.conf.urls import url
from.import views

urlpatterns = [
    url(r'^ScanPort/$',views.ScanPort, name="ScanPort"),
    url(r'^show/$',views.show, name="show"),
    url(r'^addArticle/$',views.addArticle, name="addArticle"),
    url(r'^ScanReseau/$',views.ScanReseau, name="ScanReseau"),
    url(r'^Apropos/$',views.Apropos, name="Apropos"),
]

    # url(r'^$',views.acc, name="acc"),
