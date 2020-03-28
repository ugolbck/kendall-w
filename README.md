kendall-w

![version](https://img.shields.io/pypi/v/kendall-w?style=plastic)
![python](https://img.shields.io/pypi/pyversions/kendall-w?style=plastic)
![format](https://img.shields.io/pypi/format/kendall-w?style=plastic)
![license](https://img.shields.io/pypi/l/kendall-w?style=plastic)
![downloads](https://img.shields.io/pypi/dm/kendall-w?style=plastic)

Author: Ugo Loobuyck

Overview
--------

Computes Kendall's coefficient of concordance for inter-annotator agreement
in the case of item ranking.

Installation / Usage
--------------------

To install use pip:

    $ pip install kendall-w


Or clone the repo:

    $ git clone https://github.com/ugolbck/kendall-w.git
    $ python setup.py install


Example
-------

```python
from kendall_w.kendall_w import compute_w

annotations = [
        [1, 1, 1, 2],
        [2, 2, 2, 3],
        [3, 3, 3, 1],
    ]

W = compute_w(annotations) # returns 0.4375 (fair overall agreement)
```
