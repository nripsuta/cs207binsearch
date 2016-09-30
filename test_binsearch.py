from pytest import raises 
import numpy as np
from binarysearch import binary_search

input = [1,2,2,4,5,7,8]

def test_binary_search():
    assert binary_search(input,8) == 6
    
def test_outside():
    assert binary_search(input, 10) == -1

def test_far_right():
    assert binary_search(input, 8) == 6
    
def test_far_left():
    assert binary_search(input, 1) == 0
    
def test_only_element():
    assert binary_search([5], 5) == 0
    
def test_infinity():
    assert binary_search([1,2,np.inf], 2) == 1
    
def test_float():
    assert binary_search(input,4.5) == -1

def test_outside_lim():
    assert binary_search(input, 5, 0,2) == -1

def test_wrong_ind():
    assert binary_search(input, 2, 3, 1) == -1
    
def test_type_of_array():
    with raises(TypeError):
        binary_search(set(input), 245)

def test_overflow():
    assert binary_search(range(100000000), 1) == 1
    
def test_all_equal_inp():
    assert binary_search(input, 2, 2, 2) == 2
    
def test_empty():
    assert binary_search([], 5) == -1

def test_no_needle():
    with raises(TypeError):
        binary_search(input)
        
def test_needle_out_of_range():
    with raises(IndexError):
        binary_search(input,3,13,21)

def test_char():
    with raises(TypeError):
        binary_search([input,'a'])
