from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
        ## server a gidip sayfayi yeniledigimizde buradaki printler powershell de calisir
    # print(request)
    # print(request.user)
    # print(request.method)
    # print(request.COOKIES)
    # print(request.path)
    print(request.META)

    ## http.response da request in verilerini cekemeyiz. Asagaidaki kod calismaz
    http = "<html> <h3> Hello World!!! </h3> </html> <br> {{ request.user }} "
    return HttpResponse(http)



# Note: context, react da props un karsiligidir. 
## isim farkli olabilir ama best practice budur.
## dict formatinda olmasi gerekir render icinde vermek icin
## context degiskenine atamadan direkt render icine de yazilabilir.
## template de cagirirken context.title sekline degil direkt olarak title seklinde cagrilir

def special(request):
    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [1, 2, 3]
    }

    return render(request, "app/special.html", context)