from datetime import timedelta

from django.shortcuts import render, reverse
from django.utils import timezone
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Report
from .forms import ReportForm

# Create your views here.
@login_required
def homepage_view(request):
    reports = Report.objects.order_by("-date")[:3]
    context = {
        "reports": reports
    }
    return render(request, 'index.html', context=context)


class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    related_object_name = 'report'
    form_class = ReportForm
    template_name = 'inspection/create_report.html'


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    related_object_name = 'report'
    template_name = 'inspection/report_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        report = context['report']
        context['managers_preference'] = report.manager.after_and
        managers_preference = context['managers_preference']
        if managers_preference.strip().endswith('.'):
            context['ends_with_full_stop'] = True
        context['now'] = timezone.now()
        context['day'] = report.date.day
        month = timedelta(weeks=4)
        context['effective_date'] = context['report'].date
        if context['day'] > 15:
            context['effective_date'] = context['report'].date + month
        return context


class ReportListView(LoginRequiredMixin, ListView):
    # model = Report
    queryset = Report.objects.order_by('-date')
    related_object_name = 'reports'
    paginate_by = 12
    template_name = 'inspection/report_list.html'


class ReportUpdateView(LoginRequiredMixin, UpdateView):
    model = Report
    context_object_name = 'reports'
    form_class = ReportForm
    template_name = 'inspection/create_report.html'