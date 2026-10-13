from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('books/',views.book_list, name='book_list'),

    path('books/<int:id>/',views.book_detail, name='book_detail'),

    path('add-book/',views.add_book, name='add_book'),

    path('edit-book/<int:id>/', views.edit_book, name='edit_book'),

    path('delete-book/<int:id>/', views.delete_book, name='delete_book'),

    path('register/', views.register,name='register'),

    path('login/',views.login_view,name='login'),

    path('logout/',  views.logout_view, name='logout' ),

    path('profile/', views.profile, name='profile' ),
]