from django.shortcuts import render
from django.utils.translation import gettext as _


def index(request):
    return render(request, "app/home_page.html", {
        "title": _("Website Statistics"),
        "visits": 82374
    })
