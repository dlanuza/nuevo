from django.shortcuts import render_to_response
import datetime
 
def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('template.html', {'current_date': now})

"""

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
    
    
def current(request):
    html = "<html><body>It is now 11.</body></html>" 
    return HttpResponse(html)
    
    """