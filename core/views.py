from django.shortcuts import render
from django.db.models import Q

from .models import Craftsperson, Building

# Create your views here.


def index(request):
    return render(request, "core/index.html")


def search(request):
    q = request.GET.get('q', '').strip()
    craftspersons = Craftsperson.objects.none()
    buildings = Building.objects.none()
    if q:
        craftspersons = Craftsperson.objects.filter(
            Q(name__icontains=q) |
            Q(forename__icontains=q) |
            Q(label__icontains=q) |
            Q(sequence_label__icontains=q)
        ).order_by('name')[:100]
        buildings = Building.objects.filter(
            Q(name__icontains=q)
        ).order_by('name')[:100]
    context = {
        'query': q,
        'craftspersons': craftspersons,
        'buildings': buildings,
    }
    return render(request, "core/search_results.html", context)
