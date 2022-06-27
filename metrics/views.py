from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


class MetricsView(View):
    def get(self, request):
        return render(request, 'metrics/results.html')

    def post(self, request):
        return redirect(reverse('metrics:results'))
