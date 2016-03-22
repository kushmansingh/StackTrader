from __future__ import unicode_literals
import uuid

from django.db import models

# from custom_fields import SeparatedValuesField


class Stack(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    # tags = SeparatedValuesField(default=[])
    user_id = models.UUIDField()  # Created By
    created_ts = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)  # Update on vote event


class Ingredients(models.Model):
    stack_id = models.UUIDField()
    origin = models.CharField(default='subway', max_length=30)
    lettuce = models.IntegerField(default=-1)
    tomato = models.IntegerField(default=-1)
    spinach = models.IntegerField(default=-1)
    cucumber = models.IntegerField(default=-1)


class Favorite(models.Model):

    class Meta:
        unique_together = (('stack_id', 'user_id'),)

    stack_id = models.UUIDField()
    user_id = models.UUIDField()
    ts = models.DateTimeField(auto_now_add=True)


class VoteUp(models.Model):

    class Meta:
        unique_together = (('stack_id', 'user_id'),)

    stack_id = models.UUIDField()
    user_id = models.UUIDField()
    ts = models.DateTimeField(auto_now_add=True)


class VoteDown(models.Model):

    class Meta:
        unique_together = (('stack_id', 'user_id'),)

    stack_id = models.UUIDField()
    user_id = models.UUIDField()
    ts = models.DateTimeField(auto_now_add=True)
