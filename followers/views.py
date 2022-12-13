from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model

from .models import FollowRequest, Follower

User = get_user_model()

# Create your views here.

def send_follow_request(request, receiver_id):
    sender = request.user
    receiver = User.objects.get(id=receiver_id)
    follow_request, created = FollowRequest.objects.get_or_create(sender=sender, receiver=receiver, status=False)

    if not created:
        return JsonResponse({"requested": False})
        
    return JsonResponse({"requested": True})

def accept_follow_request(request, request_id):
    follow_request = FollowRequest.objects.get(id=request_id)
    follow_request.status = True
    follow_request.save()
    sender = follow_request.sender
    receiver= follow_request.receiver
    follower = Follower.objects.create(follower=follow_request.sender, followee=follow_request.receiver)
    follows_sender = receiver.is_followed(sender.id)
    data = {
        "accepted": True,
        "sender_id": sender.id,
        "follows_sender": follows_sender
    }
    return JsonResponse(data)

def unfollow_user(request, user_id):
    user = User.objects.get(id=user_id)
    follower = Follower.objects.get(follower=request.user, followee=user)
    follower.delete()
    return JsonResponse({"unfollowed": True})