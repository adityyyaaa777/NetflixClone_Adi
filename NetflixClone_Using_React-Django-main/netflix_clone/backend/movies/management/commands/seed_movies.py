from django.core.management.base import BaseCommand
from movies.models import Movie
DATA = [
 {'title':'Midnight Run','description':'A former detective races across the city after discovering a hidden conspiracy.','content_type':'movie','genre':'Action, Thriller','release_year':2025,'rating':8.2,'duration':'2h 08m','maturity':'U/A 16+','poster_url':'https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=800&q=80','backdrop_url':'https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?auto=format&fit=crop&w=1600&q=80','featured':True},
 {'title':'Dark Horizon','description':'A crew trapped beyond the solar system finds a signal that should not exist.','content_type':'movie','genre':'Sci-Fi, Drama','release_year':2024,'rating':8.7,'duration':'2h 21m','maturity':'U/A 13+','poster_url':'https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&w=800&q=80','backdrop_url':'https://images.unsplash.com/photo-1516339901601-2e1b62dc0c45?auto=format&fit=crop&w=1600&q=80'},
 {'title':'The Last Signal','description':'A mysterious broadcast connects four strangers and changes their lives overnight.','content_type':'series','genre':'Mystery, Drama','release_year':2025,'rating':9.1,'duration':'8 Episodes','maturity':'U/A 16+','poster_url':'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=800&q=80','backdrop_url':'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1600&q=80','featured':True},
 {'title':'City of Echoes','description':'A journalist returns home to investigate a disappearance everyone wants forgotten.','content_type':'series','genre':'Crime, Mystery','release_year':2023,'rating':8.5,'duration':'10 Episodes','maturity':'U/A 16+','poster_url':'https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&w=800&q=80','backdrop_url':'https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=1600&q=80'},
]
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for item in DATA: Movie.objects.update_or_create(title=item['title'], defaults=item)
        self.stdout.write(self.style.SUCCESS('Seeded sample catalog.'))
