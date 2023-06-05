import logging.config

from time import time


def euler_problem(logging_level=None, timing=False):
    def format_params(args, _):
        return ','.join(map(str, args))

    """
    Annotation for Euler problems
    Usage:
    @euler_problem(logging_level=logging.DEBUG,timing=True)
    def euler099():

    Timing and logging can be enabled separately. If timing is True and logging is off, timing info
    will print to standard out. Otherwise, it will appear as a log with level INFO.
    """

    def outer(function):
        def inner(*args, **kwargs):
            if logging_level:
                config_log_level(logging_level)

            if timing:
                start = time()
                result = function(*args, **kwargs)
                end = time()
                params = format_params(args, kwargs)
                message = f'{function.__name__}({params}) completed in {(end - start) * 1000:.1f} ms'
                if logging_level and logging_level <= logging.INFO:
                    logging.info(message)
                else:
                    print(message)
                return result
            else:
                return function(*args, **kwargs)

        return inner

    return outer


def config_logging():
    logging.config.fileConfig("config/logging.conf")


def config_paths():
    pass


def config_all():
    config_paths()
    config_logging()


def config_log_level(level: int):
    logging.basicConfig(
        level=level,
        format='%(levelname)s [%(filename)s - %(funcName)s():%(lineno)s] %(message)s')
