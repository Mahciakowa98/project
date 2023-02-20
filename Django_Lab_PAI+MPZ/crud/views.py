from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from crud.models import Article
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

#zadanie 3
class ArticleList(ListView):
    model = Article
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArticleList, self).dispatch(*args, **kwargs)


class ArticleView(DetailView):
    model = Article

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArticleView, self).dispatch(*args, **kwargs)


class ArticleCreate(CreateView):
    model = Article
    fields = ['title', 'author', 'number_of_words', 'rate']
    success_url = reverse_lazy('article_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArticleCreate, self).dispatch(*args, **kwargs)


class ArticleUpdate(UpdateView):
    model = Article
    fields = ['title', 'author', 'number_of_words', 'rate']
    success_url = reverse_lazy('article_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArticleUpdate, self).dispatch(*args, **kwargs)


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArticleDelete, self).dispatch(*args, **kwargs)
