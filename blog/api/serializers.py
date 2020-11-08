from rest_framework import serializers
from .. import models
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = ('id', 'title', 'body', 'pub_date')
