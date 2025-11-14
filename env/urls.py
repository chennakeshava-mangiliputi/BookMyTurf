from django.contrib import admin
from django.urls import path, include
from turfbooking import views as turf_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', turf_views.home, name='home'),
    path('register/', turf_views.register, name='register'),
    path('book/<int:turf_id>/', turf_views.book_turf, name='book_turf'),
]
