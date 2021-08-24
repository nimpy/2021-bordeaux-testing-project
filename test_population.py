import numpy as np
import pytest
import population
import math
#from conftest import random_state

@pytest.mark.parametrize('x,r,f', [(0.1, 2.2, 0.198),(0.2, 3.4, 0.544),(0.75, 1.7, 0.31875)])
def test_population(x,r,f):
    output = population.logistic_map(x,r)
    expected = f
    assert math.isclose(output, expected)


@pytest.mark.parametrize('x,r,it,f', [(0.1, 2.2, 1, [0.198]),(0.2, 3.4, 4, [0.544, 0.843418, 0.449019, 0.841163]),(0.75, 1.7, 2, [0.31875, 0.369152])])
def test_population_it(x,r,it,f):
    output = np.array(population.iterate_f(x,r,it))
    expected = np.array(f)
    np.testing.assert_array_almost_equal(output, expected, decimal=5)



def test_convergence(random_state):
    for _ in range(10):
        x = random_state.uniform(0,1)
        result = population.iterate_f(x,1.5,50)
        expected = 1/3
        assert math.isclose(expected,result[-1])
