kendall-w
===============================

version number: 0.0.1
author: Ugo Loobuyck

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
    
Contributing
------------

TBD

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