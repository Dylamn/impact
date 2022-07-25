from django.shortcuts import render
from django.views import View

from .core import Runner
from .models import Report


class MetricsView(View):
    def get(self, request):
        return render(request, 'metrics/results.html')

    def post(self, request):
        url = request.POST.get('page_url')

        runner = Runner(url)

        score, results = runner.start()

        previous_report = Report.objects.filter(url=url).first()

        #  max(created_at)
        if previous_report is not None:
            previous_report = previous_report.id

        report = Report(
            url=url, score=score, metrics=results,
            previous_report=previous_report
        )

        ctx = {
            'report': report,
        }

        return render(request, 'metrics/results.html', ctx)
