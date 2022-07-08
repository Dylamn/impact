import json

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .core import Runner


class MetricsView(View):
    def get(self, request):
        return render(request, 'metrics/results.html')

    def post(self, request):
        url = request.POST.get('page_url')

        runner = Runner(url)

        results = runner.start()
        applied_rules = runner.get_rules_from_results()

        ctx = {
            'results': results,
            'applied_rules': applied_rules,
        }

        return render(request, 'metrics/results.html', ctx)
