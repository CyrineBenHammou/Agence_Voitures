from django.http import HttpResponse
from django.template import loader

def App(request):
  template = loader.get_template('Home.html')
  return HttpResponse(template.render())