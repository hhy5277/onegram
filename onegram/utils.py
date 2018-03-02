import json
import logging
import time
import jmespath

from itertools import chain
from itertools import repeat as iter_repeat
from functools import partial

from random import uniform
from random import choice
from requests import Response

logger = logging.getLogger(__name__)


def jsearch(jspath, content):
    if isinstance(content, dict):
        dct = content
    else:
        if isinstance(content, Response):
            text = content.text
        elif isinstance(content, str):
            text = content
        else:
            raise TypeError()
        dct = json.loads(text)

    return jmespath.search(jspath, dct)


def sleep(t, var=.5):
    if t:
        sleep_time = uniform((1-var)*t, (1+var)*t) 
        logger.info(f'{sleep_time:.{2}f} seconds')
        time.sleep(sleep_time)


def repeat(*a, **kw):
    return partial(iter_repeat, *a, **kw)
    
def choice_repeat(seq):
    def _choice_repeat():
        while True:
            yield choice(seq)
    return _choice_repeat

def head_tail(head, tail):
    return partial(chain, [head], iter_repeat(tail))
