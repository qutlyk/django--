from django.http import  HttpResponse,Http404
import  datetime


def current_time(requests):
    now =datetime.datetime.now()
    html = 'it in now {}'.format(now)
    return HttpResponse(html)


def hour(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now()+datetime.timedelta(hours = offset)
    html = "in %s hour,it will be%s"%(offset,dt)
    return HttpResponse(html)



