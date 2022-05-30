
// Func i burada tanimlamamiz yeterli degil. Bu func i daha sonra base.html de cagiriyoruz.
{/* <script src="{% static 'users/js/timeout.js' %}"></script> */}

// message home sayfasinda cikar. bu nedenle bu message in class yada id sini ögrenmek icin home sayfasinda iken inspect yapariz.

let element = document.querySelector('.alert');

setTimeout(function () {
  element.style.display = 'none';
}, 3000);
