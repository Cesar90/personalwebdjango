from django.shortcuts import render, HttpResponse

html_base = """
    <h1>My personal web</h1>
    <ul>
        <li><a href="/">Front Page</a></li>
        <li><a href="/about-me/">About me</a></li>
        <li><a href="/porfolio/">Porfolio</a></li>
        <li><a href="/contact/">Contanct</a></li>
    </ul>
"""

# Create your views here.
def home(request):
    # html_response = html_base + "<h1>My personal web</h1>"
    # for i in range(10):
    #     html_response += "<h2>Por</h2>"
    # return HttpResponse(html_response)
    return render(request, "core/home.html")

def about(request):
    # return HttpResponse(html_base + """
    #     <h2>About me</h2>
    #     <p>My name is Cesar and I am programmer</p>
    # """)
    return render(request, "core/about.html")

def porfolio(request):
    # return HttpResponse(html_base + """
    #     <h2>Porfolio</h2>
    #     <p>Some of my projects</p>
    # """)
    return render(request, "core/porfolio.html")

def contact(request):
    # return HttpResponse(html_base + """
    #     <h2>Contanct</h2>
    #     <p>Here is my email if you have questions: <a href="mailto:test@test.test">test@test.test</a></p>
    # """)
    return render(request, "core/contact.html")