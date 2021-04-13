from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('snippets/', views.snippet_list),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    # path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    path('', views.api_root),
    path('snippets/<int:pk>/highlight', views.SnippetHighlight.as_view(), name='snippet-highlight'),
]