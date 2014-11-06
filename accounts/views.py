from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
from datetime import datetime
from django.utils import timezone
# Create your views here.


def profile(request, uid=None):
    if(not uid):
        uid = request.user.id
    now = timezone.now()
    month = datetime(now.year, now.month, 1, tzinfo=now.tzinfo)
    user = get_object_or_404(User, id=uid)
    total_filled = user.machine_set.count()
    month_filled = user.machine_set.filter(request__filled_at__gte=month).count()
    render_to_response('accounts/profile.html',
        {'profile': user, 'total_filled': total_filled, 'month_filled': month_filled},
        context_instance=RequestContext(request))