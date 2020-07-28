from django.db import models




class Upload(models.Model):
    title = models.CharField(max_length=50)
    left_images = models.ImageField(upload_to='left/', verbose_name='Left Image')

    class Meta:
        verbose_name_plural = "Left Images"

    def __str__(self):
        return self.title

class Upload_two(models.Model):
    title = models.CharField(max_length=50)
    middle_images = models.ImageField(upload_to='middle/', verbose_name='Middle Image')

    class Meta:
        verbose_name_plural = "Middle Images"

    def __str__(self):
        return self.title

class Upload_three(models.Model):
    title = models.CharField(max_length=50)
    right_images = models.ImageField(upload_to='right/', verbose_name='Right Image')

    class Meta:
        verbose_name_plural = "Right Images"

    def __str__(self):
        return self.title
