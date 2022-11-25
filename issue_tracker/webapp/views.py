from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, reverse
from webapp.models import Issue
from django.views.generic import TemplateView, View, FormView
from webapp.forms import IssueForm
from webapp.base_views import FormView as CustomFormView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.order_by('-created_at')
        return context


class IssueView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs.get('pk'))
        return context


class DeleteView(View):
    def get(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        context = {'issue': issue}
        return render(request, 'delete.html', context)

    def post(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        issue.delete()
        return redirect('index')


# class CreateView(View):
#     def get(self, request, *args, **kwargs):
#         context = {'issue_form': IssueForm()}
#         return render(request, 'create.html', context)
#
#     def post(self, request):
#         issue_form = IssueForm(data=request.POST)
#         if issue_form.is_valid():
#             issue_type = issue_form.cleaned_data.pop('type')
#             issue = Issue.objects.create(**issue_form.cleaned_data)
#             issue.type.set(issue_type)
#             return redirect('issue', issue.pk)
#         else:
#             context = {
#                 'issue_form': IssueForm()
#             }
#             return render(request, 'create.html', context)


class CreateView(CustomFormView):
    template_name = "create.html"
    form_class = IssueForm

    def get_redirect_url(self):
        return reverse('issue', kwargs={'pk': self.issue.pk})

    def form_valid(self, form):
        self.issue = form.save()
        return super().form_valid(form)


# class UpdateView(View):
#     def get(self, request, pk):
#         issue = get_object_or_404(Issue, pk=pk)
#         context = {
#             'pk': issue.pk,
#             'issue_form': IssueForm(initial={
#                 'summary': issue.summary,
#                 'description': issue.description,
#                 'type': issue.type.all(),
#                 'status': issue.status
#             })
#         }
#         return render(request, 'update.html', context)
#
#     def post(self, request, pk):
#         issue = get_object_or_404(Issue, pk=pk)
#         issue_form = IssueForm(data=request.POST)
#         if issue_form.is_valid():
#             issue.summary = issue_form.cleaned_data['summary']
#             issue.description = issue_form.cleaned_data['description']
#             issue.status = issue_form.cleaned_data['status']
#             issue.save()
#             issue.type.set(issue_form.cleaned_data['type'])
#             return redirect('issue', issue.pk)
#         else:
#             return render(request, 'update.html', {'issue_form': issue_form})


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


