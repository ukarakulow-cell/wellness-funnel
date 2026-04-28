from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    # Panelde hangi sütunların görüneceğini belirliyoruz
    list_display = ('email', 'phone_number', 'primary_goal', 'created_at')
    search_fields = ('email', 'phone_number')