import sympy

def derivative(f, x):

    """

    Returns the derivative of f at x.

    Args:

        f: A sympy expression.

        x: The point at which to evaluate the derivative.

    Returns:

        The derivative of f at x.

    """

    return sympy.diff(f, x)

def integral(f, a, b):

    """

    Returns the definite integral of f from a to b.

    Args:

        f: A sympy expression.

        a: The lower bound of the integral.

        b: The upper bound of the integral.

    Returns:

        The definite integral of f from a to b.

    """

    return sympy.integrate(f, (x, a, b))

def solve_quadratic(a, b, c):

    """

    Returns the roots of the quadratic equation ax^2 + bx + c = 0.

    Args:

        a: The coefficient of x^2.

        b: The coefficient of x.

        c: The constant term.

    Returns:

        A tuple of the roots of the quadratic equation.

    """

    d = b**2 - 4 * a * c

    if d < 0:

        return ()

    elif d == 0:

        return (-b / (2 * a),)

    else:

        return ((-b + sympy.sqrt(d)) / (2 * a), (-b - sympy.sqrt(d)) / (2 * a))

def solve_linear(a, b):

    """

    Returns the solution of the linear equation ax + b = 0.

    Args:

        a: The coefficient of x.

        b: The constant term.

    Returns:

        The solution of the linear equation ax + b = 0.

    """

    if a == 0:

        if b == 0:

            return ()

        else:

            return (None,)

    else:

        return (-b / a,)

