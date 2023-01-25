from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    print('\n\nRequest object:', request)
    print('Request object type:', type(request), '\n\n')

    html_tags = '''
    <h1>This is the Home Page</h1>
    <h3>This is the Home Page</h3>
    <p>MVT means:</p>
    <ul>
        <li>Model</li>
        <li>View</li>
        <li>Template</li>
    </ul>'''

    response = HttpResponse(html_tags)

    # remove these print statements later
    print('Response object:', response)
    print('Response object type:', type(response))
    print('\n\nUser-agent info :', end='')
    print(request.META['HTTP_USER_AGENT'], '\n\n')
   
    return response