from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView
from django.utils.decorators import method_decorator
from .forms import LoginForm, AccountForm, MiniSiteForm, MiniSiteUpdateForm
from authtools.views import LoginView as ALoginView
from product_minisite.models import MiniSite
from product_minisite.forms import  ( SiteConfigModulesForm,
    SiteConfigContentForm, SiteConfigStyleForm )
from business.models import Organization
from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse_lazy

def has_customer_user(user):
    try:
        customer_user = user.customer_user
    except:
        return False
    return True

class RegisterView(TemplateView):
    template_name = 'ui/register.html'

class LoginView(ALoginView):
    template_name = 'ui/login.html'
    form_class = LoginForm
    success_url = 'dashboard'


@method_decorator(user_passes_test(has_customer_user), name='dispatch')
class HomeView(TemplateView):
    template_name = 'ui/home.html'

@method_decorator(user_passes_test(has_customer_user), name='dispatch')
class AccountView(TemplateView):
    template_name = 'ui/account.html'

@method_decorator(user_passes_test(has_customer_user), name='dispatch')
class AccountEditView(FormView):
    template_name = 'ui/account_edit.html'
    form_class = AccountForm

@method_decorator(user_passes_test(has_customer_user), name='dispatch')
class DashboardView(TemplateView):
    template_name = 'ui/dashboard.html'

@method_decorator(user_passes_test(has_customer_user), name='dispatch')
class MinisiteCreateView(CreateView):
    template_name = 'ui/minisite_create.html'
    form_class = MiniSiteForm
    model = MiniSite
    success_url = 'minisite-list'

    def form_valid(self, form):
        minisite = form.save(commit=False)
        minisite.customer = self.request.user.customer_user.customer
        return super(MinisiteCreateView, self).form_valid(form)


@method_decorator(user_passes_test(has_customer_user), name='dispatch')
class MinisiteUpdateModulesView(UpdateView):
    template_name = 'ui/minisite_update.html'
    form_class = SiteConfigModulesForm
    model = MiniSite
    def get_success_url(self):
        return reverse_lazy('minisite-update-modules', kwargs={"pk":self.object.pk})


@method_decorator(user_passes_test(has_customer_user), name='dispatch')
class MinisiteUpdateContentView(UpdateView):
    template_name = 'ui/minisite_update.html'
    form_class = SiteConfigContentForm
    model = MiniSite
    def get_success_url(self):
        return reverse_lazy('minisite-update-content', kwargs={"pk":self.object.pk})


@method_decorator(user_passes_test(has_customer_user), name='dispatch')
class MinisiteUpdateStyleView(UpdateView):
    template_name = 'ui/minisite_update.html'
    form_class = SiteConfigStyleForm
    model = MiniSite
    def get_success_url(self):
        return reverse_lazy('minisite-update-style', kwargs={"pk":self.object.pk})


@method_decorator(user_passes_test(has_customer_user), name='dispatch')
class MinisiteDetailView(DetailView):
    template_name = 'ui/minisite_detail.html'
    model = MiniSite

@method_decorator(user_passes_test(has_customer_user), name='dispatch')
class MiniSiteListView(ListView):
    model = MiniSite
    page_kwarg = 'page'
    paginate_by = 100
    template_name = 'ui/minisite_list.html'

    def get_queryset(self):
        return MiniSite.objects.filter(customer=self.request.user.customer_user.customer)


class MiniSitePublicView(DetailView):
    model = MiniSite
    #template_name = 'TEMPLATE_NAME'

    def get_template_names(self):
        return [self.object.site_template+"/index.html"]
