

<span class="c16 c30">▶ </span><span
class="c46 c48 c42">Interview Questions</span>

<span class="c30">▶ </span><span class="c46 c48 c42">Coding Challenge
</span>

<span class="c16 c30">▶ </span><span class="c23 c16">Video of the
week</span>

<span class="c16 c30">▶ </span><span class="c23 c16">Retro
meeting</span>


<span class="c30">▶ </span><span class="c46 c48 c42">Case study /
project</span>

<br>
<br>
<br>

<h1><strong><span style="color: #3498DB;">Teamwork Schedule</strong></h1></span>

<table style= "width:100%;">
                <tr>
                <td style="color: #FA8072; text-align:left "><h3><strong><p>Ice-breaking</td>
                <td style="color: #FA8072; text-align:right;"><h3><strong><p>5m</p><td>                </tr>
</table>

- Personal Questions (Stay at home & Corona, Study Environment, Kids etc.) 
- Any challenges (Classes, Coding, studying, etc.) 
- Ask how they’re studying, give personal advice. 
- Remind that practice makes perfect. 

<br>

<table style= "width:100%;">
                <tr>
                <td style="color: #FA8072; text-align:left "><h3><strong><p>Team work</td>
                <td style="color: #FA8072; text-align:right;"><h3><strong><p>5m</p><td>                </tr>
</table>

- Ask what exactly each student does for the team, if they know each other, if they care for each other, if they follow and talk with each other etc. 

<br>
<table style= "width:100%;">
                <tr>
                <td style="color: #FA8072; text-align:left "><h3><strong><p>Questions</td>
                <td style="color: #FA8072; text-align:right;"><h3><strong><p>15m</p><td>                </tr>
</table>


**1. One of the most powerful features of Django is its _________,  which enables you to interact with your database"
<storng>Which option is suitable for the blank above?</strong>**

<strong>A.</strong> DTL – Django Template Language<br>
<strong>B.</strong> ORM – Object Relational Mapping<br>
<strong>C.</strong> manage.py file<br>
<strong>D.</strong> Django superuser<br>



<br>

**2. Which ORM query retrieves a single object from People table?**

<strong>A.</strong> People.objects.all()<br>
<strong>B.</strong> People.objects.filter(first_name=”Paul”)<br>
<strong>C.</strong> People.objects.get(id=3)<br>
<strong>D.</strong> People.objects.exclude(last_name=”Lonan”)<br>

<br>

**3. Which one is the false about DTL?**

<strong>A. </strong>{% comment %} tag provides multi-line comments.<br>
<strong>B. </strong>{! this is comment line and won't be rendered !}<br>
<strong>C. </strong>Tags are surrounded by {% and %} like this : {% csrf_token %}<br>
<strong>D. </strong> Variables are surrounded by {{ and }} like this:     My first name is {{ first_name }} <br>


<br>

**4. Because Django’s URL resolver expects to send the request and associated arguments to a callable function, not a class, class-based views have an _______ class method which returns a function that can be called when a request arrives for a URL matching the associated pattern. <storng>Which option is suitable for the blank above?</strong>**


<strong>A. </strong>as_view() <br>
<strong>B. </strong>View()<br>
<strong>C. </strong>Display_view()<br>
<strong>D. </strong>GenericView<br>

<br>

**5. We can see this code blog in which file?**

```py
from django.shortcuts import render
from .models import Article
def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

```
<strong>A.</strong> Templates <br>
<strong>B.</strong> Models<br>
<strong>B.</strong> Forms<br>
<strong>B.</strong> Views<br>


<br>


<table style= "width:100%;">
                <tr>
                <td style="color: #FA8072; text-align:left "><h3><strong><p>Interview Questions</td>
                <td style="color: #FA8072; text-align:right;"><h3><strong><p>15m</p><td>                </tr>
</table>

**1. What are views in Django?**


<br>

**2. What is the difference between a project and an app in Django?**


<br>

**3. What are Django URLs?**

<br>

**4. Define static files and explain their uses?**

<br>

**5.  How to configure static files?**


<br>


<table style= "width:100%;">
                <tr>
                <td style="color: #FA8072; text-align:left "><h3><strong><p>Coding  Challenge</td>
                <td style="color: #FA8072; text-align:right;"><h3><strong><p>0m</p><td>                </tr>
</table>


- No

<br>

<hr><hr>
 
☕
<table style= "width:100%;">
                <tr>
                <td style="color: #FA8072; text-align:left "><h3><strong><p>Coffee Break</td>
                <td style="color: #FA8072; text-align:right;"><h3><strong><p>10m</p><td>                </tr>
</table>

☕
<br>
<hr><hr>

<br>

<br>
<table style= "width:100%;">
                <tr>
                <td style="color: #FA8072; text-align:left "><h3><strong><p>Video of the Week</td>
                <td style="color: #FA8072; text-align:right;"><h3><strong><p>10m</p><td>                </tr>
</table>


- [Using Bootstrap in Python Django Projects Tutorial](https://www.youtube.com/watch?v=zglBdzzoDjM)

<br>

<table style= "width:97%;">
                <tr>
                <td style="color: #FA8072; text-align:left "><h3><strong><p>Retro Meeting on a personal and team level</td>
                <td style="color: #FA8072; text-align:right;"><h3><strong><p>5m</p><td>                </tr>
</table>

Ask the questions below:

- What went well? 
- What went wrong? 
- What are the improvement areas? 
<br>

<table style= "width:100%;">
                <tr>
                <td style="color: #FA8072; text-align:left "><h3><strong><p>Case study/Project</td>
                <td style="color: #FA8072; text-align:right;"><h3><strong><p>10m</p><td>                </tr>
</table>

**This Workshop will be solved after Blog Project week**

[Django CRUD Operations](https://lms.clarusway.com/pluginfile.php/27371/mod_resource/content/1/FS-Backend-Workshop-3-Student%20%281%29.pdf)

<br>

<table style= "width:105%;">
                <tr>
                <td style="color: #FA8072; text-align:left "><h3><strong><p>Closing</td>
                <td style="color: #FA8072; text-align:right;"><h3><strong><p>5m</p><td>                   </tr>
</table>

-Next week’s plan

-QA Session 

<hr>
