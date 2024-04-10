# test_bindingenergy.py
import pytest
from bindingenergy import binding_energy


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


def test_calculate_binding_energy_known():
    """Test r for a known resulting energy"""
    r = 6.82e-10
    expected_energy = -1.0e-22
    calculated_energy = binding_energy(r)
    assert calculated_energy == pytest.approx(expected_energy)
