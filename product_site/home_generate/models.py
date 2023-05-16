from django.db import models


class HomeCustom(models.Model):
    icon = models.ImageField(upload_to='./media/HomeCustom/logo/img/%y/%m/%d/')
    title = models.CharField(max_length=20)
    details = models.CharField(max_length=5024)

    class Meta:
        verbose_name = 'HomeCostom'
        verbose_name_plural = 'HomeCostoms'

    def __str__(self):
        return self.title