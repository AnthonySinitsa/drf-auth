# from django.apps import AppConfig


# class NotCloudsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'not_clouds'
def app(environ, start_response):
    """Simplest possible application object"""
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])