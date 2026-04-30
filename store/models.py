from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    description = models.TextField(verbose_name="Tavsifi", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    image = models.ImageField(upload_to='products/', verbose_name="Rasmi", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
        ordering = ['-created_at']
