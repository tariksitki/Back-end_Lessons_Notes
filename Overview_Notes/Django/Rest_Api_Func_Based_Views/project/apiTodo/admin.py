from django.contrib import admin
from .models import Todo

# Register your models here.

## Burada yazdigimiz TodoAdmin ile; admin panel de todo lar olusturulduktan sonraki list sayfasinda olacak verileri düzenliyoruz.

class TodoAdmin(admin.ModelAdmin):
    list_display = ["task", "description", "priority", "done", "createDate", "updateDate"]


# TodoAdmin  in Todo modeli ile tek baglantisi burasidir.
admin.site.register(Todo, TodoAdmin)


