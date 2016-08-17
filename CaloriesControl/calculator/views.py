from django.shortcuts import render


def index(request):

    context = {
        'page': 'welcome to The Dietary Calculator',
    }

    request.session['location'] = "unknown"
    if request.user.is_authenticated():
        request.session['location'] = "Earth"
    return render(request, 'base.html',context)

