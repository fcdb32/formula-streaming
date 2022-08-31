import functools
import random

from time import sleep

from evaluate_formula import evaluate_formula

formulas = [line.strip() for line in open('formulas.txt', 'r')]

while True:
    args = {
        'a': random.randint(1, 1000),
        'b': random.randint(1, 1000),
        'c': random.randint(1, 1000)
    }

    results = list(map(functools.partial(evaluate_formula, vars=args), formulas))

    args_output = ', '.join(f'{var} = {value}' for var, value in args.items())
    results_output = '\n'.join(f'{formula} = {result}' for formula, result in zip(formulas, results))

    print(args_output, results_output, sep='\n')

    sleep(5)
