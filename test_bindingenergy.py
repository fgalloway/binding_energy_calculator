# test_bindingenergy.py
import pytest
import bindingenergy

binding_energy = bindingenergy.binding_energy


def test_calculate_binding_energy_zero():
    """Test r == sigma, expect binding energy to be 0."""
    r = 3.41e-10  # m
    expected_energy = 0  # J
    calculated_energy = binding_energy(r)
    assert calculated_energy == pytest.approx(expected_energy), "The calculated energy should be zero for r equal to sigma."


def test_calculate_binding_energy_negative():
    """Test r > sigma, expect binding energy to be negative."""
    r = 4e-10  # m
    calculated_energy = binding_energy(r)
    assert calculated_energy < 0, "The calculated energy should be negative."


def test_calculate_binding_energy_positive():
    """Test r > sigma, expect binding energy to be negative."""
    r = 3e-10  # m
    calculated_energy = binding_energy(r)
    assert calculated_energy > 0, "The calculated energy should be positive."


def test_calculate_binding_energy_2sigma():
    """Test when r = 2*sigma. Result can be calculated."""
    r = 2*bindingenergy._SIGMA  # 6.82e-10
    epsilon = bindingenergy._EPSILON
    expected_energy = 4*epsilon*(1/2**12 - 1/2**6)  # -1.0e-22
    calculated_energy = binding_energy(r)
    assert calculated_energy == pytest.approx(expected_energy), "The calcuated energy should be -1.0e-22"


def test_calculate_binding_energy_min():
    """Test min(u(r)). Result can be calculated."""
    r = 2**(1/6)*bindingenergy._SIGMA  # du/dr = 0
    expected_energy = -bindingenergy._EPSILON  # model behaviour
    calculated_energy = binding_energy(r)
    assert calculated_energy == pytest.approx(expected_energy), "The calcuated energy should be -1.65e-10"