from django.http import JsonResponse
from genres.models import Genre


def genre_view(request):
    genres = Genre.objects.all()
    data = [{'id': genre.id, 'name': genre.name}
            for genre in genres]
    return JsonResponse(data, safe=False)
