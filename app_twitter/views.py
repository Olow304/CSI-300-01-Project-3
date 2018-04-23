from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from twitter_app.forms import AuthForm, UserForm, TweetForm
from django.contrib.auth.models import User
from django.http import Http404
from twitter_app.models import Tweet
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request, auth_form=None, user_form=None):
    current_user = request.user
    if request.user.is_authenticated():
        tweet_form = TweetForm()
        user = request.user
        tweets_self = Tweet.objects.filter(user=user.id)
        tweet_count = len(tweets_self)
        tweets_buddies = Tweet.objects.filter(user__userprofile__in=user.profile.follows.all)
        tweets = (tweets_self | tweets_buddies).reverse()[::-1]
        return render(request, 'logged_in.html',
            {'tweet_form': tweet_form, 'user': user,
            'tweets': tweets, 'tweet_count': tweet_count, 'next_url': '/',})
    else:
        auth_form = auth_form or AuthForm()
        user_form = user_form or UserForm()
        return render(request, 'home.html', {'auth_form': auth_form, 'user_form': user_form, })


def login_view(request):
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
        else:
            return index(request, auth_form=form)
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')


def signup(request):
    user_form = UserForm(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return index(request, user_form=user_form)
    return redirect('/')


def public(request, tweet_form=None):
    tweet_form = tweet_form or TweetForm()
    tweets = Tweet.objects.reverse()[::-1]
    return render(request,
                  'tweets.html',
                  {'tweet_form': tweet_form, 'next_url': '/tweets',
                   'tweets': tweets, 'username': request.user.username,})


def submit(request):
    if request.method == "POST":
        tweet_form = TweetForm(data=request.POST)
        next_url = request.POST.get("next_url", "/")
        if tweet_form.is_valid():
            tweet = tweet_form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect(next_url)
        else:
            return public(request, tweet_form)
    return redirect('/')


def users(request, username="", tweet_form=None):
    if username:
        try:
            user = User.objects.get(username=username)
            current_user = request.user;
        except User.DoesNotExist:
            raise Http404
        tweets = Tweet.objects.filter(user=user.id).reverse()[::-1]
        tweet_count = len(tweets)

        alltweets = Tweet.objects.all()
        all_tweets = len(alltweets)

        if username == request.user.username or request.user.profile.follows.filter(user__username=username):
            return render(request, 'profile.html', {'user': user, 'tweet_count': tweet_count, 'current_user': current_user, 'tweets': tweets, })
        return render(request, 'profile.html', {'user': user, 'tweet_count': tweet_count, 'current_user': current_user, 'tweets': tweets, 'follow': True, })

    users = User.objects.all().annotate(tweet_count=Count('tweet'))
    tweets = users
    obj = zip(users, tweets)
    tweet_form = tweet_form or TweetForm()
    return render(request,
                  'users.html',
                  {'obj': obj, 'next_url': '/users/',
                   'tweet_form': tweet_form,
                   'username': request.user.username, })

def follow(request):
    if request.method == "POST":
        follow_id = request.POST.get('follow', False)
        if follow_id:
            try:
                user = User.objects.get(id=follow_id)
                request.user.profile.follows.add(user.profile)
            except ObjectDoesNotExist:
                return redirect('/users/')
    return redirect('/users/')

def unfollow(request):
    if request.method == "POST":
        unfollow_id = request.POST.get('unfollow', False)
        if unfollow_id:
            try:
                user = User.objects.get(id = unfollow_id)
                user.delete()
                #request.user.profile.follows.add(user.profile)
            except ObjectDoesNotExist:
                return redirect('/users/')
    return redirect('/users/')
