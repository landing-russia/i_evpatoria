from django.shortcuts import render


def tailwind_home(request):
    return render(request, 'tailwind/main.html')


def sidenav_scrimba(request):
    return render(request, 'tailwind/tmp/sidenav-scrimba.html')


def navbars_dark_with_quick_action(request):
    return render(request, 'tailwind/navbars/dark_with_quick_action.html')


def navbars_dark_with_search(request):
    return render(request, 'tailwind/navbars/dark_with_search.html')


def navbars_simple(request):
    return render(request, 'tailwind/navbars/simple.html')


def navbars_simple_dark_with_menu_button_on_left(request):
    return render(request, 'tailwind/navbars/simple_dark_with_menu_button_on_left.html')


def navbars_simple_dark(request):
    return render(request, 'tailwind/navbars/simple_dark.html')


def navbars_simple_with_menu_button_on_left(request):
    return render(request, 'tailwind/navbars/simple_with_menu_button_on_left.html')


def navbars_with_centered_search_and_secondary_links_dark(request):
    return render(request, 'tailwind/navbars/with_centered_search_and_secondary_links_dark.html')


def navbars_with_centered_search_and_secondary_links(request):
    return render(request, 'tailwind/navbars/with_centered_search_and_secondary_links.html')


def navbars_with_quick_action(request):
    return render(request, 'tailwind/navbars/with_quick_action.html')


def navbars_with_search_in_column_layout(request):
    return render(request, 'tailwind/navbars/with_search_in_column_layout.html')


def navbars_with_search(request):
    return render(request, 'tailwind/navbars/with_search.html')
