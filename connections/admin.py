from django.contrib import admin
from .models import Player

# Register your models here
admin.site.register(Player)

# class PlayerAdmin(admin.ModelAdmin):
#     # list_display = ('user', 'user_info', 'city', 'phone', 'website')

#     def user_info(self, obj):
#         return obj.description

#     def get_queryset(self, request):
#         queryset = super(PlayerAdmin, self).get_queryset(request)
#         queryset = queryset.order_by('user')
#         return queryset

#     user_info.short_description = 'Info'

# admin.site.register(Player, PlayerAdmin)