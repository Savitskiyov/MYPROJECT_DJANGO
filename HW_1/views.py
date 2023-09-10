from django.http import HttpResponse  # HttpResponse - класс, к-й возвращает http-ответ от сервера клиенту
import logging
from functools import wraps
from datetime import datetime

logger = logging.getLogger(__name__)


def write_log(func):
    @wraps(func)
    def wrapper(request):
        view_name = func.__name__
        # print(view_name)
        client_ip = get_client_ip(request)
        # print(client_ip)
        logger.info(f'=== Page "{view_name}" was visited from ip = {client_ip}')
        return func(request)

    return wrapper


@write_log
def index(request):
    html_text = "<h1>Главная страница Савицкого Олега.</h1>" \
                "<h2>Мне 36 лет.</h2>"
    return HttpResponse(html_text)


@write_log
def about(request):
    html_text = f"<h1>Я аналитик, изучающий python.</h1>" \
                f"<h2>Сейчас изучаю блок Django.</h2>"
    return HttpResponse(html_text)


# возвращает ip, с которого пришёл request
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # если ip передан через proxy
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    # если открыто
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
