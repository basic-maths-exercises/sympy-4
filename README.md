# Definite integrals

As a final point, we can also use Python to compute definite integrals.  The code on the left shows how this is done.  Notice that if the result is a fraction (as it is for the first of the three integrals shown on the left) sympy will output a fraction and not a decimal.  This particular feature is extremely cool!

__To pass the exercise modify the code in `main.py` to set the variables `integral1` and `integral2` as follows__:

1. `integral1` should be set equal to ![](https://render.githubusercontent.com/render/math?math=\int_{-1}^1x^3%2Bx^2\textrm{d}x)
2. `integral2` should be set equal to ![](https://render.githubusercontent.com/render/math?math=\int_{-\pi}^\pi\sin(x)%2B\cos(x)\textrm{d}x)

You should obviously use sympy to determine the values of these integrals

Please note, finally, that we have used the sympy library in these final four exercises.  You can use this library to do more than just differentiation, integration and simplification as we have shown here.  You can find further details of how to use sympy online.  If you understand how to use it sympy is very useful for checking the answers that you obtain when you do the problems on your problem sheets.
