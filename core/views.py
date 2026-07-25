from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db import models

# Import models we will search/list
from buildings.models.building_name import Building
from people.models import Person


def about_view(request):
    """View for the about page."""
    return render(request, 'core/about.html')


def search_view(request):
    """Search across Buildings and People.

    Accepts GET param `q` and returns matching results.
    """
    q = request.GET.get('q', '').strip()

    building_results = Building.objects.none()
    person_results = Person.objects.none()

    if q:
        building_results = Building.objects.filter(
            models.Q(name__icontains=q)
            | models.Q(location__icontains=q)
            | models.Q(county__icontains=q)
        ).order_by('name')

        person_results = Person.objects.filter(
            models.Q(given_name__icontains=q)
            | models.Q(surname__icontains=q)
            | models.Q(label__icontains=q)
            | models.Q(preposition__icontains=q)
        ).order_by('surname', 'given_name')

    # Paginate building results
    page_number = request.GET.get('page')
    paginator = Paginator(building_results, 12)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'core/search.html',
        {
            'q': q,
            'building_results': page_obj,
            'person_results': person_results[:50],
        },
    )


def record_list(request):
    records = Building.objects.all().order_by('name')
    paginator = Paginator(records, 10)  # Show 10 records per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/record_list.html', {'page_obj': page_obj})


def record_detail(request, pk):
    record = get_object_or_404(Building, pk=pk)
    return render(request, 'core/record_detail.html', {'record': record})
