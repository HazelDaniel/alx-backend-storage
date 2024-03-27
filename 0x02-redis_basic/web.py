#!/usr/bin/env python3
"""
Caching request module
"""
from functools import wraps
from typing import Callable
import redis
import requests


def track_get_page(fn: Callable) -> Callable:
    """ Decorator for get_page """
    @wraps(fn)
    def wrapper(url: str) -> str:
        """ This wrapper tracks the number
            of times the wrapped function is called """
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached = client.get(f'{url}')

        if cached:
            return cached.decode('utf-8')
        response = fn(url)
        client.set(f'{url}', response, 10)
        return response

    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """ makes an http request to a given endpoint and tracks
        the number of times the URL was accessed """
    response = requests.get(url)
    return response.text
