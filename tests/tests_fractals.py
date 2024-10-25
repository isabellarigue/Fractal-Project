import pytest
from fractals.helper import suite, suite_mandelbrot, suite_julia, is_in_Mandelbrot, is_in_Julia, create_matrix_mandelbrot, create_matrix_julia

def test_suite():
    gen = suite(0, 0.5 + 0.5j)
    assert next(gen) == 0  # Premier element

def test_suite_mandelbrot():
    gen = suite_mandelbrot(0.3 + 0.5j)
    assert next(gen) == 0 # Premier element

def test_suite_julia():
    gen = suite_julia(0.5 + 0.5j, -0.8 + 0.156j)
    assert next(gen) == 0.5 + 0.5j  # Premier element

@pytest.mark.parametrize("c, max_iter, expected", [
    (0, 100, True),           
    (2 + 2j, 100, False),     
    (0.251, 1000, False) 
])
def test_is_in_Mandelbrot(c, max_iter, expected):
    assert is_in_Mandelbrot(c, max_iter) == expected

@pytest.mark.parametrize("z, c, max_iter, expected", [
    (0, -0.8 + 0.156j, 100, True),         
    (2 + 2j, -0.8 + 0.156j, 100, False),   
    (0.3 + 0.5j, -0.8 + 0.156j, 100, False) 
])
def test_is_in_Julia(z, c, max_iter, expected):
    assert is_in_Julia(z, c, max_iter) == expected
