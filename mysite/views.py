from django.template.loader import get_template
from django.template import Template,Context
from django.http import HttpResponse
import datetime
def hello(request):
	return HttpResponse('Hello world!')

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date':now}))
	return HttpResponse(html)

#Can be replace with the underline function
#from django.shortcuts import render_to_response
#def current_datetime(request):
#	current_date = datetime.datetime.now()
#	return render_to_response('current_datetime.html',locals())

from django.shortcuts import render_to_response
def hours_ahead(request,offset):
	try:
		hours_offset = int(offset)
		next_time = datetime.datetime.now() + datetime.timedelta(hours=hours_offset)
	except ValueError:
		raise Http404
	return render_to_response('hours_ahead.html',locals())
