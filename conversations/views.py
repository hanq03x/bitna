from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect, reverse, render
from django.views.generic import View, ListView
from users import models as user_models
from . import models


def go_conversation(request, user_pk):
    user = user_models.User.objects.get_or_none(pk=user_pk)
    admin = user_models.User.objects.get_or_none(username="admin")
    if user is not None:
        if user != admin:
            try:
                conversation = models.Conversation.objects.get(participants=user)
            except models.Conversation.DoesNotExist:
                conversation = models.Conversation.objects.create()
                conversation.participants.add(admin, user)
            return redirect(reverse("conversations:detail", kwargs={"pk": conversation.pk}))
        else:
            return redirect(reverse("conversations:manage"))
        
        
def select_conversation(request):
    admin = user_models.User.objects.get(username="admin")
    conversation =[c for c in models.Conversation.objects.filter(participants=admin)]
    return render(request, "conversations/conversation_admin.html", {"conversation": conversation})


class ConversationDetailView(View):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get_or_none(pk=pk)
        if not conversation:
            raise Http404()
        return render(
            self.request,
            "conversations/conversation_detail.html",
            {"conversation": conversation},
        )

    def post(self, *args, **kwargs):
        message = self.request.POST.get("message", None)
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get_or_none(pk=pk)
        if not conversation:
            raise Http404()
        if message is not None:
            models.Message.objects.create(
                message=message, user=self.request.user, conversation=conversation
            )
        return redirect(reverse("conversations:detail", kwargs={"pk": pk}))
    
    