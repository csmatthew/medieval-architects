from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render

from .models.building_name import Building


def mapper_view(request):
	"""
	View for the map page.
	"""
	return render(request, 'mapper/mapper.html')


def building_georef_data(request):
	"""Return building coordinates for the map."""
	data = []

	for building in Building.objects.select_related("geo_ref").order_by("name"):
		try:
			geo_ref = building.geo_ref
		except ObjectDoesNotExist:
			continue

		if geo_ref.latitude is None or geo_ref.longitude is None:
			continue

		data.append(
			{
				"id": building.id,
				"name": building.name,
				"location": building.location,
				"county": building.county,
				"latitude": float(geo_ref.latitude),
				"longitude": float(geo_ref.longitude),
			}
		)

	return JsonResponse(data, safe=False)
