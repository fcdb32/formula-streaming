from ast import Expression, parse
import random

from time import sleep


str_formulas = [line.strip() for line in open('formulas.txt', 'r')]
compiled_formulas = [compile(Expression(parse(formula).body[0].value), '<string>', 'eval') for formula in str_formulas]

while True:
    args = {
        'a': random.randint(1, 1000),
        'b': random.randint(1, 1000),
        'c': random.randint(1, 1000)
    }

    results = [eval(formula, args) for formula in compiled_formulas]

    del args['__builtins__']
    args_output = ', '.join(f'{var} = {value}' for var, value in args.items())
    results_output = '\n'.join(f'{str(formula)} = {result}' for formula, result in zip(str_formulas, results))

    print(args_output, results_output, sep='\n')

    sleep(5)
