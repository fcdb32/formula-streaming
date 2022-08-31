# Formula streaming task

There is an arbitrary stream of numerical data - arguments.
Arguments come in a fixed set with arbitrary values. The argument name is fixed.
There is a reference book of formulas (for example, in a text file).

For example:
F1 = a + b - c
F2 = a - (b + c)
F3 = a * b - c
F4 = a / b

Each formula can use part of the incoming arguments.
Arguments in formulas and incoming sets are linked by name.

It is necessary to write a console application to calculate the values for each of the reference formulas for each incoming set of arguments.
A heavy load is expected, so it is impossible to parse formulas for each data set.
It is necessary to ensure that formulas are compiled only at the start of the application.
A stream of argument sets can be provided by continuously reading from a file in a loop, or by continuously generating random numbers.

# Usage

```
docker pull ghcr.io/fcdb32/formula-streaming:main
docker run ghcr.io/fcdb32/formula-streaming:main
```
