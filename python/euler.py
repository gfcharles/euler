import logging.config

def euler_problem(function:callable) -> callable:
    def wrapper(*args, **kwargs):
        config_all()
        return function(*args, **kwargs)

    return wrapper

def config_logging():
    logging.config.fileConfig("config/logging.conf")

def config_paths():
    pass

def config_all():
    config_paths()
    config_logging()

