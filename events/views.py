from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from dateutil.parser import parse

from .models import Event
from .forms import EventSearchForm

# Create your views here.
def index(request):
  event_list = Event.objects.order_by("-start_date")
  form = EventSearchForm()
  
  if request.method == 'GET':
    activity = request.GET.getlist('activity')
    location = request.GET.get('location', 'Any')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    price = request.GET.get('price', 'Any')
    category = request.GET.getlist('category')

    if activity:
      event_list = event_list.filter(event_type__in=activity)
    if location != 'Any':
      event_list = event_list.filter(location__icontains=location)
    if start_date != '':
      sdate = parse(start_date)
      event_list = event_list.filter(start_date__gte=sdate)
    if end_date != '':
      edate = parse(end_date)
      event_list = event_list.filter(start_date__lte=edate)
    if price != 'Any':
      event_list = event_list.filter(price__lte=price)
    if category:
      event_list = event_list.filter(category__in=category)

  context = {"event_list": event_list, "form": form}
  return render(request, "events/index.html", context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "events/detail.html", {"event": event})