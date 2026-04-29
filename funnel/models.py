from django.db import models

class WellnessLead(models.Model):
    CATEGORY_CHOICES = [
        ('weight_loss', 'Weight Loss & Metabolism'),
        ('energy', 'General Health & Energy'),
        ('muscle', 'Muscle & Toning'),
        ('beauty', 'Beauty & Aesthetics'),
    ]
    
    # Kullanıcı testin başında bu ikisini seçecek
    target_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    age_range = models.CharField(max_length=20)
    
    # Kategoriye göre değişen 4 sorunun cevapları
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    answer_3 = models.CharField(max_length=255)
    answer_4 = models.CharField(max_length=255)
    
    # E-posta kapısı (Opt-in)
    email = models.EmailField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.target_category}"