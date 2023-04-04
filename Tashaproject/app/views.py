from django.shortcuts import render

from django.http import HttpResponse

import datetime
# Create your views here.
def app1(request):
    now = datetime.datetime.now()
    return render(request, "index.html", {
        "new": now.month == 4 and now.day == 4
})

