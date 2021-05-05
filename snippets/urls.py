from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url

app_name = 'snippets'

urlpatterns = [
    # path('snippets/', views.snippet_list),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    # # path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    path('create_book_normal/', views.create_book_normal, name='create_book_normal'),
    path('book_list/', views.BookList.as_view(), name='book_list'),
    path('add_bird/', views.BirdAddView.as_view(), name="add_bird"),
    path('bird_list/', views.BirdListView.as_view(), name="bird_list")
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    path('', views.api_root),
    path('snippets/<int:pk>/highlight', views.SnippetHighlight.as_view(), name='snippet-highlight'),
]

urlpatterns += [
    # url(r'^book/create', views.ComicsCreate, name="BookCreate"),
    # url(r'^author/create', views.AuthorCreatePopup, name="AuthorCreate"),
    # url(r'^author/(?P<pk>\d+)/edit', views.AuthorEditPopup, name="AuthorEdit"),
    # url(r'^author/ajax/get_author_id', views.get_author_id, name="get_author_id"),
    path('comics/create/', views.ComicsCreate, name="ComicsCreate"),
    path('author/create/', views.AuthorCreatePopup, name="AuthorCreate"),
    path('author/<int:pk>/edit/', views.AuthorEditPopup, name="AuthorEdit"),
    path('author/ajax/get_author_id/', views.get_author_id, name="get_author_id"),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
