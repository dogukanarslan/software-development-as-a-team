from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Space, Label, Post,Comment,SpaceJoinRequest
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Space)
class SpaceAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("id", "title")
    group_fieldsets = True


@admin.register(Label)
class SpaceAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("id", "name")
    group_fieldsets = True

@admin.register(Comment)
class SpaceAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ("id",)
    list_filter = ("id",)
    group_fieldsets = True


@admin.register(Post)
class SpaceAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("id", "title")
    group_fieldsets = True

@admin.register(SpaceJoinRequest)
class SpaceAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ("id",)
    list_filter = ("id", "status")
    group_fieldsets = True
