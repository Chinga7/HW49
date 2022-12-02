from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, reverse
from django.utils.http import urlencode

from webapp.models import Issue
from django.views.generic import TemplateView, View, FormView, ListView
from webapp.forms import IssueForm, SearchForm
from webapp.base_views import CustomFormView, CustomListView, CustomSearchView
from datetime import timedelta


# class HomeView(CustomListView):
#     template_name = 'index.html'
#     model = Issue
#     context_key = 'issues'
#
#     def get_objects(self):
#         return super().get_objects().order_by('-created_at')


class HomeView(ListView):
    template_name = 'index.html'
    model = Issue
    context_object_name = 'issues'
    ordering = ('-created_at')
    paginate_by = 3
    paginate_orphans = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SearchForm
        return context


class SearchView(CustomSearchView):
    template_name = 'index.html'
    model = Issue
    search_form = SearchForm
    context_object_name = 'issues'
    ordering = ('-created_at')
    paginate_by = 3
    paginate_orphans = 2

    def get_queryset(self):
        if self.search_value:
            queryset = super().get_queryset()
            queryset = queryset.filter(Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class IssueView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs.get('pk'))
        return context


class CreateView(CustomFormView):
    template_name = "create.html"
    form_class = IssueForm

    def get_redirect_url(self):
        return reverse('issue', kwargs={'pk': self.issue.pk})

    def form_valid(self, form):
        self.issue = form.save()
        return super().form_valid(form)


class UpdateView(FormView):
    template_name = "update.html"
    form_class = IssueForm

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Issue, pk=pk)

    def dispatch(self, request, *args, **kwargs):
        self.issue = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = self.issue
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.issue
        return kwargs

    def form_valid(self, form):
        self.issue = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issue', kwargs={'pk': self.issue.pk})


class DeleteView(View):
    def get(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        context = {'issue': issue}
        return render(request, 'delete.html', context)

    def post(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        issue.delete()
        return redirect('index')