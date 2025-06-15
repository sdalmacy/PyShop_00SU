from django.http import HttpResponse


def index(request):
    """Simple view for payments home page."""
    return HttpResponse('Payments Home')
