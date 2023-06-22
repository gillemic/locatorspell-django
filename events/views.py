from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Event
from .forms import EventSearchForm

# Create your views here.
def index(request):
  event_list = Event.objects.order_by("-start_date")
  form = EventSearchForm()
  
  if request.method == 'GET':
    activity = request.GET.get('activity', None)
    location = request.GET.get('location', 'Any')
    #start_date = request.GET.get('start_date', '')
    #end_date = request.GET.get('end_date', '')
    price = request.GET.get('price', 0)
    category = request.GET.get('category', None)

    if activity is not None:
      event_list = event_list.exclude(event_type__exact='').filter(event_type=activity)
    if location != 'Any':
      event_list = event_list.filter(location=location)

  context = {"event_list": event_list, "form": form}
  return render(request, "events/index.html", context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "events/detail.html", {"event": event})