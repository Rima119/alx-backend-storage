#!/usr/bin/env python3
"""Task 5 module"""
import redis
import requests
from typing import Callable
from functools import wraps


r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """obtain the HTML content of a particular URL and returns it"""

    @wraps(method)
    def wrapper(url):
        """ Wrapper for the decorated function """

        cached_html = r.get("cached_html:{}".format(url))
        if cached_html:
            return cached_html.decode('utf-8')

        r.incr("count:{}".format(url))

        html = method(url)
        r.setex("cached_html:{}".format(url), 10, html)

        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """track how many times a particular URL was accessed"""
    return requests.get(url).text
