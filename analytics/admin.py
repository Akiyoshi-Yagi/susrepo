from django.contrib import admin
from .models import Company, CharacterNum, WordRate, InputCategory

admin.site.register(Company)
admin.site.register(CharacterNum)
admin.site.register(WordRate)
admin.site.register(InputCategory)