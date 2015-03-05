from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html', {
       'navoptions': [('Activities','/activity/'),
					  ('Login Page','/login/'),
					  ('About Us','/about/'),
					  ('Browse','/browse'),
					  ('Upload','/upload/')]
    })

def login(request):
    return render(request, 'login.html', {
	    'navoptions': [('Go Home', '/home/'),
	                  ('Activities','/activity/'),
					  ('About Us','/about/'),
					  ('Browse','/browse'),
					  ('Upload','/upload/')]
		})


def about(request):
    return render(request, 'about.html', {
        'navoptions': [('Go Home', '/home/'),
	                  ('Activities','/activity/'),
					  ('Login Page','/login/'),
					  ('Browse','/browse'),
					  ('Upload','/upload/')]
    })


def browse(request):
    return render(request, 'browse.html', {
	    'navoptions': [('Go Home', '/home/'),
	                  ('Activities','/activity/'),
					  ('Login Page','/login/'),
					  ('About Us','/about/'),
					  ('Upload','/upload/')]
	})


def activity(request):
    return render(request, 'activity.html', {})


def upload(request):
    return render(request, 'upload.html', {
	    'navoptions': [('Go Home', '/home/'),
	                  ('Activities','/activity/'),
					  ('Login Page','/login/'),
					  ('About Us','/about/'),
					  ('Browse','/browse')]
		})
