# urls.py

from django.urls import path
from .views import home, register, login_view, logout_view, upload_dataset, create_visualization, add_data_point, map_columns

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('upload-dataset/', upload_dataset, name='upload_dataset'),
    path('create-visualization/', create_visualization, name='create_visualization'),
    path('add-data-point/<int:visualization_id>/', add_data_point, name='add_data_point'),
    path('map-columns/<int:visualization_id>/', map_columns, name='map_columns'),
    # Add more paths for additional views as needed
]
