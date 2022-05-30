
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta():
        model = User
        # fields = '__all__'
        fields = ('username', 'password1', 'password2', 'portfolio', 'profile_pic', 'first_name', 'last_name')
        exclude = ('is_staff', 'is_active', 'date_joined', 'password', 'last_login', 'is_superuser', 'groups', 'user_permissions', )

### Önemli: Burada password1 ve password2 hic yazmazsak password inputunu ve password confirmation inputunu formun en sonuna atar. ama yazdigimizda istedigimiz siraya getiriyor.

## AbstractUser in orijinalindeki username i email yaptigimiz icin buradaki email i sildik