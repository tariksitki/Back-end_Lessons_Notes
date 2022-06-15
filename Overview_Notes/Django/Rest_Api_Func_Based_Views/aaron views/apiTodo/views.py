from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.renderers import JSONRenderer



# Create your views here.
def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )



## Not: alt alta birden cok decorator yazilabilir ama en üstte api_view olmali.

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

## Bu basit view i yazarak su verileri elde ederiz. api_view  icinde izin verilen methodlari yazmadigimiz icin sadece get e izin verilir. Browser da bu görünür.

# HTTP 200 OK
# Allow: GET, OPTIONS
# Content-Type: application/json
# Vary: Accept

# {
#     "message": "Hello, world!"
# }





@api_view(["GET"])
def TodoList(request):
        # db den tüm verileri cekiyoruz
    queryset = Todo.objects.all()
    print(queryset)
        # cekilen tüm verileri convert ediyoruz. birden cok veri gelecegi icin many
    serializer = TodoSerializers(queryset, many=True)
    print(serializer)
    print(serializer.data)
    return Response(serializer.data)






## Önemli: 
## queryset print edildiginde <QuerySet [<Todo: aaa>]>   döner

## Serializer Return edilince:
# TodoSerializers(<QuerySet [<Todo: aaa>]>, many=True):
#     id = IntegerField(label='ID', read_only=True)
#     task = CharField(max_length=50)
#     description = CharField(style={'base_template': 'textarea.html'})
#     priority = ChoiceField(choices=(('H', 'High'), ('M', 'Medium'), ('L', 'Low')), required=False)      
#     done = BooleanField()
#     createDate = DateTimeField(label='CreateDate', read_only=True)
#     updateDate = DateTimeField(label='UpdateDate', read_only=True)


# serializer.data print edilince

# [OrderedDict([('id', 1), ('task', 'aaa'), ('description', 'aaa'), ('priority', 'M'), ('done', True), ('createDate', '2022-06-15T10:54:18.928994Z'), ('updateDate', '2022-06-15T10:54:18.928994Z')])]




##sadece post yapar. get bile yapmaz.
@api_view(["POST"])
def todoCreate(request):
        ## request ile bize gelen veriyi request.data ile aliyoruz ve convertor a sokuyoruz.
    serializer = TodoSerializers(data = request.data)
        ## is_valid mi diye kontrol ediyoruz.
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
        




#### get ve post methodlarini birlestiriyoruz:
## tek endpoint de ikisini de yapiyoruz.

@api_view(["GET", "POST"])
def todoListCreate(request):
    if request.method == "GET":
        queryset = Todo.objects.all()
        serializer = TodoSerializers(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = TodoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

    



## Note: frontend ciler icin status code cok önemlidir. Bu nedenle her islemin ayri bir kodu vardir bunlarda docs da yer alir.
## Biz status yazmasak da default degerler gider ama dogrusu yazmaktir.





#######  Update:  eger burada get de yazmazsak hatali calisir.

@api_view(["GET", "PUT"])
def todoUpdate(request, pk):
    queryset = Todo.objects.get(id = pk)

    if request.method == "GET":
        ## dikkat burada tek eleman o nedenle many=true yok
        serializer = TodoSerializers(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
        


    elif request.method == "PUT":
        serializer = TodoSerializers(instance=queryset, data=request.data)
        ### bu kodun anlami su: request ile gelen ve update edilmek istenen veriyi instance=queryset olarak sol cebine koy. Bu verinin databaseden gelen halini data=request.data olarak sag cebine koy. Ve ikisi üzerinde karsilastirma yap demek.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)