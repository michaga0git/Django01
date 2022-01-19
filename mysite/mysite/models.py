from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    content = models.TextField(max_length=33)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    poleabc = models.TextField(max_length=30)

    def __str__(self):
        return self.headline