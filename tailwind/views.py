from django.shortcuts import render


def tailwind_home(request):
    return render(request, 'tailwind/base.html')


def sidenav_scrimba(request):
    return render(request, 'tailwind/tmp/sidenav-scrimba.html')
