# Synthetic-data-generator
Synthetic data generator for generating data follows normal distribution

##Introduction
I was struggling for getting large scale synthetic data to do my experiments. I know there are people also face this issue. But they may not know how easy to write their own generator. This is a simple synthetic data generator. This data generator is able to generate random data follows uniform distribution and skewed data follows normal distribution.

##How to get started

1. I assume you already get Python installed on your machine. If not, it is easy to get one.
2. Download DatabaseGnerator.py.
3. Run DatabaseGnerator.py:
  ```
  python3 generator.py
  ```
4. Follow the instruction prompted on your screen.
5. Python will generate the output onto disk row by row. (This is good for generating large scale data). It also can append data to an existing output.csv.
6. output.csv will be shown at the same folder with the python script.

output.csv uses the following schema:

```
+------------------------------+
| serial id | number | payload |
+------------------------------+
```
You are free to change the payload or even the scheme as you want.
