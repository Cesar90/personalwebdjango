from django.shortcuts import render
from .models import Project

# Create your views here.
def porfolio(request):
    # return HttpResponse(html_base + """
    #     <h2>Porfolio</h2>
    #     <p>Some of my projects</p>
    # """)
    projects = Project.objects.all()
    return render(request, "portfolio/porfolio.html", {
        'projects': projects
    })