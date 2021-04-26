from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

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

urlpatterns = format_suffix_patterns(urlpatterns)

