from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def Soma(request):
    x = int(request.post['x'])
    y = int(request.post['y'])

    soma: int = x + y

    return render(request, "adicao.html", {"adicao": soma})

