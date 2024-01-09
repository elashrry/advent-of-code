from math import sqrt


def solve_quadratic_eqn(a, b, c):
    """Solves a quadratic equation of the form ax^2 + bx + c = 0.

    Args:
        a (float): Coefficient of the quadratic term.
        b (float): Coefficient of the linear term.
        c (float): Constant term.

    Returns:
        list or None: A list containing the two real roots of the quadratic equation,
                      or None if the discriminant is negative.

    Raises:
        ValueError: If the coefficients do not form a quadratic equation.
    """
    if a == 0:
        raise ValueError(
            "Coefficient 'a' must not be zero for a valid quadratic equation."
        )

    discr = b**2 - 4 * a * c
    if discr < 0:
        return
    sol1 = (-b + sqrt(discr)) / (2 * a)
    sol2 = (-b - sqrt(discr)) / (2 * a)

    return sorted([sol1, sol2])
