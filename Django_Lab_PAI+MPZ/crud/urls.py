from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article_list'),
    path('view/<int:pk>', views.ArticleView.as_view(), name='article_view'),
    path('new', views.ArticleCreate.as_view(), name='article_new'),
    path('view/<int:pk>', views.ArticleView.as_view(), name='article_view'),
    path('edit/<int:pk>', views.ArticleUpdate.as_view(), name='article_edit'),
    path('delete/<int:pk>', views.ArticleDelete.as_view(), name='article_delete'),
]
