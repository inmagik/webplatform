from django.conf.urls import url, include
from django.contrib import admin

from .views import ( HomeView, DashboardView,
    RegisterView, LoginView, AccountView, AccountEditView,
     MinisiteCreateView, MiniSiteListView, MinisiteDetailView,
     MinisiteUpdateModulesView, MinisiteUpdateContentView,
     MinisiteUpdateStyleView,
     MiniSitePublicView )


urlpatterns = [

    url(r'^register', RegisterView.as_view(), name="register"),
    url(r'^login', LoginView.as_view(), name="login"),
    url(r'^account-edit', AccountEditView.as_view(), name="account-edit"),
    url(r'^account', AccountView.as_view(), name="account"),
    url(r'^dashboard', DashboardView.as_view(), name="dashboard"),

    url(r'^minisite-list', MiniSiteListView.as_view(), name="minisite-list"),
    url(r'^minisite-create', MinisiteCreateView.as_view(), name="minisite-create"),
    url(r'^minisite-detail/(?P<pk>\d)', MinisiteDetailView.as_view(), name="minisite-detail"),
    url(r'^minisite-update-modules/(?P<pk>\d)', MinisiteUpdateModulesView.as_view(), name="minisite-update-modules"),
    url(r'^minisite-update-content/(?P<pk>\d)', MinisiteUpdateContentView.as_view(), name="minisite-update-content"),
    url(r'^minisite-update-style/(?P<pk>\d)', MinisiteUpdateStyleView.as_view(), name="minisite-update-style"),

    url(r'^minisite-public/(?P<pk>\d)', MiniSitePublicView.as_view(), name="minisite-public"),



    url(r'^$', HomeView.as_view(), name="home"),


]
