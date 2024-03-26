from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

__all__ = []


class EmailConfirmationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        """
        user: models.User
        """
        return (
            six.text_type(user.pk)
            + user.email
            + six.text_type(timestamp)
            + six.text_type(user.is_active)
        )


email_confirmation_token = EmailConfirmationTokenGenerator()
