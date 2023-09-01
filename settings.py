import os
settings = {
    'cookie_secret': '053d1bd0-6af1-4d81-b195-e72f9a133160',
    'login_url': '/login',
    'xsrf_cookies': True,
    # 'debug': True,
    # 'autoreload': True,
    # 'compiled_template_cache': False,
    # 'static_hash_cache': False,
    # 'serve_traceback': True,
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
}