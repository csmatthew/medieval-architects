from django.shortcuts import render


def about_view(request):
    """
    View for the about page.
    """
    return render(request, 'core/about.html')
