# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


KIND_CHOICES = (
    (u'Python技术', u'Python技术'),
    (u'数据库技术', u'数据库技术'),
    (u'经济学', u'经济学'),
    (u'文体咨询', u'文体咨询'),
    (u'个人心情', u'个人心情'),
    (u'其他', u'其他'),
)

class Moment(models.Model):
    content = models.CharField(max_length=300)
    user_name = models.CharField(max_length=20)
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])
    
