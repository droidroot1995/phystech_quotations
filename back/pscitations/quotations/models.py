from django.db import models


class Quotation(models.Model):
    author = models.TextField(max_length=64)
    quot_text = models.TextField(max_length=2056)
    added_at = models.DateTimeField(null=True, auto_now_add=True)
    added_by = models.ForeignKey(to='users.User', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'
        ordering = ['added_at']
