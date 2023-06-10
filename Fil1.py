import sympy
import matplotlib.pyplot as plt

def differentiate(func, var):
  """Differentiates the given function with respect to the given variable.

  Args:
    func: The function to differentiate.
    var: The variable to differentiate with respect to.

  Returns:
    The derivative of the function.
  """
  return sympy.diff(func, var)

def integrate(func, var, lower_bound, upper_bound):
  """Integrates the given function with respect to the given variable.

  Args:
    func: The function to integrate.
    var: The variable to integrate with respect to.
    lower_bound: The lower bound of the integration.
    upper_bound: The upper bound of the integration.

  Returns:
    The integral of the function.
  """
  return sympy.integrate(func, var, lower_bound, upper_bound)

def plot_function(func, var, x_range):
  """Plots the given function over the given range.

  Args:
    func: The function to plot.
    var: The variable to plot the function over.
    x_range: The range of values to plot the function over.
  """
  x = sympy.Symbol('x')
  y = func(x)
  plt.plot(x_range, y)
  plt.show()

def main():
  # Differentiate a function.
  f = sympy.sin(x)
  g = differentiate(f, x)
  print(g)

  # Integrate a function.
  h = sympy.cos(x)
  i = integrate(h, x, 0, sympy.pi/2)
  print(i)

  # Plot a function.
  j = sympy.exp(x)
  plot_function(j, x, sympy.linspace(0, 5, 100))

if __name__ == '__main__':
  main()
