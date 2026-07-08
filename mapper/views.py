from django.shortcuts import render


def mapper_view(request):
    """
    View for the map page.
    """
    return render(request, 'mapper/mapper.html')
