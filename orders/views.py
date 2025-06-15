from django.http import HttpResponse


def index(request):
    """Simple view for orders home page."""
    return HttpResponse('Orders Home')
