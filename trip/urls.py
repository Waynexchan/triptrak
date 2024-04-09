
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, trip_list, trip_search, TripCreateView ,TripDetailView, NoteDetailView, NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView, TripUpdateView, TripDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home' ),
    path('dashboard/', trip_list, name='trip-list' ),
    path('dashboard/trip/search', trip_search, name='trip-search' ),
    path('dashboard/note/', NoteListView.as_view(), name='note-list' ),
    path('dashboard/trip/create/', TripCreateView.as_view(), name='trip-create' ),
    path('dashboard/note/create/', NoteCreateView.as_view(), name='note-create' ),
    path('dashboard/trip/<int:pk>/', TripDetailView.as_view(), name='trip-detail' ),
    path('dashboard/note/<int:pk>/', NoteDetailView.as_view(), name='note-detail' ),
    path('dashboard/note/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update' ),
    path('dashboard/note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete' ),
    path('dashboard/trip/<int:pk>/update/', TripUpdateView.as_view(), name='trip-update' ),
    path('dashboard/trip/<int:pk>/delete/', TripDeleteView.as_view(), name='trip-delete' ),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

