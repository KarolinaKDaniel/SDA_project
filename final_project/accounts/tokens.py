from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .__init__ import Six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            Six.text_type(user.pk) + Six.text_type(timestamp) +
            Six.text_type(user.email_confirmed)
        )

account_activation_token = AccountActivationTokenGenerator()