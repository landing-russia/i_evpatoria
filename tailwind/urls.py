from django.urls import path
from .views import *

app_name = 'tailwind'

urlpatterns = [
    path('', tailwind_home),
    path('tmp/sidenav-scrimba/', sidenav_scrimba),
    path('navbars/dark_with_quick_action/', navbars_dark_with_quick_action),
    path('navbars/dark_with_search/', navbars_dark_with_search),
    path('navbars/simple/', navbars_simple),
    path('navbars/simple_dark_with_menu_button_on_left/', navbars_simple_dark_with_menu_button_on_left),
    path('navbars/simple_dark/', navbars_simple_dark),
    path('navbars/simple_with_menu_button_on_left/', navbars_simple_with_menu_button_on_left),
    path('navbars/with_centered_search_and_secondary_links_dark/', navbars_with_centered_search_and_secondary_links_dark),
    path('navbars/with_centered_search_and_secondary_links/', navbars_with_centered_search_and_secondary_links),
    path('navbars/with_search_in_column_layout/', navbars_with_search_in_column_layout),
    path('navbars/with_search/', navbars_with_search),
]
