# 이메일 발송을 위한 email 정보

EMAIL = {
    'EMAIL_BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
    'EMAIL_USE_TLS': True,
    'EMAIL_PORT': 587,
    'EMAIL_HOST': 'smtp.gmail.com',
    'EMAIL_HOST_USER': 'wkdtjdxo2@gmail.com',
    'EMAIL_HOST_PASSWORD': 'wkd3124265!',
    'SERVER_EMAIL': 'wkdtjdxo2',
    'REDIRECT_PAGE': 'https://www.naver.com'
}