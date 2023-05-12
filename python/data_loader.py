import csv
import logging

def load_solutions():
    logging.info('Loading solutions ...')
    with open('euler_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        solutions = {int(row['problem']): row for row in reader}
        return solutions

def load_primes():
    logging.debug('Loading primes ...')
    with open('primes1000.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(map(lambda row: int(row['prime']), reader))
