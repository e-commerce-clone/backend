import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk) + six.text_type(timestamp)) + six.text_type(user.is_active)

# user 의 pk, 현재시간, user 의 활성화를 가지고 합쳐 tokens 을 생성
account_activation_token = AccountActivationTokenGenerator()