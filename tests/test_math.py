"""
Testing math.py module.
"""

import friendly_computing_machine as fcm
import pytest

def test_add():
	assert fcm.math.add(3,7) == 10
	assert fcm.math.add(5,6) == 11



def test_mult():
	assert fcm.math.mult(3,6) == 18
