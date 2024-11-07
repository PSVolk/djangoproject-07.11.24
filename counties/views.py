from django.http import HttpResponse
def index(reqwest):
    res = '''<a href=/history>История</a><br>
    <a href=/cities>Города</a><br>
    <a href=/facts>Факты</a>'''
    return HttpResponse(res)

def history(reqwest):
    return HttpResponse('История')

def cities(reqwest):
    return HttpResponse('Город')

def facts(reqwest):
    return HttpResponse('Факты')