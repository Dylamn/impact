from math import floor

from django.utils import translation
from django.utils.translation import gettext as _
from phantomas import PhantomasError
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from metrics.core import Runner
from metrics.core.phantomas_wrapper.metrics_modules import AssetsMetrics
from metrics.models import Report
from .utils import check_url


class GenerateReport(APIView):
    """
    View which generates a report of the page that the url points to.

    * Requires token authentication.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    http_method_names = ['post']

    score_messages = [
        "Comment vous dire...vous bénéficiez d’une belle marge de progression ;-) "
        "mais pas de panique, nous sommes là pour ça !",

        "Même si vous êtes sous la moyenne, c’est votre jour de chance : on vous "
        "propose une séance de rattrapage ;)",

        "Vous êtes sur la bonne voie même s’il va falloir poursuivre pour atteindre "
        "vos objectifs. On y va ensemble ?",

        "Le fruit de vos efforts est clairement visible et vous faites partie des "
        "bons élèves. Prêt à relever le défi pour vous rapprocher des meilleurs ?",

        "Des félicitations s’imposent ! Vous vous hissez sur le podium et vous avez "
        "intégré l’essentiel des bonnes pratiques. Et si on allait encore plus loin ?"
    ]

    def post(self, request, *args, **kwargs):
        translation.activate(request.headers.get('Accept-Language', 'en'))
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

            Report(url=url, score=score, metrics=results).save()
        except PhantomasError as e:
            if "URL" in e.args[0]:
                error_msg = "URL is not valid."
            else:
                error_msg = "A network error occurred. Maybe the website is not " \
                            "accessible."

            return Response({'message': error_msg}, status=422)

        if score == 100:
            score_message = self.score_messages[len(self.score_messages) - 1]
        else:
            index = floor(score / 100 * len(self.score_messages))
            score_message = self.score_messages[index]

        json_body = {
            'message': _('report was successfully generated'),
            'report': {
                'global_score': score,
                'score_message': score_message,
                'data': results
            }
        }

        return Response(json_body, status=200)
