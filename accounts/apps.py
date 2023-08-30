from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    # ready() is responsible for making the signals work in the signals
    def ready(self):
        import accounts.signals
