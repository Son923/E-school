from django.http import HttpResponse
from django.views.decorators.http import require_POST

import json

@require_POST
def example(request):
	return HttpResponse(f'Hello, world. This is the webhook request. Data: {request}')
