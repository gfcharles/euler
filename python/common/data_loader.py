import csv
import logging


def load_solutions():
    logging.info('Loading solutions ...')
    with open('./euler_data/euler_solutions.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        solutions = {int(row['problem']): row for row in reader}
        return solutions


def load_primes():
    logging.debug('Loading 1000 primes ...')
    with open('./euler_data/primes1000.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(map(lambda row: int(row['prime']), reader))


def load_more_primes():
    logging.debug('Loading 10,000 primes ...')

    more_primes = list()
    with open('./euler_data/primes10000.txt', newline='') as datafile:
        rows = datafile.readlines()[100:]  # skip first 1000 primes, already loaded
        for row in rows:
            if row.strip() != '':  # skip blank lines
                more_primes.extend(map(int, row.split(':')[1].strip().split(' ')))

    return more_primes
