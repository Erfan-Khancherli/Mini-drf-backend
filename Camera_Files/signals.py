from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Camera_Files ,Gtoken
import requests
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
    PushTicketError,
)
import os
import requests
from requests.exceptions import ConnectionError, HTTPError




@receiver(post_save, sender=Camera_Files)
def note_created(sender, instance, created, **kwargs):
    if created:
        message_title = "New Note Created"
        message_body = f"A new note was created: {instance.created_by}"
        
        token = Gtoken.objects.get(created_by=instance.created_by)
        token = token.gtoken    
        print(token)
        send_push_message(message_title, message_body , session)
session = requests.Session()
session.headers.update(
    {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate",
        "content-type": "application/json",
    }
)        
def send_push_message(token, message, extra=None):
    try:
        response = PushClient(session=session).publish(
            PushMessage(to=token,
                        body=message,
                        data=extra))
    except PushServerError as exc:
        print("PushServerError")
        raise
    except (ConnectionError, HTTPError) as exc:
        print("Connection Error")
        raise 

    try:
        response.validate_response()
    except DeviceNotRegisteredError:
        print("Device Not Registered")
        raise
    except PushTicketError:
        print("Ticket Error")
        raise 
