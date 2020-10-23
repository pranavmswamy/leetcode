**Asha Kelly -**

Asha Daily = 3
Kelly Daily = 5
Asha Ahead By = 5

How many days will Kelly take to cross Asha?

- if asha daily ≥ kelly daily,
    - Then return -1, because kelly will never catch up to asha

else:

diff = kellydaily - ashadaily

return ceil (ashaaheadby / diff)

ceil can also be calculated as (ashaaheadby / diff) + (ashaaheadby % diff ≠ 0)

or ceil (a/b) = (a+b-1/b)
