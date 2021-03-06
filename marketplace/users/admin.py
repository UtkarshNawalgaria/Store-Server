from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _

from marketplace.users.forms import UserChangeForm, UserCreationForm
from marketplace.users.models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = (
        (_("Personal info"), {"fields": ("name", "email", "phone")}),
        (None, {"fields": ("password",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                ),
            },
        ),
    )
    list_display = ("email", "is_superuser")
    search_fields = (
        "email",
        "phone",
    )
    ordering = ("email",)
