from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
import datetime
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world!")

def my_homepage_view(request):
    return HttpResponse("美少女战士之家")

# 方式1：使用HttpResponse返回网页
def current_datetime(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    t = get_template('current_datetime.html')
    html = t.render({'current_datetime': now})
    return HttpResponse(html)

# 方式2：使用render_to_response()返回网页
def another_time_page(request):
    now = datetime.datetime.now()
    # return render_to_response('current_datetime.html', {'current_datetime': now})
    return render(request, 'current_datetime.html', {'current_datetime': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    # return HttpResponse(html)
    return render(request, 'hours_ahead.html', {'hour_offset': offset,
                                                'next_time': dt})

# 使用子目录中的模板
def another_time_page_2(request):
    now = datetime.datetime.now()
    # 直接将目录级别添加到文件名中
    return render(request, 'time/another_time_page.html', {'current_datetime': now})

def display_meta(request):
    values = request.META.items()
    browser = request.META.get('HTTP_USER_AGENT', 'unknown')
    ip = request.META.get('REMOTE_ADDR', 'unknown')
    return render(request, 'request.html',
                  {'meta': values,
                   'agent': browser,
                   'ip': ip}
                  )

def time_capsule(request, year, month, day):
    year = int(year)
    month = int(month)
    day = int(day)
    if year < 1:
        raise ValueError('year [%s] is out of range') % year
    if month < 1 or month > 12:
        raise ValueError('month [%s] is out of range') % month
    if day < 1 or day > 31:
        raise ValueError('day [%s] is out of range') % day
    date = datetime.date(year, month, day)
    date_dif = (datetime.date.today() - date).days
    days = abs(date_dif)
    return render(request, 'date_archive.html', {'date': date,
                                                 'date_dif': date_dif,
                                                 'days': days})