from django.shortcuts import render


def about_view(request):
    """
    View for the about page.
    """
    return render(request, 'core/about.html')


def search_view(request):
    """
    View for the search page.
    """
    return render(request, 'core/search.html')
