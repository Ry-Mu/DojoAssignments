from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re, bcrypt

EMAIL_RE = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{3}$')

Name_RE= EMAIL_REGEX = re.compile(r'^[a-zA-Z]{2,}')


class UserManager(models.Manager):
    #first_name=0 last_name=1 email=2 password=3 password_confirmation=4
    def register(self, request, *args):
        if not Name_RE.match(args[0]):
            messages.error(request, 'Invalid First Name')
            return False
        elif not Name_RE.match(args[1]):
            messages.error(request, 'Invalid Last Name')
            return False
        elif not Name_RE.match(args[2]):
            messages.error(request, 'Invalid  ')
            return False
        elif len(args[3]) < 8:
            messages.error(request, 'Invalid Password')
            return False
        elif args[3] != args[4]:
            messages.error(request, 'Passwords dont match')
            return False
        else:
            password = args[3].encode()
            pwhash = bcrypt.hashpw(password, bcrypt.gensalt())
            super(UserManager, self).create(first_name=args[0], last_name=args[1], email=args[2], password=pwhash)
            return True

    def login(self, email, password, request):
        them = Users.objects.filter(email=email)
        if not them:
            message.error('No {} in database!' .format(email))
            return False
        else:
            if not bcrypt.checkpw(password.encode(), them[0].password.encode()):
                messages.error('Invalid Password')
                return False
            else:
                return {'True': them[0].id}



class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()
