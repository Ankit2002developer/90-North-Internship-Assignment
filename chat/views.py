from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def chat_view(request):
    return render(request, 'chat/chat.html')
