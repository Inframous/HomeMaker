from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.home, name='home'),
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    path('edit_recipe/<recipe_id>', views.edit_recipe, name='edit_recipe'),
    path('show_recipe/<recipe_id>', views.show_recipe, name='show_recipe'),
    path('delete_recipe/<recipe_id>', views.delete_recipe, name='delete_recipe'),    
    path('search/', views.search_db, name='search_db'),
    path('db/', views.show_db, name='show_db'),
] 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, 
                              document_root=settings.STATIC_ROOT)