kendall-w
==========

![version](https://img.shields.io/pypi/v/kendall-w)
[![codecov](https://codecov.io/gh/ugolbck/kendall-w/branch/master/graph/badge.svg)](https://codecov.io/gh/ugolbck/kendall-w)
[![Build Status](https://travis-ci.com/ugolbck/kendall-w.svg?branch=master)](https://travis-ci.com/ugolbck/kendall-w)
![python](https://img.shields.io/pypi/pyversions/kendall-w)
![downloads](https://pepy.tech/badge/kendall-w)

Author: **Ugo Loobuyck**

Overview
--------

Computes Kendall's coefficient of concordance for inter-annotator agreement
in the case of item ranking between more than two annotators.

Installation
------------

To install use pip:

    $ pip install kendall-w


Or clone the repo:

    $ git clone https://github.com/ugolbck/kendall-w.git
    $ python setup.py install


Usage
-------

```python
import kendall_w as kw

annotations = [
        [1, 1, 1, 2],
        [2, 2, 2, 3],
        [3, 3, 3, 1],
    ]

W = kw.compute_w(annotations) # returns 0.4375 (fair overall agreement)
```

Contributions
-------------

*All contributions are welcome.*

#### How to help?

1. Fork this repository to your GitHub account
2. Clone the forked repositery to local
3. Code something and push to your branch
4. Create a pull request from your repository

#### TODO:

- Handle ```pandas.DataFrame``` as an input with the instructions in [the main file](https://github.com/ugolbck/kendall-w/blob/master/kendall_w/kendall_w.py)
- Use numpy for faster computation?