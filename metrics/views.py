from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import SuspiciousOperation, PermissionDenied
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import View, ListView
from phantomas import PhantomasError

from .core import Runner
from .models import Report


def run(request):
    url = request.POST.get('page_url')

    runner = Runner(url)

    try:
        score, results = runner.start()

        report = Report(url=url, score=score, metrics=results)
    except PhantomasError as e:
        if "URL" in e.args[0]:
            error_code = "url"
        else:
            error_code = "network"

        return redirect(f"{reverse('landing')}?error={error_code}")

    if request.user.is_authenticated:
        report.user = request.user
        previous_report = Report.objects \
            .filter(url=url, user=request.user).order_by('-created_at').first()

        report.previous_report = previous_report

    report.save()

    return redirect(reverse('metrics:results', args=(report.pk,)), permanent=True)


@login_required
def compare_reports(request, actual_report_uuid, previous_report_uuid):
    previous_report = Report.objects.get(pk=previous_report_uuid)
    actual_report = Report.objects.get(pk=actual_report_uuid)

    if request.user.id != previous_report.user_id \
            or request.user.id != actual_report.user_id:
        raise PermissionDenied('One of the reports are not owned by yourself.')

    if previous_report.url != actual_report.url:
        raise SuspiciousOperation("Reports are not related.")

    context = {
        "actual_report": actual_report,
        "previous_report": previous_report,
    }

    return render(request, 'metrics/compare.html', context)


class ReportView(View):
    object: Report

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.object = get_object_or_404(Report, pk=kwargs.get('pk'))

    def get_render_data(self):
        ctx = {}
        template_name = 'metrics/results.html'
        section_name: str = self.kwargs.get('section')

        if section_name in self.object.metrics and self.kwargs.get('metric'):
            ctx['metric'] = self.get_metric(self.object.metrics[section_name])
            ctx['report_uuid'] = self.object.pk
            template_name = 'metrics/metric.html'
        else:
            ctx['report'] = self.object

        return template_name, ctx

    def get(self, request, *args, **kwargs):
        template_name, context = self.get_render_data()

        return render(request, template_name, context)

    def get_metric(self, section: dict):
        if not isinstance(section, dict):
            return

        metric = self.kwargs['metric']

        return {
            'value': section['metrics'].get(metric),
            'rule': section['rules'].get(metric),
        }


class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'metrics/report-list.html'
    context_object_name = 'report_list'

    def get_queryset(self):
        """Return the list of items for this view."""
        return super() \
            .get_queryset() \
            .filter(user=self.request.user)
