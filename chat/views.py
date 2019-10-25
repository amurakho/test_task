from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy

from chat.forms import UserSignUpForm


def index(request):
    return render(request, 'chat/index.html', {})


# @login_required
def room(request):
    room_name = 'main_room'
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username))
    })


class RegisterView(generic.CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login_url')
    template_name = 'chat/register.html'
