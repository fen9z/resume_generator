from django.db import models


# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    education = models.TextField(blank=True)  # 教育背景
    experience = models.TextField(blank=True)  # 工作经历
    skills = models.TextField(blank=True)  # 技能

    def __str__(self):
        return self.name
