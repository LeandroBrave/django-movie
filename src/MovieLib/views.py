from django.views.generic import ListView
from MovieLib.models import Movie
from MovieLib.forms import MovieMixin
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.core.urlresolvers import reverse

# Create your views here.
class IndexView(ListView):
	template_name = 'index.html'
	model = Movie
	
	def get_queryset(self):
		qs = super(IndexView, self).get_queryset()
		if self.kwargs.get('exp') is not None:
			qs = qs.filter(experience_level__exact=self.kwargs['exp'])
		return qs

class CreateView(CreateView):
	template_name = 'create.html'
	model = Movie
	fields = ['title','genre','price','release_date']
	success_url = '/'
	
class UpdateView(UpdateView):
	template_name = 'update.html'
	model = Movie
	fields = ['title','genre','price','release_date']
	success_url = '/'
	
class DeleteView(MovieMixin, DeleteView):
    template_name = 'delete_confirm.html'
    def get_success_url(self):
        return reverse('movie_index')
		
class SearchView(ListView):
    model = Movie
    select_related = ['title']
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.REQUEST.get("q")
        return self.model.objects.filter(title__icontains=query)