from django.db import models


class Membership(models.Model):
    slug = models.SlugField()
    membershiptype = models.CharField()
    price = models.IntegerField(default=50)
    stripe_plan_id = models.CharField(max_length=40)
