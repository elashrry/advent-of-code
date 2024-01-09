import pytest
from aocutils import solve_quadratic_eqn


def test_solve_quadratic_eqn_valid_roots():
    assert solve_quadratic_eqn(1, -3, 2) == [1, 2]
    assert solve_quadratic_eqn(2, 5, -3) == [-3, 0.5]


def test_solve_quadratic_eqn_imaginary_roots():
    assert solve_quadratic_eqn(1, 1, 1) is None


def test_solve_quadratic_eqn_zero_discriminant():
    assert solve_quadratic_eqn(1, -6, 9) == [3, 3]


def test_solve_quadratic_eqn_coefficient_a_zero():
    err_msg = "Coefficient 'a' must not be zero for a valid quadratic equation."
    with pytest.raises(ValueError, match=err_msg):
        solve_quadratic_eqn(0, 2, 1)


if __name__ == "__main__":
    # pytest.main()
    test_solve_quadratic_eqn_zero_discriminant()
