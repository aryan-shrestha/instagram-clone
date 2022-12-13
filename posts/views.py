from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required

from .models import Post, Like, PostImage, Story
from followers.models import FollowRequest

import requests as req

# Create your views here.

class HomeView(View):
    template_name = 'posts/posts.html'

    def get(self, request):
        user = request.user
        followings = user.followee.all()
        followings_arr = []
        for following in followings:
            followings_arr.append(following.followee.id)

        posts = Post.objects.filter(user__in=followings_arr).order_by('-date_created')  # getting all the posts of following users
        followings_arr.append(request.user)
        stories = Story.objects.filter(user__in=followings_arr)
        follow_requests = FollowRequest.objects.filter(receiver=request.user, status=False)
        
        
        context = {
            "stories": stories,
            "posts": posts,
            "follow_requests": follow_requests
        }
        
        return render(request, self.template_name, context=context)
    
    # since the form is on the same page accepting post request 
    # of the form on the same url
    def post(self, request):
        user = request.user
        photo = request.FILES.get('photo')
        caption = request.POST.get('caption')
        post = Post.objects.create(user=user, caption=caption)
        post_image = PostImage.objects.create(post=post, image=photo)
        return JsonResponse({'posted': True})

@login_required(login_url='login')
def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    like, created = Like.objects.get_or_create(user=user, post=post)

    if not created:
        like.delete()
        total_likes = post.like.all().count()
        data = {
            'liked': False,
            'total_likes': total_likes,
        }
        return JsonResponse(data)

    total_likes = post.like.all().count()
    data = {
        'liked': True,
        'total_likes': total_likes
    }

    return JsonResponse(data)


def storyUpload(request):
    if request.method == "POST":
        story_image = request.FILES.get('photo')
        user = request.user
        story = Story.objects.create(user=user, image=story_image)
        return JsonResponse({"status": 202})

# esewa integration trial
def esewaPaymentView(request):
    return render(request, 'posts/esewa.html')

def esewaVerificationView(request):
    refId = request.GET.get('refId')
    
    url ="https://uat.esewa.com.np/epay/transrec/"
    d = {
        'amt': 100,
        'scd': 'EPAYTEST',
        'rid': refId,
        'pid':'ee2c3ca1-696b-4cc5-a6be-2c40d929d45a7',
    }
    resp = req.post(url, d)
    return HttpResponse(resp.text)


