import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.room_group_name = f"chat_{self.user.id}"
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    def receive(self, text_data):
        data = json.loads(text_data)
        sender = self.scope["user"]
        receiver_id = data["receiver_id"]
        content = data["content"]

        receiver = User.objects.get(id=receiver_id)
        Message.objects.create(sender=sender, receiver=receiver, content=content)

        async_to_sync(self.channel_layer.group_send)(
            f"chat_{receiver.id}",
            {
                "type": "chat_message",
                "message": content,
                "sender": sender.username,
            },
        )

    def chat_message(self, event):
        self.send(text_data=json.dumps({"message": event["message"], "sender": event["sender"]}))
