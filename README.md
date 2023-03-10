**Author:** [Behrouz Safari](https://astrodatascience.net//)<br/>
**License:** [MIT](https://opensource.org/licenses/MIT)<br/>

# cals
*A python package for calendrical calculations*


## Installation

Install the latest version of *cals* from [PyPI](https://pypi.org/project/cals/):

    pip install cals

Requirements are *numpy*, *scipy*, *pandas* and *requests*.


## Examples

Let's read a file:

```python
>>> from cals import Gregorian, gregorian_from_jd
>>> g = Gregorian(2023, 2, 1, 2, 36, 15)
>>> g
Gregorian(2023, 2, 1, 2, 36, 15, 0)
>>> jd = g.to_jd()
>>> jd
2459976.6085069445
>>> date = gregorian_from_jd(2459976.5)
>>> date
Gregorian(2023, 2, 1, 0, 0, 0, 0)
>>> date.add_days(10)
>>> date
Gregorian(2023, 2, 11, 0, 0, 0, 0)
>>> date.to_persian()
Persian(1401, 11, 22, 0, 0, 0, 0)
>>> 
>>> from cals import Persian, persian_from_jd
>>> p = Persian(1401, 11, 8, 15)
>>> p
Persian(1401, 11, 8, 15, 0, 0, 0)
>>> p.to_gregorian()
Gregorian(2023, 1, 28, 15, 0, 0, 0)
>>> p.to_jd()
2459973.125
>>> persian_from_jd(2459973.125)
Persian(1401, 11, 8, 15, 0, 0, 0)
>>> p.add_days(50)
>>> p
Persian(1401, 12, 28, 15, 0, 0, 0)
```


See more at [astrodatascience.net](https://astrodatascience.net/)