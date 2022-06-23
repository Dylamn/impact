from django.views.generic import TemplateView


class LandingView(TemplateView):
    """Display the landing page of the website."""
    template_name = 'impact/index.html'


class TermsView(TemplateView):
    """Display the terms and conditions page of the website."""
    template_name = 'impact/terms.html'
