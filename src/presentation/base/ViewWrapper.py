
from django.http import HttpResponse
from django.views import View
from rest_framework import status

import json
from dataclasses import asdict


class ViewWrapper(View):

    view_factory = None

    def get(self, request, *args, **kwargs):
        try:
            if request.method == 'GET':
                body, statusResponse = self.view_factory.get().get(**kwargs)
            else:
                body = {
                    'message': 'METHOD NOT ALLOWED'
                }
                statusResponse = status.HTTP_405_METHOD_NOT_ALLOWED

        except Exception as error:
            body = { 'error': str(error) }
            statusResponse = status.HTTP_500_INTERNAL_SERVER_ERROR
        
        return HttpResponse(
            json.dumps(asdict(body)),
            status=statusResponse,
            content_type='application/json'
        )