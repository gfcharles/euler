import logging.config

from time import time

# def timing_decorator(function):
#     def timing(*args, **kwargs):
#         start = time()
#         result = function(*args, **kwargs)
#         end = time()
#         class_name = type(args[0]).__name__
#         print(f'{class_name}.{function.__name__} completed in {(end - start) * 1000:.1f} ms')
#         return result
#     return timing


# def euler_problem(function:callable) -> callable:
#     def wrapper(*args, **kwargs):
#         # config_all()
#         return function(*args, **kwargs)
#
#     return wrapper

def euler_problem(logging_level=None, timing=False):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if logging_level:
                config_log_level(logging_level)

            if timing:
                start = time()
                result = function(*args, **kwargs)
                end = time()
                message = f'{function.__name__}({args}) completed in {(end - start) * 1000:.1f} ms'
                if logging_level and logging_level <= logging.INFO:
                    logging.info(message)
                else:
                    print(message)
                return result
            else:
                return function(*args, **kwargs)
        return wrapper
    return decorator

def config_logging():
    logging.config.fileConfig("config/logging.conf")

def config_paths():
    pass

def config_all():
    config_paths()
    config_logging()

def config_log_level(level:int):
    logging.basicConfig(
        level=level,
        format='%(levelname)s [%(filename)s - %(funcName)s():%(lineno)s] %(message)s')
