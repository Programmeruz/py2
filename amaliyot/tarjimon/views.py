from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """views bolimida sahifada nima chiqishi yoziladi va unda malumot olish va jonatish mumkin"""
    #soz = request.GET.get(input name ni yoziladi)
    rang = request.GET.get('rang')
    if rang == 'Qizil':
        soz = 'red'
    elif rang == 'Sariq':
        soz = 'yellow'
    elif rang == 'Kok':
        soz = 'blue'
    elif rang == 'Qora':
        soz = 'black'
    else:
        soz = 'text'

    xabar = request.GET.get('xab')
    if  xabar =='Jadval' or xabar == 'jadval':
        mes = 'table'
    elif xabar == 'Club' or xabar == 'club':
        mes = 'logo'
    elif xabar == 'Learn' or xabar == 'learn':
        mes = 'comp'
    elif xabar == 'Liga' or xabar == 'liga':
        mes = 'apl'
    else:
        mes = None
    return render(request, 'index.html', {'rang': soz, 'sty': mes, 'mes':xabar})
