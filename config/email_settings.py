# 이메일 발송을 위한 email 정보

EMAIL = {
    'EMAIL_BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
    'EMAIL_USE_TLS': True,
    'EMAIL_PORT': 587,
    'EMAIL_HOST': 'smtp.gmail.com',
    'EMAIL_HOST_USER': 'G-mail 아이디',
    'EMAIL_HOST_PASSWORD': 'G-mail 비밀번호',
    'SERVER_EMAIL': '서버 이메일(아이디?)',
    'REDIRECT_PAGE': 'https://www.naver.com'    # redirect할 page
}
