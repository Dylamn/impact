from django.http import HttpResponse
from phantomas import PhantomasError
from rest_framework.response import Response
from rest_framework.views import APIView

from metrics.core import Runner
from metrics.core.phantomas_wrapper.metrics_modules import AssetsMetrics
from .utils import check_url


class GenerateReport(APIView):
    """
    View which generates a report of the page that the url points to.

    * Requires token authentication.
    """

    def post(self, request, *args, **kwargs):
        if request.method != 'POST':
            return HttpResponse(status=405)

        url = request.POST.get('page_url', '')

        if url == '' or check_url(url) is False:
            error_body = {
                'error': {
                    'message': 'Url is empty or malformed.'
                }
            }

            return Response(error_body, status=400)

        runner = Runner(url)

        try:
            score, results = runner.start(extra_modules=[AssetsMetrics])
        except PhantomasError as e:
            if "URL" in e.args[0]:
                error_msg = "URL is not valid."
            else:
                error_msg = "A network error occurred. Maybe the website is not " \
                            "accessible."

            return Response({'message': error_msg}, status=422)

        json_body = {
            'message': 'report was successfully generated',
            'report': {
                'global_score': score,
                'data': results
            }
        }

        return Response(json_body, status=200)
