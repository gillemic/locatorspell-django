from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Event
from .forms import EventSearchForm

# Create your views here.
def index(request):
  event_list = Event.objects.order_by("-start_date")[::-1]
  form = EventSearchForm()
  context = {"event_list": event_list, "form": form}
  return render(request, "events/index.html", context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "events/detail.html", {"event": event})