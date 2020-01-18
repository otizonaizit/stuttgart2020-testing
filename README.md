# TESTING
- start right away with the [`maxima.py`](maxima.py) function and the corresponding [`maxima_exercise.md`](maxima_exercise.md)
- how do you keep track of the manual testing?
- need for automation! (workaround discipline and reproducibility issues)
- avoid big fail risk, a.k.a. the Python's `glob.glob` (un)sorted output bug:
    - [first in the press](https://www.vice.com/en_us/article/zmjwda/a-code-glitch-may-have-caused-errors-in-more-than-100-published-studies)
    - [more interesting article](https://www.theregister.co.uk/2019/10/15/bug_python_scripts/)
    - [original publication](https://pubs.acs.org/doi/full/10.1021/acs.orglett.9b03216)
    - to avoid all of this, we need automated multiplatform tests

## general statements about testing
- Confidence: Write the code once and use it confidently everywhere else
- Confidence: Correctness is main requirement for scientific code

## the agile development workflow
  - add a test for the new functionality
  - implement the new functionality (!) ⟶ yes, *after* implementing the test ;)
  - run test suite ⟶ debug until all tests are green again
  - optimize and/or refactor

## test automation 
  - [`pytest`](http://pytest.org)
      - how does it work? the `test_` functions
      - the `assert` statement
      - our first test suite
  - side effect: trust
  - side effect: faster development cycles
  - side effect: better code

## testing scientific code
  - floating point equality (`1.1+2.2 != 3.3`)): [`np.isclose`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isclose.html), [`np.allclose`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html)
  - issues with numpy arrays:

      ```python
         >>> x = np.array([1, 1])
         >>> y = np.array([2, 2])
         >>> z = np.array([3, 3])
         >>> x+y==z
         array([True, True])
         >>> assert x+y == z
         ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
         >>> assert np.all(x+y==z)
         >>> np.allclose(x+y, z)
         True
      ```
  - classical reference: [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html) ⟶ rewrite for humans: [Why don’t my numbers add up?](http://floating-point-gui.de)

## random bits
  - tests should be short and quick to execute
  - tests should be easy to read
  - tests should exercise *one* thing
  - test simple but general cases
  - test corner cases and boundary conditions
  - numerical fuzzing and the importance of the random seed (`np.random.RandomState` and `np.random.seed`)
  - for learning algorithms, for example to verify that they don't get stuck in local optima:
      - test stability of one optimal solution:
          - start from optimal solution
          - start from little perturbation of optimal solution
      - generate data from the model with known parameters and recover the parameters

## the problem with random numbers in the tests
  - how do we make sure tests failures are reproducible if we use random data?
  - different approaches, with different level of complexity:
      - test cases: [`test_randomness.py`](test_randomness.py)
      - use `pytest` fixtures: [`conftest_minimal.py`](conftest_minimal.py)
      - add argument to `pytest` CLI and use test setup hooks in `pytest`: [`conftest.py`](conftest.py)


## Continuous integration
We will use Travis CI (but there are many others). Note that it's for free only for **public** repositories:

- login to https://travis-ci.com/ with your GitHub account
- authorize Travis CI to have access to the repos
- put a `.travis.yml` file in the repo
- now your PR will automatically trigger a travis CI build
- you can manually trigger a build if you go to the travis repo page: https://travis-ci.com/USERNAME/REPONAME/ under `More options...`

